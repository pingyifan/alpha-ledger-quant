# Out-of-sample report: model `oc` (next session open-to-close (the ledger's day-trade rule))

Validation year; the model never trained on these sessions. Window 2025-11-03 to 2026-11-03, 252 sessions. Target = next session open-to-close (the ledger's day-trade rule) return. Costs = 4 bps round trip, the same as the ledger's simulated fund.

## Signal quality

| Metric | Value |
|---|---|
| IC (mean daily Pearson) | 0.0013 |
| ICIR | 0.008 |
| Rank IC | 0.0027 |
| Rank ICIR | 0.019 |
| Days with IC > 0 | 48.8% |

For scale: Qlib's LightGBM/Alpha158 benchmark on CSI300 reports IC 0.045 and Rank IC 0.047 (next-day close-to-close).

## Name-day hit rates (compare with the ledger's hit rate)

| Basket | Hit rate |
|---|---|
| Top-5 longs, share with a positive horizon return | 48.6% |
| Bottom-5 shorts, share with a negative horizon return | 47.9% |
| Top decile longs | 49.4% |
| Bottom decile shorts | 49.6% |
| Base rate: all tradable names with a positive horizon return | 49.8% |

## Horizon-return simulations, net of costs (per $1 of gross exposure)

| Simulation | Days | Mean/day (bps) | Annualized | Sharpe | Hit days | Max DD | t |
|---|---|---|---|---|---|---|---|
| decile_long_short | 252 | -7.1 | -16.4% | -1.899 | 45.6% | -17.3% | -1.9 |
| decile_long_only | 252 | -3.9 | -9.4% | -0.472 | 48.4% | -23.4% | -0.47 |
| top5_long_only | 252 | -2.2 | -5.4% | -0.138 | 48.0% | -36.9% | -0.14 |
| top5_long_bottom5_short | 252 | -16.8 | -34.4% | -1.75 | 46.0% | -41.1% | -1.75 |
| universe_equal_weight_long | 252 | -2.2 | -5.5% | -0.527 | 44.0% | -15.0% | -0.53 |
| spy_same_horizon | 252 | -3.1 | -7.6% | -0.795 | 49.2% | -11.1% | -0.79 |

## Reference: Qlib TopkDropout portfolio backtest (long only, close-to-close)

TopkDropout topk=30 n_drop=3, deal at close, 5+5 bps, benchmark SPY

- Annualized excess return vs SPY: +30.9%
- Information ratio: 1.207
- Max drawdown (excess): -18.2%

## Monthly decile long-short, net

| Month | Return |
|---|---|
| 2025-11 | -1.12% |
| 2025-12 | -2.86% |
| 2026-01 | -0.03% |
| 2026-02 | +1.13% |
| 2026-03 | +0.41% |
| 2026-04 | -2.35% |
| 2026-05 | -1.40% |
| 2026-06 | -2.00% |
| 2026-07 | -4.17% |
| 2026-08 | -1.75% |
| 2026-09 | -1.00% |
| 2026-10 | -2.80% |
| 2026-11 | -0.16% |

_Research output, not investment advice. Survivorship: the universe is current index membership._
