"""Score the gap model live from the quote relay (standalone: needs only pandas, numpy, lightgbm).

    python gap_score.py --static gap_static.csv --model gapmodel.txt --card gapmodel_card.json \
        --quotes quotes_latest.json --out gap_scores.csv

Writes one row per universe name with the official open from the relay: gap, p_up and the
model's rank. The ledger treats p_up as a prior for the open-to-close move; whether it is
used at all is decided by the gate in gapmodel_card.json (see gap_report.md).
"""
from __future__ import annotations

import argparse
import json
import math

import numpy as np
import pandas as pd

FEATURES = [
    "gap", "gap_idio", "gap_z", "gap_prev", "cc_prev", "oc_prev", "r3_prev", "r5_prev", "mom20_prev", "mom60_prev",
    "vol_ratio_prev", "rvol20", "range_pos_prev", "dist_high20", "dist_low20", "log_dv", "dow",
    "spy_gap", "spy_cc_prev", "spy_mom5", "mkt_gap_med", "sector_gap_med", "sector_id",
]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--static", required=True)
    ap.add_argument("--model", required=True)
    ap.add_argument("--card", required=True)
    ap.add_argument("--quotes", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    import lightgbm as lgb

    stat = pd.read_csv(a.static)
    card = json.load(open(a.card))
    q = json.load(open(a.quotes))
    quotes = q["quotes"]
    session = q["session_date"]
    if stat["asof"].iloc[0] >= session:
        raise SystemExit(f"static features as of {stat['asof'].iloc[0]} are not before the session {session}")
    spy = quotes.get("SPY")
    if not spy or not spy.get("open"):
        raise SystemExit("no SPY open in the relay snapshot")
    spy_static = card["spy_static"]
    spy_gap = spy["open"] / spy_static["close_raw"] - 1
    rows = []
    for _, r in stat.iterrows():
        qq = quotes.get(r["ticker"])
        if not qq or not qq.get("open") or not r["close_raw"] or math.isnan(r["close_raw"]):
            continue
        gap = qq["open"] / r["close_raw"] - 1
        if abs(gap) > 0.5:
            continue
        rows.append({**r.to_dict(), "open_today": qq["open"], "last": qq.get("last"), "gap": gap})
    df = pd.DataFrame(rows)
    if df.empty:
        raise SystemExit("no names could be matched between the relay and the static features")
    df["gap_idio"] = df["gap"] - spy_gap
    df["gap_z"] = df["gap"] / df["atr20_pct"].replace(0, np.nan)
    df["spy_gap"] = spy_gap
    df["spy_cc_prev"] = spy_static["spy_cc_prev"]
    df["spy_mom5"] = spy_static["spy_mom5"]
    df["mkt_gap_med"] = df["gap"].median()
    df["sector_gap_med"] = df.groupby("sector")["gap"].transform("median")
    df["dow"] = pd.Timestamp(session).dayofweek
    booster = lgb.Booster(model_file=a.model)
    df["p_up"] = booster.predict(df[FEATURES])
    df = df.sort_values("p_up", ascending=False).reset_index(drop=True)
    df["rank"] = np.arange(1, len(df) + 1)
    df["decile"] = (10 - (df["rank"] - 1) * 10 // len(df)).clip(1, 10)
    cols = ["ticker", "sector", "tradable", "close_raw", "open_today", "last", "gap", "gap_idio", "gap_z", "p_up", "rank", "decile"]
    df[cols].to_csv(a.out, index=False, float_format="%.6f")
    gate = card.get("gate", {})
    print(json.dumps({"session": session, "asof_static": stat["asof"].iloc[0], "n": int(len(df)), "spy_gap": round(spy_gap, 6),
                      "gate_passes": gate.get("passes"), "relay_asof": q.get("asof_et"), "out": a.out}))


if __name__ == "__main__":
    main()
