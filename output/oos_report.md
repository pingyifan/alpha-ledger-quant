# Out-of-sample report: model `oc` (next session open-to-close (the ledger's day-trade rule))

Validation year; the model never trained on these sessions. Window 2025-10-30 to 2026-10-30, 252 sessions. Target = next session open-to-close (the ledger's day-trade rule) return. Costs = 4 bps round trip, the same as the ledger's simulated fund.

## Signal quality

| Metric | Value |
|---|---|
| IC (mean daily Pearson) | 0.0004 |
| ICIR | 0.003 |
| Rank IC | -0.0014 |
| Rank ICIR | -0.011 |
| Days with IC > 0 | 48.0% |

For scale: Qlib's LightGBM/Alpha158 benchmark on CSI300 reports IC 0.045 and Rank IC 0.047 (next-day close-to-close).

## Name-day hit rates (compare with the ledger's hit rate)

| Basket | Hit rate |
|---|---|
| Top-5 longs, share with a positive horizon return | 49.7% |
| Bottom-5 shorts, share with a negative horizon return | 47.2% |
| Top decile longs | 49.5% |
| Bottom decile shorts | 49.5% |
| Base rate: all tradable names with a positive horizon return | 49.8% |

## Horizon-return simulations, net of costs (per $1 of gross exposure)

| Simulation | Days | Mean/day (bps) | Annualized | Sharpe | Hit days | Max DD | t |
|---|---|---|---|---|---|---|---|
| decile_long_short | 252 | -6.4 | -14.9% | -1.796 | 45.6% | -16.3% | -1.8 |
| decile_long_only | 252 | -2.9 | -7.0% | -0.349 | 48.4% | -22.6% | -0.35 |
| top5_long_only | 252 | +12.4 | +36.5% | 0.747 | 51.2% | -30.9% | 0.75 |
| top5_long_bottom5_short | 252 | -10.4 | -23.0% | -1.107 | 51.2% | -31.2% | -1.11 |
| universe_equal_weight_long | 252 | -2.2 | -5.3% | -0.516 | 44.0% | -15.0% | -0.52 |
| spy_same_horizon | 252 | -3.7 | -9.0% | -0.945 | 48.4% | -11.1% | -0.94 |

## Reference: Qlib TopkDropout portfolio backtest (long only, close-to-close)

TopkDropout topk=30 n_drop=3, deal at close, 5+5 bps, benchmark SPY

- Annualized excess return vs SPY: +33.5%
- Information ratio: 1.386
- Max drawdown (excess): -15.0%

## Monthly decile long-short, net

| Month | Return |
|---|---|
| 2025-10 | -0.07% |
| 2025-11 | +0.18% |
| 2025-12 | -2.94% |
| 2026-01 | +0.56% |
| 2026-02 | +0.07% |
| 2026-03 | +0.04% |
| 2026-04 | -1.88% |
| 2026-05 | -0.29% |
| 2026-06 | -2.01% |
| 2026-07 | -4.65% |
| 2026-08 | -1.23% |
| 2026-09 | -1.09% |
| 2026-10 | -3.04% |

_Research output, not investment advice. Survivorship: the universe is current index membership._
