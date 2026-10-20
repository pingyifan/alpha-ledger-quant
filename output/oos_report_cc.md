# Out-of-sample report: model `cc` (next session close to the following session's close (Qlib's native one-session hold, includes the overnight))

Validation year; the model never trained on these sessions. Window 2025-10-15 to 2026-10-15, 252 sessions. Target = next session close to the following session's close (Qlib's native one-session hold, includes the overnight) return. Costs = 4 bps round trip, the same as the ledger's simulated fund.

## Signal quality

| Metric | Value |
|---|---|
| IC (mean daily Pearson) | 0.0184 |
| ICIR | 0.090 |
| Rank IC | 0.0167 |
| Rank ICIR | 0.095 |
| Days with IC > 0 | 59.5% |

For scale: Qlib's LightGBM/Alpha158 benchmark on CSI300 reports IC 0.045 and Rank IC 0.047 (next-day close-to-close).

## Name-day hit rates (compare with the ledger's hit rate)

| Basket | Hit rate |
|---|---|
| Top-5 longs, share with a positive horizon return | 51.9% |
| Bottom-5 shorts, share with a negative horizon return | 46.5% |
| Top decile longs | 50.9% |
| Bottom decile shorts | 49.5% |
| Base rate: all tradable names with a positive horizon return | 50.7% |

## Horizon-return simulations, net of costs (per $1 of gross exposure)

| Simulation | Days | Mean/day (bps) | Annualized | Sharpe | Hit days | Max DD | t |
|---|---|---|---|---|---|---|---|
| decile_long_short | 252 | +2.0 | +5.1% | 0.348 | 54.0% | -10.7% | 0.35 |
| decile_long_only | 252 | +11.9 | +35.1% | 1.021 | 54.8% | -15.4% | 1.02 |
| top5_long_only | 252 | +31.0 | +118.1% | 1.341 | 53.6% | -24.1% | 1.34 |
| top5_long_bottom5_short | 252 | -0.4 | -1.0% | -0.033 | 48.4% | -20.0% | -0.03 |
| universe_equal_weight_long | 252 | +2.9 | +7.7% | 0.585 | 51.6% | -9.1% | 0.58 |
| spy_same_horizon | 252 | +2.6 | +6.9% | 0.524 | 51.6% | -11.3% | 0.52 |

## Reference: Qlib TopkDropout portfolio backtest (long only, close-to-close)

TopkDropout topk=30 n_drop=3, deal at close, 5+5 bps, benchmark SPY

- Annualized excess return vs SPY: +39.5%
- Information ratio: 1.312
- Max drawdown (excess): -21.3%

## Monthly decile long-short, net

| Month | Return |
|---|---|
| 2025-10 | +0.50% |
| 2025-11 | -1.46% |
| 2025-12 | +2.08% |
| 2026-01 | -0.59% |
| 2026-02 | -0.85% |
| 2026-03 | +0.93% |
| 2026-04 | +4.14% |
| 2026-05 | +4.94% |
| 2026-06 | -4.28% |
| 2026-07 | +2.20% |
| 2026-08 | -1.18% |
| 2026-09 | +2.62% |
| 2026-10 | -4.61% |

_Research output, not investment advice. Survivorship: the universe is current index membership._
