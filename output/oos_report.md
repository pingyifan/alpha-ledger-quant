# Out-of-sample report: model `oc` (next session open-to-close (the ledger's day-trade rule))

Validation year; the model never trained on these sessions. Window 2025-11-10 to 2026-11-10, 252 sessions. Target = next session open-to-close (the ledger's day-trade rule) return. Costs = 4 bps round trip, the same as the ledger's simulated fund.

## Signal quality

| Metric | Value |
|---|---|
| IC (mean daily Pearson) | 0.0015 |
| ICIR | 0.011 |
| Rank IC | 0.0032 |
| Rank ICIR | 0.029 |
| Days with IC > 0 | 49.6% |

For scale: Qlib's LightGBM/Alpha158 benchmark on CSI300 reports IC 0.045 and Rank IC 0.047 (next-day close-to-close).

## Name-day hit rates (compare with the ledger's hit rate)

| Basket | Hit rate |
|---|---|
| Top-5 longs, share with a positive horizon return | 48.8% |
| Bottom-5 shorts, share with a negative horizon return | 49.0% |
| Top decile longs | 49.7% |
| Bottom decile shorts | 49.9% |
| Base rate: all tradable names with a positive horizon return | 49.7% |

## Horizon-return simulations, net of costs (per $1 of gross exposure)

| Simulation | Days | Mean/day (bps) | Annualized | Sharpe | Hit days | Max DD | t |
|---|---|---|---|---|---|---|---|
| decile_long_short | 252 | -5.2 | -12.3% | -1.561 | 46.0% | -13.5% | -1.56 |
| decile_long_only | 252 | -2.6 | -6.4% | -0.317 | 48.8% | -21.8% | -0.32 |
| top5_long_only | 252 | -15.9 | -33.1% | -0.927 | 49.2% | -49.1% | -0.93 |
| top5_long_bottom5_short | 252 | -21.7 | -42.2% | -2.28 | 45.6% | -44.3% | -2.28 |
| universe_equal_weight_long | 252 | -3.0 | -7.3% | -0.677 | 44.4% | -15.3% | -0.68 |
| spy_same_horizon | 252 | -4.1 | -9.9% | -0.958 | 49.6% | -14.3% | -0.96 |

## Reference: Qlib TopkDropout portfolio backtest (long only, close-to-close)

TopkDropout topk=30 n_drop=3, deal at close, 5+5 bps, benchmark SPY

- Annualized excess return vs SPY: +18.9%
- Information ratio: 0.729
- Max drawdown (excess): -19.4%

## Monthly decile long-short, net

| Month | Return |
|---|---|
| 2025-11 | -1.35% |
| 2025-12 | -1.74% |
| 2026-01 | -1.15% |
| 2026-02 | +1.29% |
| 2026-03 | -0.18% |
| 2026-04 | -2.75% |
| 2026-05 | +1.13% |
| 2026-06 | -0.76% |
| 2026-07 | -2.65% |
| 2026-08 | -1.68% |
| 2026-09 | +0.16% |
| 2026-10 | -1.73% |
| 2026-11 | -1.89% |

_Research output, not investment advice. Survivorship: the universe is current index membership._
