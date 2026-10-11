# Out-of-sample report (validation year, model never trained on these sessions)

Window 2025-10-08 to 2026-10-08, 252 sessions. Target = next session open-to-close return. Costs = 4 bps round trip, the same as the ledger's simulated fund.

## Signal quality

| Metric | Value |
|---|---|
| IC (mean daily Pearson) | 0.0036 |
| ICIR | 0.026 |
| Rank IC | -0.0013 |
| Rank ICIR | -0.011 |
| Days with IC > 0 | 52.8% |

For scale: Qlib's LightGBM/Alpha158 benchmark on CSI300 reports IC 0.045 and Rank IC 0.047 (next-day close-to-close).

## Name-day hit rates (compare with the ledger's hit rate)

| Basket | Hit rate |
|---|---|
| Top-5 longs, share that closed above the open | 47.7% |
| Bottom-5 shorts, share that closed below the open | 50.2% |
| Top decile longs | 49.4% |
| Bottom decile shorts | 50.0% |
| Base rate: all tradable names that closed above the open | 49.3% |

## Open-to-close simulations, net of costs (per $1 of gross exposure)

| Simulation | Days | Mean/day (bps) | Annualized | Sharpe | Hit days | Max DD | t |
|---|---|---|---|---|---|---|---|
| decile_long_short | 252 | -4.9 | -11.7% | -1.619 | 45.2% | -14.3% | -1.62 |
| decile_long_only | 252 | -2.8 | -6.7% | -0.349 | 45.6% | -17.7% | -0.35 |
| top5_long_only | 252 | +1.9 | +4.9% | 0.115 | 51.6% | -38.8% | 0.12 |
| top5_long_bottom5_short | 252 | -7.2 | -16.7% | -0.834 | 47.6% | -26.2% | -0.83 |
| universe_equal_weight_long | 252 | -4.8 | -11.3% | -1.066 | 43.6% | -15.0% | -1.07 |
| spy_open_to_close | 252 | -3.9 | -9.4% | -0.96 | 48.0% | -11.5% | -0.96 |

## Reference: Qlib TopkDropout portfolio backtest (long only, close-to-close)

TopkDropout topk=30 n_drop=3, deal at close, 5+5 bps, benchmark SPY

- Annualized excess return vs SPY: +32.6%
- Information ratio: 1.405
- Max drawdown (excess): -19.8%

## Monthly decile long-short, net

| Month | Return |
|---|---|
| 2025-10 | +0.22% |
| 2025-11 | -0.51% |
| 2025-12 | -3.95% |
| 2026-01 | +0.31% |
| 2026-02 | -0.61% |
| 2026-03 | -0.55% |
| 2026-04 | -1.76% |
| 2026-05 | -0.02% |
| 2026-06 | -1.17% |
| 2026-07 | -3.86% |
| 2026-08 | -0.65% |
| 2026-09 | -0.14% |
| 2026-10 | +0.20% |

_Research output, not investment advice. Survivorship: the universe is current index membership._
