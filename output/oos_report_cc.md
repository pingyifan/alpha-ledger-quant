# Out-of-sample report: model `cc` (next session close to the following session's close (Qlib's native one-session hold, includes the overnight))

Validation year; the model never trained on these sessions. Window 2025-11-20 to 2026-11-20, 252 sessions. Target = next session close to the following session's close (Qlib's native one-session hold, includes the overnight) return. Costs = 4 bps round trip, the same as the ledger's simulated fund.

## Signal quality

| Metric | Value |
|---|---|
| IC (mean daily Pearson) | 0.0220 |
| ICIR | 0.102 |
| Rank IC | 0.0179 |
| Rank ICIR | 0.094 |
| Days with IC > 0 | 58.3% |

For scale: Qlib's LightGBM/Alpha158 benchmark on CSI300 reports IC 0.045 and Rank IC 0.047 (next-day close-to-close).

## Name-day hit rates (compare with the ledger's hit rate)

| Basket | Hit rate |
|---|---|
| Top-5 longs, share with a positive horizon return | 52.6% |
| Bottom-5 shorts, share with a negative horizon return | 50.2% |
| Top decile longs | 50.9% |
| Bottom decile shorts | 49.2% |
| Base rate: all tradable names with a positive horizon return | 50.7% |

## Horizon-return simulations, net of costs (per $1 of gross exposure)

| Simulation | Days | Mean/day (bps) | Annualized | Sharpe | Hit days | Max DD | t |
|---|---|---|---|---|---|---|---|
| decile_long_short | 252 | -0.1 | -0.2% | -0.013 | 53.6% | -16.1% | -0.01 |
| decile_long_only | 252 | +9.7 | +27.6% | 0.734 | 53.6% | -26.6% | 0.73 |
| top5_long_only | 252 | +34.8 | +139.9% | 1.464 | 52.0% | -30.0% | 1.46 |
| top5_long_bottom5_short | 252 | +19.4 | +63.1% | 1.515 | 52.4% | -12.4% | 1.51 |
| universe_equal_weight_long | 252 | +3.3 | +8.6% | 0.592 | 52.0% | -10.7% | 0.59 |
| spy_same_horizon | 252 | +0.3 | +0.8% | 0.053 | 49.6% | -13.6% | 0.05 |

## Reference: Qlib TopkDropout portfolio backtest (long only, close-to-close)

TopkDropout topk=30 n_drop=3, deal at close, 5+5 bps, benchmark SPY

- Annualized excess return vs SPY: +40.5%
- Information ratio: 1.3
- Max drawdown (excess): -17.6%

## Monthly decile long-short, net

| Month | Return |
|---|---|
| 2025-11 | +2.80% |
| 2025-12 | +1.47% |
| 2026-01 | +0.32% |
| 2026-02 | -1.54% |
| 2026-03 | +1.41% |
| 2026-04 | +2.72% |
| 2026-05 | +5.30% |
| 2026-06 | -5.95% |
| 2026-07 | +1.95% |
| 2026-08 | -1.34% |
| 2026-09 | +2.32% |
| 2026-10 | -6.06% |
| 2026-11 | -4.22% |

_Research output, not investment advice. Survivorship: the universe is current index membership._
