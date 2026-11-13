# Out-of-sample report: model `cc` (next session close to the following session's close (Qlib's native one-session hold, includes the overnight))

Validation year; the model never trained on these sessions. Window 2025-11-10 to 2026-11-10, 252 sessions. Target = next session close to the following session's close (Qlib's native one-session hold, includes the overnight) return. Costs = 4 bps round trip, the same as the ledger's simulated fund.

## Signal quality

| Metric | Value |
|---|---|
| IC (mean daily Pearson) | 0.0199 |
| ICIR | 0.091 |
| Rank IC | 0.0191 |
| Rank ICIR | 0.103 |
| Days with IC > 0 | 58.3% |

For scale: Qlib's LightGBM/Alpha158 benchmark on CSI300 reports IC 0.045 and Rank IC 0.047 (next-day close-to-close).

## Name-day hit rates (compare with the ledger's hit rate)

| Basket | Hit rate |
|---|---|
| Top-5 longs, share with a positive horizon return | 52.4% |
| Bottom-5 shorts, share with a negative horizon return | 47.0% |
| Top decile longs | 50.8% |
| Bottom decile shorts | 49.0% |
| Base rate: all tradable names with a positive horizon return | 50.8% |

## Horizon-return simulations, net of costs (per $1 of gross exposure)

| Simulation | Days | Mean/day (bps) | Annualized | Sharpe | Hit days | Max DD | t |
|---|---|---|---|---|---|---|---|
| decile_long_short | 252 | -0.7 | -1.7% | -0.109 | 54.4% | -14.4% | -0.11 |
| decile_long_only | 252 | +8.4 | +23.7% | 0.672 | 54.4% | -22.0% | 0.67 |
| top5_long_only | 252 | +33.3 | +131.0% | 1.42 | 56.0% | -31.7% | 1.42 |
| top5_long_bottom5_short | 252 | +7.1 | +19.5% | 0.579 | 50.8% | -19.7% | 0.58 |
| universe_equal_weight_long | 252 | +3.8 | +9.9% | 0.704 | 51.2% | -9.1% | 0.7 |
| spy_same_horizon | 252 | +0.9 | +2.3% | 0.163 | 50.4% | -10.8% | 0.16 |

## Reference: Qlib TopkDropout portfolio backtest (long only, close-to-close)

TopkDropout topk=30 n_drop=3, deal at close, 5+5 bps, benchmark SPY

- Annualized excess return vs SPY: +33.0%
- Information ratio: 1.038
- Max drawdown (excess): -21.2%

## Monthly decile long-short, net

| Month | Return |
|---|---|
| 2025-11 | -0.45% |
| 2025-12 | +1.70% |
| 2026-01 | -1.00% |
| 2026-02 | -1.75% |
| 2026-03 | +0.81% |
| 2026-04 | +2.93% |
| 2026-05 | +4.98% |
| 2026-06 | -5.62% |
| 2026-07 | +2.08% |
| 2026-08 | -1.43% |
| 2026-09 | +3.33% |
| 2026-10 | -6.11% |
| 2026-11 | -1.78% |

_Research output, not investment advice. Survivorship: the universe is current index membership._
