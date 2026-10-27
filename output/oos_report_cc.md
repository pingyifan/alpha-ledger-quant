# Out-of-sample report: model `cc` (next session close to the following session's close (Qlib's native one-session hold, includes the overnight))

Validation year; the model never trained on these sessions. Window 2025-10-22 to 2026-10-22, 252 sessions. Target = next session close to the following session's close (Qlib's native one-session hold, includes the overnight) return. Costs = 4 bps round trip, the same as the ledger's simulated fund.

## Signal quality

| Metric | Value |
|---|---|
| IC (mean daily Pearson) | 0.0201 |
| ICIR | 0.096 |
| Rank IC | 0.0158 |
| Rank ICIR | 0.088 |
| Days with IC > 0 | 59.1% |

For scale: Qlib's LightGBM/Alpha158 benchmark on CSI300 reports IC 0.045 and Rank IC 0.047 (next-day close-to-close).

## Name-day hit rates (compare with the ledger's hit rate)

| Basket | Hit rate |
|---|---|
| Top-5 longs, share with a positive horizon return | 52.1% |
| Bottom-5 shorts, share with a negative horizon return | 48.4% |
| Top decile longs | 50.9% |
| Bottom decile shorts | 49.3% |
| Base rate: all tradable names with a positive horizon return | 50.6% |

## Horizon-return simulations, net of costs (per $1 of gross exposure)

| Simulation | Days | Mean/day (bps) | Annualized | Sharpe | Hit days | Max DD | t |
|---|---|---|---|---|---|---|---|
| decile_long_short | 252 | +0.3 | +0.8% | 0.053 | 54.8% | -10.8% | 0.05 |
| decile_long_only | 252 | +9.8 | +28.0% | 0.833 | 56.0% | -16.4% | 0.83 |
| top5_long_only | 252 | +45.1 | +210.6% | 1.943 | 55.2% | -20.0% | 1.94 |
| top5_long_bottom5_short | 252 | +15.6 | +48.1% | 1.308 | 54.8% | -12.6% | 1.31 |
| universe_equal_weight_long | 252 | +2.8 | +7.2% | 0.549 | 51.6% | -9.1% | 0.55 |
| spy_same_horizon | 252 | +1.9 | +5.0% | 0.381 | 51.6% | -11.3% | 0.38 |

## Reference: Qlib TopkDropout portfolio backtest (long only, close-to-close)

TopkDropout topk=30 n_drop=3, deal at close, 5+5 bps, benchmark SPY

- Annualized excess return vs SPY: +41.1%
- Information ratio: 1.317
- Max drawdown (excess): -24.2%

## Monthly decile long-short, net

| Month | Return |
|---|---|
| 2025-10 | +1.18% |
| 2025-11 | -1.20% |
| 2025-12 | +1.80% |
| 2026-01 | -0.24% |
| 2026-02 | -1.07% |
| 2026-03 | -0.09% |
| 2026-04 | +4.18% |
| 2026-05 | +3.82% |
| 2026-06 | -4.09% |
| 2026-07 | +2.07% |
| 2026-08 | -2.11% |
| 2026-09 | +2.48% |
| 2026-10 | -6.46% |

_Research output, not investment advice. Survivorship: the universe is current index membership._
