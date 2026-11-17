# Out-of-sample report: model `cc` (next session close to the following session's close (Qlib's native one-session hold, includes the overnight))

Validation year; the model never trained on these sessions. Window 2025-11-12 to 2026-11-12, 252 sessions. Target = next session close to the following session's close (Qlib's native one-session hold, includes the overnight) return. Costs = 4 bps round trip, the same as the ledger's simulated fund.

## Signal quality

| Metric | Value |
|---|---|
| IC (mean daily Pearson) | 0.0207 |
| ICIR | 0.096 |
| Rank IC | 0.0188 |
| Rank ICIR | 0.101 |
| Days with IC > 0 | 57.9% |

For scale: Qlib's LightGBM/Alpha158 benchmark on CSI300 reports IC 0.045 and Rank IC 0.047 (next-day close-to-close).

## Name-day hit rates (compare with the ledger's hit rate)

| Basket | Hit rate |
|---|---|
| Top-5 longs, share with a positive horizon return | 52.3% |
| Bottom-5 shorts, share with a negative horizon return | 50.6% |
| Top decile longs | 51.0% |
| Bottom decile shorts | 49.1% |
| Base rate: all tradable names with a positive horizon return | 50.8% |

## Horizon-return simulations, net of costs (per $1 of gross exposure)

| Simulation | Days | Mean/day (bps) | Annualized | Sharpe | Hit days | Max DD | t |
|---|---|---|---|---|---|---|---|
| decile_long_short | 252 | -0.3 | -0.7% | -0.041 | 53.6% | -14.5% | -0.04 |
| decile_long_only | 252 | +8.6 | +24.1% | 0.674 | 54.8% | -22.9% | 0.67 |
| top5_long_only | 252 | +24.1 | +83.5% | 1.025 | 56.8% | -31.5% | 1.03 |
| top5_long_bottom5_short | 252 | +5.7 | +15.4% | 0.464 | 55.6% | -20.4% | 0.46 |
| universe_equal_weight_long | 252 | +3.7 | +9.9% | 0.703 | 51.2% | -9.1% | 0.7 |
| spy_same_horizon | 252 | +0.6 | +1.6% | 0.114 | 50.0% | -10.8% | 0.11 |

## Reference: Qlib TopkDropout portfolio backtest (long only, close-to-close)

TopkDropout topk=30 n_drop=3, deal at close, 5+5 bps, benchmark SPY

- Annualized excess return vs SPY: +36.1%
- Information ratio: 1.164
- Max drawdown (excess): -24.6%

## Monthly decile long-short, net

| Month | Return |
|---|---|
| 2025-11 | +1.12% |
| 2025-12 | +1.28% |
| 2026-01 | -0.92% |
| 2026-02 | -1.23% |
| 2026-03 | +1.38% |
| 2026-04 | +3.43% |
| 2026-05 | +4.30% |
| 2026-06 | -4.91% |
| 2026-07 | +1.90% |
| 2026-08 | -2.09% |
| 2026-09 | +3.35% |
| 2026-10 | -5.44% |
| 2026-11 | -3.46% |

_Research output, not investment advice. Survivorship: the universe is current index membership._
