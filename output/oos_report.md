# Out-of-sample report: model `oc` (next session open-to-close (the ledger's day-trade rule))

Validation year; the model never trained on these sessions. Window 2025-11-11 to 2026-11-11, 252 sessions. Target = next session open-to-close (the ledger's day-trade rule) return. Costs = 4 bps round trip, the same as the ledger's simulated fund.

## Signal quality

| Metric | Value |
|---|---|
| IC (mean daily Pearson) | -0.0030 |
| ICIR | -0.022 |
| Rank IC | -0.0021 |
| Rank ICIR | -0.018 |
| Days with IC > 0 | 51.2% |

For scale: Qlib's LightGBM/Alpha158 benchmark on CSI300 reports IC 0.045 and Rank IC 0.047 (next-day close-to-close).

## Name-day hit rates (compare with the ledger's hit rate)

| Basket | Hit rate |
|---|---|
| Top-5 longs, share with a positive horizon return | 47.9% |
| Bottom-5 shorts, share with a negative horizon return | 47.3% |
| Top decile longs | 49.9% |
| Bottom decile shorts | 49.4% |
| Base rate: all tradable names with a positive horizon return | 49.6% |

## Horizon-return simulations, net of costs (per $1 of gross exposure)

| Simulation | Days | Mean/day (bps) | Annualized | Sharpe | Hit days | Max DD | t |
|---|---|---|---|---|---|---|---|
| decile_long_short | 252 | -4.5 | -10.7% | -1.421 | 44.0% | -11.4% | -1.42 |
| decile_long_only | 252 | -0.1 | -0.4% | -0.018 | 47.2% | -19.4% | -0.02 |
| top5_long_only | 252 | -6.8 | -15.8% | -0.42 | 49.6% | -36.5% | -0.42 |
| top5_long_bottom5_short | 252 | -19.0 | -38.0% | -2.088 | 42.1% | -41.4% | -2.09 |
| universe_equal_weight_long | 252 | -3.4 | -8.3% | -0.771 | 44.0% | -15.3% | -0.77 |
| spy_same_horizon | 252 | -4.1 | -9.9% | -0.961 | 49.6% | -14.3% | -0.96 |

## Reference: Qlib TopkDropout portfolio backtest (long only, close-to-close)

TopkDropout topk=30 n_drop=3, deal at close, 5+5 bps, benchmark SPY

- Annualized excess return vs SPY: +16.4%
- Information ratio: 0.663
- Max drawdown (excess): -20.6%

## Monthly decile long-short, net

| Month | Return |
|---|---|
| 2025-11 | -1.42% |
| 2025-12 | -2.15% |
| 2026-01 | -0.52% |
| 2026-02 | +1.39% |
| 2026-03 | +1.02% |
| 2026-04 | -2.03% |
| 2026-05 | -1.37% |
| 2026-06 | -1.13% |
| 2026-07 | -0.70% |
| 2026-08 | -0.36% |
| 2026-09 | -1.14% |
| 2026-10 | -0.67% |
| 2026-11 | -2.43% |

_Research output, not investment advice. Survivorship: the universe is current index membership._
