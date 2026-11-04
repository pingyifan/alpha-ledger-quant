# Out-of-sample report: model `oc` (next session open-to-close (the ledger's day-trade rule))

Validation year; the model never trained on these sessions. Window 2025-10-31 to 2026-11-02, 252 sessions. Target = next session open-to-close (the ledger's day-trade rule) return. Costs = 4 bps round trip, the same as the ledger's simulated fund.

## Signal quality

| Metric | Value |
|---|---|
| IC (mean daily Pearson) | 0.0021 |
| ICIR | 0.014 |
| Rank IC | 0.0015 |
| Rank ICIR | 0.013 |
| Days with IC > 0 | 48.8% |

For scale: Qlib's LightGBM/Alpha158 benchmark on CSI300 reports IC 0.045 and Rank IC 0.047 (next-day close-to-close).

## Name-day hit rates (compare with the ledger's hit rate)

| Basket | Hit rate |
|---|---|
| Top-5 longs, share with a positive horizon return | 48.3% |
| Bottom-5 shorts, share with a negative horizon return | 47.2% |
| Top decile longs | 49.6% |
| Bottom decile shorts | 49.9% |
| Base rate: all tradable names with a positive horizon return | 49.8% |

## Horizon-return simulations, net of costs (per $1 of gross exposure)

| Simulation | Days | Mean/day (bps) | Annualized | Sharpe | Hit days | Max DD | t |
|---|---|---|---|---|---|---|---|
| decile_long_short | 252 | -4.8 | -11.3% | -1.444 | 42.9% | -13.9% | -1.44 |
| decile_long_only | 252 | -0.9 | -2.4% | -0.119 | 48.4% | -18.7% | -0.12 |
| top5_long_only | 252 | -10.4 | -23.2% | -0.623 | 48.0% | -53.9% | -0.62 |
| top5_long_bottom5_short | 252 | -20.9 | -40.9% | -2.137 | 43.2% | -44.8% | -2.14 |
| universe_equal_weight_long | 252 | -2.4 | -5.9% | -0.565 | 43.2% | -15.1% | -0.56 |
| spy_same_horizon | 252 | -3.5 | -8.4% | -0.88 | 48.8% | -11.1% | -0.88 |

## Reference: Qlib TopkDropout portfolio backtest (long only, close-to-close)

TopkDropout topk=30 n_drop=3, deal at close, 5+5 bps, benchmark SPY

- Annualized excess return vs SPY: +32.1%
- Information ratio: 1.606
- Max drawdown (excess): -15.4%

## Monthly decile long-short, net

| Month | Return |
|---|---|
| 2025-10 | -0.00% |
| 2025-11 | -0.44% |
| 2025-12 | -3.49% |
| 2026-01 | +0.05% |
| 2026-02 | +0.77% |
| 2026-03 | +0.84% |
| 2026-04 | -2.49% |
| 2026-05 | -0.82% |
| 2026-06 | -1.66% |
| 2026-07 | -3.74% |
| 2026-08 | -0.57% |
| 2026-09 | +0.37% |
| 2026-10 | -1.57% |
| 2026-11 | +0.56% |

_Research output, not investment advice. Survivorship: the universe is current index membership._
