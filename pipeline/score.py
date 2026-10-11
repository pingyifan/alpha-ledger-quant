"""Tonight's cross-sectional scores for the next session, written to output/.

scores_latest.csv columns
    asof_date      last complete session the features were computed from
    ticker, name, sector, index
    score          model output (higher = higher expected open-to-close return next session)
    rank           1 = best among tradable names
    rank_pct       0..1 percentile among tradable names (1 = best)
    decile         1..10 among tradable names (10 = best)
    close          last raw close (USD)
    adv20_usd      20-day average dollar volume
    tradable       price >= MIN_PRICE and adv20 >= MIN_ADV_USD and enough history
"""
from __future__ import annotations

import logging

import numpy as np
import pandas as pd

from . import config
from .qlib_env import calendar, liquidity_frame, tradable_mask
from .train import TrainResult

log = logging.getLogger(__name__)


def score_latest(res: TrainResult, universe: pd.DataFrame) -> pd.DataFrame:
    from qlib.data import D

    cal = calendar()
    end = cal[-1]
    pred = res.model.predict(res.dataset, segment="test")
    pred = pred.xs(end, level="datetime") if "datetime" in pred.index.names else pred
    pred.name = "score"

    liq = liquidity_frame(cal[-30], end)
    liq_last = liq.groupby(level="instrument").tail(1).droplevel("datetime")
    hist = D.features(D.instruments(config.MARKET_NAME), ["$close"], start_time=cal[0], end_time=end, freq="day")
    n_hist = hist.groupby(level="instrument").size().rename("n_history")

    df = pd.concat([pred, liq_last, n_hist], axis=1)
    df = df[df["score"].notna()]
    df["tradable"] = tradable_mask(df) & (df["n_history"] >= config.MIN_HISTORY_DAYS)
    df.index.name = "ticker"
    df = df.reset_index()
    df["ticker"] = df["ticker"].str.upper()
    uni = universe.drop_duplicates("ticker").set_index("ticker")
    df = df.join(uni[["name", "sector", "index"]], on="ticker")
    df = df[df["index"] != "ETF"]

    trad = df["tradable"]
    df["rank"] = np.nan
    df.loc[trad, "rank"] = df.loc[trad, "score"].rank(ascending=False, method="first")
    n_trad = int(trad.sum())
    df.loc[trad, "rank_pct"] = 1 - (df.loc[trad, "rank"] - 1) / max(n_trad - 1, 1)
    df.loc[trad, "decile"] = np.ceil(df.loc[trad, "rank_pct"].clip(1e-9, 1) * 10).clip(1, 10)
    df["asof_date"] = end.strftime("%Y-%m-%d")
    df["model"] = res.key
    df["horizon"] = res.spec["desc"]
    df = df.rename(columns={"raw_close": "close"})
    df["close"] = df["close"].round(4)
    df["adv20_usd"] = df["adv20_usd"].round(0)
    df["score"] = df["score"].round(6)
    cols = ["asof_date", "model", "horizon", "ticker", "name", "sector", "index", "score", "rank", "rank_pct", "decile",
            "close", "adv20_usd", "tradable"]
    df = df[cols].sort_values(["tradable", "score"], ascending=[False, False]).reset_index(drop=True)
    df["rank"] = df["rank"].astype("Int64")
    df["decile"] = df["decile"].astype("Int64")
    df["rank_pct"] = df["rank_pct"].round(4)
    return df


def write_scores(df: pd.DataFrame, key: str = config.DEFAULT_MODEL) -> dict:
    spec = config.MODELS[key]
    config.OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(config.OUTPUT_DIR / spec["scores_file"], index=False)
    asof = df["asof_date"].iloc[0]
    trad = df[df["tradable"]]
    top = trad.head(config.HISTORY_TOP_N).assign(side="top")
    bottom = trad.tail(config.HISTORY_TOP_N).assign(side="bottom")
    new_rows = pd.concat([top, bottom])[["asof_date", "ticker", "side", "rank", "score", "close"]]
    hist_path = config.OUTPUT_DIR / spec["history_file"]
    hist = new_rows
    if hist_path.exists():
        prev = pd.read_csv(hist_path)
        prev = prev[prev["asof_date"] != asof]
        if not prev.empty:
            hist = pd.concat([prev, new_rows], ignore_index=True)
    keep_dates = sorted(hist["asof_date"].unique())[-config.HISTORY_KEEP_DAYS:]
    hist = hist[hist["asof_date"].isin(keep_dates)].sort_values(["asof_date", "side", "rank"])
    hist.to_csv(hist_path, index=False)
    return {
        "model": key,
        "asof_date": asof,
        "n_scored": int(len(df)),
        "n_tradable": int(df["tradable"].sum()),
        "top5": trad.head(5)["ticker"].tolist(),
        "bottom5": trad.tail(5)["ticker"].tolist()[::-1],
    }
