# Out-of-sample report: model `cc` (next session close to the following session's close (Qlib's native one-session hold, includes the overnight))

Validation year; the model never trained on these sessions. Window 2025-10-24 to 2026-10-26, 252 sessions. Target = next session close to the following session's close (Qlib's native one-session hold, includes the overnight) return. Costs = 4 bps round trip, the same as the ledger's simulated fund.

## Signal quality

| Metric | Value |
|---|---|
| IC (mean daily Pearson) | 0.0211 |
| ICIR | 0.100 |
| Rank IC | 0.0171 |
| Rank ICIR | 0.094 |
| Days with IC > 0 | 59.1% |

For scale: Qlib's LightGBM/Alpha158 benchmark on CSI300 reports IC 0.045 and Rank IC 0.047 (next-day close-to-close).

## Name-day hit rates (compare with the ledger's hit rate)

| Basket | Hit rate |
|---|---|
| Top-5 longs, share with a positive horizon return | 53.2% |
| Bottom-5 shorts, share with a negative horizon return | 48.4% |
| Top decile longs | 50.9% |
| Bottom decile shorts | 49.4% |
| Base rate: all tradable names with a positive horizon return | 50.6% |

## Horizon-return simulations, net of costs (per $1 of gross exposure)

| Simulation | Days | Mean/day (bps) | Annualized | Sharpe | Hit days | Max DD | t |
|---|---|---|---|---|---|---|---|
| decile_long_short | 252 | +1.3 | +3.3% | 0.218 | 54.4% | -10.0% | 0.22 |
| decile_long_only | 252 | +10.1 | +28.9% | 0.852 | 55.6% | -16.1% | 0.85 |
| top5_long_only | 252 | +42.6 | +192.1% | 1.857 | 57.9% | -24.8% | 1.86 |
| top5_long_bottom5_short | 252 | +12.6 | +37.4% | 1.1 | 52.8% | -12.7% | 1.1 |
| universe_equal_weight_long | 252 | +2.6 | +6.7% | 0.514 | 51.2% | -9.1% | 0.51 |
| spy_same_horizon | 252 | +1.5 | +3.8% | 0.296 | 51.6% | -11.3% | 0.3 |

## Reference: Qlib TopkDropout portfolio backtest (long only, close-to-close)

TopkDropout topk=30 n_drop=3, deal at close, 5+5 bps, benchmark SPY

- Annualized excess return vs SPY: +36.0%
- Information ratio: 1.177
- Max drawdown (excess): -21.2%

## Monthly decile long-short, net

| Month | Return |
|---|---|
| 2025-10 | +0.08% |
| 2025-11 | -1.54% |
| 2025-12 | +1.23% |
| 2026-01 | -0.35% |
| 2026-02 | -0.88% |
| 2026-03 | +1.03% |
| 2026-04 | +3.35% |
| 2026-05 | +5.04% |
| 2026-06 | -3.68% |
| 2026-07 | +2.18% |
| 2026-08 | -1.81% |
| 2026-09 | +2.30% |
| 2026-10 | -4.37% |

_Research output, not investment advice. Survivorship: the universe is current index membership._
