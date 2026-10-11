# Out-of-sample report: model `oc` (next session open-to-close (the ledger's day-trade rule))

Validation year; the model never trained on these sessions. Window 2025-10-08 to 2026-10-08, 252 sessions. Target = next session open-to-close (the ledger's day-trade rule) return. Costs = 4 bps round trip, the same as the ledger's simulated fund.

## Signal quality

| Metric | Value |
|---|---|
| IC (mean daily Pearson) | 0.0031 |
| ICIR | 0.021 |
| Rank IC | 0.0001 |
| Rank ICIR | 0.001 |
| Days with IC > 0 | 49.6% |

For scale: Qlib's LightGBM/Alpha158 benchmark on CSI300 reports IC 0.045 and Rank IC 0.047 (next-day close-to-close).

## Name-day hit rates (compare with the ledger's hit rate)

| Basket | Hit rate |
|---|---|
| Top-5 longs, share with a positive horizon return | 47.5% |
| Bottom-5 shorts, share with a negative horizon return | 47.7% |
| Top decile longs | 48.9% |
| Bottom decile shorts | 49.8% |
| Base rate: all tradable names with a positive horizon return | 49.3% |

## Horizon-return simulations, net of costs (per $1 of gross exposure)

| Simulation | Days | Mean/day (bps) | Annualized | Sharpe | Hit days | Max DD | t |
|---|---|---|---|---|---|---|---|
| decile_long_short | 252 | -5.5 | -13.0% | -1.58 | 41.7% | -15.3% | -1.58 |
| decile_long_only | 252 | -4.3 | -10.2% | -0.521 | 44.4% | -20.5% | -0.52 |
| top5_long_only | 252 | +1.3 | +3.4% | 0.083 | 48.4% | -30.9% | 0.08 |
| top5_long_bottom5_short | 252 | -12.5 | -27.0% | -1.305 | 48.8% | -37.0% | -1.3 |
| universe_equal_weight_long | 252 | -4.8 | -11.3% | -1.066 | 43.6% | -15.0% | -1.07 |
| spy_same_horizon | 252 | -3.9 | -9.4% | -0.96 | 48.0% | -11.5% | -0.96 |

## Reference: Qlib TopkDropout portfolio backtest (long only, close-to-close)

TopkDropout topk=30 n_drop=3, deal at close, 5+5 bps, benchmark SPY

- Annualized excess return vs SPY: +37.0%
- Information ratio: 1.662
- Max drawdown (excess): -14.7%

## Monthly decile long-short, net

| Month | Return |
|---|---|
| 2025-10 | -0.01% |
| 2025-11 | +0.14% |
| 2025-12 | -3.83% |
| 2026-01 | -0.20% |
| 2026-02 | +1.09% |
| 2026-03 | -0.18% |
| 2026-04 | -1.54% |
| 2026-05 | -1.36% |
| 2026-06 | -2.04% |
| 2026-07 | -4.45% |
| 2026-08 | -1.09% |
| 2026-09 | -0.66% |
| 2026-10 | +0.08% |

_Research output, not investment advice. Survivorship: the universe is current index membership._
