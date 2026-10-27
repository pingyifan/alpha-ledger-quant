# Out-of-sample report: model `oc` (next session open-to-close (the ledger's day-trade rule))

Validation year; the model never trained on these sessions. Window 2025-10-23 to 2026-10-23, 252 sessions. Target = next session open-to-close (the ledger's day-trade rule) return. Costs = 4 bps round trip, the same as the ledger's simulated fund.

## Signal quality

| Metric | Value |
|---|---|
| IC (mean daily Pearson) | 0.0027 |
| ICIR | 0.018 |
| Rank IC | -0.0006 |
| Rank ICIR | -0.004 |
| Days with IC > 0 | 48.4% |

For scale: Qlib's LightGBM/Alpha158 benchmark on CSI300 reports IC 0.045 and Rank IC 0.047 (next-day close-to-close).

## Name-day hit rates (compare with the ledger's hit rate)

| Basket | Hit rate |
|---|---|
| Top-5 longs, share with a positive horizon return | 49.2% |
| Bottom-5 shorts, share with a negative horizon return | 48.2% |
| Top decile longs | 49.2% |
| Bottom decile shorts | 49.7% |
| Base rate: all tradable names with a positive horizon return | 49.5% |

## Horizon-return simulations, net of costs (per $1 of gross exposure)

| Simulation | Days | Mean/day (bps) | Annualized | Sharpe | Hit days | Max DD | t |
|---|---|---|---|---|---|---|---|
| decile_long_short | 252 | -5.3 | -12.4% | -1.517 | 46.0% | -13.9% | -1.52 |
| decile_long_only | 252 | -2.5 | -6.0% | -0.302 | 44.8% | -22.0% | -0.3 |
| top5_long_only | 252 | +5.8 | +15.8% | 0.352 | 48.4% | -39.4% | 0.35 |
| top5_long_bottom5_short | 252 | -11.5 | -25.2% | -1.194 | 48.8% | -33.9% | -1.19 |
| universe_equal_weight_long | 252 | -3.4 | -8.2% | -0.803 | 42.9% | -15.0% | -0.8 |
| spy_same_horizon | 252 | -3.4 | -8.1% | -0.857 | 48.0% | -10.3% | -0.86 |

## Reference: Qlib TopkDropout portfolio backtest (long only, close-to-close)

TopkDropout topk=30 n_drop=3, deal at close, 5+5 bps, benchmark SPY

- Annualized excess return vs SPY: +23.2%
- Information ratio: 0.988
- Max drawdown (excess): -14.6%

## Monthly decile long-short, net

| Month | Return |
|---|---|
| 2025-10 | -0.55% |
| 2025-11 | -0.26% |
| 2025-12 | -3.24% |
| 2026-01 | +0.54% |
| 2026-02 | +0.89% |
| 2026-03 | +0.60% |
| 2026-04 | -1.78% |
| 2026-05 | -0.51% |
| 2026-06 | -1.90% |
| 2026-07 | -4.54% |
| 2026-08 | -1.09% |
| 2026-09 | -0.70% |
| 2026-10 | -0.88% |

_Research output, not investment advice. Survivorship: the universe is current index membership._
