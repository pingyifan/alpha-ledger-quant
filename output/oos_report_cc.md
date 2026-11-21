# Out-of-sample report: model `cc` (next session close to the following session's close (Qlib's native one-session hold, includes the overnight))

Validation year; the model never trained on these sessions. Window 2025-11-18 to 2026-11-18, 252 sessions. Target = next session close to the following session's close (Qlib's native one-session hold, includes the overnight) return. Costs = 4 bps round trip, the same as the ledger's simulated fund.

## Signal quality

| Metric | Value |
|---|---|
| IC (mean daily Pearson) | 0.0191 |
| ICIR | 0.087 |
| Rank IC | 0.0165 |
| Rank ICIR | 0.087 |
| Days with IC > 0 | 57.5% |

For scale: Qlib's LightGBM/Alpha158 benchmark on CSI300 reports IC 0.045 and Rank IC 0.047 (next-day close-to-close).

## Name-day hit rates (compare with the ledger's hit rate)

| Basket | Hit rate |
|---|---|
| Top-5 longs, share with a positive horizon return | 51.8% |
| Bottom-5 shorts, share with a negative horizon return | 49.4% |
| Top decile longs | 50.6% |
| Bottom decile shorts | 49.6% |
| Base rate: all tradable names with a positive horizon return | 50.6% |

## Horizon-return simulations, net of costs (per $1 of gross exposure)

| Simulation | Days | Mean/day (bps) | Annualized | Sharpe | Hit days | Max DD | t |
|---|---|---|---|---|---|---|---|
| decile_long_short | 252 | -1.1 | -2.7% | -0.165 | 52.4% | -15.1% | -0.17 |
| decile_long_only | 252 | +5.6 | +15.1% | 0.425 | 52.8% | -27.9% | 0.42 |
| top5_long_only | 252 | +14.1 | +42.6% | 0.59 | 54.0% | -34.1% | 0.59 |
| top5_long_bottom5_short | 252 | +3.3 | +8.7% | 0.265 | 50.8% | -16.0% | 0.26 |
| universe_equal_weight_long | 252 | +2.3 | +6.0% | 0.426 | 51.6% | -10.7% | 0.43 |
| spy_same_horizon | 252 | -1.6 | -3.9% | -0.276 | 49.6% | -13.6% | -0.28 |

## Reference: Qlib TopkDropout portfolio backtest (long only, close-to-close)

TopkDropout topk=30 n_drop=3, deal at close, 5+5 bps, benchmark SPY

- Annualized excess return vs SPY: +37.2%
- Information ratio: 1.182
- Max drawdown (excess): -20.6%

## Monthly decile long-short, net

| Month | Return |
|---|---|
| 2025-11 | +1.06% |
| 2025-12 | +0.80% |
| 2026-01 | -0.61% |
| 2026-02 | -1.04% |
| 2026-03 | +1.96% |
| 2026-04 | +3.41% |
| 2026-05 | +5.00% |
| 2026-06 | -5.20% |
| 2026-07 | +3.30% |
| 2026-08 | -1.85% |
| 2026-09 | +1.74% |
| 2026-10 | -6.24% |
| 2026-11 | -5.66% |

_Research output, not investment advice. Survivorship: the universe is current index membership._
