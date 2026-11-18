# Out-of-sample report: model `cc` (next session close to the following session's close (Qlib's native one-session hold, includes the overnight))

Validation year; the model never trained on these sessions. Window 2025-11-13 to 2026-11-13, 252 sessions. Target = next session close to the following session's close (Qlib's native one-session hold, includes the overnight) return. Costs = 4 bps round trip, the same as the ledger's simulated fund.

## Signal quality

| Metric | Value |
|---|---|
| IC (mean daily Pearson) | 0.0201 |
| ICIR | 0.093 |
| Rank IC | 0.0177 |
| Rank ICIR | 0.095 |
| Days with IC > 0 | 57.5% |

For scale: Qlib's LightGBM/Alpha158 benchmark on CSI300 reports IC 0.045 and Rank IC 0.047 (next-day close-to-close).

## Name-day hit rates (compare with the ledger's hit rate)

| Basket | Hit rate |
|---|---|
| Top-5 longs, share with a positive horizon return | 53.1% |
| Bottom-5 shorts, share with a negative horizon return | 48.4% |
| Top decile longs | 51.1% |
| Bottom decile shorts | 49.2% |
| Base rate: all tradable names with a positive horizon return | 50.7% |

## Horizon-return simulations, net of costs (per $1 of gross exposure)

| Simulation | Days | Mean/day (bps) | Annualized | Sharpe | Hit days | Max DD | t |
|---|---|---|---|---|---|---|---|
| decile_long_short | 252 | -1.1 | -2.7% | -0.168 | 51.6% | -16.9% | -0.17 |
| decile_long_only | 252 | +8.0 | +22.2% | 0.62 | 53.6% | -24.6% | 0.62 |
| top5_long_only | 252 | +45.9 | +216.9% | 1.884 | 54.0% | -30.4% | 1.88 |
| top5_long_bottom5_short | 252 | +14.6 | +44.6% | 1.177 | 52.0% | -14.6% | 1.18 |
| universe_equal_weight_long | 252 | +3.3 | +8.7% | 0.615 | 51.2% | -9.1% | 0.61 |
| spy_same_horizon | 252 | +0.2 | +0.6% | 0.041 | 50.0% | -10.8% | 0.04 |

## Reference: Qlib TopkDropout portfolio backtest (long only, close-to-close)

TopkDropout topk=30 n_drop=3, deal at close, 5+5 bps, benchmark SPY

- Annualized excess return vs SPY: +40.5%
- Information ratio: 1.261
- Max drawdown (excess): -22.7%

## Monthly decile long-short, net

| Month | Return |
|---|---|
| 2025-11 | +0.76% |
| 2025-12 | +1.52% |
| 2026-01 | -0.05% |
| 2026-02 | -1.65% |
| 2026-03 | +1.09% |
| 2026-04 | +3.30% |
| 2026-05 | +4.68% |
| 2026-06 | -5.00% |
| 2026-07 | +0.98% |
| 2026-08 | -2.97% |
| 2026-09 | +2.21% |
| 2026-10 | -5.19% |
| 2026-11 | -3.09% |

_Research output, not investment advice. Survivorship: the universe is current index membership._
