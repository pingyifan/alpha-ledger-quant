# Out-of-sample report: model `cc` (next session close to the following session's close (Qlib's native one-session hold, includes the overnight))

Validation year; the model never trained on these sessions. Window 2025-10-20 to 2026-10-20, 252 sessions. Target = next session close to the following session's close (Qlib's native one-session hold, includes the overnight) return. Costs = 4 bps round trip, the same as the ledger's simulated fund.

## Signal quality

| Metric | Value |
|---|---|
| IC (mean daily Pearson) | 0.0185 |
| ICIR | 0.091 |
| Rank IC | 0.0140 |
| Rank ICIR | 0.080 |
| Days with IC > 0 | 58.7% |

For scale: Qlib's LightGBM/Alpha158 benchmark on CSI300 reports IC 0.045 and Rank IC 0.047 (next-day close-to-close).

## Name-day hit rates (compare with the ledger's hit rate)

| Basket | Hit rate |
|---|---|
| Top-5 longs, share with a positive horizon return | 51.6% |
| Bottom-5 shorts, share with a negative horizon return | 47.1% |
| Top decile longs | 50.9% |
| Bottom decile shorts | 49.0% |
| Base rate: all tradable names with a positive horizon return | 50.7% |

## Horizon-return simulations, net of costs (per $1 of gross exposure)

| Simulation | Days | Mean/day (bps) | Annualized | Sharpe | Hit days | Max DD | t |
|---|---|---|---|---|---|---|---|
| decile_long_short | 252 | +0.4 | +1.0% | 0.069 | 54.8% | -10.3% | 0.07 |
| decile_long_only | 252 | +10.3 | +29.7% | 0.868 | 56.0% | -15.7% | 0.87 |
| top5_long_only | 252 | +27.1 | +97.8% | 1.138 | 55.6% | -28.2% | 1.14 |
| top5_long_bottom5_short | 252 | -1.5 | -3.7% | -0.127 | 49.2% | -19.9% | -0.13 |
| universe_equal_weight_long | 252 | +2.9 | +7.6% | 0.582 | 51.6% | -9.1% | 0.58 |
| spy_same_horizon | 252 | +1.9 | +4.9% | 0.372 | 51.6% | -11.3% | 0.37 |

## Reference: Qlib TopkDropout portfolio backtest (long only, close-to-close)

TopkDropout topk=30 n_drop=3, deal at close, 5+5 bps, benchmark SPY

- Annualized excess return vs SPY: +30.7%
- Information ratio: 1.033
- Max drawdown (excess): -23.1%

## Monthly decile long-short, net

| Month | Return |
|---|---|
| 2025-10 | +0.75% |
| 2025-11 | -1.27% |
| 2025-12 | +1.67% |
| 2026-01 | -0.82% |
| 2026-02 | -1.36% |
| 2026-03 | +0.66% |
| 2026-04 | +4.58% |
| 2026-05 | +4.18% |
| 2026-06 | -4.19% |
| 2026-07 | +2.22% |
| 2026-08 | -1.40% |
| 2026-09 | +2.64% |
| 2026-10 | -7.08% |

_Research output, not investment advice. Survivorship: the universe is current index membership._
