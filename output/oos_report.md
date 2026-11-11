# Out-of-sample report: model `oc` (next session open-to-close (the ledger's day-trade rule))

Validation year; the model never trained on these sessions. Window 2025-11-07 to 2026-11-09, 252 sessions. Target = next session open-to-close (the ledger's day-trade rule) return. Costs = 4 bps round trip, the same as the ledger's simulated fund.

## Signal quality

| Metric | Value |
|---|---|
| IC (mean daily Pearson) | -0.0013 |
| ICIR | -0.008 |
| Rank IC | -0.0004 |
| Rank ICIR | -0.003 |
| Days with IC > 0 | 49.2% |

For scale: Qlib's LightGBM/Alpha158 benchmark on CSI300 reports IC 0.045 and Rank IC 0.047 (next-day close-to-close).

## Name-day hit rates (compare with the ledger's hit rate)

| Basket | Hit rate |
|---|---|
| Top-5 longs, share with a positive horizon return | 48.2% |
| Bottom-5 shorts, share with a negative horizon return | 47.3% |
| Top decile longs | 49.3% |
| Bottom decile shorts | 49.2% |
| Base rate: all tradable names with a positive horizon return | 49.7% |

## Horizon-return simulations, net of costs (per $1 of gross exposure)

| Simulation | Days | Mean/day (bps) | Annualized | Sharpe | Hit days | Max DD | t |
|---|---|---|---|---|---|---|---|
| decile_long_short | 252 | -7.7 | -17.7% | -2.143 | 42.9% | -18.3% | -2.14 |
| decile_long_only | 252 | -4.6 | -10.9% | -0.534 | 46.4% | -25.1% | -0.53 |
| top5_long_only | 252 | -4.5 | -10.7% | -0.254 | 48.4% | -44.8% | -0.25 |
| top5_long_bottom5_short | 252 | -15.4 | -32.3% | -1.601 | 46.0% | -37.2% | -1.6 |
| universe_equal_weight_long | 252 | -3.2 | -7.7% | -0.72 | 44.0% | -15.3% | -0.72 |
| spy_same_horizon | 252 | -4.0 | -9.7% | -0.937 | 49.6% | -14.3% | -0.94 |

## Reference: Qlib TopkDropout portfolio backtest (long only, close-to-close)

TopkDropout topk=30 n_drop=3, deal at close, 5+5 bps, benchmark SPY

- Annualized excess return vs SPY: +13.4%
- Information ratio: 0.444
- Max drawdown (excess): -32.6%

## Monthly decile long-short, net

| Month | Return |
|---|---|
| 2025-11 | -0.94% |
| 2025-12 | -3.06% |
| 2026-01 | -0.11% |
| 2026-02 | +0.29% |
| 2026-03 | -0.25% |
| 2026-04 | -1.72% |
| 2026-05 | -0.89% |
| 2026-06 | -2.14% |
| 2026-07 | -3.70% |
| 2026-08 | -1.59% |
| 2026-09 | -1.05% |
| 2026-10 | -1.79% |
| 2026-11 | -2.71% |

_Research output, not investment advice. Survivorship: the universe is current index membership._
