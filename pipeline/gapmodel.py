"""Open-aware direction model ("gap model").

The Alpha158 models score every name the evening before, from information that
ends at the previous close. The ledger, however, enters at the 9:30 open, and the
playbook's own backtests show that most of what is predictable about the
open-to-close move is only visible AT the open: the overnight gap, how the gap
compares with the stock's normal range and with the market's gap, yesterday's
move, and where the stock sits against its recent range.

This module trains a LightGBM classifier on features known at the open of day t
to predict whether the stock's open-to-close return beats the day's cross-sectional
median (the label the literature recommends: it removes the market's own move, so
the model learns stock selection rather than guessing the index). Hit rates are
still reported on the absolute sign, which is what the ledger scores. It is evaluated walk-forward by year and
scored live by `gap_score.py` from the 5-minute quote relay's official opens.

Outputs (in config.OUTPUT_DIR):
    gapmodel.txt        LightGBM booster trained on the full history
    gapmodel_card.json  walk-forward metrics, calibration bins, top-K hit rates
    gap_static.csv      per-ticker features as of the last session that need
                        history (the session adds today's open and predicts)
    gap_report.md       human-readable summary for the ledger's morning run
"""
from __future__ import annotations

import json
import logging
import math
from datetime import datetime, timezone
from pathlib import Path

import lightgbm as lgb
import numpy as np
import pandas as pd
from sklearn.metrics import roc_auc_score

from . import config

log = logging.getLogger(__name__)

FEATURES = [
    "gap", "gap_idio", "gap_z", "gap_prev", "cc_prev", "oc_prev", "r3_prev", "r5_prev", "mom20_prev", "mom60_prev",
    "vol_ratio_prev", "rvol20", "range_pos_prev", "dist_high20", "dist_low20", "log_dv", "dow",
    "spy_gap", "spy_cc_prev", "spy_mom5", "mkt_gap_med", "sector_gap_med", "sector_id",
]
STATIC_COLS = [
    "ticker", "sector", "sector_id", "asof", "close_raw", "close_adj", "atr20_pct", "gap_prev", "cc_prev", "oc_prev",
    "r3_prev", "r5_prev", "mom20_prev", "mom60_prev", "vol_ratio_prev", "rvol20", "range_pos_prev", "dist_high20",
    "dist_low20", "log_dv", "tradable",
]
PARAMS = {
    "objective": "binary", "learning_rate": 0.03, "num_leaves": 31, "max_depth": 6, "feature_fraction": 0.7,
    "bagging_fraction": 0.7, "bagging_freq": 1, "lambda_l1": 10.0, "lambda_l2": 100.0, "min_data_in_leaf": 2000,
    "num_threads": 4, "seed": 2026, "verbosity": -1,
}
NUM_ROUNDS = 2000
EARLY_STOP = 100
FIRST_TEST_YEAR = 2021
TOPK = 5
THRESHOLDS = [0.55, 0.57, 0.60, 0.63]


def load_panel(csv_dir: Path = config.CSV_DIR) -> pd.DataFrame:
    frames = []
    for p in sorted(csv_dir.glob("*.csv")):
        t = p.stem.upper()
        if t in config.ETF_TICKERS or t.startswith("^"):
            continue
        f = pd.read_csv(p, usecols=["date", "open", "high", "low", "close", "volume", "factor"])
        f["ticker"] = t
        frames.append(f)
    if not frames:
        raise RuntimeError("no CSV data for the gap model")
    df = pd.concat(frames, ignore_index=True)
    df["date"] = pd.to_datetime(df["date"])
    return df.sort_values(["ticker", "date"]).reset_index(drop=True)


def load_spy(csv_dir: Path = config.CSV_DIR) -> pd.DataFrame:
    p = csv_dir / "SPY.csv"
    if not p.exists():
        raise RuntimeError("SPY.csv missing: the gap model needs the market's gap")
    s = pd.read_csv(p, usecols=["date", "open", "close"])
    s["date"] = pd.to_datetime(s["date"])
    s = s.sort_values("date").reset_index(drop=True)
    s["spy_prev_close"] = s["close"].shift(1)
    s["spy_gap"] = s["open"] / s["spy_prev_close"] - 1
    s["spy_cc_prev"] = (s["close"] / s["spy_prev_close"] - 1).shift(1)
    s["spy_mom5"] = s["spy_prev_close"] / s["close"].shift(6) - 1
    return s[["date", "spy_gap", "spy_cc_prev", "spy_mom5"]]


def sector_map() -> tuple[dict[str, str], dict[str, int]]:
    uni = pd.read_csv(config.OUTPUT_DIR / "universe.csv") if (config.OUTPUT_DIR / "universe.csv").exists() else None
    if uni is None or "sector" not in uni.columns:
        return {}, {}
    sec = dict(zip(uni["ticker"].str.upper(), uni["sector"].fillna("Unknown")))
    ids = {s: i for i, s in enumerate(sorted(set(sec.values())))}
    return sec, ids


def build_features(df: pd.DataFrame, spy: pd.DataFrame) -> pd.DataFrame:
    """Per-ticker history features (shifted so they are known at the open) plus the day's gap."""
    g = df.groupby("ticker", sort=False)
    df["prev_close"] = g["close"].shift(1)
    df["gap"] = df["open"] / df["prev_close"] - 1
    df["oc"] = df["close"] / df["open"] - 1
    df["cc"] = df["close"] / df["prev_close"] - 1
    df["cc_prev"] = g["cc"].shift(1)
    df["oc_prev"] = g["oc"].shift(1)
    df["gap_prev"] = g["gap"].shift(1)
    df["r3_prev"] = df["prev_close"] / g["close"].shift(4) - 1
    df["r5_prev"] = df["prev_close"] / g["close"].shift(6) - 1
    df["mom20_prev"] = df["prev_close"] / g["close"].shift(21) - 1
    df["mom60_prev"] = df["prev_close"] / g["close"].shift(61) - 1
    tr = pd.concat([(df["high"] - df["low"]), (df["high"] - df["prev_close"]).abs(), (df["low"] - df["prev_close"]).abs()], axis=1).max(axis=1)
    df["tr_pct"] = tr / df["prev_close"]
    df["atr20_pct"] = df.groupby("ticker", sort=False)["tr_pct"].transform(lambda s: s.rolling(20).mean().shift(1))
    df["gap_z"] = df["gap"] / df["atr20_pct"].replace(0, np.nan)
    vol20 = g["volume"].transform(lambda s: s.rolling(20).mean().shift(1))
    df["vol_ratio_prev"] = g["volume"].shift(1) / vol20.replace(0, np.nan)
    df["rvol20"] = g["cc"].transform(lambda s: s.rolling(20).std().shift(1))
    rng = (df["high"] - df["low"]).replace(0, np.nan)
    df["range_pos_prev"] = ((df["close"] - df["low"]) / rng).groupby(df["ticker"]).shift(1)
    hi20 = g["high"].transform(lambda s: s.rolling(20).max().shift(1))
    lo20 = g["low"].transform(lambda s: s.rolling(20).min().shift(1))
    df["dist_high20"] = df["prev_close"] / hi20 - 1
    df["dist_low20"] = df["prev_close"] / lo20 - 1
    dollar = (df["close"] * df["volume"]).groupby(df["ticker"]).transform(lambda s: s.rolling(20).mean().shift(1))
    df["adv20_prev"] = dollar
    df["log_dv"] = np.log(dollar.clip(lower=1.0))
    df["raw_close_prev"] = (df["close"] / df["factor"]).groupby(df["ticker"]).shift(1)
    df["tradable"] = (df["raw_close_prev"] >= config.MIN_PRICE) & (df["adv20_prev"] >= config.MIN_ADV_USD)
    df["dow"] = df["date"].dt.dayofweek
    df = df.merge(spy, on="date", how="left")
    df["gap_idio"] = df["gap"] - df["spy_gap"]
    df["mkt_gap_med"] = df.groupby("date")["gap"].transform("median")
    sec, ids = sector_map()
    df["sector"] = df["ticker"].map(sec).fillna("Unknown")
    df["sector_id"] = df["sector"].map(ids).fillna(-1).astype(int)
    df["sector_gap_med"] = df.groupby(["date", "sector"])["gap"].transform("median")
    df = df[(df["oc"].abs() < 0.5) & (df["gap"].abs() < 0.5)]
    return df


def _fit(train: pd.DataFrame, valid: pd.DataFrame | None, rounds: int | None = None) -> lgb.Booster:
    dtr = lgb.Dataset(train[FEATURES], label=(train["oc_rel"] > 0).astype(int), categorical_feature=["sector_id", "dow"], free_raw_data=False)
    if valid is not None and rounds is None:
        dva = lgb.Dataset(valid[FEATURES], label=(valid["oc_rel"] > 0).astype(int), reference=dtr, categorical_feature=["sector_id", "dow"])
        return lgb.train(PARAMS, dtr, num_boost_round=NUM_ROUNDS, valid_sets=[dva], callbacks=[lgb.early_stopping(EARLY_STOP, verbose=False)])
    return lgb.train(PARAMS, dtr, num_boost_round=rounds or 300)


def _selective(test: pd.DataFrame, p: np.ndarray) -> dict:
    """Hit rates when only the most confident slice is acted on, both sides, before costs."""
    out = {}
    y = (test["oc"].values > 0)
    oc = test["oc"].values
    n = len(test)
    for th in THRESHOLDS:
        long = p >= th
        short = p <= 1 - th
        act = long | short
        if act.sum() == 0:
            out[f"p{th:.2f}"] = {"coverage": 0.0, "n": 0}
            continue
        correct = (long & y) | (short & ~y)
        signed = np.where(long, oc, -oc)[act]
        out[f"p{th:.2f}"] = {
            "coverage": round(float(act.mean()), 4), "n": int(act.sum()), "hit_rate": round(float(correct[act].mean()), 4),
            "mean_bps": round(float(signed.mean() * 1e4), 1), "longs": int(long.sum()), "shorts": int(short.sum()),
        }
    # top-K / bottom-K per day among tradable names: what a 5-name daily sleeve would have done
    t = test.assign(p=p)
    t = t[t["tradable"]]
    for k in (3, TOPK, 10):
        rows = []
        for _, day in t.groupby("date", sort=True):
            if len(day) < 2 * k:
                continue
            d = day.sort_values("p")
            bot, top = d.head(k), d.tail(k)
            rows.append({"long_hits": int((top["oc"] > 0).sum()), "short_hits": int((bot["oc"] < 0).sum()),
                         "long_bps": float(top["oc"].mean() * 1e4), "short_bps": float(-bot["oc"].mean() * 1e4)})
        if rows:
            r = pd.DataFrame(rows)
            out["topk" if k == TOPK else f"top{k}"] = {"k": k, "days": int(len(r)), "long_hit_rate": round(float(r["long_hits"].sum() / (k * len(r))), 4),
                       "short_hit_rate": round(float(r["short_hits"].sum() / (k * len(r))), 4),
                       "long_bps": round(float(r["long_bps"].mean()), 1), "short_bps": round(float(r["short_bps"].mean()), 1),
                       "ls_bps": round(float((r["long_bps"] + r["short_bps"]).mean() / 2), 1)}
    t["dec"] = t.groupby("date")["p"].transform(lambda s: pd.qcut(s.rank(method="first"), 10, labels=False))
    out["decile_spread_bps"] = round(float((t[t["dec"] == 9]["oc"].mean() - t[t["dec"] == 0]["oc"].mean()) * 1e4), 1)
    out["auc_rel"] = round(float(roc_auc_score((test["oc_rel"].values > 0), p)), 4)
    base = float(y.mean())
    out["base_up_rate"] = round(base, 4)
    out["accuracy_at_half"] = round(float(((p >= 0.5) == y).mean()), 4)
    out["auc"] = round(float(roc_auc_score(y, p)), 4)
    return out


def _calibration(y: np.ndarray, p: np.ndarray) -> list[dict]:
    bins = [0, 0.4, 0.45, 0.48, 0.5, 0.52, 0.55, 0.6, 1.0]
    out = []
    idx = np.digitize(p, bins) - 1
    for b in range(len(bins) - 1):
        m = idx == b
        if m.sum() == 0:
            continue
        out.append({"lo": bins[b], "hi": bins[b + 1], "n": int(m.sum()), "mean_p": round(float(p[m].mean()), 4), "up_rate": round(float(y[m].mean()), 4)})
    return out


def train_gapmodel(csv_dir: Path = config.CSV_DIR, out_dir: Path = config.OUTPUT_DIR) -> dict:
    df = build_features(load_panel(csv_dir), load_spy(csv_dir))
    data = df.dropna(subset=FEATURES + ["oc"]).copy()
    data = data[data["tradable"]]
    data["oc_rel"] = data["oc"] - data.groupby("date")["oc"].transform("median")
    years = sorted(data["date"].dt.year.unique())
    folds = []
    oos_p, oos_y = [], []
    for ty in [y for y in years if y >= FIRST_TEST_YEAR]:
        train = data[data["date"].dt.year < ty]
        test = data[data["date"].dt.year == ty]
        if len(train) < 100_000 or len(test) < 10_000:
            continue
        cut = train["date"].quantile(0.9)
        booster = _fit(train[train["date"] < cut], train[train["date"] >= cut])
        p = booster.predict(test[FEATURES], num_iteration=booster.best_iteration)
        sel = _selective(test, p)
        sel.update({"year": int(ty), "train_rows": int(len(train)), "test_rows": int(len(test)), "best_iteration": int(booster.best_iteration)})
        folds.append(sel)
        oos_p.append(p)
        oos_y.append((test["oc"].values > 0).astype(int))
        folds[-1]["calibration"] = _calibration(oos_y[-1], p)
        log.info("gap model %s: auc %.4f acc %.4f top%d long %.3f short %.3f", ty, sel.get("auc", float("nan")), sel["accuracy_at_half"], TOPK,
                 sel.get("topk", {}).get("long_hit_rate", float("nan")), sel.get("topk", {}).get("short_hit_rate", float("nan")))
    oos_p_all = np.concatenate(oos_p) if oos_p else np.array([])
    oos_y_all = np.concatenate(oos_y) if oos_y else np.array([])
    calib = _calibration(oos_y_all, oos_p_all) if len(oos_p_all) else []
    # final model on everything, rounds = median best iteration of the folds (or 300)
    rounds = int(np.median([f["best_iteration"] for f in folds])) if folds else 300
    final = _fit(data, None, rounds=max(50, rounds))
    out_dir.mkdir(parents=True, exist_ok=True)
    final.save_model(str(out_dir / "gapmodel.txt"))
    imp = dict(zip(FEATURES, [int(x) for x in final.feature_importance("gain")]))
    last_date = data["date"].max()
    # static per-ticker features as of the last session, for live scoring at the next open
    last = df[df["date"] == df["date"].max()].copy()
    last["close_raw"] = last["close"] / last["factor"]
    last["close_adj"] = last["close"]
    # the live features for the NEXT session use today's row as "prev": shift the definitions forward
    stat = pd.DataFrame({
        "ticker": last["ticker"], "sector": last["sector"], "sector_id": last["sector_id"], "asof": last["date"].dt.strftime("%Y-%m-%d"),
        "close_raw": last["close_raw"], "close_adj": last["close_adj"],
    })
    # recompute "prev" features relative to the last row itself (they become *_prev for tomorrow)
    g = df.groupby("ticker", sort=False)
    nxt = pd.DataFrame({
        "ticker": df["ticker"], "date": df["date"],
        "atr20_pct": df.groupby("ticker", sort=False)["tr_pct"].transform(lambda s: s.rolling(20).mean()),
        "gap_prev": df["gap"], "cc_prev": df["cc"], "oc_prev": df["oc"],
        "r3_prev": df["close"] / g["close"].shift(3) - 1, "r5_prev": df["close"] / g["close"].shift(5) - 1,
        "mom20_prev": df["close"] / g["close"].shift(20) - 1, "mom60_prev": df["close"] / g["close"].shift(60) - 1,
        "vol_ratio_prev": df["volume"] / g["volume"].transform(lambda s: s.rolling(20).mean()).replace(0, np.nan),
        "rvol20": g["cc"].transform(lambda s: s.rolling(20).std()),
        "range_pos_prev": (df["close"] - df["low"]) / (df["high"] - df["low"]).replace(0, np.nan),
        "dist_high20": df["close"] / g["high"].transform(lambda s: s.rolling(20).max()) - 1,
        "dist_low20": df["close"] / g["low"].transform(lambda s: s.rolling(20).min()) - 1,
        "log_dv": np.log((df["close"] * df["volume"]).groupby(df["ticker"]).transform(lambda s: s.rolling(20).mean()).clip(lower=1.0)),
        "tradable": ((df["close"] / df["factor"]) >= config.MIN_PRICE) & ((df["close"] * df["volume"]).groupby(df["ticker"]).transform(lambda s: s.rolling(20).mean()) >= config.MIN_ADV_USD),
    })
    nxt = nxt[nxt["date"] == last_date].drop(columns=["date"])
    stat = stat.merge(nxt, on="ticker", how="left")[STATIC_COLS]
    stat.to_csv(out_dir / "gap_static.csv", index=False, float_format="%.6f")
    spy = load_spy(csv_dir)
    spy_last = pd.read_csv(csv_dir / "SPY.csv", usecols=["date", "open", "close", "factor"]).sort_values("date")
    spy_last["date"] = pd.to_datetime(spy_last["date"])
    srow = spy_last.iloc[-1]
    spy_static = {"asof": srow["date"].strftime("%Y-%m-%d"), "close_raw": float(srow["close"] / srow["factor"]),
                  "spy_cc_prev": float(spy_last["close"].iloc[-1] / spy_last["close"].iloc[-2] - 1),
                  "spy_mom5": float(spy_last["close"].iloc[-1] / spy_last["close"].iloc[-6] - 1)}
    card = {
        "model": "gap", "desc": "open-aware LightGBM classifier: P(close > open) from features known at the 9:30 open",
        "trained_at": datetime.now(timezone.utc).isoformat(timespec="seconds"), "data_end_date": last_date.strftime("%Y-%m-%d"),
        "rows": int(len(data)), "tickers": int(data["ticker"].nunique()), "features": FEATURES, "params": PARAMS, "final_rounds": rounds,
        "walk_forward": folds, "calibration_oos": calib, "feature_importance_gain": imp, "spy_static": spy_static,
        "pooled_oos": _selective(pd.concat([data[data["date"].dt.year == f["year"]] for f in folds]), oos_p_all) if folds else {},
        "label": "open-to-close return minus the day's cross-sectional median (> 0)",
        "gate": {"rule": "pooled walk-forward top-5 long hit rate >= 0.55 AND top-5 short hit rate >= 0.53 AND long-short >= +10 bps/day before costs, and the latest test year's top-5 long >= 0.53", "passes": None},
    }
    pooled = card["pooled_oos"]
    try:
        last_year = folds[-1]["topk"]
        card["gate"]["passes"] = bool(pooled["topk"]["long_hit_rate"] >= 0.55 and pooled["topk"]["short_hit_rate"] >= 0.53
                                      and pooled["topk"]["ls_bps"] >= 10 and last_year["long_hit_rate"] >= 0.53)
    except Exception:  # noqa: BLE001
        card["gate"]["passes"] = False
    (out_dir / "gapmodel_card.json").write_text(json.dumps(card, indent=1, default=float))
    (out_dir / "gap_report.md").write_text(_report(card))
    return {"data_end_date": card["data_end_date"], "rows": card["rows"], "gate_passes": card["gate"]["passes"],
            "pooled": {k: v for k, v in pooled.items() if k in ("auc", "accuracy_at_half", "base_up_rate", "topk", "p0.60")}}


def _report(card: dict) -> str:
    L = [f"# Gap model (open-aware direction) — data to {card['data_end_date']}", "",
         "P(open-to-close return beats the day's median) from what is known at the 9:30 open: the overnight gap (raw, vs SPY, vs the stock's ATR), yesterday's move, "
         "5/20/60-day momentum, volume, range position, SPY's gap and momentum, the market's and the sector's median gap, day of week.", "",
         "## Walk-forward by year (train on earlier years, test on the year shown; tradable names only; before costs)", "",
         "| year | rows | AUC (vs median) | AUC (abs) | top-3 long / short hit | top-5 long hit / bps | bottom-5 short hit / bps | D10−D1 bps/day |", "|---|---|---|---|---|---|---|---|"]
    for f in card["walk_forward"]:
        t3 = f.get("top3", {}); t = f.get("topk", {})
        L.append(f"| {f['year']} | {f['test_rows']:,} | {f.get('auc_rel', float('nan')):.3f} | {f.get('auc', float('nan')):.3f} | "
                 f"{t3.get('long_hit_rate', float('nan')):.3f} / {t3.get('short_hit_rate', float('nan')):.3f} | "
                 f"{t.get('long_hit_rate', float('nan')):.3f} / {t.get('long_bps', float('nan'))} | {t.get('short_hit_rate', float('nan')):.3f} / {t.get('short_bps', float('nan'))} | {f.get('decile_spread_bps', float('nan'))} |")
    p = card.get("pooled_oos", {})
    L += ["", "## Pooled out-of-sample", ""]
    for k, v in p.items():
        if k != "calibration":
            L.append(f"- {k}: {v}")
    L += ["", "## Calibration (out of sample): predicted P(up) bin -> observed up rate", "", "| bin | n | mean p | up rate |", "|---|---|---|---|"]
    for c in card["calibration_oos"]:
        L.append(f"| {c['lo']:.2f}–{c['hi']:.2f} | {c['n']:,} | {c['mean_p']:.3f} | {c['up_rate']:.3f} |")
    L += ["", f"Gate: {card['gate']['rule']} → **{'PASS' if card['gate']['passes'] else 'FAIL'}**", "",
          "Top features by gain: " + ", ".join(f"{k} ({v})" for k, v in sorted(card["feature_importance_gain"].items(), key=lambda kv: -kv[1])[:8])]
    return "\n".join(L) + "\n"


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    print(json.dumps(train_gapmodel(), indent=1, default=float))
