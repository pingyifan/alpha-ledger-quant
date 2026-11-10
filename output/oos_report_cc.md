# Out-of-sample report: model `cc` (next session close to the following session's close (Qlib's native one-session hold, includes the overnight))

Validation year; the model never trained on these sessions. Window 2025-11-05 to 2026-11-05, 252 sessions. Target = next session close to the following session's close (Qlib's native one-session hold, includes the overnight) return. Costs = 4 bps round trip, the same as the ledger's simulated fund.

## Signal quality

| Metric | Value |
|---|---|
| IC (mean daily Pearson) | 0.0197 |
| ICIR | 0.091 |
| Rank IC | 0.0177 |
| Rank ICIR | 0.095 |
| Days with IC > 0 | 59.9% |

For scale: Qlib's LightGBM/Alpha158 benchmark on CSI300 reports IC 0.045 and Rank IC 0.047 (next-day close-to-close).

## Name-day hit rates (compare with the ledger's hit rate)

| Basket | Hit rate |
|---|---|
| Top-5 longs, share with a positive horizon return | 51.7% |
| Bottom-5 shorts, share with a negative horizon return | 49.4% |
| Top decile longs | 51.0% |
| Bottom decile shorts | 49.2% |
| Base rate: all tradable names with a positive horizon return | 51.1% |

## Horizon-return simulations, net of costs (per $1 of gross exposure)

| Simulation | Days | Mean/day (bps) | Annualized | Sharpe | Hit days | Max DD | t |
|---|---|---|---|---|---|---|---|
| decile_long_short | 252 | -0.3 | -0.8% | -0.05 | 54.0% | -14.7% | -0.05 |
| decile_long_only | 252 | +10.4 | +30.0% | 0.822 | 55.2% | -22.4% | 0.82 |
| top5_long_only | 252 | +30.2 | +114.0% | 1.295 | 54.8% | -26.1% | 1.29 |
| top5_long_bottom5_short | 252 | +8.9 | +25.0% | 0.751 | 48.8% | -22.2% | 0.75 |
| universe_equal_weight_long | 252 | +4.7 | +12.6% | 0.885 | 52.4% | -9.1% | 0.89 |
| spy_same_horizon | 252 | +1.4 | +3.6% | 0.257 | 51.2% | -10.8% | 0.26 |

## Reference: Qlib TopkDropout portfolio backtest (long only, close-to-close)

TopkDropout topk=30 n_drop=3, deal at close, 5+5 bps, benchmark SPY

- Annualized excess return vs SPY: +33.2%
- Information ratio: 1.062
- Max drawdown (excess): -22.8%

## Monthly decile long-short, net

| Month | Return |
|---|---|
| 2025-11 | -0.48% |
| 2025-12 | +1.52% |
| 2026-01 | -0.26% |
| 2026-02 | -0.69% |
| 2026-03 | +1.17% |
| 2026-04 | +3.64% |
| 2026-05 | +4.71% |
| 2026-06 | -4.80% |
| 2026-07 | +2.07% |
| 2026-08 | -1.75% |
| 2026-09 | +2.63% |
| 2026-10 | -5.96% |
| 2026-11 | -3.26% |

_Research output, not investment advice. Survivorship: the universe is current index membership._
