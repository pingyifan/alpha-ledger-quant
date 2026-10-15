# Out-of-sample report: model `oc` (next session open-to-close (the ledger's day-trade rule))

Validation year; the model never trained on these sessions. Window 2025-10-13 to 2026-10-13, 252 sessions. Target = next session open-to-close (the ledger's day-trade rule) return. Costs = 4 bps round trip, the same as the ledger's simulated fund.

## Signal quality

| Metric | Value |
|---|---|
| IC (mean daily Pearson) | 0.0040 |
| ICIR | 0.027 |
| Rank IC | 0.0001 |
| Rank ICIR | 0.001 |
| Days with IC > 0 | 50.0% |

For scale: Qlib's LightGBM/Alpha158 benchmark on CSI300 reports IC 0.045 and Rank IC 0.047 (next-day close-to-close).

## Name-day hit rates (compare with the ledger's hit rate)

| Basket | Hit rate |
|---|---|
| Top-5 longs, share with a positive horizon return | 48.6% |
| Bottom-5 shorts, share with a negative horizon return | 49.7% |
| Top decile longs | 49.3% |
| Bottom decile shorts | 49.9% |
| Base rate: all tradable names with a positive horizon return | 49.5% |

## Horizon-return simulations, net of costs (per $1 of gross exposure)

| Simulation | Days | Mean/day (bps) | Annualized | Sharpe | Hit days | Max DD | t |
|---|---|---|---|---|---|---|---|
| decile_long_short | 252 | -5.1 | -12.1% | -1.461 | 42.1% | -12.9% | -1.46 |
| decile_long_only | 252 | -2.5 | -6.0% | -0.302 | 45.6% | -21.7% | -0.3 |
| top5_long_only | 252 | +11.4 | +33.2% | 0.729 | 51.6% | -26.0% | 0.73 |
| top5_long_bottom5_short | 252 | -3.5 | -8.3% | -0.384 | 50.8% | -31.1% | -0.38 |
| universe_equal_weight_long | 252 | -3.5 | -8.5% | -0.822 | 43.2% | -15.0% | -0.82 |
| spy_same_horizon | 252 | -3.1 | -7.5% | -0.782 | 48.0% | -10.0% | -0.78 |

## Reference: Qlib TopkDropout portfolio backtest (long only, close-to-close)

TopkDropout topk=30 n_drop=3, deal at close, 5+5 bps, benchmark SPY

- Annualized excess return vs SPY: +25.5%
- Information ratio: 1.039
- Max drawdown (excess): -18.1%

## Monthly decile long-short, net

| Month | Return |
|---|---|
| 2025-10 | -0.06% |
| 2025-11 | -0.55% |
| 2025-12 | -2.91% |
| 2026-01 | +0.81% |
| 2026-02 | +1.10% |
| 2026-03 | +0.25% |
| 2026-04 | -1.41% |
| 2026-05 | -0.14% |
| 2026-06 | -1.91% |
| 2026-07 | -4.74% |
| 2026-08 | -1.49% |
| 2026-09 | -0.91% |
| 2026-10 | -1.08% |

_Research output, not investment advice. Survivorship: the universe is current index membership._
