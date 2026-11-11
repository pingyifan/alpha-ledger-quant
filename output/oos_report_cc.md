# Out-of-sample report: model `cc` (next session close to the following session's close (Qlib's native one-session hold, includes the overnight))

Validation year; the model never trained on these sessions. Window 2025-11-06 to 2026-11-06, 252 sessions. Target = next session close to the following session's close (Qlib's native one-session hold, includes the overnight) return. Costs = 4 bps round trip, the same as the ledger's simulated fund.

## Signal quality

| Metric | Value |
|---|---|
| IC (mean daily Pearson) | 0.0195 |
| ICIR | 0.088 |
| Rank IC | 0.0165 |
| Rank ICIR | 0.087 |
| Days with IC > 0 | 59.9% |

For scale: Qlib's LightGBM/Alpha158 benchmark on CSI300 reports IC 0.045 and Rank IC 0.047 (next-day close-to-close).

## Name-day hit rates (compare with the ledger's hit rate)

| Basket | Hit rate |
|---|---|
| Top-5 longs, share with a positive horizon return | 52.5% |
| Bottom-5 shorts, share with a negative horizon return | 50.0% |
| Top decile longs | 50.8% |
| Bottom decile shorts | 49.0% |
| Base rate: all tradable names with a positive horizon return | 50.9% |

## Horizon-return simulations, net of costs (per $1 of gross exposure)

| Simulation | Days | Mean/day (bps) | Annualized | Sharpe | Hit days | Max DD | t |
|---|---|---|---|---|---|---|---|
| decile_long_short | 252 | -0.9 | -2.2% | -0.134 | 54.4% | -15.3% | -0.13 |
| decile_long_only | 252 | +8.4 | +23.5% | 0.652 | 54.8% | -23.6% | 0.65 |
| top5_long_only | 252 | +25.7 | +90.7% | 1.101 | 54.8% | -31.3% | 1.1 |
| top5_long_bottom5_short | 252 | +5.5 | +14.8% | 0.458 | 48.4% | -15.8% | 0.46 |
| universe_equal_weight_long | 252 | +4.2 | +11.2% | 0.793 | 52.0% | -9.1% | 0.79 |
| spy_same_horizon | 252 | +1.2 | +3.1% | 0.223 | 50.8% | -10.8% | 0.22 |

## Reference: Qlib TopkDropout portfolio backtest (long only, close-to-close)

TopkDropout topk=30 n_drop=3, deal at close, 5+5 bps, benchmark SPY

- Annualized excess return vs SPY: +32.1%
- Information ratio: 1.004
- Max drawdown (excess): -22.9%

## Monthly decile long-short, net

| Month | Return |
|---|---|
| 2025-11 | -0.21% |
| 2025-12 | +1.50% |
| 2026-01 | -1.16% |
| 2026-02 | -1.12% |
| 2026-03 | +1.78% |
| 2026-04 | +4.11% |
| 2026-05 | +4.29% |
| 2026-06 | -5.61% |
| 2026-07 | +2.46% |
| 2026-08 | -2.08% |
| 2026-09 | +2.85% |
| 2026-10 | -5.85% |
| 2026-11 | -3.81% |

_Research output, not investment advice. Survivorship: the universe is current index membership._
