# Out-of-sample report: model `oc` (next session open-to-close (the ledger's day-trade rule))

Validation year; the model never trained on these sessions. Window 2025-10-21 to 2026-10-21, 252 sessions. Target = next session open-to-close (the ledger's day-trade rule) return. Costs = 4 bps round trip, the same as the ledger's simulated fund.

## Signal quality

| Metric | Value |
|---|---|
| IC (mean daily Pearson) | 0.0031 |
| ICIR | 0.020 |
| Rank IC | -0.0000 |
| Rank ICIR | -0.000 |
| Days with IC > 0 | 49.6% |

For scale: Qlib's LightGBM/Alpha158 benchmark on CSI300 reports IC 0.045 and Rank IC 0.047 (next-day close-to-close).

## Name-day hit rates (compare with the ledger's hit rate)

| Basket | Hit rate |
|---|---|
| Top-5 longs, share with a positive horizon return | 47.9% |
| Bottom-5 shorts, share with a negative horizon return | 47.6% |
| Top decile longs | 49.4% |
| Bottom decile shorts | 50.0% |
| Base rate: all tradable names with a positive horizon return | 49.4% |

## Horizon-return simulations, net of costs (per $1 of gross exposure)

| Simulation | Days | Mean/day (bps) | Annualized | Sharpe | Hit days | Max DD | t |
|---|---|---|---|---|---|---|---|
| decile_long_short | 252 | -4.5 | -10.6% | -1.277 | 45.6% | -12.3% | -1.28 |
| decile_long_only | 252 | -1.6 | -3.8% | -0.19 | 44.8% | -22.0% | -0.19 |
| top5_long_only | 252 | +3.6 | +9.6% | 0.222 | 48.8% | -36.8% | 0.22 |
| top5_long_bottom5_short | 252 | -11.6 | -25.4% | -1.235 | 46.4% | -35.9% | -1.23 |
| universe_equal_weight_long | 252 | -3.5 | -8.5% | -0.827 | 42.9% | -15.0% | -0.83 |
| spy_same_horizon | 252 | -3.6 | -8.6% | -0.905 | 48.0% | -10.3% | -0.9 |

## Reference: Qlib TopkDropout portfolio backtest (long only, close-to-close)

TopkDropout topk=30 n_drop=3, deal at close, 5+5 bps, benchmark SPY

- Annualized excess return vs SPY: +37.7%
- Information ratio: 1.67
- Max drawdown (excess): -12.7%

## Monthly decile long-short, net

| Month | Return |
|---|---|
| 2025-10 | +0.18% |
| 2025-11 | -0.64% |
| 2025-12 | -2.69% |
| 2026-01 | +1.01% |
| 2026-02 | +0.72% |
| 2026-03 | +1.12% |
| 2026-04 | -1.43% |
| 2026-05 | -0.48% |
| 2026-06 | -1.68% |
| 2026-07 | -4.96% |
| 2026-08 | -1.06% |
| 2026-09 | -0.67% |
| 2026-10 | -0.80% |

_Research output, not investment advice. Survivorship: the universe is current index membership._
