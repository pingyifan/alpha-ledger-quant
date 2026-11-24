# Out-of-sample report: model `cc` (next session close to the following session's close (Qlib's native one-session hold, includes the overnight))

Validation year; the model never trained on these sessions. Window 2025-11-19 to 2026-11-19, 252 sessions. Target = next session close to the following session's close (Qlib's native one-session hold, includes the overnight) return. Costs = 4 bps round trip, the same as the ledger's simulated fund.

## Signal quality

| Metric | Value |
|---|---|
| IC (mean daily Pearson) | 0.0227 |
| ICIR | 0.105 |
| Rank IC | 0.0197 |
| Rank ICIR | 0.104 |
| Days with IC > 0 | 58.7% |

For scale: Qlib's LightGBM/Alpha158 benchmark on CSI300 reports IC 0.045 and Rank IC 0.047 (next-day close-to-close).

## Name-day hit rates (compare with the ledger's hit rate)

| Basket | Hit rate |
|---|---|
| Top-5 longs, share with a positive horizon return | 52.6% |
| Bottom-5 shorts, share with a negative horizon return | 48.7% |
| Top decile longs | 51.1% |
| Bottom decile shorts | 49.5% |
| Base rate: all tradable names with a positive horizon return | 50.8% |

## Horizon-return simulations, net of costs (per $1 of gross exposure)

| Simulation | Days | Mean/day (bps) | Annualized | Sharpe | Hit days | Max DD | t |
|---|---|---|---|---|---|---|---|
| decile_long_short | 252 | +0.5 | +1.3% | 0.079 | 53.6% | -16.7% | 0.08 |
| decile_long_only | 252 | +9.5 | +27.0% | 0.71 | 54.8% | -28.7% | 0.71 |
| top5_long_only | 252 | +38.1 | +160.5% | 1.553 | 54.8% | -29.8% | 1.55 |
| top5_long_bottom5_short | 252 | +8.6 | +24.2% | 0.678 | 50.4% | -16.8% | 0.68 |
| universe_equal_weight_long | 252 | +4.1 | +10.9% | 0.735 | 52.0% | -10.7% | 0.74 |
| spy_same_horizon | 252 | +0.9 | +2.3% | 0.152 | 50.0% | -13.6% | 0.15 |

## Reference: Qlib TopkDropout portfolio backtest (long only, close-to-close)

TopkDropout topk=30 n_drop=3, deal at close, 5+5 bps, benchmark SPY

- Annualized excess return vs SPY: +36.2%
- Information ratio: 1.155
- Max drawdown (excess): -27.6%

## Monthly decile long-short, net

| Month | Return |
|---|---|
| 2025-11 | +3.48% |
| 2025-12 | +1.55% |
| 2026-01 | -0.31% |
| 2026-02 | -1.13% |
| 2026-03 | +0.92% |
| 2026-04 | +4.07% |
| 2026-05 | +4.55% |
| 2026-06 | -5.69% |
| 2026-07 | +0.77% |
| 2026-08 | -1.87% |
| 2026-09 | +2.11% |
| 2026-10 | -5.45% |
| 2026-11 | -2.41% |

_Research output, not investment advice. Survivorship: the universe is current index membership._
