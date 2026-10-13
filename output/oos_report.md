# Out-of-sample report: model `oc` (next session open-to-close (the ledger's day-trade rule))

Validation year; the model never trained on these sessions. Window 2025-10-09 to 2026-10-09, 252 sessions. Target = next session open-to-close (the ledger's day-trade rule) return. Costs = 4 bps round trip, the same as the ledger's simulated fund.

## Signal quality

| Metric | Value |
|---|---|
| IC (mean daily Pearson) | 0.0021 |
| ICIR | 0.014 |
| Rank IC | 0.0006 |
| Rank ICIR | 0.005 |
| Days with IC > 0 | 49.6% |

For scale: Qlib's LightGBM/Alpha158 benchmark on CSI300 reports IC 0.045 and Rank IC 0.047 (next-day close-to-close).

## Name-day hit rates (compare with the ledger's hit rate)

| Basket | Hit rate |
|---|---|
| Top-5 longs, share with a positive horizon return | 49.5% |
| Bottom-5 shorts, share with a negative horizon return | 47.9% |
| Top decile longs | 49.2% |
| Bottom decile shorts | 49.8% |
| Base rate: all tradable names with a positive horizon return | 49.4% |

## Horizon-return simulations, net of costs (per $1 of gross exposure)

| Simulation | Days | Mean/day (bps) | Annualized | Sharpe | Hit days | Max DD | t |
|---|---|---|---|---|---|---|---|
| decile_long_short | 252 | -4.9 | -11.5% | -1.382 | 45.6% | -13.3% | -1.38 |
| decile_long_only | 252 | -3.0 | -7.2% | -0.357 | 44.0% | -21.2% | -0.36 |
| top5_long_only | 252 | +6.7 | +18.5% | 0.415 | 49.6% | -34.9% | 0.41 |
| top5_long_bottom5_short | 252 | -10.7 | -23.6% | -1.1 | 50.0% | -40.0% | -1.1 |
| universe_equal_weight_long | 252 | -4.3 | -10.3% | -0.977 | 43.6% | -15.0% | -0.98 |
| spy_same_horizon | 252 | -3.8 | -9.2% | -0.935 | 48.0% | -10.0% | -0.94 |

## Reference: Qlib TopkDropout portfolio backtest (long only, close-to-close)

TopkDropout topk=30 n_drop=3, deal at close, 5+5 bps, benchmark SPY

- Annualized excess return vs SPY: +35.2%
- Information ratio: 1.504
- Max drawdown (excess): -11.9%

## Monthly decile long-short, net

| Month | Return |
|---|---|
| 2025-10 | +0.69% |
| 2025-11 | -0.54% |
| 2025-12 | -3.38% |
| 2026-01 | +0.85% |
| 2026-02 | +0.69% |
| 2026-03 | +0.85% |
| 2026-04 | -1.34% |
| 2026-05 | -0.69% |
| 2026-06 | -1.80% |
| 2026-07 | -4.70% |
| 2026-08 | -2.07% |
| 2026-09 | -0.51% |
| 2026-10 | -0.47% |

_Research output, not investment advice. Survivorship: the universe is current index membership._
