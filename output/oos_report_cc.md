# Out-of-sample report: model `cc` (next session close to the following session's close (Qlib's native one-session hold, includes the overnight))

Validation year; the model never trained on these sessions. Window 2025-10-17 to 2026-10-19, 252 sessions. Target = next session close to the following session's close (Qlib's native one-session hold, includes the overnight) return. Costs = 4 bps round trip, the same as the ledger's simulated fund.

## Signal quality

| Metric | Value |
|---|---|
| IC (mean daily Pearson) | 0.0201 |
| ICIR | 0.097 |
| Rank IC | 0.0172 |
| Rank ICIR | 0.097 |
| Days with IC > 0 | 59.1% |

For scale: Qlib's LightGBM/Alpha158 benchmark on CSI300 reports IC 0.045 and Rank IC 0.047 (next-day close-to-close).

## Name-day hit rates (compare with the ledger's hit rate)

| Basket | Hit rate |
|---|---|
| Top-5 longs, share with a positive horizon return | 52.3% |
| Bottom-5 shorts, share with a negative horizon return | 48.1% |
| Top decile longs | 51.1% |
| Bottom decile shorts | 49.6% |
| Base rate: all tradable names with a positive horizon return | 50.7% |

## Horizon-return simulations, net of costs (per $1 of gross exposure)

| Simulation | Days | Mean/day (bps) | Annualized | Sharpe | Hit days | Max DD | t |
|---|---|---|---|---|---|---|---|
| decile_long_short | 252 | +2.5 | +6.6% | 0.447 | 56.0% | -10.9% | 0.45 |
| decile_long_only | 252 | +13.1 | +38.9% | 1.12 | 55.2% | -16.2% | 1.12 |
| top5_long_only | 252 | +36.6 | +150.9% | 1.653 | 55.2% | -19.5% | 1.65 |
| top5_long_bottom5_short | 252 | +8.5 | +23.8% | 0.749 | 51.6% | -11.1% | 0.75 |
| universe_equal_weight_long | 252 | +2.9 | +7.6% | 0.58 | 51.6% | -9.1% | 0.58 |
| spy_same_horizon | 252 | +2.4 | +6.1% | 0.467 | 51.6% | -11.3% | 0.47 |

## Reference: Qlib TopkDropout portfolio backtest (long only, close-to-close)

TopkDropout topk=30 n_drop=3, deal at close, 5+5 bps, benchmark SPY

- Annualized excess return vs SPY: +25.5%
- Information ratio: 0.836
- Max drawdown (excess): -25.3%

## Monthly decile long-short, net

| Month | Return |
|---|---|
| 2025-10 | +1.43% |
| 2025-11 | -1.20% |
| 2025-12 | +2.13% |
| 2026-01 | -0.34% |
| 2026-02 | -1.35% |
| 2026-03 | +1.03% |
| 2026-04 | +4.13% |
| 2026-05 | +5.01% |
| 2026-06 | -4.62% |
| 2026-07 | +2.25% |
| 2026-08 | -1.73% |
| 2026-09 | +2.86% |
| 2026-10 | -3.71% |

_Research output, not investment advice. Survivorship: the universe is current index membership._
