# Out-of-sample report: model `oc` (next session open-to-close (the ledger's day-trade rule))

Validation year; the model never trained on these sessions. Window 2025-11-05 to 2026-11-05, 252 sessions. Target = next session open-to-close (the ledger's day-trade rule) return. Costs = 4 bps round trip, the same as the ledger's simulated fund.

## Signal quality

| Metric | Value |
|---|---|
| IC (mean daily Pearson) | -0.0014 |
| ICIR | -0.009 |
| Rank IC | 0.0027 |
| Rank ICIR | 0.020 |
| Days with IC > 0 | 48.0% |

For scale: Qlib's LightGBM/Alpha158 benchmark on CSI300 reports IC 0.045 and Rank IC 0.047 (next-day close-to-close).

## Name-day hit rates (compare with the ledger's hit rate)

| Basket | Hit rate |
|---|---|
| Top-5 longs, share with a positive horizon return | 48.1% |
| Bottom-5 shorts, share with a negative horizon return | 49.5% |
| Top decile longs | 49.3% |
| Bottom decile shorts | 50.4% |
| Base rate: all tradable names with a positive horizon return | 49.6% |

## Horizon-return simulations, net of costs (per $1 of gross exposure)

| Simulation | Days | Mean/day (bps) | Annualized | Sharpe | Hit days | Max DD | t |
|---|---|---|---|---|---|---|---|
| decile_long_short | 252 | -4.9 | -11.7% | -1.356 | 46.8% | -12.8% | -1.36 |
| decile_long_only | 252 | -4.4 | -10.5% | -0.525 | 46.0% | -24.2% | -0.53 |
| top5_long_only | 252 | -12.5 | -27.0% | -0.733 | 47.2% | -43.1% | -0.73 |
| top5_long_bottom5_short | 252 | -15.4 | -32.2% | -1.51 | 46.8% | -38.9% | -1.51 |
| universe_equal_weight_long | 252 | -3.7 | -9.0% | -0.841 | 43.6% | -15.3% | -0.84 |
| spy_same_horizon | 252 | -4.9 | -11.6% | -1.142 | 49.2% | -14.3% | -1.14 |

## Reference: Qlib TopkDropout portfolio backtest (long only, close-to-close)

TopkDropout topk=30 n_drop=3, deal at close, 5+5 bps, benchmark SPY

- Annualized excess return vs SPY: +31.1%
- Information ratio: 1.181
- Max drawdown (excess): -18.4%

## Monthly decile long-short, net

| Month | Return |
|---|---|
| 2025-11 | +0.29% |
| 2025-12 | -2.02% |
| 2026-01 | -0.33% |
| 2026-02 | +0.99% |
| 2026-03 | +1.25% |
| 2026-04 | -1.62% |
| 2026-05 | -1.31% |
| 2026-06 | -1.38% |
| 2026-07 | -2.96% |
| 2026-08 | -1.10% |
| 2026-09 | +0.06% |
| 2026-10 | -1.74% |
| 2026-11 | -2.83% |

_Research output, not investment advice. Survivorship: the universe is current index membership._
