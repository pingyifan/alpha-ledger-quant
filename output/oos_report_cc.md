# Out-of-sample report: model `cc` (next session close to the following session's close (Qlib's native one-session hold, includes the overnight))

Validation year; the model never trained on these sessions. Window 2025-11-04 to 2026-11-04, 252 sessions. Target = next session close to the following session's close (Qlib's native one-session hold, includes the overnight) return. Costs = 4 bps round trip, the same as the ledger's simulated fund.

## Signal quality

| Metric | Value |
|---|---|
| IC (mean daily Pearson) | 0.0168 |
| ICIR | 0.076 |
| Rank IC | 0.0137 |
| Rank ICIR | 0.073 |
| Days with IC > 0 | 58.3% |

For scale: Qlib's LightGBM/Alpha158 benchmark on CSI300 reports IC 0.045 and Rank IC 0.047 (next-day close-to-close).

## Name-day hit rates (compare with the ledger's hit rate)

| Basket | Hit rate |
|---|---|
| Top-5 longs, share with a positive horizon return | 52.4% |
| Bottom-5 shorts, share with a negative horizon return | 48.2% |
| Top decile longs | 51.0% |
| Bottom decile shorts | 49.0% |
| Base rate: all tradable names with a positive horizon return | 50.8% |

## Horizon-return simulations, net of costs (per $1 of gross exposure)

| Simulation | Days | Mean/day (bps) | Annualized | Sharpe | Hit days | Max DD | t |
|---|---|---|---|---|---|---|---|
| decile_long_short | 252 | -0.9 | -2.3% | -0.144 | 53.6% | -15.5% | -0.14 |
| decile_long_only | 252 | +8.3 | +23.1% | 0.651 | 54.8% | -21.7% | 0.65 |
| top5_long_only | 252 | +33.8 | +133.8% | 1.419 | 56.0% | -29.0% | 1.42 |
| top5_long_bottom5_short | 252 | +7.8 | +21.8% | 0.631 | 50.8% | -19.2% | 0.63 |
| universe_equal_weight_long | 252 | +3.3 | +8.8% | 0.638 | 51.6% | -9.1% | 0.64 |
| spy_same_horizon | 252 | +0.0 | +0.1% | 0.006 | 50.8% | -10.8% | 0.01 |

## Reference: Qlib TopkDropout portfolio backtest (long only, close-to-close)

TopkDropout topk=30 n_drop=3, deal at close, 5+5 bps, benchmark SPY

- Annualized excess return vs SPY: +23.7%
- Information ratio: 0.718
- Max drawdown (excess): -27.4%

## Monthly decile long-short, net

| Month | Return |
|---|---|
| 2025-11 | -1.77% |
| 2025-12 | +1.68% |
| 2026-01 | -0.40% |
| 2026-02 | -0.93% |
| 2026-03 | +1.73% |
| 2026-04 | +4.24% |
| 2026-05 | +5.89% |
| 2026-06 | -5.23% |
| 2026-07 | +1.84% |
| 2026-08 | -1.50% |
| 2026-09 | +2.31% |
| 2026-10 | -6.05% |
| 2026-11 | -4.67% |

_Research output, not investment advice. Survivorship: the universe is current index membership._
