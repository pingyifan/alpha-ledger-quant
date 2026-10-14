# Out-of-sample report: model `oc` (next session open-to-close (the ledger's day-trade rule))

Validation year; the model never trained on these sessions. Window 2025-10-10 to 2026-10-12, 252 sessions. Target = next session open-to-close (the ledger's day-trade rule) return. Costs = 4 bps round trip, the same as the ledger's simulated fund.

## Signal quality

| Metric | Value |
|---|---|
| IC (mean daily Pearson) | 0.0023 |
| ICIR | 0.015 |
| Rank IC | 0.0003 |
| Rank ICIR | 0.002 |
| Days with IC > 0 | 49.6% |

For scale: Qlib's LightGBM/Alpha158 benchmark on CSI300 reports IC 0.045 and Rank IC 0.047 (next-day close-to-close).

## Name-day hit rates (compare with the ledger's hit rate)

| Basket | Hit rate |
|---|---|
| Top-5 longs, share with a positive horizon return | 47.7% |
| Bottom-5 shorts, share with a negative horizon return | 47.2% |
| Top decile longs | 49.1% |
| Bottom decile shorts | 49.6% |
| Base rate: all tradable names with a positive horizon return | 49.6% |

## Horizon-return simulations, net of costs (per $1 of gross exposure)

| Simulation | Days | Mean/day (bps) | Annualized | Sharpe | Hit days | Max DD | t |
|---|---|---|---|---|---|---|---|
| decile_long_short | 252 | -5.6 | -13.1% | -1.567 | 46.0% | -14.0% | -1.57 |
| decile_long_only | 252 | -1.8 | -4.4% | -0.22 | 46.8% | -20.1% | -0.22 |
| top5_long_only | 252 | +5.6 | +15.1% | 0.344 | 49.2% | -35.8% | 0.34 |
| top5_long_bottom5_short | 252 | -13.5 | -28.8% | -1.371 | 49.6% | -39.0% | -1.37 |
| universe_equal_weight_long | 252 | -3.2 | -7.8% | -0.755 | 43.6% | -15.0% | -0.75 |
| spy_same_horizon | 252 | -2.7 | -6.5% | -0.677 | 48.4% | -10.0% | -0.68 |

## Reference: Qlib TopkDropout portfolio backtest (long only, close-to-close)

TopkDropout topk=30 n_drop=3, deal at close, 5+5 bps, benchmark SPY

- Annualized excess return vs SPY: +35.9%
- Information ratio: 1.477
- Max drawdown (excess): -14.8%

## Monthly decile long-short, net

| Month | Return |
|---|---|
| 2025-10 | -0.46% |
| 2025-11 | -0.97% |
| 2025-12 | -3.67% |
| 2026-01 | -0.32% |
| 2026-02 | +1.05% |
| 2026-03 | +0.63% |
| 2026-04 | -1.39% |
| 2026-05 | -0.16% |
| 2026-06 | -1.51% |
| 2026-07 | -4.03% |
| 2026-08 | -1.77% |
| 2026-09 | -1.35% |
| 2026-10 | -0.26% |

_Research output, not investment advice. Survivorship: the universe is current index membership._
