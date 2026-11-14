# Out-of-sample report: model `cc` (next session close to the following session's close (Qlib's native one-session hold, includes the overnight))

Validation year; the model never trained on these sessions. Window 2025-11-11 to 2026-11-11, 252 sessions. Target = next session close to the following session's close (Qlib's native one-session hold, includes the overnight) return. Costs = 4 bps round trip, the same as the ledger's simulated fund.

## Signal quality

| Metric | Value |
|---|---|
| IC (mean daily Pearson) | 0.0197 |
| ICIR | 0.090 |
| Rank IC | 0.0186 |
| Rank ICIR | 0.099 |
| Days with IC > 0 | 58.7% |

For scale: Qlib's LightGBM/Alpha158 benchmark on CSI300 reports IC 0.045 and Rank IC 0.047 (next-day close-to-close).

## Name-day hit rates (compare with the ledger's hit rate)

| Basket | Hit rate |
|---|---|
| Top-5 longs, share with a positive horizon return | 52.1% |
| Bottom-5 shorts, share with a negative horizon return | 50.1% |
| Top decile longs | 50.9% |
| Bottom decile shorts | 49.1% |
| Base rate: all tradable names with a positive horizon return | 50.8% |

## Horizon-return simulations, net of costs (per $1 of gross exposure)

| Simulation | Days | Mean/day (bps) | Annualized | Sharpe | Hit days | Max DD | t |
|---|---|---|---|---|---|---|---|
| decile_long_short | 252 | -1.1 | -2.8% | -0.177 | 54.8% | -15.0% | -0.18 |
| decile_long_only | 252 | +8.4 | +23.5% | 0.654 | 54.0% | -23.3% | 0.65 |
| top5_long_only | 252 | +23.4 | +80.0% | 0.987 | 54.8% | -35.8% | 0.99 |
| top5_long_bottom5_short | 252 | +8.0 | +22.4% | 0.645 | 52.8% | -19.3% | 0.64 |
| universe_equal_weight_long | 252 | +3.7 | +9.7% | 0.691 | 51.2% | -9.1% | 0.69 |
| spy_same_horizon | 252 | +0.7 | +1.8% | 0.133 | 50.0% | -10.8% | 0.13 |

## Reference: Qlib TopkDropout portfolio backtest (long only, close-to-close)

TopkDropout topk=30 n_drop=3, deal at close, 5+5 bps, benchmark SPY

- Annualized excess return vs SPY: +37.8%
- Information ratio: 1.151
- Max drawdown (excess): -24.7%

## Monthly decile long-short, net

| Month | Return |
|---|---|
| 2025-11 | -0.61% |
| 2025-12 | +1.74% |
| 2026-01 | -0.88% |
| 2026-02 | -0.99% |
| 2026-03 | +0.79% |
| 2026-04 | +2.42% |
| 2026-05 | +4.08% |
| 2026-06 | -4.27% |
| 2026-07 | +1.55% |
| 2026-08 | -1.16% |
| 2026-09 | +2.78% |
| 2026-10 | -6.42% |
| 2026-11 | -2.66% |

_Research output, not investment advice. Survivorship: the universe is current index membership._
