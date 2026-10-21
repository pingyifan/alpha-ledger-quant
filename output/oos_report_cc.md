# Out-of-sample report: model `cc` (next session close to the following session's close (Qlib's native one-session hold, includes the overnight))

Validation year; the model never trained on these sessions. Window 2025-10-16 to 2026-10-16, 252 sessions. Target = next session close to the following session's close (Qlib's native one-session hold, includes the overnight) return. Costs = 4 bps round trip, the same as the ledger's simulated fund.

## Signal quality

| Metric | Value |
|---|---|
| IC (mean daily Pearson) | 0.0194 |
| ICIR | 0.095 |
| Rank IC | 0.0170 |
| Rank ICIR | 0.097 |
| Days with IC > 0 | 57.5% |

For scale: Qlib's LightGBM/Alpha158 benchmark on CSI300 reports IC 0.045 and Rank IC 0.047 (next-day close-to-close).

## Name-day hit rates (compare with the ledger's hit rate)

| Basket | Hit rate |
|---|---|
| Top-5 longs, share with a positive horizon return | 51.6% |
| Bottom-5 shorts, share with a negative horizon return | 47.9% |
| Top decile longs | 50.7% |
| Bottom decile shorts | 49.5% |
| Base rate: all tradable names with a positive horizon return | 50.8% |

## Horizon-return simulations, net of costs (per $1 of gross exposure)

| Simulation | Days | Mean/day (bps) | Annualized | Sharpe | Hit days | Max DD | t |
|---|---|---|---|---|---|---|---|
| decile_long_short | 252 | +1.1 | +2.7% | 0.192 | 52.8% | -11.0% | 0.19 |
| decile_long_only | 252 | +10.9 | +31.6% | 0.94 | 55.2% | -16.5% | 0.94 |
| top5_long_only | 252 | +36.9 | +153.1% | 1.636 | 53.6% | -19.6% | 1.64 |
| top5_long_bottom5_short | 252 | +8.2 | +23.0% | 0.707 | 49.6% | -12.0% | 0.71 |
| universe_equal_weight_long | 252 | +3.3 | +8.6% | 0.647 | 51.6% | -9.1% | 0.65 |
| spy_same_horizon | 252 | +2.5 | +6.6% | 0.506 | 51.6% | -11.3% | 0.51 |

## Reference: Qlib TopkDropout portfolio backtest (long only, close-to-close)

TopkDropout topk=30 n_drop=3, deal at close, 5+5 bps, benchmark SPY

- Annualized excess return vs SPY: +35.5%
- Information ratio: 1.169
- Max drawdown (excess): -24.5%

## Monthly decile long-short, net

| Month | Return |
|---|---|
| 2025-10 | +1.38% |
| 2025-11 | -1.15% |
| 2025-12 | +1.79% |
| 2026-01 | -0.73% |
| 2026-02 | -1.52% |
| 2026-03 | +0.58% |
| 2026-04 | +3.28% |
| 2026-05 | +4.25% |
| 2026-06 | -3.98% |
| 2026-07 | +1.64% |
| 2026-08 | -1.58% |
| 2026-09 | +2.49% |
| 2026-10 | -4.29% |

_Research output, not investment advice. Survivorship: the universe is current index membership._
