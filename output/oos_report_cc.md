# Out-of-sample report: model `cc` (next session close to the following session's close (Qlib's native one-session hold, includes the overnight))

Validation year; the model never trained on these sessions. Window 2025-11-03 to 2026-11-03, 252 sessions. Target = next session close to the following session's close (Qlib's native one-session hold, includes the overnight) return. Costs = 4 bps round trip, the same as the ledger's simulated fund.

## Signal quality

| Metric | Value |
|---|---|
| IC (mean daily Pearson) | 0.0178 |
| ICIR | 0.082 |
| Rank IC | 0.0156 |
| Rank ICIR | 0.085 |
| Days with IC > 0 | 58.3% |

For scale: Qlib's LightGBM/Alpha158 benchmark on CSI300 reports IC 0.045 and Rank IC 0.047 (next-day close-to-close).

## Name-day hit rates (compare with the ledger's hit rate)

| Basket | Hit rate |
|---|---|
| Top-5 longs, share with a positive horizon return | 51.0% |
| Bottom-5 shorts, share with a negative horizon return | 49.1% |
| Top decile longs | 51.0% |
| Bottom decile shorts | 49.1% |
| Base rate: all tradable names with a positive horizon return | 50.9% |

## Horizon-return simulations, net of costs (per $1 of gross exposure)

| Simulation | Days | Mean/day (bps) | Annualized | Sharpe | Hit days | Max DD | t |
|---|---|---|---|---|---|---|---|
| decile_long_short | 252 | -2.0 | -5.0% | -0.322 | 53.6% | -14.5% | -0.32 |
| decile_long_only | 252 | +7.1 | +19.7% | 0.569 | 54.8% | -21.4% | 0.57 |
| top5_long_only | 252 | +21.0 | +69.8% | 0.884 | 54.0% | -37.4% | 0.88 |
| top5_long_bottom5_short | 252 | +4.3 | +11.6% | 0.346 | 50.0% | -19.8% | 0.35 |
| universe_equal_weight_long | 252 | +3.6 | +9.5% | 0.686 | 52.0% | -9.1% | 0.69 |
| spy_same_horizon | 252 | +0.1 | +0.1% | 0.009 | 50.8% | -10.8% | 0.01 |

## Reference: Qlib TopkDropout portfolio backtest (long only, close-to-close)

TopkDropout topk=30 n_drop=3, deal at close, 5+5 bps, benchmark SPY

- Annualized excess return vs SPY: +41.1%
- Information ratio: 1.317
- Max drawdown (excess): -22.7%

## Monthly decile long-short, net

| Month | Return |
|---|---|
| 2025-11 | -0.97% |
| 2025-12 | +1.84% |
| 2026-01 | -0.88% |
| 2026-02 | -1.15% |
| 2026-03 | +1.16% |
| 2026-04 | +3.62% |
| 2026-05 | +4.84% |
| 2026-06 | -4.55% |
| 2026-07 | +2.23% |
| 2026-08 | -2.49% |
| 2026-09 | +2.94% |
| 2026-10 | -5.41% |
| 2026-11 | -6.80% |

_Research output, not investment advice. Survivorship: the universe is current index membership._
