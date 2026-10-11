"""Download daily bars from Yahoo Finance and write Qlib-style CSVs.

One CSV per symbol in data/csv with columns
    symbol, date, open, high, low, close, volume, factor, adjclose
following Qlib's Yahoo collector conventions: factor = adjclose / close,
prices are multiplied by factor (split- and dividend-adjusted, continuous
across corporate actions), volume is divided by factor. Ratios within a day
(open-to-close) are unaffected; overnight gaps are correct across splits.
"""
from __future__ import annotations

import json
import logging
import time
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd
import yfinance as yf

from . import config

log = logging.getLogger(__name__)
COLUMNS = ["symbol", "date", "open", "high", "low", "close", "volume", "factor", "adjclose"]


def _frame_from_yf(df: pd.DataFrame, symbol: str) -> pd.DataFrame | None:
    """Convert one yfinance OHLCV frame (auto_adjust=False) to the CSV layout."""
    if df is None or df.empty:
        return None
    df = df.copy()
    df.columns = [str(c).strip().lower().replace(" ", "") for c in df.columns]
    needed = {"open", "high", "low", "close", "volume"}
    if not needed.issubset(df.columns):
        return None
    if "adjclose" not in df.columns:
        df["adjclose"] = df["close"]
    df = df[["open", "high", "low", "close", "volume", "adjclose"]].astype(float)
    df.index = pd.to_datetime(df.index).tz_localize(None)
    df = df[~df.index.duplicated(keep="last")].sort_index()
    df = df[df["close"].notna() & (df["close"] > 0)]
    if df.empty:
        return None
    factor = (df["adjclose"] / df["close"]).replace([np.inf, -np.inf], np.nan).ffill().bfill()
    out = pd.DataFrame(
        {
            "symbol": symbol,
            "date": df.index.strftime("%Y-%m-%d"),
            "open": df["open"].values * factor.values,
            "high": df["high"].values * factor.values,
            "low": df["low"].values * factor.values,
            "close": df["close"].values * factor.values,
            "volume": df["volume"].fillna(0).values / factor.values,
            "factor": factor.values,
            "adjclose": df["adjclose"].values,
        }
    )
    # Yahoo occasionally reports a zero open/high/low; patch with close so ratios stay finite
    for c in ["open", "high", "low"]:
        bad = ~(out[c] > 0)
        out.loc[bad, c] = out.loc[bad, "close"]
    return out


def _download_chunk(tickers: list[str], start: str) -> dict[str, pd.DataFrame]:
    raw = yf.download(
        tickers,
        start=start,
        auto_adjust=False,
        group_by="ticker",
        threads=True,
        progress=False,
        timeout=30,
    )
    frames: dict[str, pd.DataFrame] = {}
    if raw is None or raw.empty:
        return frames
    if len(tickers) == 1:
        f = _frame_from_yf(raw, tickers[0])
        if f is not None:
            frames[tickers[0]] = f
        return frames
    for t in tickers:
        if t in raw.columns.get_level_values(0):
            f = _frame_from_yf(raw[t].dropna(how="all"), t)
            if f is not None:
                frames[t] = f
    return frames


def download_all(tickers: list[str], start: str = config.START_DATE, chunk_size: int = 100, pause: float = 1.0) -> dict:
    """Download every ticker; retry failures one by one. Returns a meta dict."""
    config.CSV_DIR.mkdir(parents=True, exist_ok=True)
    config.AUX_DIR.mkdir(parents=True, exist_ok=True)
    tickers = sorted(set(tickers))
    got: dict[str, pd.DataFrame] = {}
    for i in range(0, len(tickers), chunk_size):
        chunk = tickers[i : i + chunk_size]
        for attempt in range(3):
            try:
                got.update(_download_chunk(chunk, start))
                break
            except Exception as exc:  # noqa: BLE001
                log.warning("chunk %d attempt %d failed: %s", i // chunk_size, attempt + 1, exc)
                time.sleep(5 * (attempt + 1))
        time.sleep(pause)
    missing = [t for t in tickers if t not in got]
    for t in missing:
        try:
            got.update(_download_chunk([t], start))
        except Exception as exc:  # noqa: BLE001
            log.warning("retry %s failed: %s", t, exc)
        time.sleep(0.5)
    short = []
    written = 0
    for t, f in got.items():
        if t in config.AUX_TICKERS:
            f.to_csv(config.AUX_DIR / f"{config.AUX_TICKERS[t]}.csv", index=False)
            continue
        if len(f) < 60:
            short.append(t)
            continue
        f[COLUMNS].to_csv(config.CSV_DIR / f"{t}.csv", index=False)
        written += 1
    still_missing = sorted(set(tickers) - set(got))
    meta = {
        "downloaded_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "start": start,
        "requested": len(tickers),
        "written": written,
        "missing": still_missing,
        "too_short": short,
        "last_dates": _last_dates(),
    }
    (config.DATA_DIR / "download_meta.json").write_text(json.dumps(meta, indent=2))
    log.info("download: %d written, %d missing, %d too short", written, len(still_missing), len(short))
    return meta


def _last_dates() -> dict:
    """Distribution of last available dates across symbols (stale-data check)."""
    counts: dict[str, int] = {}
    for p in config.CSV_DIR.glob("*.csv"):
        try:
            last = pd.read_csv(p, usecols=["date"])["date"].iloc[-1]
        except Exception:  # noqa: BLE001
            continue
        counts[last] = counts.get(last, 0) + 1
    return dict(sorted(counts.items())[-5:])


def panel_end_date() -> str:
    """The most common last date across symbols = the last complete session."""
    ld = _last_dates()
    if not ld:
        raise RuntimeError("no CSV data")
    return max(ld.items(), key=lambda kv: kv[1])[0]


def clean_csv_dir(path: Path = config.CSV_DIR) -> None:
    if path.exists():
        for p in path.glob("*.csv"):
            p.unlink()
