"""Run the whole pipeline. `python -m pipeline.run_all` (all steps) or `--steps download,bin`.

Writes output/status.json at the end of every run, whatever happened, so the
nightly commit always records what the ledger can rely on.
"""
from __future__ import annotations

import argparse
import json
import logging
import sys
import time
import traceback
from datetime import datetime, timezone

from . import config

log = logging.getLogger("pipeline")
ALL_STEPS = ["universe", "download", "bin", "train", "score", "evaluate", "priors"]


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--steps", default=",".join(ALL_STEPS))
    ap.add_argument("--synthetic", type=int, default=0, help="generate N synthetic tickers instead of downloading")
    args = ap.parse_args(argv)
    steps = [s.strip() for s in args.steps.split(",") if s.strip()]
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(name)s %(levelname)s %(message)s")

    status = {"started_at": datetime.now(timezone.utc).isoformat(timespec="seconds"), "steps": {}, "ok": True}
    config.OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    ctx: dict = {}

    def run(step, fn):
        t0 = time.time()
        try:
            info = fn()
            status["steps"][step] = {"ok": True, "seconds": round(time.time() - t0, 1), "info": info}
            log.info("step %s done in %.1fs", step, time.time() - t0)
        except Exception as exc:  # noqa: BLE001
            status["ok"] = False
            status["steps"][step] = {"ok": False, "seconds": round(time.time() - t0, 1), "error": f"{type(exc).__name__}: {exc}",
                                     "trace": traceback.format_exc()[-2000:]}
            log.error("step %s failed: %s", step, exc)
            return False
        return True

    if args.synthetic:
        from tests.synthetic import make_synthetic
        run("synthetic", lambda: make_synthetic(args.synthetic))
        steps = [s for s in steps if s not in ("universe", "download")]

    if "universe" in steps:
        from .universe import build_universe
        run("universe", lambda: {"tickers": int(len(build_universe()))})
    if "download" in steps and status["ok"]:
        from .download import clean_csv_dir, download_all
        from .universe import load_universe
        clean_csv_dir()
        uni = load_universe()
        tickers = uni["ticker"].tolist() + list(config.AUX_TICKERS)
        run("download", lambda: {k: v for k, v in download_all(tickers).items() if k != "missing"} | {"missing_n": 0})
    if "bin" in steps and status["ok"]:
        from .make_qlib_data import build_qlib_dir
        run("bin", build_qlib_dir)
    if "train" in steps and status["ok"]:
        from .train import train, write_model_card

        def _train():
            ctx["res"] = train()
            write_model_card(ctx["res"])
            return {"dates": ctx["res"].dates, "best_iteration": ctx["res"].best_iteration, "validation": ctx["res"].valid_metrics}
        run("train", _train)
    if "score" in steps and status["ok"] and "res" in ctx:
        from .score import score_latest, write_scores
        from .universe import load_universe
        run("score", lambda: write_scores(score_latest(ctx["res"], load_universe())))
    if "evaluate" in steps and "res" in ctx:
        from .evaluate import evaluate
        run("evaluate", lambda: {k: evaluate(ctx["res"]).get(k) for k in ("window", "signal", "name_day_hit_rates")})
    if "priors" in steps:
        from .priors import run_priors
        run("priors", lambda: {k: run_priors().get(k) for k in ("panel", "verdicts")})

    status["finished_at"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
    try:
        status["data_end_date"] = (config.OUTPUT_DIR / "scores_latest.csv").read_text().splitlines()[1].split(",")[0]
    except Exception:  # noqa: BLE001
        pass
    (config.OUTPUT_DIR / "status.json").write_text(json.dumps(status, indent=2, default=str))
    log.info("status: %s", "ok" if status["ok"] else "FAILED")
    return 0 if status["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
