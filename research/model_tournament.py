"""Weekly model tournament on the Alpha158 features.

Trains several CPU-feasible models from Qlib's model zoo on the same split the
nightly LightGBM uses (train to T-252, validate on the last 252 sessions) for each
horizon in config.MODELS, scores them out of sample on the validation year, and
writes output/tournament.json plus output/tournament.md. The nightly pipeline reads
`champion` per horizon and, when a challenger has beaten the incumbent on BOTH
Rank IC and top-5 hit rate by the margins below for two consecutive tournaments,
promotes it (config.CHAMPION_FILE). Nothing is promoted on one good week.

    python -m research.model_tournament --models lgb,xgb,cat,densemble --horizons cc,oc
"""
from __future__ import annotations

import argparse
import json
import logging
import math
import time
from datetime import datetime, timezone

import pandas as pd

from pipeline import config
from pipeline.qlib_env import calendar, init_qlib, make_handler, raw_label
from pipeline.train import _ic_summary, _segments, label_lag
from research.label_experiments import basket_stats

log = logging.getLogger("tournament")
PROMOTE_RANK_IC_MARGIN = 0.005
PROMOTE_HIT_MARGIN = 0.01


def build_model(name: str):
    if name == "lgb":
        from qlib.contrib.model.gbdt import LGBModel
        return LGBModel(num_boost_round=config.NUM_BOOST_ROUND, early_stopping_rounds=config.EARLY_STOPPING_ROUNDS, **config.LGB_PARAMS)
    if name == "lgb_bench":
        from qlib.contrib.model.gbdt import LGBModel
        return LGBModel(num_boost_round=1000, early_stopping_rounds=50, loss="mse", learning_rate=0.2, num_leaves=210, max_depth=8,
                        colsample_bytree=0.8879, subsample=0.8789, lambda_l1=205.6999, lambda_l2=580.9768,
                        num_threads=config.LGB_PARAMS["num_threads"], verbosity=-1)
    if name == "xgb":
        from qlib.contrib.model.xgboost import XGBModel
        return XGBModel(eta=0.03, max_depth=6, subsample=0.8, colsample_bytree=0.7, reg_lambda=100.0, reg_alpha=10.0, min_child_weight=200,
                        nthread=config.LGB_PARAMS["num_threads"], eval_metric="rmse", num_boost_round=1500, early_stopping_rounds=100)
    if name == "cat":
        from qlib.contrib.model.catboost_model import CatBoostModel
        return CatBoostModel(loss="RMSE", learning_rate=0.05, depth=6, l2_leaf_reg=30, thread_count=config.LGB_PARAMS["num_threads"],
                             num_boost_round=1500, early_stopping_rounds=100)
    if name == "densemble":
        from qlib.contrib.model.double_ensemble import DEnsembleModel
        return DEnsembleModel(base_model="gbm", loss="mse", num_models=4, enable_sr=True, enable_fs=True, alpha1=1.0, alpha2=1.0,
                             bins_sr=10, bins_fs=5, decay=0.5, sample_ratios=[0.8, 0.7, 0.6, 0.5, 0.4], sub_weights=[1, 0.6, 0.6, 0.6],
                             epochs=28, learning_rate=0.05, num_leaves=31, max_depth=6, feature_fraction=0.7, bagging_fraction=0.7,
                             bagging_freq=1, lambda_l1=50.0, lambda_l2=300.0, min_data_in_leaf=500, num_threads=config.LGB_PARAMS["num_threads"],
                             verbosity=-1)
    if name == "linear":
        from qlib.contrib.model.linear import LinearModel
        return LinearModel(estimator="ridge", alpha=10.0, fit_intercept=True)
    if name == "mlp":
        from qlib.contrib.model.pytorch_nn import DNNModelPytorch
        return DNNModelPytorch(lr=0.001, max_steps=4000, batch_size=4096, early_stop_rounds=200, eval_steps=200, optimizer="adam",
                               loss="mse", GPU=0, weight_decay=1e-4, pt_model_kwargs={"input_dim": 158, "layers": (256, 128)})
    raise ValueError(name)


def run_one(name: str, horizon: str) -> dict:
    from qlib.data.dataset import DatasetH

    spec = config.MODELS[horizon]
    cal = calendar()
    d = _segments(cal, label_lag(spec["label"]))
    handler = make_handler(d["start"], d["end"], d["start"], d["train_end"], label_expr=spec["label"])
    dataset = DatasetH(handler=handler, segments={"train": (d["start"], d["train_end"]), "valid": (d["valid_start"], d["valid_end"]),
                                                  "test": (d["end"], d["end"])})
    t0 = time.time()
    model = build_model(name)
    model.fit(dataset)
    pred = model.predict(dataset, segment="valid")
    pred.name = "score"
    label = raw_label(handler, d["valid_start"], d["valid_end"]).reindex(pred.index)
    label.name = "label"
    ic = _ic_summary(pred, label)
    basket = basket_stats(pred, label)
    out = {"model": name, "horizon": horizon, "seconds": round(time.time() - t0, 1), "valid": {k: str(v.date()) for k, v in d.items()},
           **{k: v for k, v in ic.items() if k in ("ic_mean", "rank_ic_mean", "icir", "rank_icir", "ic_positive_days", "days")},
           **{f"basket_{k}": v for k, v in basket.items()}}
    log.info("%s/%s: rank_ic %.4f top5 %.3f ls %.1f bps (%.0fs)", name, horizon, out.get("rank_ic_mean", float("nan")),
             out.get("basket_top5_hit", float("nan")), out.get("basket_ls_bps", float("nan")), out["seconds"])
    return out


def pick_champions(results: list[dict], previous: dict | None) -> dict:
    """Challenger must beat the incumbent on Rank IC and top-5 hit rate by the margins, twice in a row."""
    champions = dict((previous or {}).get("champions", {}))
    pending = dict((previous or {}).get("pending", {}))
    for horizon in sorted({r["horizon"] for r in results}):
        rows = [r for r in results if r["horizon"] == horizon and r.get("rank_ic_mean") is not None]
        if not rows:
            continue
        incumbent = champions.get(horizon, "lgb")
        inc = next((r for r in rows if r["model"] == incumbent), None)
        best = max(rows, key=lambda r: (r["rank_ic_mean"], r.get("basket_top5_hit") or 0))
        if inc is None or best["model"] == incumbent:
            pending.pop(horizon, None)
            champions.setdefault(horizon, incumbent)
            continue
        beats = (best["rank_ic_mean"] >= inc["rank_ic_mean"] + PROMOTE_RANK_IC_MARGIN
                 and (best.get("basket_top5_hit") or 0) >= (inc.get("basket_top5_hit") or 0) + PROMOTE_HIT_MARGIN)
        if beats and pending.get(horizon) == best["model"]:
            champions[horizon] = best["model"]
            pending.pop(horizon, None)
        elif beats:
            pending[horizon] = best["model"]
        else:
            pending.pop(horizon, None)
    return {"champions": champions, "pending": pending}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--models", default="lgb,xgb,cat,densemble,linear")
    ap.add_argument("--horizons", default=",".join(config.MODELS))
    ap.add_argument("--out", default=str(config.OUTPUT_DIR / "tournament.json"))
    a = ap.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    init_qlib()
    prev = None
    try:
        prev = json.load(open(a.out))
    except Exception:  # noqa: BLE001
        pass
    results = []
    for horizon in [h for h in a.horizons.split(",") if h in config.MODELS]:
        for name in [m.strip() for m in a.models.split(",") if m.strip()]:
            try:
                results.append(run_one(name, horizon))
            except Exception as exc:  # noqa: BLE001
                log.exception("%s/%s failed", name, horizon)
                results.append({"model": name, "horizon": horizon, "error": f"{type(exc).__name__}: {exc}"})
    champ = pick_champions(results, prev)
    out = {"ran_at": datetime.now(timezone.utc).isoformat(timespec="seconds"), "results": results, **champ,
           "history": ((prev or {}).get("history") or [])[-11:] + [{"ran_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                       "summary": {f"{r['model']}/{r['horizon']}": {"rank_ic": r.get("rank_ic_mean"), "top5_hit": r.get("basket_top5_hit")} for r in results if "error" not in r}}]}
    config.OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    json.dump(out, open(a.out, "w"), indent=1, default=float)
    lines = [f"# Model tournament — {out['ran_at']}", "", "Validation = the last 252 sessions, out of sample; basket numbers net of 4 bps.", "",
             "| horizon | model | Rank IC | ICIR | IC>0 days | top-5 hit | bottom-5 hit | decile L/S bps/day | seconds |", "|---|---|---|---|---|---|---|---|---|"]
    for r in results:
        if "error" in r:
            lines.append(f"| {r['horizon']} | {r['model']} | error: {r['error'][:60]} | | | | | | |")
            continue
        lines.append(f"| {r['horizon']} | {r['model']} | {r.get('rank_ic_mean', float('nan')):.4f} | {r.get('rank_icir', float('nan')):.3f} | "
                     f"{r.get('ic_positive_days', float('nan')):.3f} | {r.get('basket_top5_hit', float('nan')):.3f} | {r.get('basket_bot5_hit', float('nan')):.3f} | "
                     f"{r.get('basket_ls_bps', float('nan'))} | {r['seconds']} |")
    lines += ["", f"Champions: {champ['champions']}  ·  pending (must repeat next week): {champ['pending']}",
              f"Promotion rule: challenger beats the incumbent by ≥ {PROMOTE_RANK_IC_MARGIN} Rank IC AND ≥ {PROMOTE_HIT_MARGIN} top-5 hit rate on two consecutive tournaments."]
    (config.OUTPUT_DIR / "tournament.md").write_text("\n".join(lines) + "\n")
    print(json.dumps(champ))


if __name__ == "__main__":
    main()
