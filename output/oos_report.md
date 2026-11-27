# Out-of-sample report: model `oc` (next session open-to-close (the ledger's day-trade rule))

Validation year; the model never trained on these sessions. Window 2025-11-24 to 2026-11-24, 252 sessions. Target = next session open-to-close (the ledger's day-trade rule) return. Costs = 4 bps round trip, the same as the ledger's simulated fund.

## Signal quality

| Metric | Value |
|---|---|
| IC (mean daily Pearson) | -0.0020 |
| ICIR | -0.017 |
| Rank IC | -0.0042 |
| Rank ICIR | -0.039 |
| Days with IC > 0 | 47.2% |

For scale: Qlib's LightGBM/Alpha158 benchmark on CSI300 reports IC 0.045 and Rank IC 0.047 (next-day close-to-close).

## Name-day hit rates (compare with the ledger's hit rate)

| Basket | Hit rate |
|---|---|
| Top-5 longs, share with a positive horizon return | 49.6% |
| Bottom-5 shorts, share with a negative horizon return | 49.2% |
| Top decile longs | 49.5% |
| Bottom decile shorts | 49.7% |
| Base rate: all tradable names with a positive horizon return | 49.5% |

## Horizon-return simulations, net of costs (per $1 of gross exposure)

| Simulation | Days | Mean/day (bps) | Annualized | Sharpe | Hit days | Max DD | t |
|---|---|---|---|---|---|---|---|
| decile_long_short | 252 | -5.9 | -13.8% | -2.079 | 42.1% | -15.4% | -2.08 |
| decile_long_only | 252 | -2.4 | -5.9% | -0.308 | 45.2% | -28.7% | -0.31 |
| top5_long_only | 252 | +7.2 | +19.8% | 0.452 | 52.0% | -44.1% | 0.45 |
| top5_long_bottom5_short | 252 | -10.2 | -22.6% | -1.174 | 48.8% | -34.4% | -1.17 |
| universe_equal_weight_long | 252 | -4.1 | -9.8% | -0.894 | 43.6% | -19.3% | -0.89 |
| spy_same_horizon | 252 | -6.0 | -14.1% | -1.33 | 48.8% | -20.8% | -1.33 |

## Reference: Qlib TopkDropout portfolio backtest (long only, close-to-close)

TopkDropout topk=30 n_drop=3, deal at close, 5+5 bps, benchmark SPY

- Annualized excess return vs SPY: +22.7%
- Information ratio: 0.926
- Max drawdown (excess): -20.5%

## Monthly decile long-short, net

| Month | Return |
|---|---|
| 2025-11 | -0.23% |
| 2025-12 | -3.05% |
| 2026-01 | +0.65% |
| 2026-02 | +1.45% |
| 2026-03 | +1.22% |
| 2026-04 | -3.65% |
| 2026-05 | -1.45% |
| 2026-06 | -1.37% |
| 2026-07 | -0.92% |
| 2026-08 | -0.56% |
| 2026-09 | -0.62% |
| 2026-10 | -1.59% |
| 2026-11 | -4.70% |

_Research output, not investment advice. Survivorship: the universe is current index membership._
