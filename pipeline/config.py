"""Central configuration for the alpha-ledger-quant pipeline.

Everything that a run writes lives in two places:
  data/    raw CSV bars, the Qlib binary store, saved model  (never committed)
  output/  derived, small, committed every run: scores, reports, status
"""
from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = Path(os.environ.get("ALQ_DATA_DIR", ROOT / "data"))
CSV_DIR = DATA_DIR / "csv"            # one CSV per symbol, Qlib dump_bin input format
AUX_DIR = DATA_DIR / "aux"            # series kept out of the Qlib store (VIX)
QLIB_DIR = DATA_DIR / "qlib_us"       # Qlib binary provider directory
MODEL_PATH = DATA_DIR / "model_lgbm.txt"
OUTPUT_DIR = ROOT / "output"

# --- universe -----------------------------------------------------------------
# S&P 500 + S&P 400 constituents (Wikipedia, current membership) plus a few ETFs.
INDEX_PAGES = {
    "SP500": "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies",
    "SP400": "https://en.wikipedia.org/wiki/List_of_S%26P_400_companies",
}
ETF_TICKERS = ["SPY", "QQQ", "IWM"]   # in the Qlib store, excluded from training/scoring
AUX_TICKERS = {"^VIX": "VIX"}         # downloaded, stored under data/aux only
MARKET_NAME = "stocks"                # Qlib instruments list = universe minus ETFs

# --- history --------------------------------------------------------------------
START_DATE = os.environ.get("ALQ_START_DATE", "2016-01-01")
MIN_HISTORY_DAYS = 250                # a symbol needs this many bars to be scored

# --- tradability filter (applied at scoring and in the priors tests) -------------
MIN_PRICE = 5.0                       # last raw close, USD
MIN_ADV_USD = 5_000_000               # 20-day average dollar volume

# --- models: one per horizon. Every label is measured from the NEXT session, i.e. what a
# call made before that session's open can capture. "oc" is the Alpha Ledger's scoring rule.
LABEL_NAME = "LABEL0"
MODELS = {
    "oc": {
        "label": "Ref($close, -1)/Ref($open, -1) - 1",
        "desc": "next session open-to-close (the ledger's day-trade rule)",
        "entry": "next open", "exit": "same session close",
        "scores_file": "scores_latest.csv", "card_file": "model_card.json",
        "oos_file": "oos_report", "history_file": "scores_history_top.csv",
    },
    "oo": {
        "label": "Ref($open, -2)/Ref($open, -1) - 1",
        "desc": "next session open to the following session's open (one-session hold, includes the overnight)",
        "entry": "next open", "exit": "following session open",
        "scores_file": "scores_oo_latest.csv", "card_file": "model_card_oo.json",
        "oos_file": "oos_report_oo", "history_file": "scores_history_top_oo.csv",
    },
}
DEFAULT_MODEL = "oc"
LABEL_EXPR = MODELS[DEFAULT_MODEL]["label"]   # kept for backward compatibility

# --- walk-forward split -----------------------------------------------------------
VALID_DAYS = 252                      # last year of complete sessions = validation
# train = [START_DATE, end - VALID_DAYS - 2 sessions]; valid = the following window
# the final model is refit on train+valid with the early-stopped round count

# --- LightGBM (Qlib LGBModel kwargs) -----------------------------------------------
# Daily cross-sectional targets are mostly noise, so the model is regularised hard: slow
# learning rate, shallow trees, large leaves, strong L2. Early stopping picks the rounds.
LGB_PARAMS = {
    "loss": "mse",
    "learning_rate": 0.02,
    "num_leaves": 31,
    "max_depth": 6,
    "feature_fraction": 0.6,
    "bagging_fraction": 0.7,
    "bagging_freq": 1,
    "lambda_l1": 50.0,
    "lambda_l2": 300.0,
    "min_data_in_leaf": 500,
    "num_threads": max(1, os.cpu_count() or 1),
    "seed": 2026,
    "verbosity": -1,
}
NUM_BOOST_ROUND = 3000
EARLY_STOPPING_ROUNDS = 200

# --- costs used in every open-to-close simulation (matches the ledger's fund) ------
COST_PER_SIDE = 0.0002                # 2 bps at the open + 2 bps at the close

# --- outputs -----------------------------------------------------------------------
HISTORY_TOP_N = 25                    # top/bottom N kept per day in scores_history_top.csv
HISTORY_KEEP_DAYS = 300
