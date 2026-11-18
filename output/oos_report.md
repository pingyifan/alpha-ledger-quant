# Out-of-sample report: model `oc` (next session open-to-close (the ledger's day-trade rule))

Validation year; the model never trained on these sessions. Window 2025-11-14 to 2026-11-16, 252 sessions. Target = next session open-to-close (the ledger's day-trade rule) return. Costs = 4 bps round trip, the same as the ledger's simulated fund.

## Signal quality

| Metric | Value |
|---|---|
| IC (mean daily Pearson) | -0.0001 |
| ICIR | -0.001 |
| Rank IC | -0.0024 |
| Rank ICIR | -0.022 |
| Days with IC > 0 | 52.4% |

For scale: Qlib's LightGBM/Alpha158 benchmark on CSI300 reports IC 0.045 and Rank IC 0.047 (next-day close-to-close).

## Name-day hit rates (compare with the ledger's hit rate)

| Basket | Hit rate |
|---|---|
| Top-5 longs, share with a positive horizon return | 50.5% |
| Bottom-5 shorts, share with a negative horizon return | 49.9% |
| Top decile longs | 49.5% |
| Bottom decile shorts | 49.9% |
| Base rate: all tradable names with a positive horizon return | 49.4% |

## Horizon-return simulations, net of costs (per $1 of gross exposure)

| Simulation | Days | Mean/day (bps) | Annualized | Sharpe | Hit days | Max DD | t |
|---|---|---|---|---|---|---|---|
| decile_long_short | 252 | -4.2 | -9.9% | -1.407 | 46.0% | -11.5% | -1.41 |
| decile_long_only | 252 | -1.6 | -4.1% | -0.209 | 46.4% | -21.6% | -0.21 |
| top5_long_only | 252 | +0.1 | +0.3% | 0.007 | 50.4% | -38.7% | 0.01 |
| top5_long_bottom5_short | 252 | -5.9 | -13.7% | -0.775 | 50.8% | -26.4% | -0.78 |
| universe_equal_weight_long | 252 | -4.2 | -10.1% | -0.946 | 43.2% | -15.9% | -0.95 |
| spy_same_horizon | 252 | -5.1 | -12.0% | -1.18 | 49.2% | -14.8% | -1.18 |

## Reference: Qlib TopkDropout portfolio backtest (long only, close-to-close)

TopkDropout topk=30 n_drop=3, deal at close, 5+5 bps, benchmark SPY

- Annualized excess return vs SPY: +31.8%
- Information ratio: 1.545
- Max drawdown (excess): -16.0%

## Monthly decile long-short, net

| Month | Return |
|---|---|
| 2025-11 | +0.11% |
| 2025-12 | -2.61% |
| 2026-01 | -0.02% |
| 2026-02 | +1.94% |
| 2026-03 | +1.72% |
| 2026-04 | -1.81% |
| 2026-05 | -0.50% |
| 2026-06 | -0.81% |
| 2026-07 | -3.80% |
| 2026-08 | +0.14% |
| 2026-09 | -1.75% |
| 2026-10 | -0.76% |
| 2026-11 | -2.37% |

_Research output, not investment advice. Survivorship: the universe is current index membership._
