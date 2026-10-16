# Out-of-sample report: model `cc` (next session close to the following session's close (Qlib's native one-session hold, includes the overnight))

Validation year; the model never trained on these sessions. Window 2025-10-13 to 2026-10-13, 252 sessions. Target = next session close to the following session's close (Qlib's native one-session hold, includes the overnight) return. Costs = 4 bps round trip, the same as the ledger's simulated fund.

## Signal quality

| Metric | Value |
|---|---|
| IC (mean daily Pearson) | 0.0208 |
| ICIR | 0.104 |
| Rank IC | 0.0182 |
| Rank ICIR | 0.106 |
| Days with IC > 0 | 58.7% |

For scale: Qlib's LightGBM/Alpha158 benchmark on CSI300 reports IC 0.045 and Rank IC 0.047 (next-day close-to-close).

## Name-day hit rates (compare with the ledger's hit rate)

| Basket | Hit rate |
|---|---|
| Top-5 longs, share with a positive horizon return | 52.9% |
| Bottom-5 shorts, share with a negative horizon return | 46.0% |
| Top decile longs | 51.0% |
| Bottom decile shorts | 49.3% |
| Base rate: all tradable names with a positive horizon return | 50.7% |

## Horizon-return simulations, net of costs (per $1 of gross exposure)

| Simulation | Days | Mean/day (bps) | Annualized | Sharpe | Hit days | Max DD | t |
|---|---|---|---|---|---|---|---|
| decile_long_short | 252 | +2.2 | +5.7% | 0.406 | 53.6% | -10.8% | 0.41 |
| decile_long_only | 252 | +12.3 | +36.3% | 1.081 | 54.8% | -15.4% | 1.08 |
| top5_long_only | 252 | +38.0 | +159.8% | 1.659 | 56.4% | -18.7% | 1.66 |
| top5_long_bottom5_short | 252 | +5.9 | +16.1% | 0.523 | 49.6% | -13.8% | 0.52 |
| universe_equal_weight_long | 252 | +2.9 | +7.5% | 0.574 | 52.0% | -9.1% | 0.57 |
| spy_same_horizon | 252 | +2.8 | +7.4% | 0.561 | 51.6% | -11.3% | 0.56 |

## Reference: Qlib TopkDropout portfolio backtest (long only, close-to-close)

TopkDropout topk=30 n_drop=3, deal at close, 5+5 bps, benchmark SPY

- Annualized excess return vs SPY: +43.8%
- Information ratio: 1.462
- Max drawdown (excess): -21.8%

## Monthly decile long-short, net

| Month | Return |
|---|---|
| 2025-10 | +1.92% |
| 2025-11 | -1.21% |
| 2025-12 | +1.67% |
| 2026-01 | -0.64% |
| 2026-02 | -0.97% |
| 2026-03 | +0.59% |
| 2026-04 | +4.09% |
| 2026-05 | +4.04% |
| 2026-06 | -4.14% |
| 2026-07 | +1.93% |
| 2026-08 | -1.78% |
| 2026-09 | +2.37% |
| 2026-10 | -2.84% |

_Research output, not investment advice. Survivorship: the universe is current index membership._
