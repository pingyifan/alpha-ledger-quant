# Out-of-sample report: model `cc` (next session close to the following session's close (Qlib's native one-session hold, includes the overnight))

Validation year; the model never trained on these sessions. Window 2025-10-09 to 2026-10-09, 252 sessions. Target = next session close to the following session's close (Qlib's native one-session hold, includes the overnight) return. Costs = 4 bps round trip, the same as the ledger's simulated fund.

## Signal quality

| Metric | Value |
|---|---|
| IC (mean daily Pearson) | 0.0244 |
| ICIR | 0.120 |
| Rank IC | 0.0202 |
| Rank ICIR | 0.116 |
| Days with IC > 0 | 59.1% |

For scale: Qlib's LightGBM/Alpha158 benchmark on CSI300 reports IC 0.045 and Rank IC 0.047 (next-day close-to-close).

## Name-day hit rates (compare with the ledger's hit rate)

| Basket | Hit rate |
|---|---|
| Top-5 longs, share with a positive horizon return | 53.1% |
| Bottom-5 shorts, share with a negative horizon return | 47.0% |
| Top decile longs | 51.3% |
| Bottom decile shorts | 49.4% |
| Base rate: all tradable names with a positive horizon return | 50.9% |

## Horizon-return simulations, net of costs (per $1 of gross exposure)

| Simulation | Days | Mean/day (bps) | Annualized | Sharpe | Hit days | Max DD | t |
|---|---|---|---|---|---|---|---|
| decile_long_short | 252 | +4.8 | +12.7% | 0.861 | 55.2% | -9.8% | 0.86 |
| decile_long_only | 252 | +16.9 | +52.9% | 1.465 | 54.8% | -14.8% | 1.47 |
| top5_long_only | 252 | +42.5 | +191.0% | 1.829 | 56.8% | -19.2% | 1.83 |
| top5_long_bottom5_short | 252 | +10.4 | +29.9% | 0.894 | 51.6% | -13.6% | 0.89 |
| universe_equal_weight_long | 252 | +3.6 | +9.7% | 0.726 | 52.4% | -9.1% | 0.73 |
| spy_same_horizon | 252 | +3.7 | +9.8% | 0.733 | 51.6% | -11.3% | 0.73 |

## Reference: Qlib TopkDropout portfolio backtest (long only, close-to-close)

TopkDropout topk=30 n_drop=3, deal at close, 5+5 bps, benchmark SPY

- Annualized excess return vs SPY: +56.2%
- Information ratio: 1.839
- Max drawdown (excess): -24.9%

## Monthly decile long-short, net

| Month | Return |
|---|---|
| 2025-10 | +2.72% |
| 2025-11 | -0.20% |
| 2025-12 | +1.67% |
| 2026-01 | -1.17% |
| 2026-02 | -0.96% |
| 2026-03 | +0.63% |
| 2026-04 | +4.25% |
| 2026-05 | +5.35% |
| 2026-06 | -3.37% |
| 2026-07 | +2.63% |
| 2026-08 | -1.31% |
| 2026-09 | +1.96% |
| 2026-10 | -0.76% |

_Research output, not investment advice. Survivorship: the universe is current index membership._
