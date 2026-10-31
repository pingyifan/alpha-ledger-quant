# Out-of-sample report: model `cc` (next session close to the following session's close (Qlib's native one-session hold, includes the overnight))

Validation year; the model never trained on these sessions. Window 2025-10-28 to 2026-10-28, 252 sessions. Target = next session close to the following session's close (Qlib's native one-session hold, includes the overnight) return. Costs = 4 bps round trip, the same as the ledger's simulated fund.

## Signal quality

| Metric | Value |
|---|---|
| IC (mean daily Pearson) | 0.0186 |
| ICIR | 0.087 |
| Rank IC | 0.0153 |
| Rank ICIR | 0.084 |
| Days with IC > 0 | 59.1% |

For scale: Qlib's LightGBM/Alpha158 benchmark on CSI300 reports IC 0.045 and Rank IC 0.047 (next-day close-to-close).

## Name-day hit rates (compare with the ledger's hit rate)

| Basket | Hit rate |
|---|---|
| Top-5 longs, share with a positive horizon return | 52.2% |
| Bottom-5 shorts, share with a negative horizon return | 47.5% |
| Top decile longs | 50.8% |
| Bottom decile shorts | 49.0% |
| Base rate: all tradable names with a positive horizon return | 50.9% |

## Horizon-return simulations, net of costs (per $1 of gross exposure)

| Simulation | Days | Mean/day (bps) | Annualized | Sharpe | Hit days | Max DD | t |
|---|---|---|---|---|---|---|---|
| decile_long_short | 252 | -0.6 | -1.5% | -0.097 | 54.0% | -11.2% | -0.1 |
| decile_long_only | 252 | +8.3 | +23.2% | 0.685 | 55.2% | -17.9% | 0.69 |
| top5_long_only | 252 | +42.8 | +193.6% | 1.838 | 55.2% | -21.8% | 1.84 |
| top5_long_bottom5_short | 252 | +11.0 | +32.0% | 0.918 | 52.8% | -12.9% | 0.92 |
| universe_equal_weight_long | 252 | +3.5 | +9.2% | 0.697 | 51.6% | -9.1% | 0.7 |
| spy_same_horizon | 252 | +0.5 | +1.3% | 0.101 | 50.8% | -10.8% | 0.1 |

## Reference: Qlib TopkDropout portfolio backtest (long only, close-to-close)

TopkDropout topk=30 n_drop=3, deal at close, 5+5 bps, benchmark SPY

- Annualized excess return vs SPY: +38.3%
- Information ratio: 1.228
- Max drawdown (excess): -20.8%

## Monthly decile long-short, net

| Month | Return |
|---|---|
| 2025-10 | -1.35% |
| 2025-11 | -1.40% |
| 2025-12 | +1.46% |
| 2026-01 | -0.57% |
| 2026-02 | -1.49% |
| 2026-03 | +0.41% |
| 2026-04 | +3.24% |
| 2026-05 | +5.46% |
| 2026-06 | -4.28% |
| 2026-07 | +1.88% |
| 2026-08 | -1.98% |
| 2026-09 | +2.48% |
| 2026-10 | -5.93% |

_Research output, not investment advice. Survivorship: the universe is current index membership._
