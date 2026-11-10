# Out-of-sample report: model `oc` (next session open-to-close (the ledger's day-trade rule))

Validation year; the model never trained on these sessions. Window 2025-11-06 to 2026-11-06, 252 sessions. Target = next session open-to-close (the ledger's day-trade rule) return. Costs = 4 bps round trip, the same as the ledger's simulated fund.

## Signal quality

| Metric | Value |
|---|---|
| IC (mean daily Pearson) | -0.0027 |
| ICIR | -0.017 |
| Rank IC | -0.0021 |
| Rank ICIR | -0.016 |
| Days with IC > 0 | 48.8% |

For scale: Qlib's LightGBM/Alpha158 benchmark on CSI300 reports IC 0.045 and Rank IC 0.047 (next-day close-to-close).

## Name-day hit rates (compare with the ledger's hit rate)

| Basket | Hit rate |
|---|---|
| Top-5 longs, share with a positive horizon return | 48.9% |
| Bottom-5 shorts, share with a negative horizon return | 47.9% |
| Top decile longs | 49.3% |
| Bottom decile shorts | 49.0% |
| Base rate: all tradable names with a positive horizon return | 49.8% |

## Horizon-return simulations, net of costs (per $1 of gross exposure)

| Simulation | Days | Mean/day (bps) | Annualized | Sharpe | Hit days | Max DD | t |
|---|---|---|---|---|---|---|---|
| decile_long_short | 252 | -7.7 | -17.7% | -2.177 | 44.8% | -18.9% | -2.18 |
| decile_long_only | 252 | -4.4 | -10.5% | -0.511 | 46.4% | -26.8% | -0.51 |
| top5_long_only | 252 | +0.2 | +0.5% | 0.011 | 49.2% | -44.4% | 0.01 |
| top5_long_bottom5_short | 252 | -12.1 | -26.3% | -1.275 | 48.0% | -30.7% | -1.28 |
| universe_equal_weight_long | 252 | -2.8 | -6.8% | -0.627 | 44.0% | -15.3% | -0.63 |
| spy_same_horizon | 252 | -4.0 | -9.5% | -0.918 | 49.6% | -14.3% | -0.92 |

## Reference: Qlib TopkDropout portfolio backtest (long only, close-to-close)

TopkDropout topk=30 n_drop=3, deal at close, 5+5 bps, benchmark SPY

- Annualized excess return vs SPY: +13.5%
- Information ratio: 0.484
- Max drawdown (excess): -23.6%

## Monthly decile long-short, net

| Month | Return |
|---|---|
| 2025-11 | -1.34% |
| 2025-12 | -3.58% |
| 2026-01 | +0.06% |
| 2026-02 | +0.39% |
| 2026-03 | +0.01% |
| 2026-04 | -0.11% |
| 2026-05 | -0.28% |
| 2026-06 | -2.27% |
| 2026-07 | -5.55% |
| 2026-08 | -1.87% |
| 2026-09 | -1.10% |
| 2026-10 | -1.54% |
| 2026-11 | -2.32% |

_Research output, not investment advice. Survivorship: the universe is current index membership._
