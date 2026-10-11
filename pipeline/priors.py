"""Backtests of the Alpha Ledger playbook's priors on the full price panel.

Each test conditions on something known before the open (yesterday's move, the
overnight gap, a multi-day drawdown, 20-day momentum) and measures the open-to-
close return of that session, exactly how the ledger scores its calls. Numbers
are reported before costs; the ledger's round trip costs 4 bps.
"""
from __future__ import annotations

import json
import logging
import math
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

from . import config

log = logging.getLogger(__name__)
PERIODS = {"full": None, "last_24m": 24, "last_12m": 12}


def load_panel(csv_dir: Path = config.CSV_DIR) -> pd.DataFrame:
    frames = []
    for p in sorted(csv_dir.glob("*.csv")):
        t = p.stem.upper()
        if t in config.ETF_TICKERS:
            continue
        f = pd.read_csv(p, usecols=["date", "open", "high", "low", "close", "volume", "factor"])
        f["ticker"] = t
        frames.append(f)
    if not frames:
        raise RuntimeError("no CSV data for priors")
    df = pd.concat(frames, ignore_index=True)
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values(["ticker", "date"]).reset_index(drop=True)
    g = df.groupby("ticker", sort=False)
    df["prev_close"] = g["close"].shift(1)
    df["gap"] = df["open"] / df["prev_close"] - 1
    df["oc"] = df["close"] / df["open"] - 1
    df["cc"] = df["close"] / df["prev_close"] - 1
    df["cc_prev"] = g["cc"].shift(1)
    df["r3_prev"] = df["prev_close"] / g["close"].shift(4) - 1
    df["mom20_prev"] = df["prev_close"] / g["close"].shift(21) - 1
    dollar = df["close"] * df["volume"]
    df["adv20_prev"] = dollar.groupby(df["ticker"]).transform(lambda s: s.rolling(20).mean().shift(1))
    df["raw_close_prev"] = (df["close"] / df["factor"]).groupby(df["ticker"]).shift(1)
    df["tradable"] = (df["raw_close_prev"] >= config.MIN_PRICE) & (df["adv20_prev"] >= config.MIN_ADV_USD)
    df = df[df["oc"].abs() < 0.5]  # drop obvious data errors
    return df


def load_spy(csv_dir: Path = config.CSV_DIR) -> pd.DataFrame | None:
    p = csv_dir / "SPY.csv"
    if not p.exists():
        return None
    s = pd.read_csv(p, usecols=["date", "open", "close"])
    s["date"] = pd.to_datetime(s["date"])
    s = s.sort_values("date")
    s["prev_close"] = s["close"].shift(1)
    s["gap"] = s["open"] / s["prev_close"] - 1
    s["oc"] = s["close"] / s["open"] - 1
    s["cc"] = s["close"] / s["prev_close"] - 1
    s["up_streak_prev"] = (s["cc"].shift(1) > 0) & (s["cc"].shift(2) > 0) & (s["cc"].shift(3) > 0)
    s["down1_prev"] = s["cc"].shift(1) < -0.01
    return s


def _row(label: str, period: str, oc: pd.Series, sign_ref: pd.Series | None = None) -> dict:
    oc = oc.dropna()
    n = int(len(oc))
    if n == 0:
        return {"condition": label, "period": period, "n": 0}
    mean, std = oc.mean(), oc.std()
    out = {
        "condition": label,
        "period": period,
        "n": n,
        "mean_oc_bps": round(float(mean * 1e4), 1),
        "median_oc_bps": round(float(oc.median() * 1e4), 1),
        "share_up": round(float((oc > 0).mean()), 4),
        "t_stat": round(float(mean / std * math.sqrt(n)), 2) if std > 0 and n > 1 else None,
    }
    if sign_ref is not None:
        sr = sign_ref.reindex(oc.index)
        out["continuation_rate"] = round(float((np.sign(oc) == np.sign(sr)).mean()), 4)
    return out


def _periods(df: pd.DataFrame, date_col: str = "date"):
    end = df[date_col].max()
    for name, months in PERIODS.items():
        if months is None:
            yield name, df
        else:
            yield name, df[df[date_col] > end - pd.DateOffset(months=months)]


def run_priors(csv_dir: Path = config.CSV_DIR) -> dict:
    df = load_panel(csv_dir)
    tr = df[df["tradable"]]
    tests: dict[str, list[dict]] = {}

    # 1. overnight gap buckets -> open-to-close continuation or fade
    bins = [-np.inf, -0.05, -0.02, -0.01, -0.003, 0.003, 0.01, 0.02, 0.05, np.inf]
    labels = ["gap <= -5%", "-5% < gap <= -2%", "-2% < gap <= -1%", "-1% < gap <= -0.3%", "flat (|gap| < 0.3%)",
              "+0.3% <= gap < +1%", "+1% <= gap < +2%", "+2% <= gap < +5%", "gap >= +5%"]
    tr = tr.assign(gap_bucket=pd.cut(tr["gap"], bins=bins, labels=labels, right=False))
    rows = []
    for period, sub in _periods(tr):
        for lab in labels:
            s = sub[sub["gap_bucket"] == lab]
            rows.append(_row(lab, period, s["oc"], s["gap"]))
    tests["gap_buckets"] = rows

    # 2. day two after a big close-to-close move
    conds = {"yesterday +10% or more": tr["cc_prev"] >= 0.10, "yesterday +5% to +10%": (tr["cc_prev"] >= 0.05) & (tr["cc_prev"] < 0.10),
             "yesterday -5% to -10%": (tr["cc_prev"] <= -0.05) & (tr["cc_prev"] > -0.10), "yesterday -10% or worse": tr["cc_prev"] <= -0.10}
    rows = []
    for period, sub in _periods(tr):
        for lab, mask in conds.items():
            s = sub[mask.reindex(sub.index).fillna(False)]
            rows.append(_row(lab, period, s["oc"], s["cc_prev"]))
    tests["day_two_after_big_move"] = rows

    # 3. multi-day drawdown bounce
    conds = {"3-day return <= -15%": tr["r3_prev"] <= -0.15, "3-day return -15% to -10%": (tr["r3_prev"] > -0.15) & (tr["r3_prev"] <= -0.10),
             "3-day return >= +15%": tr["r3_prev"] >= 0.15}
    rows = []
    for period, sub in _periods(tr):
        for lab, mask in conds.items():
            s = sub[mask.reindex(sub.index).fillna(False)]
            rows.append(_row(lab, period, s["oc"]))
    tests["three_day_move"] = rows

    # 4. 20-day momentum deciles (cross-sectional per day)
    tr = tr.assign(mom_dec=tr.groupby("date")["mom20_prev"].transform(
        lambda s: pd.qcut(s.rank(method="first"), 10, labels=False) + 1 if s.notna().sum() >= 50 else np.nan))
    rows = []
    for period, sub in _periods(tr):
        for dec, lab in [(10, "momentum top decile (20d)"), (1, "momentum bottom decile (20d)")]:
            s = sub[sub["mom_dec"] == dec]
            rows.append(_row(lab, period, s["oc"]))
    tests["momentum_20d"] = rows

    # 5. base rates by year (the always-up baseline)
    yr = tr.groupby(tr["date"].dt.year)["oc"]
    tests["base_rate_by_year"] = [
        {"year": int(y), "n": int(len(s)), "share_up": round(float((s > 0).mean()), 4), "mean_oc_bps": round(float(s.mean() * 1e4), 1)}
        for y, s in yr
    ]

    # 6. SPY conditionals
    spy = load_spy(csv_dir)
    if spy is not None:
        conds = {"SPY all sessions": spy["oc"].notna(), "SPY gap >= +0.5%": spy["gap"] >= 0.005, "SPY gap <= -0.5%": spy["gap"] <= -0.005,
                 "SPY after 3 up days": spy["up_streak_prev"], "SPY after a -1% day": spy["down1_prev"]}
        rows = []
        for period, sub in _periods(spy):
            for lab, mask in conds.items():
                s = sub[mask.reindex(sub.index).fillna(False)]
                rows.append(_row(lab, period, s["oc"], s["gap"] if "gap" in lab else None))
        tests["spy"] = rows
        tests["spy_base_rate_by_year"] = [
            {"year": int(y), "n": int(len(s)), "share_up": round(float((s > 0).mean()), 4), "mean_oc_bps": round(float(s.mean() * 1e4), 1)}
            for y, s in spy.groupby(spy["date"].dt.year)["oc"]
        ]

    report = {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "panel": {"tickers": int(df["ticker"].nunique()), "start": str(df["date"].min().date()), "end": str(df["date"].max().date()),
                  "stock_days": int(len(df)), "tradable_stock_days": int(len(tr))},
        "cost_round_trip_bps": 2 * config.COST_PER_SIDE * 1e4,
        "tests": tests,
        "verdicts": verdicts(tests),
    }
    config.OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    (config.OUTPUT_DIR / "priors_report.json").write_text(json.dumps(report, indent=2, default=str))
    (config.OUTPUT_DIR / "priors_report.md").write_text(render_priors_markdown(report))
    return report


def _find(rows: list[dict], cond: str, period: str = "full") -> dict | None:
    for r in rows:
        if r.get("condition") == cond and r.get("period") == period:
            return r
    return None


def _verdict_from(r: dict | None, long_side: bool, cost_bps: float) -> str:
    if not r or r.get("n", 0) < 200 or r.get("t_stat") is None:
        return "not enough data"
    m, t = r["mean_oc_bps"], r["t_stat"]
    edge = m if long_side else -m            # P&L of the prior's side, bps per session, before costs
    t_edge = t if long_side else -t
    if abs(t) < 2:
        return f"no reliable edge (mean {m:+.1f} bps, t = {t}, n = {r['n']:,})"
    if edge > cost_bps:
        return f"supported: {edge:+.1f} bps/session for that side, clears {cost_bps:.0f} bps costs (t = {t_edge}, n = {r['n']:,})"
    if edge > 0:
        return f"positive but inside costs ({edge:+.1f} bps vs {cost_bps:.0f} bps, t = {t_edge}, n = {r['n']:,})"
    return f"goes the other way: {edge:+.1f} bps/session for that side (t = {t_edge}, n = {r['n']:,})"


def verdicts(tests: dict) -> dict:
    cost = 2 * config.COST_PER_SIDE * 1e4
    g = tests.get("gap_buckets", [])
    d2 = tests.get("day_two_after_big_move", [])
    d3 = tests.get("three_day_move", [])
    mom = tests.get("momentum_20d", [])
    out = {
        "long a stock that gapped up 2-5% (continuation)": _verdict_from(_find(g, "+2% <= gap < +5%"), True, cost),
        "long a stock that gapped up 5%+ (continuation)": _verdict_from(_find(g, "gap >= +5%"), True, cost),
        "short a stock that gapped down 2-5% (continuation)": _verdict_from(_find(g, "-5% < gap <= -2%"), False, cost),
        "short a stock that gapped down 5%+ (continuation)": _verdict_from(_find(g, "gap <= -5%"), False, cost),
        "fade a +5% gap (short)": _verdict_from(_find(g, "gap >= +5%"), False, cost),
        "fade a -5% gap (long)": _verdict_from(_find(g, "gap <= -5%"), True, cost),
        "day-two fade after a +10% day (short)": _verdict_from(_find(d2, "yesterday +10% or more"), False, cost),
        "day-two bounce after a -10% day (long)": _verdict_from(_find(d2, "yesterday -10% or worse"), True, cost),
        "oversold bounce after a -15% three-day drop (long)": _verdict_from(_find(d3, "3-day return <= -15%"), True, cost),
        "20-day momentum top decile (long)": _verdict_from(_find(mom, "momentum top decile (20d)"), True, cost),
        "20-day momentum bottom decile (short)": _verdict_from(_find(mom, "momentum bottom decile (20d)"), False, cost),
    }
    return out


def _table(rows: list[dict], cont: bool) -> list[str]:
    head = "| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up |" + (" Continuation |" if cont else "") + " t |"
    sep = "|---|---|---|---|---|---|" + ("---|" if cont else "") + "---|"
    out = [head, sep]
    for r in rows:
        if r.get("n", 0) == 0:
            out.append(f"| {r['condition']} | {r['period']} | 0 | | | |" + (" |" if cont else "") + " |")
            continue
        c = f" {r.get('continuation_rate', float('nan')):.1%} |" if cont else ""
        out.append(f"| {r['condition']} | {r['period']} | {r['n']:,} | {r['mean_oc_bps']:+.1f} | {r['median_oc_bps']:+.1f} | "
                   f"{r['share_up']:.1%} |{c} {r['t_stat']} |")
    return out


def render_priors_markdown(rep: dict) -> str:
    p = rep["panel"]
    L = [
        "# Playbook priors, backtested on the full panel",
        "",
        f"{p['tickers']} tickers, {p['start']} to {p['end']}, {p['stock_days']:,} stock-days "
        f"({p['tradable_stock_days']:,} pass the ledger's price and liquidity filter). "
        "Every row measures the **open-to-close return of the session after the condition is known**, before costs; "
        f"the ledger pays about {rep['cost_round_trip_bps']:.0f} bps per round trip. "
        "Continuation = share of sessions where the open-to-close move had the same sign as the gap or the prior move.",
        "",
        "## Verdicts on the playbook's priors",
        "",
        "| Prior | Verdict |", "|---|---|",
    ]
    for k, v in rep["verdicts"].items():
        L.append(f"| {k} | {v} |")
    t = rep["tests"]
    L += ["", "## 1. Overnight gap -> open-to-close", ""] + _table(t["gap_buckets"], True)
    L += ["", "## 2. Day two after a big close-to-close move", ""] + _table(t["day_two_after_big_move"], True)
    L += ["", "## 3. Three-day moves", ""] + _table(t["three_day_move"], False)
    L += ["", "## 4. 20-day momentum deciles", ""] + _table(t["momentum_20d"], False)
    L += ["", "## 5. Base rate: share of tradable stock-days that closed above the open", "", "| Year | n | Share up | Mean OC (bps) |", "|---|---|---|---|"]
    for r in t["base_rate_by_year"]:
        L.append(f"| {r['year']} | {r['n']:,} | {r['share_up']:.1%} | {r['mean_oc_bps']:+.1f} |")
    if "spy" in t:
        L += ["", "## 6. SPY conditionals", ""] + _table(t["spy"], False)
        L += ["", "| Year | n | SPY share up (open-to-close) | Mean OC (bps) |", "|---|---|---|---|"]
        for r in t["spy_base_rate_by_year"]:
            L.append(f"| {r['year']} | {r['n']} | {r['share_up']:.1%} | {r['mean_oc_bps']:+.1f} |")
    L += ["", "_Current index membership (survivorship bias favours longs slightly). Research output, not investment advice._", ""]
    return "\n".join(L)
