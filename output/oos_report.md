# Out-of-sample report: model `oc` (next session open-to-close (the ledger's day-trade rule))

Validation year; the model never trained on these sessions. Window 2025-10-22 to 2026-10-22, 252 sessions. Target = next session open-to-close (the ledger's day-trade rule) return. Costs = 4 bps round trip, the same as the ledger's simulated fund.

## Signal quality

| Metric | Value |
|---|---|
| IC (mean daily Pearson) | 0.0027 |
| ICIR | 0.018 |
| Rank IC | 0.0019 |
| Rank ICIR | 0.015 |
| Days with IC > 0 | 47.6% |

For scale: Qlib's LightGBM/Alpha158 benchmark on CSI300 reports IC 0.045 and Rank IC 0.047 (next-day close-to-close).

## Name-day hit rates (compare with the ledger's hit rate)

| Basket | Hit rate |
|---|---|
| Top-5 longs, share with a positive horizon return | 48.6% |
| Bottom-5 shorts, share with a negative horizon return | 48.9% |
| Top decile longs | 49.4% |
| Bottom decile shorts | 50.0% |
| Base rate: all tradable names with a positive horizon return | 49.5% |

## Horizon-return simulations, net of costs (per $1 of gross exposure)

| Simulation | Days | Mean/day (bps) | Annualized | Sharpe | Hit days | Max DD | t |
|---|---|---|---|---|---|---|---|
| decile_long_short | 252 | -3.6 | -8.7% | -1.043 | 45.6% | -11.4% | -1.04 |
| decile_long_only | 252 | -0.7 | -1.7% | -0.082 | 44.8% | -21.2% | -0.08 |
| top5_long_only | 252 | +7.8 | +21.8% | 0.477 | 48.0% | -38.0% | 0.48 |
| top5_long_bottom5_short | 252 | -8.7 | -19.7% | -0.913 | 48.0% | -31.5% | -0.91 |
| universe_equal_weight_long | 252 | -3.3 | -7.9% | -0.768 | 42.9% | -15.0% | -0.77 |
| spy_same_horizon | 252 | -3.3 | -8.0% | -0.843 | 48.0% | -10.3% | -0.84 |

## Reference: Qlib TopkDropout portfolio backtest (long only, close-to-close)

TopkDropout topk=30 n_drop=3, deal at close, 5+5 bps, benchmark SPY

- Annualized excess return vs SPY: +27.7%
- Information ratio: 1.227
- Max drawdown (excess): -12.4%

## Monthly decile long-short, net

| Month | Return |
|---|---|
| 2025-10 | +0.25% |
| 2025-11 | +0.29% |
| 2025-12 | -2.49% |
| 2026-01 | +1.11% |
| 2026-02 | +0.51% |
| 2026-03 | +1.76% |
| 2026-04 | -2.35% |
| 2026-05 | -0.09% |
| 2026-06 | -1.54% |
| 2026-07 | -4.53% |
| 2026-08 | -1.74% |
| 2026-09 | -0.02% |
| 2026-10 | -0.44% |

_Research output, not investment advice. Survivorship: the universe is current index membership._
