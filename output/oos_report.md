# Out-of-sample report: model `oc` (next session open-to-close (the ledger's day-trade rule))

Validation year; the model never trained on these sessions. Window 2025-11-13 to 2026-11-13, 252 sessions. Target = next session open-to-close (the ledger's day-trade rule) return. Costs = 4 bps round trip, the same as the ledger's simulated fund.

## Signal quality

| Metric | Value |
|---|---|
| IC (mean daily Pearson) | -0.0005 |
| ICIR | -0.004 |
| Rank IC | -0.0023 |
| Rank ICIR | -0.020 |
| Days with IC > 0 | 48.0% |

For scale: Qlib's LightGBM/Alpha158 benchmark on CSI300 reports IC 0.045 and Rank IC 0.047 (next-day close-to-close).

## Name-day hit rates (compare with the ledger's hit rate)

| Basket | Hit rate |
|---|---|
| Top-5 longs, share with a positive horizon return | 50.6% |
| Bottom-5 shorts, share with a negative horizon return | 48.7% |
| Top decile longs | 49.3% |
| Bottom decile shorts | 50.0% |
| Base rate: all tradable names with a positive horizon return | 49.5% |

## Horizon-return simulations, net of costs (per $1 of gross exposure)

| Simulation | Days | Mean/day (bps) | Annualized | Sharpe | Hit days | Max DD | t |
|---|---|---|---|---|---|---|---|
| decile_long_short | 252 | -5.0 | -11.7% | -1.7 | 47.2% | -12.9% | -1.7 |
| decile_long_only | 252 | -2.9 | -7.0% | -0.374 | 46.4% | -26.4% | -0.37 |
| top5_long_only | 252 | +6.2 | +16.8% | 0.385 | 53.2% | -41.6% | 0.38 |
| top5_long_bottom5_short | 252 | -6.2 | -14.4% | -0.663 | 51.2% | -32.1% | -0.66 |
| universe_equal_weight_long | 252 | -3.6 | -8.6% | -0.799 | 43.6% | -15.3% | -0.8 |
| spy_same_horizon | 252 | -4.4 | -10.4% | -1.013 | 49.6% | -14.3% | -1.01 |

## Reference: Qlib TopkDropout portfolio backtest (long only, close-to-close)

TopkDropout topk=30 n_drop=3, deal at close, 5+5 bps, benchmark SPY

- Annualized excess return vs SPY: +22.0%
- Information ratio: 1.051
- Max drawdown (excess): -11.4%

## Monthly decile long-short, net

| Month | Return |
|---|---|
| 2025-11 | -0.18% |
| 2025-12 | -2.95% |
| 2026-01 | +0.94% |
| 2026-02 | +1.03% |
| 2026-03 | -0.12% |
| 2026-04 | -0.40% |
| 2026-05 | +0.30% |
| 2026-06 | -0.24% |
| 2026-07 | -2.85% |
| 2026-08 | -2.85% |
| 2026-09 | -2.60% |
| 2026-10 | -0.77% |
| 2026-11 | -1.85% |

_Research output, not investment advice. Survivorship: the universe is current index membership._
