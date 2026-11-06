# Out-of-sample report: model `oc` (next session open-to-close (the ledger's day-trade rule))

Validation year; the model never trained on these sessions. Window 2025-11-04 to 2026-11-04, 252 sessions. Target = next session open-to-close (the ledger's day-trade rule) return. Costs = 4 bps round trip, the same as the ledger's simulated fund.

## Signal quality

| Metric | Value |
|---|---|
| IC (mean daily Pearson) | -0.0011 |
| ICIR | -0.007 |
| Rank IC | 0.0016 |
| Rank ICIR | 0.012 |
| Days with IC > 0 | 49.2% |

For scale: Qlib's LightGBM/Alpha158 benchmark on CSI300 reports IC 0.045 and Rank IC 0.047 (next-day close-to-close).

## Name-day hit rates (compare with the ledger's hit rate)

| Basket | Hit rate |
|---|---|
| Top-5 longs, share with a positive horizon return | 49.3% |
| Bottom-5 shorts, share with a negative horizon return | 49.7% |
| Top decile longs | 48.8% |
| Bottom decile shorts | 50.1% |
| Base rate: all tradable names with a positive horizon return | 49.6% |

## Horizon-return simulations, net of costs (per $1 of gross exposure)

| Simulation | Days | Mean/day (bps) | Annualized | Sharpe | Hit days | Max DD | t |
|---|---|---|---|---|---|---|---|
| decile_long_short | 252 | -6.2 | -14.4% | -1.686 | 46.4% | -16.0% | -1.69 |
| decile_long_only | 252 | -7.0 | -16.2% | -0.812 | 44.8% | -28.9% | -0.81 |
| top5_long_only | 252 | -5.7 | -13.4% | -0.347 | 51.6% | -42.3% | -0.35 |
| top5_long_bottom5_short | 252 | -10.4 | -23.0% | -1.083 | 46.4% | -37.1% | -1.08 |
| universe_equal_weight_long | 252 | -3.6 | -8.8% | -0.82 | 43.2% | -15.3% | -0.82 |
| spy_same_horizon | 252 | -4.8 | -11.3% | -1.111 | 49.2% | -14.3% | -1.11 |

## Reference: Qlib TopkDropout portfolio backtest (long only, close-to-close)

TopkDropout topk=30 n_drop=3, deal at close, 5+5 bps, benchmark SPY

- Annualized excess return vs SPY: +22.4%
- Information ratio: 1.099
- Max drawdown (excess): -15.0%

## Monthly decile long-short, net

| Month | Return |
|---|---|
| 2025-11 | +0.35% |
| 2025-12 | -3.24% |
| 2026-01 | +1.07% |
| 2026-02 | +1.80% |
| 2026-03 | +0.86% |
| 2026-04 | -2.51% |
| 2026-05 | -1.77% |
| 2026-06 | -0.65% |
| 2026-07 | -5.30% |
| 2026-08 | -1.83% |
| 2026-09 | -0.21% |
| 2026-10 | -2.58% |
| 2026-11 | -1.59% |

_Research output, not investment advice. Survivorship: the universe is current index membership._
