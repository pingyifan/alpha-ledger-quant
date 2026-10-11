"""Compare return horizons (labels) and LightGBM settings out of sample on the real panel.

Usage (after the Qlib store exists under $ALQ_DATA_DIR):
    python -m research.label_experiments --labels oc,oo,cc_qlib,co --params base,reg
Prints a table of validation-year IC / Rank IC / best iteration / top-5 hit rates /
decile long-short mean (bps, net of 4 bps) and writes research/experiments_<date>.json.
"""
from __future__ import annotations

import argparse
import json
import logging
import math
from datetime import date

import pandas as pd

from pipeline import config
from pipeline.qlib_env import init_qlib, liquidity_frame, tradable_mask
from pipeline.train import train

LABELS = {
    "oc": "Ref($close, -1)/Ref($open, -1) - 1",          # next session open -> close (the ledger's rule)
    "oo": "Ref($open, -2)/Ref($open, -1) - 1",           # next open -> following open (one-session hold)
    "cc_qlib": "Ref($close, -2)/Ref($close, -1) - 1",    # Qlib's native label: next close -> following close
    "co": "Ref($open, -1)/$close - 1",                   # tonight's close -> next open (overnight only; not executable)
    "oc2": "Ref($close, -2)/Ref($open, -1) - 1",         # next open -> following close (two sessions)
}
PARAM_SETS = {
    "base": {"loss": "mse", "learning_rate": 0.05, "num_leaves": 63, "max_depth": 8, "feature_fraction": 0.8,
             "bagging_fraction": 0.8, "bagging_freq": 1, "lambda_l1": 10.0, "lambda_l2": 100.0, "min_data_in_leaf": 200,
             "num_threads": config.LGB_PARAMS["num_threads"], "seed": 2026, "verbosity": -1},
    "reg": dict(config.LGB_PARAMS),
    "qlib_bench": {"loss": "mse", "learning_rate": 0.2, "num_leaves": 210, "max_depth": 8, "colsample_bytree": 0.8879,
                   "subsample": 0.8789, "lambda_l1": 205.6999, "lambda_l2": 580.9768,
                   "num_threads": config.LGB_PARAMS["num_threads"], "seed": 2026, "verbosity": -1},
}


def basket_stats(pred: pd.Series, label: pd.Series) -> dict:
    df = pd.concat([pred, label], axis=1).dropna()
    start, end = df.index.get_level_values("datetime").min(), df.index.get_level_values("datetime").max()
    liq = liquidity_frame(start - pd.Timedelta(days=45), end).reindex(df.index)
    df["tradable"] = tradable_mask(liq).fillna(False).values
    cost = 2 * config.COST_PER_SIDE
    rows = []
    for dt, g in df[df["tradable"]].groupby(level="datetime"):
        if len(g) < 30:
            continue
        g = g.sort_values("score", ascending=False)
        k = max(1, len(g) // 10)
        rows.append({"ls": 0.5 * (g.head(k)["label"].mean() - g.tail(k)["label"].mean()) - cost,
                     "top5_hit": (g.head(5)["label"] > 0).mean(), "bot5_hit": (g.tail(5)["label"] < 0).mean(),
                     "top5_ret": g.head(5)["label"].mean() - cost, "base_up": (g["label"] > 0).mean(),
                     "univ": g["label"].mean()})
    d = pd.DataFrame(rows)
    ls = d["ls"]
    return {"days": int(len(d)), "ls_bps": round(float(ls.mean() * 1e4), 2),
            "ls_t": round(float(ls.mean() / ls.std() * math.sqrt(len(ls))), 2) if ls.std() > 0 else None,
            "ls_sharpe": round(float(ls.mean() / ls.std() * math.sqrt(252)), 2) if ls.std() > 0 else None,
            "top5_hit": round(float(d["top5_hit"].mean()), 4), "bot5_hit": round(float(d["bot5_hit"].mean()), 4),
            "top5_bps": round(float(d["top5_ret"].mean() * 1e4), 2), "base_up": round(float(d["base_up"].mean()), 4),
            "universe_bps": round(float(d["univ"].mean() * 1e4), 2)}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--labels", default="oc,oo,cc_qlib,co")
    ap.add_argument("--params", default="base,reg")
    args = ap.parse_args()
    logging.basicConfig(level=logging.WARNING)
    init_qlib()
    results = []
    for lab in args.labels.split(","):
        config.MODELS[lab] = {"label": LABELS[lab], "desc": lab, "entry": "", "exit": "", "scores_file": f"x_{lab}.csv",
                              "card_file": f"x_{lab}.json", "oos_file": f"x_{lab}", "history_file": f"x_{lab}_h.csv"}
        for pname in args.params.split(","):
            res = train(lab, params=PARAM_SETS[pname], refit=False)
            row = {"label": lab, "params": pname, **res.valid_metrics, **basket_stats(res.pred_valid, res.label_valid)}
            results.append(row)
            print(f"{lab:8s} {pname:10s} iter={row['best_iteration']:5d} IC={row['ic_mean']:+.4f} RankIC={row['rank_ic_mean']:+.4f} "
                  f"ICIR={row['icir']} | L/S {row['ls_bps']:+.1f} bps/d (t {row['ls_t']}) | top5 hit {row['top5_hit']:.1%} "
                  f"ret {row['top5_bps']:+.1f} | base up {row['base_up']:.1%} univ {row['universe_bps']:+.1f}", flush=True)
    out = config.ROOT / "research" / f"experiments_{date.today().isoformat()}.json"
    out.write_text(json.dumps(results, indent=2, default=str))
    print("written", out)


if __name__ == "__main__":
    main()
