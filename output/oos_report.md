# Out-of-sample report: model `oc` (next session open-to-close (the ledger's day-trade rule))

Validation year; the model never trained on these sessions. Window 2025-10-20 to 2026-10-20, 252 sessions. Target = next session open-to-close (the ledger's day-trade rule) return. Costs = 4 bps round trip, the same as the ledger's simulated fund.

## Signal quality

| Metric | Value |
|---|---|
| IC (mean daily Pearson) | 0.0023 |
| ICIR | 0.015 |
| Rank IC | 0.0008 |
| Rank ICIR | 0.006 |
| Days with IC > 0 | 48.0% |

For scale: Qlib's LightGBM/Alpha158 benchmark on CSI300 reports IC 0.045 and Rank IC 0.047 (next-day close-to-close).

## Name-day hit rates (compare with the ledger's hit rate)

| Basket | Hit rate |
|---|---|
| Top-5 longs, share with a positive horizon return | 48.8% |
| Bottom-5 shorts, share with a negative horizon return | 48.4% |
| Top decile longs | 49.2% |
| Bottom decile shorts | 49.7% |
| Base rate: all tradable names with a positive horizon return | 49.4% |

## Horizon-return simulations, net of costs (per $1 of gross exposure)

| Simulation | Days | Mean/day (bps) | Annualized | Sharpe | Hit days | Max DD | t |
|---|---|---|---|---|---|---|---|
| decile_long_short | 252 | -5.5 | -12.9% | -1.535 | 44.8% | -15.2% | -1.54 |
| decile_long_only | 252 | -2.9 | -7.0% | -0.352 | 44.8% | -21.6% | -0.35 |
| top5_long_only | 252 | +9.7 | +27.7% | 0.6 | 48.8% | -35.4% | 0.6 |
| top5_long_bottom5_short | 252 | -9.5 | -21.3% | -1.01 | 46.4% | -34.1% | -1.01 |
| universe_equal_weight_long | 252 | -3.7 | -9.0% | -0.884 | 42.9% | -15.0% | -0.88 |
| spy_same_horizon | 252 | -3.5 | -8.3% | -0.876 | 48.0% | -10.3% | -0.88 |

## Reference: Qlib TopkDropout portfolio backtest (long only, close-to-close)

TopkDropout topk=30 n_drop=3, deal at close, 5+5 bps, benchmark SPY

- Annualized excess return vs SPY: +31.5%
- Information ratio: 1.429
- Max drawdown (excess): -15.0%

## Monthly decile long-short, net

| Month | Return |
|---|---|
| 2025-10 | +0.42% |
| 2025-11 | -0.53% |
| 2025-12 | -2.76% |
| 2026-01 | +0.49% |
| 2026-02 | +0.24% |
| 2026-03 | +0.68% |
| 2026-04 | -2.15% |
| 2026-05 | -0.63% |
| 2026-06 | -2.70% |
| 2026-07 | -4.87% |
| 2026-08 | -1.20% |
| 2026-09 | +0.46% |
| 2026-10 | -1.37% |

_Research output, not investment advice. Survivorship: the universe is current index membership._
