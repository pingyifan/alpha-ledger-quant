# Out-of-sample report: model `cc` (next session close to the following session's close (Qlib's native one-session hold, includes the overnight))

Validation year; the model never trained on these sessions. Window 2025-11-14 to 2026-11-16, 252 sessions. Target = next session close to the following session's close (Qlib's native one-session hold, includes the overnight) return. Costs = 4 bps round trip, the same as the ledger's simulated fund.

## Signal quality

| Metric | Value |
|---|---|
| IC (mean daily Pearson) | 0.0197 |
| ICIR | 0.092 |
| Rank IC | 0.0184 |
| Rank ICIR | 0.100 |
| Days with IC > 0 | 57.1% |

For scale: Qlib's LightGBM/Alpha158 benchmark on CSI300 reports IC 0.045 and Rank IC 0.047 (next-day close-to-close).

## Name-day hit rates (compare with the ledger's hit rate)

| Basket | Hit rate |
|---|---|
| Top-5 longs, share with a positive horizon return | 52.1% |
| Bottom-5 shorts, share with a negative horizon return | 47.6% |
| Top decile longs | 50.9% |
| Bottom decile shorts | 49.3% |
| Base rate: all tradable names with a positive horizon return | 50.9% |

## Horizon-return simulations, net of costs (per $1 of gross exposure)

| Simulation | Days | Mean/day (bps) | Annualized | Sharpe | Hit days | Max DD | t |
|---|---|---|---|---|---|---|---|
| decile_long_short | 252 | -0.1 | -0.1% | -0.008 | 53.6% | -14.9% | -0.01 |
| decile_long_only | 252 | +8.3 | +23.3% | 0.661 | 52.8% | -22.5% | 0.66 |
| top5_long_only | 252 | +23.6 | +81.0% | 1.013 | 53.2% | -35.0% | 1.01 |
| top5_long_bottom5_short | 252 | +4.1 | +10.9% | 0.335 | 52.0% | -23.6% | 0.34 |
| universe_equal_weight_long | 252 | +4.0 | +10.5% | 0.747 | 51.6% | -9.2% | 0.75 |
| spy_same_horizon | 252 | +0.5 | +1.2% | 0.087 | 50.0% | -10.8% | 0.09 |

## Reference: Qlib TopkDropout portfolio backtest (long only, close-to-close)

TopkDropout topk=30 n_drop=3, deal at close, 5+5 bps, benchmark SPY

- Annualized excess return vs SPY: +33.4%
- Information ratio: 1.053
- Max drawdown (excess): -23.7%

## Monthly decile long-short, net

| Month | Return |
|---|---|
| 2025-11 | +1.40% |
| 2025-12 | +1.69% |
| 2026-01 | -0.12% |
| 2026-02 | -1.49% |
| 2026-03 | +1.42% |
| 2026-04 | +3.58% |
| 2026-05 | +4.21% |
| 2026-06 | -5.41% |
| 2026-07 | +2.33% |
| 2026-08 | -1.74% |
| 2026-09 | +2.41% |
| 2026-10 | -5.97% |
| 2026-11 | -2.98% |

_Research output, not investment advice. Survivorship: the universe is current index membership._
