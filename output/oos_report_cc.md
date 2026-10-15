# Out-of-sample report: model `cc` (next session close to the following session's close (Qlib's native one-session hold, includes the overnight))

Validation year; the model never trained on these sessions. Window 2025-10-10 to 2026-10-12, 252 sessions. Target = next session close to the following session's close (Qlib's native one-session hold, includes the overnight) return. Costs = 4 bps round trip, the same as the ledger's simulated fund.

## Signal quality

| Metric | Value |
|---|---|
| IC (mean daily Pearson) | 0.0215 |
| ICIR | 0.106 |
| Rank IC | 0.0184 |
| Rank ICIR | 0.106 |
| Days with IC > 0 | 59.1% |

For scale: Qlib's LightGBM/Alpha158 benchmark on CSI300 reports IC 0.045 and Rank IC 0.047 (next-day close-to-close).

## Name-day hit rates (compare with the ledger's hit rate)

| Basket | Hit rate |
|---|---|
| Top-5 longs, share with a positive horizon return | 52.6% |
| Bottom-5 shorts, share with a negative horizon return | 48.3% |
| Top decile longs | 50.9% |
| Bottom decile shorts | 49.6% |
| Base rate: all tradable names with a positive horizon return | 50.7% |

## Horizon-return simulations, net of costs (per $1 of gross exposure)

| Simulation | Days | Mean/day (bps) | Annualized | Sharpe | Hit days | Max DD | t |
|---|---|---|---|---|---|---|---|
| decile_long_short | 252 | +2.7 | +7.1% | 0.497 | 53.6% | -9.9% | 0.5 |
| decile_long_only | 252 | +12.4 | +36.8% | 1.082 | 54.4% | -14.7% | 1.08 |
| top5_long_only | 252 | +35.4 | +143.4% | 1.582 | 54.4% | -20.7% | 1.58 |
| top5_long_bottom5_short | 252 | +8.6 | +24.3% | 0.771 | 49.6% | -13.2% | 0.77 |
| universe_equal_weight_long | 252 | +2.7 | +7.1% | 0.544 | 52.0% | -9.1% | 0.54 |
| spy_same_horizon | 252 | +2.7 | +6.9% | 0.529 | 51.2% | -11.3% | 0.53 |

## Reference: Qlib TopkDropout portfolio backtest (long only, close-to-close)

TopkDropout topk=30 n_drop=3, deal at close, 5+5 bps, benchmark SPY

- Annualized excess return vs SPY: +46.3%
- Information ratio: 1.537
- Max drawdown (excess): -20.4%

## Monthly decile long-short, net

| Month | Return |
|---|---|
| 2025-10 | +1.57% |
| 2025-11 | -1.13% |
| 2025-12 | +1.76% |
| 2026-01 | -0.96% |
| 2026-02 | -1.67% |
| 2026-03 | +0.33% |
| 2026-04 | +4.10% |
| 2026-05 | +4.72% |
| 2026-06 | -3.93% |
| 2026-07 | +2.44% |
| 2026-08 | -0.86% |
| 2026-09 | +2.46% |
| 2026-10 | -2.46% |

_Research output, not investment advice. Survivorship: the universe is current index membership._
