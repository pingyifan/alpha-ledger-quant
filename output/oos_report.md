# Out-of-sample report: model `oc` (next session open-to-close (the ledger's day-trade rule))

Validation year; the model never trained on these sessions. Window 2025-11-24 to 2026-11-24, 252 sessions. Target = next session open-to-close (the ledger's day-trade rule) return. Costs = 4 bps round trip, the same as the ledger's simulated fund.

## Signal quality

| Metric | Value |
|---|---|
| IC (mean daily Pearson) | -0.0046 |
| ICIR | -0.035 |
| Rank IC | -0.0016 |
| Rank ICIR | -0.012 |
| Days with IC > 0 | 48.0% |

For scale: Qlib's LightGBM/Alpha158 benchmark on CSI300 reports IC 0.045 and Rank IC 0.047 (next-day close-to-close).

## Name-day hit rates (compare with the ledger's hit rate)

| Basket | Hit rate |
|---|---|
| Top-5 longs, share with a positive horizon return | 48.1% |
| Bottom-5 shorts, share with a negative horizon return | 52.4% |
| Top decile longs | 49.4% |
| Bottom decile shorts | 49.9% |
| Base rate: all tradable names with a positive horizon return | 49.5% |

## Horizon-return simulations, net of costs (per $1 of gross exposure)

| Simulation | Days | Mean/day (bps) | Annualized | Sharpe | Hit days | Max DD | t |
|---|---|---|---|---|---|---|---|
| decile_long_short | 252 | -5.0 | -11.7% | -1.557 | 46.8% | -14.1% | -1.56 |
| decile_long_only | 252 | -3.6 | -8.6% | -0.471 | 48.0% | -26.4% | -0.47 |
| top5_long_only | 252 | -4.7 | -11.2% | -0.302 | 49.2% | -52.6% | -0.3 |
| top5_long_bottom5_short | 252 | +0.2 | +0.5% | 0.027 | 53.6% | -19.1% | 0.03 |
| universe_equal_weight_long | 252 | -4.1 | -9.8% | -0.894 | 43.6% | -19.3% | -0.89 |
| spy_same_horizon | 252 | -6.0 | -14.1% | -1.33 | 48.8% | -20.8% | -1.33 |

## Reference: Qlib TopkDropout portfolio backtest (long only, close-to-close)

TopkDropout topk=30 n_drop=3, deal at close, 5+5 bps, benchmark SPY

- Annualized excess return vs SPY: +22.6%
- Information ratio: 0.893
- Max drawdown (excess): -15.8%

## Monthly decile long-short, net

| Month | Return |
|---|---|
| 2025-11 | +0.08% |
| 2025-12 | -3.39% |
| 2026-01 | +1.59% |
| 2026-02 | +1.01% |
| 2026-03 | +1.10% |
| 2026-04 | -0.71% |
| 2026-05 | -1.71% |
| 2026-06 | -0.80% |
| 2026-07 | -1.61% |
| 2026-08 | -0.10% |
| 2026-09 | -0.63% |
| 2026-10 | -2.55% |
| 2026-11 | -4.80% |

_Research output, not investment advice. Survivorship: the universe is current index membership._
