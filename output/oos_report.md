# Out-of-sample report: model `oc` (next session open-to-close (the ledger's day-trade rule))

Validation year; the model never trained on these sessions. Window 2025-11-17 to 2026-11-17, 252 sessions. Target = next session open-to-close (the ledger's day-trade rule) return. Costs = 4 bps round trip, the same as the ledger's simulated fund.

## Signal quality

| Metric | Value |
|---|---|
| IC (mean daily Pearson) | 0.0007 |
| ICIR | 0.007 |
| Rank IC | -0.0034 |
| Rank ICIR | -0.031 |
| Days with IC > 0 | 50.0% |

For scale: Qlib's LightGBM/Alpha158 benchmark on CSI300 reports IC 0.045 and Rank IC 0.047 (next-day close-to-close).

## Name-day hit rates (compare with the ledger's hit rate)

| Basket | Hit rate |
|---|---|
| Top-5 longs, share with a positive horizon return | 49.8% |
| Bottom-5 shorts, share with a negative horizon return | 49.2% |
| Top decile longs | 50.0% |
| Bottom decile shorts | 49.6% |
| Base rate: all tradable names with a positive horizon return | 49.6% |

## Horizon-return simulations, net of costs (per $1 of gross exposure)

| Simulation | Days | Mean/day (bps) | Annualized | Sharpe | Hit days | Max DD | t |
|---|---|---|---|---|---|---|---|
| decile_long_short | 252 | -4.8 | -11.4% | -1.656 | 44.0% | -13.6% | -1.66 |
| decile_long_only | 252 | -0.4 | -1.0% | -0.055 | 46.0% | -22.6% | -0.06 |
| top5_long_only | 252 | +10.4 | +29.9% | 0.708 | 51.6% | -39.6% | 0.71 |
| top5_long_bottom5_short | 252 | -2.3 | -5.6% | -0.285 | 51.6% | -16.3% | -0.29 |
| universe_equal_weight_long | 252 | -3.5 | -8.4% | -0.784 | 43.6% | -15.9% | -0.78 |
| spy_same_horizon | 252 | -5.0 | -11.9% | -1.165 | 49.2% | -15.2% | -1.16 |

## Reference: Qlib TopkDropout portfolio backtest (long only, close-to-close)

TopkDropout topk=30 n_drop=3, deal at close, 5+5 bps, benchmark SPY

- Annualized excess return vs SPY: +24.7%
- Information ratio: 1.146
- Max drawdown (excess): -15.2%

## Monthly decile long-short, net

| Month | Return |
|---|---|
| 2025-11 | +0.09% |
| 2025-12 | -2.84% |
| 2026-01 | +1.36% |
| 2026-02 | +1.89% |
| 2026-03 | +1.73% |
| 2026-04 | -3.28% |
| 2026-05 | -0.87% |
| 2026-06 | -1.44% |
| 2026-07 | -0.67% |
| 2026-08 | -1.70% |
| 2026-09 | -2.22% |
| 2026-10 | -0.99% |
| 2026-11 | -3.20% |

_Research output, not investment advice. Survivorship: the universe is current index membership._
