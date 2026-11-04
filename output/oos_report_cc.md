# Out-of-sample report: model `cc` (next session close to the following session's close (Qlib's native one-session hold, includes the overnight))

Validation year; the model never trained on these sessions. Window 2025-10-30 to 2026-10-30, 252 sessions. Target = next session close to the following session's close (Qlib's native one-session hold, includes the overnight) return. Costs = 4 bps round trip, the same as the ledger's simulated fund.

## Signal quality

| Metric | Value |
|---|---|
| IC (mean daily Pearson) | 0.0190 |
| ICIR | 0.089 |
| Rank IC | 0.0165 |
| Rank ICIR | 0.091 |
| Days with IC > 0 | 58.3% |

For scale: Qlib's LightGBM/Alpha158 benchmark on CSI300 reports IC 0.045 and Rank IC 0.047 (next-day close-to-close).

## Name-day hit rates (compare with the ledger's hit rate)

| Basket | Hit rate |
|---|---|
| Top-5 longs, share with a positive horizon return | 52.1% |
| Bottom-5 shorts, share with a negative horizon return | 49.5% |
| Top decile longs | 51.0% |
| Bottom decile shorts | 49.1% |
| Base rate: all tradable names with a positive horizon return | 50.9% |

## Horizon-return simulations, net of costs (per $1 of gross exposure)

| Simulation | Days | Mean/day (bps) | Annualized | Sharpe | Hit days | Max DD | t |
|---|---|---|---|---|---|---|---|
| decile_long_short | 252 | -0.1 | -0.2% | -0.012 | 54.4% | -11.5% | -0.01 |
| decile_long_only | 252 | +10.1 | +28.8% | 0.843 | 55.2% | -16.4% | 0.84 |
| top5_long_only | 252 | +24.9 | +87.1% | 1.059 | 55.6% | -27.7% | 1.06 |
| top5_long_bottom5_short | 252 | +10.1 | +29.0% | 0.857 | 54.0% | -13.7% | 0.86 |
| universe_equal_weight_long | 252 | +3.9 | +10.4% | 0.779 | 51.6% | -9.1% | 0.78 |
| spy_same_horizon | 252 | +0.8 | +1.9% | 0.147 | 50.8% | -10.8% | 0.15 |

## Reference: Qlib TopkDropout portfolio backtest (long only, close-to-close)

TopkDropout topk=30 n_drop=3, deal at close, 5+5 bps, benchmark SPY

- Annualized excess return vs SPY: +28.4%
- Information ratio: 0.911
- Max drawdown (excess): -26.5%

## Monthly decile long-short, net

| Month | Return |
|---|---|
| 2025-10 | -0.84% |
| 2025-11 | -1.22% |
| 2025-12 | +1.96% |
| 2026-01 | -0.68% |
| 2026-02 | -0.51% |
| 2026-03 | +0.66% |
| 2026-04 | +3.26% |
| 2026-05 | +4.00% |
| 2026-06 | -4.87% |
| 2026-07 | +2.43% |
| 2026-08 | -1.83% |
| 2026-09 | +3.47% |
| 2026-10 | -6.51% |

_Research output, not investment advice. Survivorship: the universe is current index membership._
