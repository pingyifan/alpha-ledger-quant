"""Synthetic price panel for exercising the pipeline without network access.

Generates N tickers of GBM daily bars (plus SPY/QQQ/IWM) with two deliberately
planted, weak patterns so the backtests have something to find:
  * open-to-close mean reversion against the overnight gap (fade edge)
  * mild 20-day momentum in the open-to-close return
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from pipeline import config
from pipeline.download import COLUMNS


def make_synthetic(n_tickers: int = 60, n_days: int = 1500, seed: int = 7) -> dict:
    rng = np.random.default_rng(seed)
    config.CSV_DIR.mkdir(parents=True, exist_ok=True)
    config.AUX_DIR.mkdir(parents=True, exist_ok=True)
    config.OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for p in config.CSV_DIR.glob("*.csv"):
        p.unlink()
    dates = pd.bdate_range(end=pd.Timestamp("2026-10-09"), periods=n_days)
    market = rng.normal(0.0003, 0.009, n_days)
    tickers = [f"T{i:03d}" for i in range(n_tickers)] + config.ETF_TICKERS
    rows_uni = []
    for i, t in enumerate(tickers):
        is_etf = t in config.ETF_TICKERS
        vol = 0.006 if is_etf else rng.uniform(0.012, 0.03)
        beta = 1.0 if is_etf else rng.uniform(0.6, 1.5)
        close = np.empty(n_days)
        open_ = np.empty(n_days)
        price = rng.uniform(20, 300)
        mom = 0.0
        for d in range(n_days):
            gap = rng.normal(0, vol * 0.6) + 0.4 * beta * market[d]
            o = price * (1 + gap)
            # planted: fade 20% of the gap intraday, plus mild momentum carry
            oc = rng.normal(0, vol) + 0.6 * beta * market[d] - 0.20 * gap + 0.02 * mom
            c = o * (1 + oc)
            open_[d], close[d] = o, c
            mom = 0.9 * mom + (c / price - 1)
            price = c
        high = np.maximum(open_, close) * (1 + np.abs(rng.normal(0, vol / 2, n_days)))
        low = np.minimum(open_, close) * (1 - np.abs(rng.normal(0, vol / 2, n_days)))
        volume = rng.lognormal(np.log(2e6 if not is_etf else 5e7), 0.4, n_days)
        f = pd.DataFrame({
            "symbol": t, "date": dates.strftime("%Y-%m-%d"), "open": open_, "high": high, "low": low, "close": close,
            "volume": volume, "factor": 1.0, "adjclose": close,
        })
        f[COLUMNS].to_csv(config.CSV_DIR / f"{t}.csv", index=False)
        rows_uni.append({"ticker": t, "name": f"Synthetic {t}", "sector": "ETF" if is_etf else f"Sector {i % 5}",
                         "index": "ETF" if is_etf else ("SP500" if i % 2 else "SP400")})
    pd.DataFrame(rows_uni).to_csv(config.OUTPUT_DIR / "universe.csv", index=False)
    vix = pd.DataFrame({"symbol": "VIX", "date": dates.strftime("%Y-%m-%d"), "close": 15 + 10 * np.abs(market).cumsum() % 20})
    vix.to_csv(config.AUX_DIR / "VIX.csv", index=False)
    return {"tickers": len(tickers), "days": n_days}
