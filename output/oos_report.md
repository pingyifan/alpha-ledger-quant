# Out-of-sample report: model `oc` (next session open-to-close (the ledger's day-trade rule))

Validation year; the model never trained on these sessions. Window 2025-11-12 to 2026-11-12, 252 sessions. Target = next session open-to-close (the ledger's day-trade rule) return. Costs = 4 bps round trip, the same as the ledger's simulated fund.

## Signal quality

| Metric | Value |
|---|---|
| IC (mean daily Pearson) | 0.0023 |
| ICIR | 0.016 |
| Rank IC | 0.0042 |
| Rank ICIR | 0.035 |
| Days with IC > 0 | 50.8% |

For scale: Qlib's LightGBM/Alpha158 benchmark on CSI300 reports IC 0.045 and Rank IC 0.047 (next-day close-to-close).

## Name-day hit rates (compare with the ledger's hit rate)

| Basket | Hit rate |
|---|---|
| Top-5 longs, share with a positive horizon return | 49.9% |
| Bottom-5 shorts, share with a negative horizon return | 46.8% |
| Top decile longs | 49.5% |
| Bottom decile shorts | 49.5% |
| Base rate: all tradable names with a positive horizon return | 49.5% |

## Horizon-return simulations, net of costs (per $1 of gross exposure)

| Simulation | Days | Mean/day (bps) | Annualized | Sharpe | Hit days | Max DD | t |
|---|---|---|---|---|---|---|---|
| decile_long_short | 252 | -5.6 | -13.1% | -1.609 | 47.2% | -14.3% | -1.61 |
| decile_long_only | 252 | -3.1 | -7.6% | -0.379 | 47.2% | -26.8% | -0.38 |
| top5_long_only | 252 | -3.0 | -7.2% | -0.177 | 50.8% | -41.3% | -0.18 |
| top5_long_bottom5_short | 252 | -15.0 | -31.5% | -1.565 | 46.8% | -38.0% | -1.56 |
| universe_equal_weight_long | 252 | -3.6 | -8.7% | -0.813 | 43.6% | -15.3% | -0.81 |
| spy_same_horizon | 252 | -4.4 | -10.4% | -1.009 | 49.6% | -14.3% | -1.01 |

## Reference: Qlib TopkDropout portfolio backtest (long only, close-to-close)

TopkDropout topk=30 n_drop=3, deal at close, 5+5 bps, benchmark SPY

- Annualized excess return vs SPY: +30.6%
- Information ratio: 1.395
- Max drawdown (excess): -11.4%

## Monthly decile long-short, net

| Month | Return |
|---|---|
| 2025-11 | -0.33% |
| 2025-12 | -2.30% |
| 2026-01 | -0.02% |
| 2026-02 | +1.21% |
| 2026-03 | +1.13% |
| 2026-04 | -2.52% |
| 2026-05 | +1.06% |
| 2026-06 | -0.09% |
| 2026-07 | -3.10% |
| 2026-08 | -4.69% |
| 2026-09 | -0.76% |
| 2026-10 | -0.87% |
| 2026-11 | -2.88% |

_Research output, not investment advice. Survivorship: the universe is current index membership._
