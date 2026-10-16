# Out-of-sample report: model `oc` (next session open-to-close (the ledger's day-trade rule))

Validation year; the model never trained on these sessions. Window 2025-10-14 to 2026-10-14, 252 sessions. Target = next session open-to-close (the ledger's day-trade rule) return. Costs = 4 bps round trip, the same as the ledger's simulated fund.

## Signal quality

| Metric | Value |
|---|---|
| IC (mean daily Pearson) | 0.0046 |
| ICIR | 0.031 |
| Rank IC | 0.0006 |
| Rank ICIR | 0.005 |
| Days with IC > 0 | 50.0% |

For scale: Qlib's LightGBM/Alpha158 benchmark on CSI300 reports IC 0.045 and Rank IC 0.047 (next-day close-to-close).

## Name-day hit rates (compare with the ledger's hit rate)

| Basket | Hit rate |
|---|---|
| Top-5 longs, share with a positive horizon return | 47.9% |
| Bottom-5 shorts, share with a negative horizon return | 47.9% |
| Top decile longs | 49.2% |
| Bottom decile shorts | 49.8% |
| Base rate: all tradable names with a positive horizon return | 49.4% |

## Horizon-return simulations, net of costs (per $1 of gross exposure)

| Simulation | Days | Mean/day (bps) | Annualized | Sharpe | Hit days | Max DD | t |
|---|---|---|---|---|---|---|---|
| decile_long_short | 252 | -5.7 | -13.3% | -1.631 | 43.6% | -14.8% | -1.63 |
| decile_long_only | 252 | -3.0 | -7.3% | -0.372 | 45.6% | -21.4% | -0.37 |
| top5_long_only | 252 | +2.9 | +7.5% | 0.18 | 49.6% | -31.6% | 0.18 |
| top5_long_bottom5_short | 252 | -12.4 | -26.9% | -1.32 | 50.4% | -38.2% | -1.32 |
| universe_equal_weight_long | 252 | -4.0 | -9.5% | -0.934 | 43.2% | -15.0% | -0.93 |
| spy_same_horizon | 252 | -3.1 | -7.5% | -0.787 | 48.0% | -10.0% | -0.79 |

## Reference: Qlib TopkDropout portfolio backtest (long only, close-to-close)

TopkDropout topk=30 n_drop=3, deal at close, 5+5 bps, benchmark SPY

- Annualized excess return vs SPY: +29.4%
- Information ratio: 1.315
- Max drawdown (excess): -12.2%

## Monthly decile long-short, net

| Month | Return |
|---|---|
| 2025-10 | -0.02% |
| 2025-11 | -0.95% |
| 2025-12 | -3.25% |
| 2026-01 | -0.04% |
| 2026-02 | +0.68% |
| 2026-03 | +0.55% |
| 2026-04 | -1.57% |
| 2026-05 | -0.44% |
| 2026-06 | -2.00% |
| 2026-07 | -4.66% |
| 2026-08 | -1.75% |
| 2026-09 | -0.86% |
| 2026-10 | -0.11% |

_Research output, not investment advice. Survivorship: the universe is current index membership._
