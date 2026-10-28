# Out-of-sample report: model `oc` (next session open-to-close (the ledger's day-trade rule))

Validation year; the model never trained on these sessions. Window 2025-10-24 to 2026-10-26, 252 sessions. Target = next session open-to-close (the ledger's day-trade rule) return. Costs = 4 bps round trip, the same as the ledger's simulated fund.

## Signal quality

| Metric | Value |
|---|---|
| IC (mean daily Pearson) | 0.0018 |
| ICIR | 0.012 |
| Rank IC | -0.0015 |
| Rank ICIR | -0.011 |
| Days with IC > 0 | 46.8% |

For scale: Qlib's LightGBM/Alpha158 benchmark on CSI300 reports IC 0.045 and Rank IC 0.047 (next-day close-to-close).

## Name-day hit rates (compare with the ledger's hit rate)

| Basket | Hit rate |
|---|---|
| Top-5 longs, share with a positive horizon return | 49.4% |
| Bottom-5 shorts, share with a negative horizon return | 48.6% |
| Top decile longs | 49.4% |
| Bottom decile shorts | 49.6% |
| Base rate: all tradable names with a positive horizon return | 49.6% |

## Horizon-return simulations, net of costs (per $1 of gross exposure)

| Simulation | Days | Mean/day (bps) | Annualized | Sharpe | Hit days | Max DD | t |
|---|---|---|---|---|---|---|---|
| decile_long_short | 252 | -5.6 | -13.1% | -1.586 | 42.5% | -14.5% | -1.59 |
| decile_long_only | 252 | -2.5 | -6.0% | -0.303 | 46.8% | -22.0% | -0.3 |
| top5_long_only | 252 | +5.5 | +15.0% | 0.327 | 49.6% | -41.8% | 0.33 |
| top5_long_bottom5_short | 252 | -12.8 | -27.7% | -1.346 | 48.4% | -37.4% | -1.35 |
| universe_equal_weight_long | 252 | -3.2 | -7.7% | -0.748 | 43.2% | -15.0% | -0.75 |
| spy_same_horizon | 252 | -3.3 | -8.0% | -0.838 | 48.0% | -10.3% | -0.84 |

## Reference: Qlib TopkDropout portfolio backtest (long only, close-to-close)

TopkDropout topk=30 n_drop=3, deal at close, 5+5 bps, benchmark SPY

- Annualized excess return vs SPY: +23.1%
- Information ratio: 0.982
- Max drawdown (excess): -17.5%

## Monthly decile long-short, net

| Month | Return |
|---|---|
| 2025-10 | -0.41% |
| 2025-11 | -0.23% |
| 2025-12 | -2.95% |
| 2026-01 | +0.56% |
| 2026-02 | +0.77% |
| 2026-03 | +0.45% |
| 2026-04 | -2.01% |
| 2026-05 | -0.90% |
| 2026-06 | -1.99% |
| 2026-07 | -4.90% |
| 2026-08 | -1.37% |
| 2026-09 | -0.18% |
| 2026-10 | -1.06% |

_Research output, not investment advice. Survivorship: the universe is current index membership._
