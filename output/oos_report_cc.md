# Out-of-sample report: model `cc` (next session close to the following session's close (Qlib's native one-session hold, includes the overnight))

Validation year; the model never trained on these sessions. Window 2025-11-17 to 2026-11-17, 252 sessions. Target = next session close to the following session's close (Qlib's native one-session hold, includes the overnight) return. Costs = 4 bps round trip, the same as the ledger's simulated fund.

## Signal quality

| Metric | Value |
|---|---|
| IC (mean daily Pearson) | 0.0212 |
| ICIR | 0.099 |
| Rank IC | 0.0179 |
| Rank ICIR | 0.097 |
| Days with IC > 0 | 57.1% |

For scale: Qlib's LightGBM/Alpha158 benchmark on CSI300 reports IC 0.045 and Rank IC 0.047 (next-day close-to-close).

## Name-day hit rates (compare with the ledger's hit rate)

| Basket | Hit rate |
|---|---|
| Top-5 longs, share with a positive horizon return | 50.6% |
| Bottom-5 shorts, share with a negative horizon return | 49.6% |
| Top decile longs | 50.9% |
| Bottom decile shorts | 49.4% |
| Base rate: all tradable names with a positive horizon return | 50.7% |

## Horizon-return simulations, net of costs (per $1 of gross exposure)

| Simulation | Days | Mean/day (bps) | Annualized | Sharpe | Hit days | Max DD | t |
|---|---|---|---|---|---|---|---|
| decile_long_short | 252 | -0.2 | -0.4% | -0.025 | 52.0% | -15.6% | -0.03 |
| decile_long_only | 252 | +7.8 | +21.6% | 0.608 | 54.4% | -24.5% | 0.61 |
| top5_long_only | 252 | +18.2 | +58.0% | 0.772 | 52.8% | -35.8% | 0.77 |
| top5_long_bottom5_short | 252 | +4.9 | +13.0% | 0.405 | 50.0% | -22.8% | 0.41 |
| universe_equal_weight_long | 252 | +3.3 | +8.6% | 0.606 | 51.6% | -9.2% | 0.61 |
| spy_same_horizon | 252 | +0.0 | +0.1% | 0.005 | 50.0% | -10.8% | 0.01 |

## Reference: Qlib TopkDropout portfolio backtest (long only, close-to-close)

TopkDropout topk=30 n_drop=3, deal at close, 5+5 bps, benchmark SPY

- Annualized excess return vs SPY: +41.0%
- Information ratio: 1.27
- Max drawdown (excess): -22.2%

## Monthly decile long-short, net

| Month | Return |
|---|---|
| 2025-11 | +1.96% |
| 2025-12 | +1.63% |
| 2026-01 | -0.95% |
| 2026-02 | -0.62% |
| 2026-03 | +1.71% |
| 2026-04 | +3.42% |
| 2026-05 | +4.40% |
| 2026-06 | -5.22% |
| 2026-07 | +1.16% |
| 2026-08 | -1.87% |
| 2026-09 | +2.82% |
| 2026-10 | -5.72% |
| 2026-11 | -3.75% |

_Research output, not investment advice. Survivorship: the universe is current index membership._
