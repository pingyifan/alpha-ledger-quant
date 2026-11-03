# Out-of-sample report: model `cc` (next session close to the following session's close (Qlib's native one-session hold, includes the overnight))

Validation year; the model never trained on these sessions. Window 2025-10-29 to 2026-10-29, 252 sessions. Target = next session close to the following session's close (Qlib's native one-session hold, includes the overnight) return. Costs = 4 bps round trip, the same as the ledger's simulated fund.

## Signal quality

| Metric | Value |
|---|---|
| IC (mean daily Pearson) | 0.0184 |
| ICIR | 0.086 |
| Rank IC | 0.0151 |
| Rank ICIR | 0.082 |
| Days with IC > 0 | 58.3% |

For scale: Qlib's LightGBM/Alpha158 benchmark on CSI300 reports IC 0.045 and Rank IC 0.047 (next-day close-to-close).

## Name-day hit rates (compare with the ledger's hit rate)

| Basket | Hit rate |
|---|---|
| Top-5 longs, share with a positive horizon return | 52.7% |
| Bottom-5 shorts, share with a negative horizon return | 47.9% |
| Top decile longs | 51.0% |
| Bottom decile shorts | 49.0% |
| Base rate: all tradable names with a positive horizon return | 51.0% |

## Horizon-return simulations, net of costs (per $1 of gross exposure)

| Simulation | Days | Mean/day (bps) | Annualized | Sharpe | Hit days | Max DD | t |
|---|---|---|---|---|---|---|---|
| decile_long_short | 252 | -0.1 | -0.3% | -0.022 | 54.4% | -11.1% | -0.02 |
| decile_long_only | 252 | +10.4 | +30.1% | 0.87 | 55.2% | -15.8% | 0.87 |
| top5_long_only | 252 | +31.1 | +118.9% | 1.379 | 56.0% | -21.7% | 1.38 |
| top5_long_bottom5_short | 252 | +4.3 | +11.6% | 0.377 | 53.2% | -15.2% | 0.38 |
| universe_equal_weight_long | 252 | +4.1 | +10.9% | 0.821 | 52.0% | -9.1% | 0.82 |
| spy_same_horizon | 252 | +0.8 | +1.9% | 0.15 | 50.8% | -10.8% | 0.15 |

## Reference: Qlib TopkDropout portfolio backtest (long only, close-to-close)

TopkDropout topk=30 n_drop=3, deal at close, 5+5 bps, benchmark SPY

- Annualized excess return vs SPY: +35.4%
- Information ratio: 1.185
- Max drawdown (excess): -21.9%

## Monthly decile long-short, net

| Month | Return |
|---|---|
| 2025-10 | -0.51% |
| 2025-11 | -1.45% |
| 2025-12 | +1.05% |
| 2026-01 | -0.34% |
| 2026-02 | -1.24% |
| 2026-03 | +0.94% |
| 2026-04 | +3.87% |
| 2026-05 | +5.05% |
| 2026-06 | -4.32% |
| 2026-07 | +2.13% |
| 2026-08 | -1.14% |
| 2026-09 | +2.62% |
| 2026-10 | -7.45% |

_Research output, not investment advice. Survivorship: the universe is current index membership._
