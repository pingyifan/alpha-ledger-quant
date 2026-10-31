# Out-of-sample report: model `oc` (next session open-to-close (the ledger's day-trade rule))

Validation year; the model never trained on these sessions. Window 2025-10-29 to 2026-10-29, 252 sessions. Target = next session open-to-close (the ledger's day-trade rule) return. Costs = 4 bps round trip, the same as the ledger's simulated fund.

## Signal quality

| Metric | Value |
|---|---|
| IC (mean daily Pearson) | 0.0033 |
| ICIR | 0.021 |
| Rank IC | 0.0027 |
| Rank ICIR | 0.020 |
| Days with IC > 0 | 46.4% |

For scale: Qlib's LightGBM/Alpha158 benchmark on CSI300 reports IC 0.045 and Rank IC 0.047 (next-day close-to-close).

## Name-day hit rates (compare with the ledger's hit rate)

| Basket | Hit rate |
|---|---|
| Top-5 longs, share with a positive horizon return | 49.6% |
| Bottom-5 shorts, share with a negative horizon return | 48.4% |
| Top decile longs | 49.6% |
| Bottom decile shorts | 49.7% |
| Base rate: all tradable names with a positive horizon return | 49.8% |

## Horizon-return simulations, net of costs (per $1 of gross exposure)

| Simulation | Days | Mean/day (bps) | Annualized | Sharpe | Hit days | Max DD | t |
|---|---|---|---|---|---|---|---|
| decile_long_short | 252 | -5.2 | -12.2% | -1.437 | 46.0% | -14.8% | -1.44 |
| decile_long_only | 252 | -1.6 | -3.9% | -0.19 | 46.0% | -21.8% | -0.19 |
| top5_long_only | 252 | +13.4 | +40.3% | 0.836 | 48.4% | -33.0% | 0.84 |
| top5_long_bottom5_short | 252 | -6.8 | -15.8% | -0.707 | 50.8% | -31.1% | -0.71 |
| universe_equal_weight_long | 252 | -2.3 | -5.7% | -0.554 | 43.6% | -15.0% | -0.55 |
| spy_same_horizon | 252 | -3.6 | -8.6% | -0.91 | 48.4% | -10.3% | -0.91 |

## Reference: Qlib TopkDropout portfolio backtest (long only, close-to-close)

TopkDropout topk=30 n_drop=3, deal at close, 5+5 bps, benchmark SPY

- Annualized excess return vs SPY: +34.0%
- Information ratio: 1.406
- Max drawdown (excess): -16.2%

## Monthly decile long-short, net

| Month | Return |
|---|---|
| 2025-10 | -0.36% |
| 2025-11 | -0.38% |
| 2025-12 | -2.40% |
| 2026-01 | +0.56% |
| 2026-02 | +0.22% |
| 2026-03 | +0.85% |
| 2026-04 | -1.97% |
| 2026-05 | -0.79% |
| 2026-06 | -2.69% |
| 2026-07 | -5.24% |
| 2026-08 | -0.93% |
| 2026-09 | -0.08% |
| 2026-10 | +0.05% |

_Research output, not investment advice. Survivorship: the universe is current index membership._
