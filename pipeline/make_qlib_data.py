"""Convert data/csv into a Qlib binary provider directory with Qlib's own dump_bin.

Also writes instruments/stocks.txt = every symbol except the ETFs, which is the
market the model trains and scores on.
"""
from __future__ import annotations

import logging
import os
import shutil
from pathlib import Path

from . import config

log = logging.getLogger(__name__)


def build_qlib_dir(csv_dir: Path = config.CSV_DIR, qlib_dir: Path = config.QLIB_DIR) -> dict:
    from .vendor.dump_bin import DumpDataAll  # vendored from microsoft/qlib scripts (MIT)

    if qlib_dir.exists():
        shutil.rmtree(qlib_dir)
    qlib_dir.mkdir(parents=True)
    n_files = len(list(csv_dir.glob("*.csv")))
    if n_files == 0:
        raise RuntimeError(f"no CSV files in {csv_dir}")
    DumpDataAll(
        data_path=str(csv_dir),
        qlib_dir=str(qlib_dir),
        freq="day",
        max_workers=max(1, min(8, (os.cpu_count() or 2))),
        date_field_name="date",
        symbol_field_name="symbol",
        include_fields="open,high,low,close,volume,factor",
    ).dump()
    all_txt = qlib_dir / "instruments" / "all.txt"
    lines = all_txt.read_text().strip().splitlines()
    etfs = {t.upper() for t in config.ETF_TICKERS}
    stocks = [ln for ln in lines if ln.split("\t")[0].upper() not in etfs]
    (qlib_dir / "instruments" / f"{config.MARKET_NAME}.txt").write_text("\n".join(stocks) + "\n")
    cal = (qlib_dir / "calendars" / "day.txt").read_text().strip().splitlines()
    info = {"csv_files": n_files, "instruments_all": len(lines), "instruments_stocks": len(stocks),
            "calendar_start": cal[0], "calendar_end": cal[-1], "calendar_days": len(cal)}
    log.info("qlib dir ready: %s", info)
    return info
