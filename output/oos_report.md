# Out-of-sample report: model `oc` (next session open-to-close (the ledger's day-trade rule))

Validation year; the model never trained on these sessions. Window 2025-11-18 to 2026-11-18, 252 sessions. Target = next session open-to-close (the ledger's day-trade rule) return. Costs = 4 bps round trip, the same as the ledger's simulated fund.

## Signal quality

| Metric | Value |
|---|---|
| IC (mean daily Pearson) | -0.0057 |
| ICIR | -0.056 |
| Rank IC | 0.0004 |
| Rank ICIR | 0.006 |
| Days with IC > 0 | 47.2% |

For scale: Qlib's LightGBM/Alpha158 benchmark on CSI300 reports IC 0.045 and Rank IC 0.047 (next-day close-to-close).

## Name-day hit rates (compare with the ledger's hit rate)

| Basket | Hit rate |
|---|---|
| Top-5 longs, share with a positive horizon return | 49.8% |
| Bottom-5 shorts, share with a negative horizon return | 48.8% |
| Top decile longs | 49.4% |
| Bottom decile shorts | 50.3% |
| Base rate: all tradable names with a positive horizon return | 49.3% |

## Horizon-return simulations, net of costs (per $1 of gross exposure)

| Simulation | Days | Mean/day (bps) | Annualized | Sharpe | Hit days | Max DD | t |
|---|---|---|---|---|---|---|---|
| decile_long_short | 252 | -5.3 | -12.5% | -2.453 | 40.5% | -13.0% | -2.45 |
| decile_long_only | 252 | -6.2 | -14.5% | -0.841 | 43.6% | -25.1% | -0.84 |
| top5_long_only | 252 | +4.7 | +12.5% | 0.309 | 47.2% | -35.9% | 0.31 |
| top5_long_bottom5_short | 252 | -11.7 | -25.6% | -1.465 | 44.4% | -33.2% | -1.46 |
| universe_equal_weight_long | 252 | -4.5 | -10.6% | -0.988 | 43.2% | -17.3% | -0.99 |
| spy_same_horizon | 252 | -6.1 | -14.2% | -1.359 | 49.2% | -17.8% | -1.36 |

## Reference: Qlib TopkDropout portfolio backtest (long only, close-to-close)

TopkDropout topk=30 n_drop=3, deal at close, 5+5 bps, benchmark SPY

- Annualized excess return vs SPY: +15.1%
- Information ratio: 0.768
- Max drawdown (excess): -14.8%

## Monthly decile long-short, net

| Month | Return |
|---|---|
| 2025-11 | -0.50% |
| 2025-12 | -1.25% |
| 2026-01 | -1.12% |
| 2026-02 | +0.30% |
| 2026-03 | -0.88% |
| 2026-04 | -0.70% |
| 2026-05 | -1.02% |
| 2026-06 | -1.31% |
| 2026-07 | -1.99% |
| 2026-08 | -2.10% |
| 2026-09 | -0.45% |
| 2026-10 | -0.39% |
| 2026-11 | -2.01% |

_Research output, not investment advice. Survivorship: the universe is current index membership._
