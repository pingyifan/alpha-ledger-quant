# Out-of-sample report: model `oc` (next session open-to-close (the ledger's day-trade rule))

Validation year; the model never trained on these sessions. Window 2025-10-16 to 2026-10-16, 252 sessions. Target = next session open-to-close (the ledger's day-trade rule) return. Costs = 4 bps round trip, the same as the ledger's simulated fund.

## Signal quality

| Metric | Value |
|---|---|
| IC (mean daily Pearson) | 0.0011 |
| ICIR | 0.007 |
| Rank IC | -0.0017 |
| Rank ICIR | -0.013 |
| Days with IC > 0 | 48.8% |

For scale: Qlib's LightGBM/Alpha158 benchmark on CSI300 reports IC 0.045 and Rank IC 0.047 (next-day close-to-close).

## Name-day hit rates (compare with the ledger's hit rate)

| Basket | Hit rate |
|---|---|
| Top-5 longs, share with a positive horizon return | 48.0% |
| Bottom-5 shorts, share with a negative horizon return | 48.1% |
| Top decile longs | 48.9% |
| Bottom decile shorts | 49.9% |
| Base rate: all tradable names with a positive horizon return | 49.5% |

## Horizon-return simulations, net of costs (per $1 of gross exposure)

| Simulation | Days | Mean/day (bps) | Annualized | Sharpe | Hit days | Max DD | t |
|---|---|---|---|---|---|---|---|
| decile_long_short | 252 | -6.0 | -14.1% | -1.697 | 45.2% | -15.9% | -1.7 |
| decile_long_only | 252 | -4.0 | -9.6% | -0.49 | 45.2% | -22.1% | -0.49 |
| top5_long_only | 252 | +0.0 | +0.1% | 0.001 | 50.4% | -43.4% | 0.0 |
| top5_long_bottom5_short | 252 | -15.3 | -32.0% | -1.605 | 46.0% | -40.6% | -1.61 |
| universe_equal_weight_long | 252 | -3.7 | -9.0% | -0.884 | 43.2% | -15.0% | -0.88 |
| spy_same_horizon | 252 | -3.2 | -7.7% | -0.805 | 48.0% | -10.3% | -0.81 |

## Reference: Qlib TopkDropout portfolio backtest (long only, close-to-close)

TopkDropout topk=30 n_drop=3, deal at close, 5+5 bps, benchmark SPY

- Annualized excess return vs SPY: +29.9%
- Information ratio: 1.228
- Max drawdown (excess): -16.2%

## Monthly decile long-short, net

| Month | Return |
|---|---|
| 2025-10 | +0.42% |
| 2025-11 | -0.25% |
| 2025-12 | -2.77% |
| 2026-01 | +0.41% |
| 2026-02 | -0.11% |
| 2026-03 | +0.37% |
| 2026-04 | -2.47% |
| 2026-05 | -1.08% |
| 2026-06 | -2.53% |
| 2026-07 | -4.24% |
| 2026-08 | -1.60% |
| 2026-09 | -0.13% |
| 2026-10 | -1.36% |

_Research output, not investment advice. Survivorship: the universe is current index membership._
