# Out-of-sample report: model `cc` (next session close to the following session's close (Qlib's native one-session hold, includes the overnight))

Validation year; the model never trained on these sessions. Window 2025-11-21 to 2026-11-23, 252 sessions. Target = next session close to the following session's close (Qlib's native one-session hold, includes the overnight) return. Costs = 4 bps round trip, the same as the ledger's simulated fund.

## Signal quality

| Metric | Value |
|---|---|
| IC (mean daily Pearson) | 0.0203 |
| ICIR | 0.094 |
| Rank IC | 0.0163 |
| Rank ICIR | 0.086 |
| Days with IC > 0 | 57.9% |

For scale: Qlib's LightGBM/Alpha158 benchmark on CSI300 reports IC 0.045 and Rank IC 0.047 (next-day close-to-close).

## Name-day hit rates (compare with the ledger's hit rate)

| Basket | Hit rate |
|---|---|
| Top-5 longs, share with a positive horizon return | 51.3% |
| Bottom-5 shorts, share with a negative horizon return | 49.3% |
| Top decile longs | 51.1% |
| Bottom decile shorts | 49.1% |
| Base rate: all tradable names with a positive horizon return | 50.8% |

## Horizon-return simulations, net of costs (per $1 of gross exposure)

| Simulation | Days | Mean/day (bps) | Annualized | Sharpe | Hit days | Max DD | t |
|---|---|---|---|---|---|---|---|
| decile_long_short | 252 | +0.2 | +0.5% | 0.03 | 52.0% | -14.9% | 0.03 |
| decile_long_only | 252 | +9.2 | +25.9% | 0.695 | 53.6% | -25.9% | 0.7 |
| top5_long_only | 252 | +22.8 | +77.3% | 0.93 | 51.6% | -25.3% | 0.93 |
| top5_long_bottom5_short | 252 | +10.6 | +30.6% | 0.831 | 48.4% | -13.0% | 0.83 |
| universe_equal_weight_long | 252 | +3.4 | +9.0% | 0.62 | 52.0% | -10.7% | 0.62 |
| spy_same_horizon | 252 | -0.4 | -1.0% | -0.065 | 49.2% | -13.6% | -0.06 |

## Reference: Qlib TopkDropout portfolio backtest (long only, close-to-close)

TopkDropout topk=30 n_drop=3, deal at close, 5+5 bps, benchmark SPY

- Annualized excess return vs SPY: +26.0%
- Information ratio: 0.802
- Max drawdown (excess): -21.3%

## Monthly decile long-short, net

| Month | Return |
|---|---|
| 2025-11 | +1.49% |
| 2025-12 | +1.78% |
| 2026-01 | +0.02% |
| 2026-02 | -1.65% |
| 2026-03 | +1.13% |
| 2026-04 | +3.68% |
| 2026-05 | +4.87% |
| 2026-06 | -5.21% |
| 2026-07 | +2.34% |
| 2026-08 | -1.75% |
| 2026-09 | +2.83% |
| 2026-10 | -6.14% |
| 2026-11 | -3.55% |

_Research output, not investment advice. Survivorship: the universe is current index membership._
