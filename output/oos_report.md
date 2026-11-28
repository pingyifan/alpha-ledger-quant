# Out-of-sample report: model `oc` (next session open-to-close (the ledger's day-trade rule))

Validation year; the model never trained on these sessions. Window 2025-11-25 to 2026-11-25, 252 sessions. Target = next session open-to-close (the ledger's day-trade rule) return. Costs = 4 bps round trip, the same as the ledger's simulated fund.

## Signal quality

| Metric | Value |
|---|---|
| IC (mean daily Pearson) | -0.0023 |
| ICIR | -0.018 |
| Rank IC | -0.0027 |
| Rank ICIR | -0.020 |
| Days with IC > 0 | 46.8% |

For scale: Qlib's LightGBM/Alpha158 benchmark on CSI300 reports IC 0.045 and Rank IC 0.047 (next-day close-to-close).

## Name-day hit rates (compare with the ledger's hit rate)

| Basket | Hit rate |
|---|---|
| Top-5 longs, share with a positive horizon return | 48.1% |
| Bottom-5 shorts, share with a negative horizon return | 52.1% |
| Top decile longs | 49.9% |
| Bottom decile shorts | 49.8% |
| Base rate: all tradable names with a positive horizon return | 49.4% |

## Horizon-return simulations, net of costs (per $1 of gross exposure)

| Simulation | Days | Mean/day (bps) | Annualized | Sharpe | Hit days | Max DD | t |
|---|---|---|---|---|---|---|---|
| decile_long_short | 252 | -3.3 | -7.9% | -1.034 | 46.8% | -11.7% | -1.03 |
| decile_long_only | 252 | +0.5 | +1.2% | 0.062 | 47.6% | -21.5% | 0.06 |
| top5_long_only | 252 | -13.7 | -29.2% | -0.939 | 48.0% | -54.0% | -0.94 |
| top5_long_bottom5_short | 252 | -6.4 | -15.0% | -0.812 | 50.4% | -24.7% | -0.81 |
| universe_equal_weight_long | 252 | -4.5 | -10.7% | -0.994 | 43.6% | -19.3% | -0.99 |
| spy_same_horizon | 252 | -6.3 | -14.7% | -1.388 | 48.8% | -20.8% | -1.39 |

## Reference: Qlib TopkDropout portfolio backtest (long only, close-to-close)

TopkDropout topk=30 n_drop=3, deal at close, 5+5 bps, benchmark SPY

- Annualized excess return vs SPY: +17.6%
- Information ratio: 0.705
- Max drawdown (excess): -21.3%

## Monthly decile long-short, net

| Month | Return |
|---|---|
| 2025-11 | -0.02% |
| 2025-12 | -3.23% |
| 2026-01 | +2.47% |
| 2026-02 | +1.69% |
| 2026-03 | +0.27% |
| 2026-04 | -0.81% |
| 2026-05 | -1.23% |
| 2026-06 | -1.04% |
| 2026-07 | -0.25% |
| 2026-08 | -0.32% |
| 2026-09 | +0.07% |
| 2026-10 | -1.83% |
| 2026-11 | -4.13% |

_Research output, not investment advice. Survivorship: the universe is current index membership._
