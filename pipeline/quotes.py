"""Intraday quote relay.

Runs on a GitHub Actions schedule every five minutes during the US session and
publishes one JSON snapshot of the whole universe (official open, high, low,
last price, volume, previous close) as the rolling release asset
`quotes/quotes_latest.json`, plus an append-only per-day CSV of every snapshot
(`quotes/snapshots_YYYY-MM-DD.csv`) for later intraday research.

The ledger's scheduled sessions cannot reach Yahoo directly, so this relay is the
one place that reads quotes; everything downstream reads the JSON.
Prices here are raw (unadjusted) trading prices, which is what a fill needs.
"""
from __future__ import annotations

import json
import logging
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

import pandas as pd
import yfinance as yf

from . import config

log = logging.getLogger(__name__)
ET = ZoneInfo("America/New_York")
QUOTES_DIR = config.ROOT / "quotes_out"
HOLIDAYS = {"2026-11-26", "2026-12-25", "2027-01-01", "2027-01-18", "2027-02-15", "2027-03-26", "2027-05-31", "2027-06-18",
            "2027-07-05", "2027-09-06", "2027-11-25", "2027-12-24"}
EARLY_CLOSE = {"2026-11-27", "2026-12-24"}


def market_window(now_et: datetime) -> tuple[bool, str]:
    d = now_et.strftime("%Y-%m-%d")
    if now_et.weekday() >= 5 or d in HOLIDAYS:
        return False, "closed day"
    hhmm = now_et.hour * 100 + now_et.minute
    end = 1310 if d in EARLY_CLOSE else 1615
    if hhmm < 925 or hhmm > end:
        return False, "outside session"
    return True, "open"


def fetch_snapshot(tickers: list[str]) -> pd.DataFrame:
    """One batch request: today's partial daily bar (Open = official open, Close = last) plus yesterday's close."""
    raw = yf.download(tickers, period="5d", interval="1d", group_by="ticker", auto_adjust=False, threads=True, progress=False)
    rows = []
    for t in tickers:
        try:
            f = raw[t] if isinstance(raw.columns, pd.MultiIndex) else raw
        except KeyError:
            continue
        f = f.dropna(subset=["Close"])
        if f.empty:
            continue
        last = f.iloc[-1]
        prev_close = float(f["Close"].iloc[-2]) if len(f) >= 2 else None
        rows.append({"ticker": t, "bar_date": pd.Timestamp(f.index[-1]).strftime("%Y-%m-%d"), "open": float(last["Open"]),
                     "high": float(last["High"]), "low": float(last["Low"]), "last": float(last["Close"]),
                     "volume": float(last["Volume"]) if pd.notna(last["Volume"]) else None, "prev_close": prev_close})
    return pd.DataFrame(rows)


def run(force: bool = False) -> dict:
    now_utc = datetime.now(timezone.utc)
    now_et = now_utc.astimezone(ET)
    is_open, why = market_window(now_et)
    if not is_open and not force:
        log.info("skip: %s (%s ET)", why, now_et.strftime("%H:%M"))
        return {"skipped": why, "et": now_et.isoformat()}
    uni = pd.read_csv(config.OUTPUT_DIR / "universe.csv")
    tickers = sorted(set(uni["ticker"].str.upper().tolist()) | set(config.ETF_TICKERS))
    t0 = time.time()
    snap = fetch_snapshot(tickers)
    today = now_et.strftime("%Y-%m-%d")
    snap = snap[snap["bar_date"] == today] if not force else snap
    QUOTES_DIR.mkdir(parents=True, exist_ok=True)
    payload = {
        "asof_utc": now_utc.isoformat(timespec="seconds"), "asof_et": now_et.strftime("%Y-%m-%d %H:%M ET"), "session_date": today,
        "n": int(len(snap)), "source": "yfinance daily bar (Open = official open, last = latest trade; may lag a few minutes)",
        "quotes": {r["ticker"]: {k: r[k] for k in ("open", "high", "low", "last", "volume", "prev_close")} for r in snap.to_dict("records")},
    }
    (QUOTES_DIR / "quotes_latest.json").write_text(json.dumps(payload, separators=(",", ":")))
    snap_path = QUOTES_DIR / f"snapshots_{today}.csv"
    snap = snap.assign(asof_utc=payload["asof_utc"])
    snap.to_csv(snap_path, mode="a", header=not snap_path.exists(), index=False)
    log.info("snapshot %s: %d names in %.1fs", payload["asof_et"], len(snap), time.time() - t0)
    return {"n": int(len(snap)), "asof_et": payload["asof_et"], "seconds": round(time.time() - t0, 1)}


if __name__ == "__main__":
    import sys
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    print(json.dumps(run(force="--force" in sys.argv)))
