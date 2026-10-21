# Out-of-sample report: model `oc` (next session open-to-close (the ledger's day-trade rule))

Validation year; the model never trained on these sessions. Window 2025-10-17 to 2026-10-19, 252 sessions. Target = next session open-to-close (the ledger's day-trade rule) return. Costs = 4 bps round trip, the same as the ledger's simulated fund.

## Signal quality

| Metric | Value |
|---|---|
| IC (mean daily Pearson) | 0.0012 |
| ICIR | 0.008 |
| Rank IC | -0.0004 |
| Rank ICIR | -0.003 |
| Days with IC > 0 | 48.4% |

For scale: Qlib's LightGBM/Alpha158 benchmark on CSI300 reports IC 0.045 and Rank IC 0.047 (next-day close-to-close).

## Name-day hit rates (compare with the ledger's hit rate)

| Basket | Hit rate |
|---|---|
| Top-5 longs, share with a positive horizon return | 49.6% |
| Bottom-5 shorts, share with a negative horizon return | 47.6% |
| Top decile longs | 49.1% |
| Bottom decile shorts | 49.6% |
| Base rate: all tradable names with a positive horizon return | 49.5% |

## Horizon-return simulations, net of costs (per $1 of gross exposure)

| Simulation | Days | Mean/day (bps) | Annualized | Sharpe | Hit days | Max DD | t |
|---|---|---|---|---|---|---|---|
| decile_long_short | 252 | -6.3 | -14.8% | -1.785 | 43.6% | -15.8% | -1.79 |
| decile_long_only | 252 | -3.6 | -8.7% | -0.438 | 44.8% | -21.7% | -0.44 |
| top5_long_only | 252 | +8.4 | +23.6% | 0.503 | 54.0% | -35.5% | 0.5 |
| top5_long_bottom5_short | 252 | -9.4 | -21.1% | -0.967 | 50.8% | -35.0% | -0.97 |
| universe_equal_weight_long | 252 | -3.5 | -8.5% | -0.831 | 43.2% | -15.0% | -0.83 |
| spy_same_horizon | 252 | -3.3 | -8.0% | -0.84 | 48.0% | -10.3% | -0.84 |

## Reference: Qlib TopkDropout portfolio backtest (long only, close-to-close)

TopkDropout topk=30 n_drop=3, deal at close, 5+5 bps, benchmark SPY

- Annualized excess return vs SPY: +27.2%
- Information ratio: 1.127
- Max drawdown (excess): -13.9%

## Monthly decile long-short, net

| Month | Return |
|---|---|
| 2025-10 | +0.20% |
| 2025-11 | -1.12% |
| 2025-12 | -3.32% |
| 2026-01 | -0.31% |
| 2026-02 | +0.20% |
| 2026-03 | -0.04% |
| 2026-04 | -1.71% |
| 2026-05 | -0.61% |
| 2026-06 | -1.94% |
| 2026-07 | -3.97% |
| 2026-08 | -1.77% |
| 2026-09 | -0.32% |
| 2026-10 | -1.44% |

_Research output, not investment advice. Survivorship: the universe is current index membership._
