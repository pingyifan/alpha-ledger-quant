# Out-of-sample report: model `cc` (next session close to the following session's close (Qlib's native one-session hold, includes the overnight))

Validation year; the model never trained on these sessions. Window 2025-10-31 to 2026-11-02, 252 sessions. Target = next session close to the following session's close (Qlib's native one-session hold, includes the overnight) return. Costs = 4 bps round trip, the same as the ledger's simulated fund.

## Signal quality

| Metric | Value |
|---|---|
| IC (mean daily Pearson) | 0.0182 |
| ICIR | 0.083 |
| Rank IC | 0.0154 |
| Rank ICIR | 0.083 |
| Days with IC > 0 | 58.3% |

For scale: Qlib's LightGBM/Alpha158 benchmark on CSI300 reports IC 0.045 and Rank IC 0.047 (next-day close-to-close).

## Name-day hit rates (compare with the ledger's hit rate)

| Basket | Hit rate |
|---|---|
| Top-5 longs, share with a positive horizon return | 51.7% |
| Bottom-5 shorts, share with a negative horizon return | 49.8% |
| Top decile longs | 50.8% |
| Bottom decile shorts | 48.9% |
| Base rate: all tradable names with a positive horizon return | 51.0% |

## Horizon-return simulations, net of costs (per $1 of gross exposure)

| Simulation | Days | Mean/day (bps) | Annualized | Sharpe | Hit days | Max DD | t |
|---|---|---|---|---|---|---|---|
| decile_long_short | 252 | -1.8 | -4.5% | -0.295 | 53.2% | -12.5% | -0.29 |
| decile_long_only | 252 | +7.6 | +21.2% | 0.627 | 53.2% | -17.5% | 0.63 |
| top5_long_only | 252 | +39.5 | +169.8% | 1.686 | 54.8% | -23.0% | 1.69 |
| top5_long_bottom5_short | 252 | +13.6 | +40.7% | 1.125 | 52.8% | -13.8% | 1.13 |
| universe_equal_weight_long | 252 | +4.7 | +12.4% | 0.919 | 52.0% | -9.1% | 0.92 |
| spy_same_horizon | 252 | +1.3 | +3.4% | 0.26 | 50.8% | -10.8% | 0.26 |

## Reference: Qlib TopkDropout portfolio backtest (long only, close-to-close)

TopkDropout topk=30 n_drop=3, deal at close, 5+5 bps, benchmark SPY

- Annualized excess return vs SPY: +19.8%
- Information ratio: 0.61
- Max drawdown (excess): -34.7%

## Monthly decile long-short, net

| Month | Return |
|---|---|
| 2025-10 | -1.08% |
| 2025-11 | -0.75% |
| 2025-12 | +1.85% |
| 2026-01 | -0.48% |
| 2026-02 | -0.96% |
| 2026-03 | +1.14% |
| 2026-04 | +2.75% |
| 2026-05 | +4.11% |
| 2026-06 | -5.17% |
| 2026-07 | +1.91% |
| 2026-08 | -1.61% |
| 2026-09 | +2.57% |
| 2026-10 | -6.02% |
| 2026-11 | -3.51% |

_Research output, not investment advice. Survivorship: the universe is current index membership._
