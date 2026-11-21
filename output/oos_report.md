# Out-of-sample report: model `oc` (next session open-to-close (the ledger's day-trade rule))

Validation year; the model never trained on these sessions. Window 2025-11-19 to 2026-11-19, 252 sessions. Target = next session open-to-close (the ledger's day-trade rule) return. Costs = 4 bps round trip, the same as the ledger's simulated fund.

## Signal quality

| Metric | Value |
|---|---|
| IC (mean daily Pearson) | -0.0046 |
| ICIR | -0.037 |
| Rank IC | -0.0015 |
| Rank ICIR | -0.012 |
| Days with IC > 0 | 46.8% |

For scale: Qlib's LightGBM/Alpha158 benchmark on CSI300 reports IC 0.045 and Rank IC 0.047 (next-day close-to-close).

## Name-day hit rates (compare with the ledger's hit rate)

| Basket | Hit rate |
|---|---|
| Top-5 longs, share with a positive horizon return | 49.8% |
| Bottom-5 shorts, share with a negative horizon return | 52.3% |
| Top decile longs | 49.5% |
| Bottom decile shorts | 50.3% |
| Base rate: all tradable names with a positive horizon return | 49.2% |

## Horizon-return simulations, net of costs (per $1 of gross exposure)

| Simulation | Days | Mean/day (bps) | Annualized | Sharpe | Hit days | Max DD | t |
|---|---|---|---|---|---|---|---|
| decile_long_short | 252 | -5.3 | -12.5% | -1.75 | 44.8% | -12.8% | -1.75 |
| decile_long_only | 252 | -5.1 | -12.1% | -0.67 | 46.8% | -25.0% | -0.67 |
| top5_long_only | 252 | -2.3 | -5.6% | -0.155 | 49.2% | -42.9% | -0.16 |
| top5_long_bottom5_short | 252 | -1.7 | -4.2% | -0.222 | 53.2% | -18.1% | -0.22 |
| universe_equal_weight_long | 252 | -5.3 | -12.6% | -1.162 | 43.2% | -19.3% | -1.16 |
| spy_same_horizon | 252 | -7.5 | -17.2% | -1.612 | 48.8% | -20.5% | -1.61 |

## Reference: Qlib TopkDropout portfolio backtest (long only, close-to-close)

TopkDropout topk=30 n_drop=3, deal at close, 5+5 bps, benchmark SPY

- Annualized excess return vs SPY: +42.2%
- Information ratio: 1.938
- Max drawdown (excess): -13.0%

## Monthly decile long-short, net

| Month | Return |
|---|---|
| 2025-11 | +0.02% |
| 2025-12 | -3.87% |
| 2026-01 | +1.52% |
| 2026-02 | +0.98% |
| 2026-03 | +0.54% |
| 2026-04 | -0.18% |
| 2026-05 | -1.21% |
| 2026-06 | +0.05% |
| 2026-07 | -1.70% |
| 2026-08 | -0.71% |
| 2026-09 | -1.28% |
| 2026-10 | -2.58% |
| 2026-11 | -4.94% |

_Research output, not investment advice. Survivorship: the universe is current index membership._
