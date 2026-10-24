# Out-of-sample report: model `cc` (next session close to the following session's close (Qlib's native one-session hold, includes the overnight))

Validation year; the model never trained on these sessions. Window 2025-10-21 to 2026-10-21, 252 sessions. Target = next session close to the following session's close (Qlib's native one-session hold, includes the overnight) return. Costs = 4 bps round trip, the same as the ledger's simulated fund.

## Signal quality

| Metric | Value |
|---|---|
| IC (mean daily Pearson) | 0.0192 |
| ICIR | 0.095 |
| Rank IC | 0.0157 |
| Rank ICIR | 0.090 |
| Days with IC > 0 | 58.3% |

For scale: Qlib's LightGBM/Alpha158 benchmark on CSI300 reports IC 0.045 and Rank IC 0.047 (next-day close-to-close).

## Name-day hit rates (compare with the ledger's hit rate)

| Basket | Hit rate |
|---|---|
| Top-5 longs, share with a positive horizon return | 53.0% |
| Bottom-5 shorts, share with a negative horizon return | 47.3% |
| Top decile longs | 50.8% |
| Bottom decile shorts | 49.7% |
| Base rate: all tradable names with a positive horizon return | 50.7% |

## Horizon-return simulations, net of costs (per $1 of gross exposure)

| Simulation | Days | Mean/day (bps) | Annualized | Sharpe | Hit days | Max DD | t |
|---|---|---|---|---|---|---|---|
| decile_long_short | 252 | +1.3 | +3.4% | 0.23 | 54.8% | -10.2% | 0.23 |
| decile_long_only | 252 | +10.9 | +31.6% | 0.926 | 55.2% | -15.4% | 0.93 |
| top5_long_only | 252 | +38.2 | +161.6% | 1.659 | 57.1% | -24.3% | 1.66 |
| top5_long_bottom5_short | 252 | +8.6 | +24.0% | 0.741 | 53.2% | -11.9% | 0.74 |
| universe_equal_weight_long | 252 | +2.9 | +7.6% | 0.582 | 51.6% | -9.1% | 0.58 |
| spy_same_horizon | 252 | +1.9 | +4.9% | 0.372 | 51.6% | -11.3% | 0.37 |

## Reference: Qlib TopkDropout portfolio backtest (long only, close-to-close)

TopkDropout topk=30 n_drop=3, deal at close, 5+5 bps, benchmark SPY

- Annualized excess return vs SPY: +33.5%
- Information ratio: 1.115
- Max drawdown (excess): -22.6%

## Monthly decile long-short, net

| Month | Return |
|---|---|
| 2025-10 | +1.55% |
| 2025-11 | -0.92% |
| 2025-12 | +1.75% |
| 2026-01 | -1.11% |
| 2026-02 | -1.27% |
| 2026-03 | +1.02% |
| 2026-04 | +4.31% |
| 2026-05 | +4.26% |
| 2026-06 | -3.80% |
| 2026-07 | +1.88% |
| 2026-08 | -0.72% |
| 2026-09 | +2.83% |
| 2026-10 | -6.90% |

_Research output, not investment advice. Survivorship: the universe is current index membership._
