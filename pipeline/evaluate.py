"""Out-of-sample evaluation of the model on the validation year.

Everything here uses the early-stopped model's predictions on sessions it never
trained on, scored against the realised next-session open-to-close return, the
same quantity the Alpha Ledger scores its calls on. Three views:

  1. signal quality: daily IC / Rank IC and their stability
  2. open-to-close simulations with the ledger's 4 bps round-trip cost:
       decile long-short, top-5 / bottom-5 (ledger-sized), top-decile long only,
       all against the equal-weight universe and SPY over the same sessions
  3. reference: Qlib's own TopkDropout portfolio backtest (close-to-close
     convention, long only), so the number is comparable with Qlib's benchmarks
"""
from __future__ import annotations

import json
import logging
import math
from datetime import datetime, timezone

import numpy as np
import pandas as pd

from . import config
from .qlib_env import liquidity_frame, tradable_mask
from .train import TrainResult

log = logging.getLogger(__name__)
ANN = 252


def _stats(daily: pd.Series) -> dict:
    daily = daily.dropna()
    if len(daily) < 5:
        return {"days": int(len(daily))}
    cum = (1 + daily).cumprod()
    dd = (cum / cum.cummax() - 1).min()
    mean, std = daily.mean(), daily.std()
    return {
        "days": int(len(daily)),
        "mean_daily_bps": round(float(mean * 1e4), 2),
        "annualized_return": round(float((1 + mean) ** ANN - 1), 4),
        "sharpe": round(float(mean / std * math.sqrt(ANN)), 3) if std > 0 else None,
        "hit_rate_days": round(float((daily > 0).mean()), 4),
        "max_drawdown": round(float(dd), 4),
        "t_stat": round(float(mean / std * math.sqrt(len(daily))), 2) if std > 0 else None,
        "total_return": round(float(cum.iloc[-1] - 1), 4),
    }


def _per_day_groups(df: pd.DataFrame):
    """Yield (date, frame sorted by score desc) for tradable names only."""
    for dt, g in df[df["tradable"]].groupby(level="datetime"):
        if len(g) >= 30:
            yield dt, g.sort_values("score", ascending=False)


def evaluate(res: TrainResult) -> dict:
    df = pd.concat([res.pred_valid, res.label_valid], axis=1).dropna()
    start, end = df.index.get_level_values("datetime").min(), df.index.get_level_values("datetime").max()
    liq = liquidity_frame(start - pd.Timedelta(days=45), end)
    # tradability known at the signal date uses that day's close/ADV (both are known at the close)
    liq = liq.reindex(df.index)
    df["tradable"] = tradable_mask(liq).fillna(False).values

    cost_rt = 2 * config.COST_PER_SIDE
    rows = []
    for dt, g in _per_day_groups(df):
        n = len(g)
        k = max(1, n // 10)
        top, bot = g.head(k)["label"], g.tail(k)["label"]
        t5, b5 = g.head(5)["label"], g.tail(5)["label"]
        rows.append({
            "date": dt,
            "n": n,
            "universe_ew": g["label"].mean(),
            "universe_up_share": (g["label"] > 0).mean(),
            "top_dec": top.mean(), "bot_dec": bot.mean(),
            "top5": t5.mean(), "bot5": b5.mean(),
            "top5_hits": (t5 > 0).sum(), "bot5_hits": (b5 < 0).sum(),
            "top_dec_hits": (top > 0).mean(), "bot_dec_hits": (bot < 0).mean(),
        })
    d = pd.DataFrame(rows).set_index("date").sort_index()
    if d.empty:
        return {"error": "no evaluable days"}

    # open-to-close simulations, net of the ledger's costs (per unit of gross exposure)
    sims = {
        "decile_long_short": 0.5 * (d["top_dec"] - d["bot_dec"]) - cost_rt,
        "decile_long_only": d["top_dec"] - cost_rt,
        "top5_long_only": d["top5"] - cost_rt,
        "top5_long_bottom5_short": 0.5 * (d["top5"] - d["bot5"]) - cost_rt,
        "universe_equal_weight_long": d["universe_ew"] - cost_rt,
    }
    spy = _spy_series(res.spec["label"], start, end)
    if spy is not None:
        sims["spy_same_horizon"] = spy.reindex(d.index) - cost_rt

    ic = df.groupby(level="datetime").apply(lambda g: g["score"].corr(g["label"]))
    ric = df.groupby(level="datetime").apply(lambda g: g["score"].corr(g["label"], method="spearman"))
    monthly = (0.5 * (d["top_dec"] - d["bot_dec"]) - cost_rt).groupby(d.index.to_period("M")).apply(lambda s: (1 + s).prod() - 1)

    report = {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "window": {"start": str(start.date()), "end": str(end.date()), "sessions": int(len(d))},
        "cost_round_trip": cost_rt,
        "signal": {
            "ic_mean": round(float(ic.mean()), 5), "icir": round(float(ic.mean() / ic.std()), 4),
            "rank_ic_mean": round(float(ric.mean()), 5), "rank_icir": round(float(ric.mean() / ric.std()), 4),
            "ic_positive_days": round(float((ic > 0).mean()), 4),
        },
        "name_day_hit_rates": {
            "top5_long_hit_rate": round(float(d["top5_hits"].sum() / (5 * len(d))), 4),
            "bottom5_short_hit_rate": round(float(d["bot5_hits"].sum() / (5 * len(d))), 4),
            "top_decile_long_hit_rate": round(float(d["top_dec_hits"].mean()), 4),
            "bottom_decile_short_hit_rate": round(float(d["bot_dec_hits"].mean()), 4),
            "universe_up_share": round(float(d["universe_up_share"].mean()), 4),
        },
        "simulations_net_of_costs": {k: _stats(v) for k, v in sims.items()},
        "monthly_decile_long_short_net": {str(k): round(float(v), 4) for k, v in monthly.items()},
    }
    try:
        report["qlib_topk_backtest_close_to_close"] = qlib_topk_backtest(res, start, end)
    except Exception as exc:  # noqa: BLE001
        log.warning("qlib portfolio backtest skipped: %s", exc)
        report["qlib_topk_backtest_close_to_close"] = {"error": str(exc)[:300]}

    report["model_key"] = res.key
    report["horizon"] = res.spec["desc"]
    config.OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    stem = res.spec["oos_file"]
    (config.OUTPUT_DIR / f"{stem}.json").write_text(json.dumps(report, indent=2, default=str))
    (config.OUTPUT_DIR / f"{stem}.md").write_text(render_oos_markdown(report))
    return report


def _spy_series(label_expr: str, start, end) -> pd.Series | None:
    from qlib.data import D

    try:
        s = D.features(["SPY"], [label_expr], start_time=start, end_time=end, freq="day")
        s = s.droplevel("instrument").iloc[:, 0]
        s.name = "spy_same_horizon"
        return s
    except Exception as exc:  # noqa: BLE001
        log.warning("SPY series unavailable: %s", exc)
        return None


def qlib_topk_backtest(res: TrainResult, start, end, topk: int = 30, n_drop: int = 3) -> dict:
    """Qlib's standard long-only daily-rebalanced portfolio backtest on the OOS window."""
    from qlib.backtest import backtest
    from qlib.contrib.evaluate import risk_analysis

    pred_df = res.pred_valid.to_frame("score")
    strategy = {
        "class": "TopkDropoutStrategy",
        "module_path": "qlib.contrib.strategy.signal_strategy",
        "kwargs": {"signal": pred_df, "topk": topk, "n_drop": n_drop},
    }
    executor = {
        "class": "SimulatorExecutor",
        "module_path": "qlib.backtest.executor",
        "kwargs": {"time_per_step": "day", "generate_portfolio_metrics": True},
    }
    portfolio_metric_dict, _ = backtest(
        start_time=start, end_time=end, strategy=strategy, executor=executor, benchmark="SPY",
        account=1_000_000,
        exchange_kwargs={"freq": "day", "limit_threshold": None, "deal_price": "close",
                         "open_cost": 0.0005, "close_cost": 0.0005, "min_cost": 0},
    )
    report_df, _positions = portfolio_metric_dict["1day"]
    excess = report_df["return"] - report_df["bench"] - report_df["cost"]
    ra = risk_analysis(excess, freq="day")["risk"]
    return {
        "strategy": f"TopkDropout topk={topk} n_drop={n_drop}, deal at close, 5+5 bps, benchmark SPY",
        "excess_return_annualized": round(float(ra["annualized_return"]), 4),
        "information_ratio": round(float(ra["information_ratio"]), 3),
        "max_drawdown": round(float(ra["max_drawdown"]), 4),
        "sessions": int(len(report_df)),
    }


def render_oos_markdown(r: dict) -> str:
    if "error" in r:
        return f"# Out-of-sample report\n\n{r['error']}\n"
    w, s, h = r["window"], r["signal"], r["name_day_hit_rates"]
    lines = [
        f"# Out-of-sample report: model `{r.get('model_key','oc')}` ({r.get('horizon','next session open-to-close')})",
        "",
        "Validation year; the model never trained on these sessions. "
        f"Window {w['start']} to {w['end']}, {w['sessions']} sessions. Target = {r.get('horizon','next session open-to-close')} return. "
        f"Costs = {r['cost_round_trip']*1e4:.0f} bps round trip, the same as the ledger's simulated fund.",
        "",
        "## Signal quality",
        "",
        "| Metric | Value |", "|---|---|",
        f"| IC (mean daily Pearson) | {s['ic_mean']:.4f} |",
        f"| ICIR | {s['icir']:.3f} |",
        f"| Rank IC | {s['rank_ic_mean']:.4f} |",
        f"| Rank ICIR | {s['rank_icir']:.3f} |",
        f"| Days with IC > 0 | {s['ic_positive_days']:.1%} |",
        "",
        "For scale: Qlib's LightGBM/Alpha158 benchmark on CSI300 reports IC 0.045 and Rank IC 0.047 (next-day close-to-close).",
        "",
        "## Name-day hit rates (compare with the ledger's hit rate)",
        "",
        "| Basket | Hit rate |", "|---|---|",
        f"| Top-5 longs, share with a positive horizon return | {h['top5_long_hit_rate']:.1%} |",
        f"| Bottom-5 shorts, share with a negative horizon return | {h['bottom5_short_hit_rate']:.1%} |",
        f"| Top decile longs | {h['top_decile_long_hit_rate']:.1%} |",
        f"| Bottom decile shorts | {h['bottom_decile_short_hit_rate']:.1%} |",
        f"| Base rate: all tradable names with a positive horizon return | {h['universe_up_share']:.1%} |",
        "",
        "## Horizon-return simulations, net of costs (per $1 of gross exposure)",
        "",
        "| Simulation | Days | Mean/day (bps) | Annualized | Sharpe | Hit days | Max DD | t |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for k, v in r["simulations_net_of_costs"].items():
        if v.get("days", 0) < 5:
            continue
        lines.append(f"| {k} | {v['days']} | {v['mean_daily_bps']:+.1f} | {v['annualized_return']:+.1%} | "
                     f"{v['sharpe'] if v['sharpe'] is not None else 'n/a'} | {v['hit_rate_days']:.1%} | {v['max_drawdown']:.1%} | {v['t_stat']} |")
    q = r.get("qlib_topk_backtest_close_to_close", {})
    lines += ["", "## Reference: Qlib TopkDropout portfolio backtest (long only, close-to-close)", ""]
    if "error" in q:
        lines.append(f"Skipped: {q['error']}")
    else:
        lines += [f"{q['strategy']}", "",
                  f"- Annualized excess return vs SPY: {q['excess_return_annualized']:+.1%}",
                  f"- Information ratio: {q['information_ratio']}",
                  f"- Max drawdown (excess): {q['max_drawdown']:.1%}"]
    lines += ["", "## Monthly decile long-short, net", "", "| Month | Return |", "|---|---|"]
    for k, v in r["monthly_decile_long_short_net"].items():
        lines.append(f"| {k} | {v:+.2%} |")
    lines += ["", "_Research output, not investment advice. Survivorship: the universe is current index membership._", ""]
    return "\n".join(lines)
