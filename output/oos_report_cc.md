# Out-of-sample report: model `cc` (next session close to the following session's close (Qlib's native one-session hold, includes the overnight))

Validation year; the model never trained on these sessions. Window 2025-11-21 to 2026-11-23, 252 sessions. Target = next session close to the following session's close (Qlib's native one-session hold, includes the overnight) return. Costs = 4 bps round trip, the same as the ledger's simulated fund.

## Signal quality

| Metric | Value |
|---|---|
| IC (mean daily Pearson) | 0.0200 |
| ICIR | 0.092 |
| Rank IC | 0.0161 |
| Rank ICIR | 0.085 |
| Days with IC > 0 | 56.8% |

For scale: Qlib's LightGBM/Alpha158 benchmark on CSI300 reports IC 0.045 and Rank IC 0.047 (next-day close-to-close).

## Name-day hit rates (compare with the ledger's hit rate)

| Basket | Hit rate |
|---|---|
| Top-5 longs, share with a positive horizon return | 51.7% |
| Bottom-5 shorts, share with a negative horizon return | 48.1% |
| Top decile longs | 50.8% |
| Bottom decile shorts | 49.1% |
| Base rate: all tradable names with a positive horizon return | 50.8% |

## Horizon-return simulations, net of costs (per $1 of gross exposure)

| Simulation | Days | Mean/day (bps) | Annualized | Sharpe | Hit days | Max DD | t |
|---|---|---|---|---|---|---|---|
| decile_long_short | 252 | -0.6 | -1.4% | -0.086 | 52.4% | -16.0% | -0.09 |
| decile_long_only | 252 | +8.0 | +22.4% | 0.599 | 54.4% | -27.8% | 0.6 |
| top5_long_only | 252 | +29.7 | +111.0% | 1.197 | 56.0% | -28.9% | 1.2 |
| top5_long_bottom5_short | 252 | +5.5 | +14.9% | 0.433 | 50.8% | -20.8% | 0.43 |
| universe_equal_weight_long | 252 | +3.4 | +9.0% | 0.62 | 52.0% | -10.7% | 0.62 |
| spy_same_horizon | 252 | -0.4 | -1.0% | -0.065 | 49.2% | -13.6% | -0.06 |

## Reference: Qlib TopkDropout portfolio backtest (long only, close-to-close)

TopkDropout topk=30 n_drop=3, deal at close, 5+5 bps, benchmark SPY

- Annualized excess return vs SPY: +35.5%
- Information ratio: 1.095
- Max drawdown (excess): -20.5%

## Monthly decile long-short, net

| Month | Return |
|---|---|
| 2025-11 | +1.58% |
| 2025-12 | +0.96% |
| 2026-01 | +0.09% |
| 2026-02 | -1.30% |
| 2026-03 | +1.15% |
| 2026-04 | +4.21% |
| 2026-05 | +4.67% |
| 2026-06 | -5.74% |
| 2026-07 | +1.47% |
| 2026-08 | -1.17% |
| 2026-09 | +2.27% |
| 2026-10 | -5.89% |
| 2026-11 | -4.40% |

_Research output, not investment advice. Survivorship: the universe is current index membership._
