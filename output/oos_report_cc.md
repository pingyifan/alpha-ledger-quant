# Out-of-sample report: model `cc` (next session close to the following session's close (Qlib's native one-session hold, includes the overnight))

Validation year; the model never trained on these sessions. Window 2025-10-13 to 2026-10-13, 252 sessions. Target = next session close to the following session's close (Qlib's native one-session hold, includes the overnight) return. Costs = 4 bps round trip, the same as the ledger's simulated fund.

## Signal quality

| Metric | Value |
|---|---|
| IC (mean daily Pearson) | 0.0216 |
| ICIR | 0.107 |
| Rank IC | 0.0178 |
| Rank ICIR | 0.103 |
| Days with IC > 0 | 58.7% |

For scale: Qlib's LightGBM/Alpha158 benchmark on CSI300 reports IC 0.045 and Rank IC 0.047 (next-day close-to-close).

## Name-day hit rates (compare with the ledger's hit rate)

| Basket | Hit rate |
|---|---|
| Top-5 longs, share with a positive horizon return | 53.0% |
| Bottom-5 shorts, share with a negative horizon return | 48.0% |
| Top decile longs | 50.8% |
| Bottom decile shorts | 49.4% |
| Base rate: all tradable names with a positive horizon return | 50.7% |

## Horizon-return simulations, net of costs (per $1 of gross exposure)

| Simulation | Days | Mean/day (bps) | Annualized | Sharpe | Hit days | Max DD | t |
|---|---|---|---|---|---|---|---|
| decile_long_short | 252 | +1.2 | +3.1% | 0.221 | 55.2% | -11.0% | 0.22 |
| decile_long_only | 252 | +10.6 | +30.5% | 0.926 | 54.8% | -16.5% | 0.93 |
| top5_long_only | 252 | +41.3 | +182.7% | 1.884 | 54.0% | -19.9% | 1.88 |
| top5_long_bottom5_short | 252 | +15.3 | +47.1% | 1.37 | 50.8% | -11.2% | 1.37 |
| universe_equal_weight_long | 252 | +2.9 | +7.6% | 0.58 | 52.0% | -9.1% | 0.58 |
| spy_same_horizon | 252 | +2.8 | +7.4% | 0.561 | 51.6% | -11.3% | 0.56 |

## Reference: Qlib TopkDropout portfolio backtest (long only, close-to-close)

TopkDropout topk=30 n_drop=3, deal at close, 5+5 bps, benchmark SPY

- Annualized excess return vs SPY: +43.1%
- Information ratio: 1.482
- Max drawdown (excess): -20.7%

## Monthly decile long-short, net

| Month | Return |
|---|---|
| 2025-10 | +1.84% |
| 2025-11 | -1.49% |
| 2025-12 | +2.23% |
| 2026-01 | -0.88% |
| 2026-02 | -2.00% |
| 2026-03 | +0.39% |
| 2026-04 | +3.48% |
| 2026-05 | +3.54% |
| 2026-06 | -4.54% |
| 2026-07 | +2.26% |
| 2026-08 | -1.56% |
| 2026-09 | +2.38% |
| 2026-10 | -3.12% |

_Research output, not investment advice. Survivorship: the universe is current index membership._
