# Out-of-sample report: model `cc` (next session close to the following session's close (Qlib's native one-session hold, includes the overnight))

Validation year; the model never trained on these sessions. Window 2025-10-07 to 2026-10-07, 252 sessions. Target = next session close to the following session's close (Qlib's native one-session hold, includes the overnight) return. Costs = 4 bps round trip, the same as the ledger's simulated fund.

## Signal quality

| Metric | Value |
|---|---|
| IC (mean daily Pearson) | 0.0261 |
| ICIR | 0.131 |
| Rank IC | 0.0214 |
| Rank ICIR | 0.125 |
| Days with IC > 0 | 59.5% |

For scale: Qlib's LightGBM/Alpha158 benchmark on CSI300 reports IC 0.045 and Rank IC 0.047 (next-day close-to-close).

## Name-day hit rates (compare with the ledger's hit rate)

| Basket | Hit rate |
|---|---|
| Top-5 longs, share with a positive horizon return | 52.0% |
| Bottom-5 shorts, share with a negative horizon return | 46.8% |
| Top decile longs | 51.2% |
| Bottom decile shorts | 49.7% |
| Base rate: all tradable names with a positive horizon return | 50.5% |

## Horizon-return simulations, net of costs (per $1 of gross exposure)

| Simulation | Days | Mean/day (bps) | Annualized | Sharpe | Hit days | Max DD | t |
|---|---|---|---|---|---|---|---|
| decile_long_short | 252 | +4.7 | +12.4% | 0.845 | 56.0% | -10.5% | 0.85 |
| decile_long_only | 252 | +15.9 | +49.2% | 1.38 | 55.6% | -15.2% | 1.38 |
| top5_long_only | 252 | +37.1 | +154.2% | 1.561 | 54.8% | -24.5% | 1.56 |
| top5_long_bottom5_short | 252 | +6.5 | +17.8% | 0.548 | 49.6% | -15.0% | 0.55 |
| universe_equal_weight_long | 252 | +2.2 | +5.8% | 0.432 | 52.0% | -9.1% | 0.43 |
| spy_same_horizon | 252 | +2.5 | +6.6% | 0.492 | 51.6% | -11.3% | 0.49 |

## Reference: Qlib TopkDropout portfolio backtest (long only, close-to-close)

TopkDropout topk=30 n_drop=3, deal at close, 5+5 bps, benchmark SPY

- Annualized excess return vs SPY: +48.9%
- Information ratio: 1.58
- Max drawdown (excess): -22.5%

## Monthly decile long-short, net

| Month | Return |
|---|---|
| 2025-10 | +2.37% |
| 2025-11 | -1.09% |
| 2025-12 | +1.59% |
| 2026-01 | -1.11% |
| 2026-02 | -1.16% |
| 2026-03 | +1.40% |
| 2026-04 | +4.24% |
| 2026-05 | +4.88% |
| 2026-06 | -4.06% |
| 2026-07 | +2.29% |
| 2026-08 | -1.63% |
| 2026-09 | +3.00% |
| 2026-10 | +0.47% |

_Research output, not investment advice. Survivorship: the universe is current index membership._
