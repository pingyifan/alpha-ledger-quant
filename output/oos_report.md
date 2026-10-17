# Out-of-sample report: model `oc` (next session open-to-close (the ledger's day-trade rule))

Validation year; the model never trained on these sessions. Window 2025-10-14 to 2026-10-14, 252 sessions. Target = next session open-to-close (the ledger's day-trade rule) return. Costs = 4 bps round trip, the same as the ledger's simulated fund.

## Signal quality

| Metric | Value |
|---|---|
| IC (mean daily Pearson) | 0.0051 |
| ICIR | 0.035 |
| Rank IC | 0.0003 |
| Rank ICIR | 0.003 |
| Days with IC > 0 | 51.2% |

For scale: Qlib's LightGBM/Alpha158 benchmark on CSI300 reports IC 0.045 and Rank IC 0.047 (next-day close-to-close).

## Name-day hit rates (compare with the ledger's hit rate)

| Basket | Hit rate |
|---|---|
| Top-5 longs, share with a positive horizon return | 47.9% |
| Bottom-5 shorts, share with a negative horizon return | 48.6% |
| Top decile longs | 49.3% |
| Bottom decile shorts | 49.7% |
| Base rate: all tradable names with a positive horizon return | 49.4% |

## Horizon-return simulations, net of costs (per $1 of gross exposure)

| Simulation | Days | Mean/day (bps) | Annualized | Sharpe | Hit days | Max DD | t |
|---|---|---|---|---|---|---|---|
| decile_long_short | 252 | -5.0 | -11.8% | -1.444 | 43.2% | -13.4% | -1.44 |
| decile_long_only | 252 | -1.7 | -4.1% | -0.208 | 45.6% | -20.2% | -0.21 |
| top5_long_only | 252 | +0.8 | +2.1% | 0.051 | 48.8% | -32.4% | 0.05 |
| top5_long_bottom5_short | 252 | -10.0 | -22.3% | -1.062 | 48.4% | -33.1% | -1.06 |
| universe_equal_weight_long | 252 | -3.9 | -9.3% | -0.911 | 43.2% | -15.0% | -0.91 |
| spy_same_horizon | 252 | -3.1 | -7.5% | -0.787 | 48.0% | -10.0% | -0.79 |

## Reference: Qlib TopkDropout portfolio backtest (long only, close-to-close)

TopkDropout topk=30 n_drop=3, deal at close, 5+5 bps, benchmark SPY

- Annualized excess return vs SPY: +32.2%
- Information ratio: 1.353
- Max drawdown (excess): -15.6%

## Monthly decile long-short, net

| Month | Return |
|---|---|
| 2025-10 | -0.16% |
| 2025-11 | -0.31% |
| 2025-12 | -3.22% |
| 2026-01 | -0.13% |
| 2026-02 | +0.47% |
| 2026-03 | +0.45% |
| 2026-04 | -0.74% |
| 2026-05 | -0.38% |
| 2026-06 | -1.88% |
| 2026-07 | -4.28% |
| 2026-08 | -1.64% |
| 2026-09 | -0.68% |
| 2026-10 | -0.21% |

_Research output, not investment advice. Survivorship: the universe is current index membership._
