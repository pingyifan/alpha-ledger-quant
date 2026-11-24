# Out-of-sample report: model `oc` (next session open-to-close (the ledger's day-trade rule))

Validation year; the model never trained on these sessions. Window 2025-11-20 to 2026-11-20, 252 sessions. Target = next session open-to-close (the ledger's day-trade rule) return. Costs = 4 bps round trip, the same as the ledger's simulated fund.

## Signal quality

| Metric | Value |
|---|---|
| IC (mean daily Pearson) | -0.0057 |
| ICIR | -0.050 |
| Rank IC | -0.0047 |
| Rank ICIR | -0.044 |
| Days with IC > 0 | 51.6% |

For scale: Qlib's LightGBM/Alpha158 benchmark on CSI300 reports IC 0.045 and Rank IC 0.047 (next-day close-to-close).

## Name-day hit rates (compare with the ledger's hit rate)

| Basket | Hit rate |
|---|---|
| Top-5 longs, share with a positive horizon return | 49.6% |
| Bottom-5 shorts, share with a negative horizon return | 51.3% |
| Top decile longs | 49.1% |
| Bottom decile shorts | 50.1% |
| Base rate: all tradable names with a positive horizon return | 49.4% |

## Horizon-return simulations, net of costs (per $1 of gross exposure)

| Simulation | Days | Mean/day (bps) | Annualized | Sharpe | Hit days | Max DD | t |
|---|---|---|---|---|---|---|---|
| decile_long_short | 252 | -7.2 | -16.5% | -2.381 | 46.4% | -17.0% | -2.38 |
| decile_long_only | 252 | -7.6 | -17.4% | -1.018 | 45.6% | -31.1% | -1.02 |
| top5_long_only | 252 | +6.0 | +16.2% | 0.426 | 47.6% | -37.2% | 0.43 |
| top5_long_bottom5_short | 252 | -0.4 | -1.0% | -0.056 | 50.0% | -12.3% | -0.06 |
| universe_equal_weight_long | 252 | -4.4 | -10.4% | -0.966 | 43.6% | -19.3% | -0.97 |
| spy_same_horizon | 252 | -6.4 | -14.9% | -1.425 | 48.8% | -20.8% | -1.42 |

## Reference: Qlib TopkDropout portfolio backtest (long only, close-to-close)

TopkDropout topk=30 n_drop=3, deal at close, 5+5 bps, benchmark SPY

- Annualized excess return vs SPY: +37.3%
- Information ratio: 1.98
- Max drawdown (excess): -9.2%

## Monthly decile long-short, net

| Month | Return |
|---|---|
| 2025-11 | +0.22% |
| 2025-12 | -1.60% |
| 2026-01 | -1.28% |
| 2026-02 | +1.64% |
| 2026-03 | +0.14% |
| 2026-04 | -0.20% |
| 2026-05 | -1.10% |
| 2026-06 | -2.04% |
| 2026-07 | -4.10% |
| 2026-08 | -1.61% |
| 2026-09 | -1.46% |
| 2026-10 | -1.18% |
| 2026-11 | -5.44% |

_Research output, not investment advice. Survivorship: the universe is current index membership._
