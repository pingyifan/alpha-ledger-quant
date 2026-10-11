"""Qlib initialisation, data handler with the open-to-close label, and shared helpers."""
from __future__ import annotations

import logging
import os
from functools import lru_cache

import pandas as pd

from . import config

log = logging.getLogger(__name__)


@lru_cache(maxsize=1)
def init_qlib(qlib_dir: str | None = None) -> None:
    import qlib
    from qlib.constant import REG_US

    # Qlib logs training metrics through MLflow; keep that store inside data/ and allow the file backend.
    os.environ.setdefault("MLFLOW_ALLOW_FILE_STORE", "true")
    os.environ.setdefault("MLFLOW_DISABLE_AGENT_HINT", "1")
    mlruns = config.DATA_DIR / "mlruns"
    mlruns.mkdir(parents=True, exist_ok=True)
    qlib.init(
        provider_uri=str(qlib_dir or config.QLIB_DIR),
        region=REG_US,
        kernels=max(1, min(4, os.cpu_count() or 1)),
        expression_cache=None,
        dataset_cache=None,
        logging_level=logging.WARNING,
        exp_manager={
            "class": "MLflowExpManager",
            "module_path": "qlib.workflow.expm",
            "kwargs": {"uri": mlruns.as_uri(), "default_exp_name": "alpha-ledger-quant"},
        },
    )


def calendar() -> pd.DatetimeIndex:
    from qlib.data import D

    return pd.DatetimeIndex(D.calendar(freq="day"))


def make_handler(start_time, end_time, fit_start_time, fit_end_time):
    """Alpha158 features with the label replaced by next session's open-to-close return."""
    from qlib.contrib.data.handler import Alpha158

    class Alpha158OC(Alpha158):
        def get_label_config(self):
            return [config.LABEL_EXPR], [config.LABEL_NAME]

    return Alpha158OC(
        instruments=config.MARKET_NAME,
        start_time=start_time,
        end_time=end_time,
        fit_start_time=fit_start_time,
        fit_end_time=fit_end_time,
    )


def raw_label(handler, start, end) -> pd.Series:
    """Unprocessed label (actual next-session open-to-close return) for a date range."""
    from qlib.data.dataset.handler import DataHandlerLP

    df = handler.fetch(selector=slice(start, end), level="datetime", col_set="label", data_key=DataHandlerLP.DK_I)
    s = df[config.LABEL_NAME] if config.LABEL_NAME in df.columns else df.iloc[:, 0]
    s.name = "label"
    return s


def liquidity_frame(start, end) -> pd.DataFrame:
    """Per (datetime, instrument): raw close and 20-day average dollar volume."""
    from qlib.data import D

    df = D.features(
        D.instruments(config.MARKET_NAME),
        ["$close/$factor", "Mean($close*$volume, 20)", "$close"],
        start_time=start,
        end_time=end,
        freq="day",
    )
    df.columns = ["raw_close", "adv20_usd", "adj_close"]
    # D.features indexes (instrument, datetime); predictions index (datetime, instrument)
    if df.index.names[0] != "datetime":
        df = df.swaplevel().sort_index()
    return df


def tradable_mask(liq: pd.DataFrame) -> pd.Series:
    return (liq["raw_close"] >= config.MIN_PRICE) & (liq["adv20_usd"] >= config.MIN_ADV_USD)
