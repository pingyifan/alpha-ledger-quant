"""Walk-forward training of a LightGBM cross-sectional model on Alpha158 features.

Split (sessions from the Qlib calendar):
    train : [START_DATE, end - VALID_DAYS - 1]
    valid : the last VALID_DAYS complete sessions (early stopping, out-of-sample report)
    test  : the last session (label unknown) -> tonight's scores
The final model is refit on train+valid with the early-stopped number of rounds.
"""
from __future__ import annotations

import json
import logging
from dataclasses import dataclass, field
from datetime import datetime, timezone

import pandas as pd

from . import config
from .qlib_env import calendar, init_qlib, make_handler, raw_label

log = logging.getLogger(__name__)


@dataclass
class TrainResult:
    model: object                 # final LGBModel (refit)
    dataset: object               # DatasetH whose "test" segment is the last session
    handler: object
    pred_valid: pd.Series         # out-of-sample predictions on the validation window
    label_valid: pd.Series        # realised next-session open-to-close returns, same index
    dates: dict = field(default_factory=dict)
    best_iteration: int = 0
    valid_metrics: dict = field(default_factory=dict)
    feature_importance: dict = field(default_factory=dict)


def _segments(cal: pd.DatetimeIndex) -> dict:
    if len(cal) < config.VALID_DAYS + 300:
        raise RuntimeError(f"calendar too short for the split: {len(cal)} sessions")
    end = cal[-1]
    valid_end = cal[-2]                       # last session with a known label
    valid_start = cal[-1 - config.VALID_DAYS]
    train_end = cal[-2 - config.VALID_DAYS]
    return {
        "start": pd.Timestamp(config.START_DATE),
        "train_end": train_end,
        "valid_start": valid_start,
        "valid_end": valid_end,
        "end": end,
    }


def train() -> TrainResult:
    from qlib.contrib.model.gbdt import LGBModel
    from qlib.data.dataset import DatasetH

    init_qlib()
    cal = calendar()
    d = _segments(cal)
    log.info("split: train %s..%s | valid %s..%s | score %s",
             d["start"].date(), d["train_end"].date(), d["valid_start"].date(), d["valid_end"].date(), d["end"].date())

    handler = make_handler(d["start"], d["end"], d["start"], d["train_end"])
    dataset = DatasetH(
        handler=handler,
        segments={
            "train": (d["start"], d["train_end"]),
            "valid": (d["valid_start"], d["valid_end"]),
            "test": (d["end"], d["end"]),
        },
    )

    # 1) early-stopped model: honest out-of-sample numbers on the validation year
    model = LGBModel(num_boost_round=config.NUM_BOOST_ROUND,
                     early_stopping_rounds=config.EARLY_STOPPING_ROUNDS, **config.LGB_PARAMS)
    evals: dict = {}
    model.fit(dataset, evals_result=evals, verbose_eval=0)
    best_iter = int(getattr(model.model, "best_iteration", 0) or model.model.num_trees())
    pred_valid = model.predict(dataset, segment="valid")
    pred_valid.name = "score"
    label_valid = raw_label(handler, d["valid_start"], d["valid_end"]).reindex(pred_valid.index)
    valid_metrics = _ic_summary(pred_valid, label_valid)
    valid_metrics.update({"best_iteration": best_iter,
                          "train_l2": float(evals.get("train", {}).get("l2", [float("nan")])[-1]) if evals else None,
                          "valid_l2": float(evals.get("valid", {}).get("l2", [float("nan")])[-1]) if evals else None})
    log.info("validation: %s", valid_metrics)

    # 2) refit on train+valid with the stopped round count -> tonight's scoring model
    dataset_final = DatasetH(
        handler=handler,
        segments={
            "train": (d["start"], d["valid_end"]),
            "valid": (cal[-22], d["valid_end"]),   # tiny tail, only so LGBModel.fit has an eval set
            "test": (d["end"], d["end"]),
        },
    )
    final = LGBModel(num_boost_round=max(50, best_iter), early_stopping_rounds=0, **config.LGB_PARAMS)
    final.fit(dataset_final, verbose_eval=0)
    config.DATA_DIR.mkdir(parents=True, exist_ok=True)
    final.model.save_model(str(config.MODEL_PATH))

    try:
        fi = final.get_feature_importance(importance_type="gain")
        fi = (fi / fi.sum()).sort_values(ascending=False)
        feature_importance = {str(k): round(float(v), 5) for k, v in fi.head(30).items()}
    except Exception as exc:  # noqa: BLE001
        log.warning("feature importance unavailable: %s", exc)
        feature_importance = {}

    return TrainResult(model=final, dataset=dataset_final, handler=handler, pred_valid=pred_valid,
                       label_valid=label_valid, dates={k: str(v.date()) for k, v in d.items()},
                       best_iteration=best_iter, valid_metrics=valid_metrics, feature_importance=feature_importance)


def _ic_summary(pred: pd.Series, label: pd.Series) -> dict:
    df = pd.concat([pred, label], axis=1).dropna()
    by_day = df.groupby(level="datetime")
    ic = by_day.apply(lambda g: g["score"].corr(g["label"]) if len(g) > 10 else float("nan")).dropna()
    ric = by_day.apply(lambda g: g["score"].corr(g["label"], method="spearman") if len(g) > 10 else float("nan")).dropna()
    return {
        "days": int(len(ic)),
        "ic_mean": round(float(ic.mean()), 5),
        "ic_std": round(float(ic.std()), 5),
        "icir": round(float(ic.mean() / ic.std()), 4) if ic.std() > 0 else None,
        "rank_ic_mean": round(float(ric.mean()), 5),
        "rank_icir": round(float(ric.mean() / ric.std()), 4) if ric.std() > 0 else None,
        "ic_positive_days": round(float((ic > 0).mean()), 4),
    }


def write_model_card(res: TrainResult, extra: dict | None = None) -> dict:
    card = {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "model": "LightGBM (qlib.contrib.model.gbdt.LGBModel)",
        "features": "Qlib Alpha158 (158 OHLCV features)",
        "label": config.LABEL_EXPR + "  (next session open-to-close return, cross-sectionally z-scored for training)",
        "universe": config.MARKET_NAME,
        "dates": res.dates,
        "params": {k: v for k, v in config.LGB_PARAMS.items() if k not in ("num_threads", "verbosity")},
        "best_iteration": res.best_iteration,
        "validation": res.valid_metrics,
        "feature_importance_top30_gain_share": res.feature_importance,
    }
    if extra:
        card.update(extra)
    config.OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    (config.OUTPUT_DIR / "model_card.json").write_text(json.dumps(card, indent=2))
    return card
