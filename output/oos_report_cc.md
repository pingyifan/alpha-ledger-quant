# Out-of-sample report: model `cc` (next session close to the following session's close (Qlib's native one-session hold, includes the overnight))

Validation year; the model never trained on these sessions. Window 2025-11-24 to 2026-11-24, 252 sessions. Target = next session close to the following session's close (Qlib's native one-session hold, includes the overnight) return. Costs = 4 bps round trip, the same as the ledger's simulated fund.

## Signal quality

| Metric | Value |
|---|---|
| IC (mean daily Pearson) | 0.0220 |
| ICIR | 0.099 |
| Rank IC | 0.0174 |
| Rank ICIR | 0.091 |
| Days with IC > 0 | 57.5% |

For scale: Qlib's LightGBM/Alpha158 benchmark on CSI300 reports IC 0.045 and Rank IC 0.047 (next-day close-to-close).

## Name-day hit rates (compare with the ledger's hit rate)

| Basket | Hit rate |
|---|---|
| Top-5 longs, share with a positive horizon return | 52.1% |
| Bottom-5 shorts, share with a negative horizon return | 49.2% |
| Top decile longs | 50.8% |
| Bottom decile shorts | 49.5% |
| Base rate: all tradable names with a positive horizon return | 50.8% |

## Horizon-return simulations, net of costs (per $1 of gross exposure)

| Simulation | Days | Mean/day (bps) | Annualized | Sharpe | Hit days | Max DD | t |
|---|---|---|---|---|---|---|---|
| decile_long_short | 252 | +0.0 | +0.1% | 0.005 | 54.4% | -15.9% | 0.0 |
| decile_long_only | 252 | +8.6 | +24.1% | 0.634 | 53.6% | -27.3% | 0.63 |
| top5_long_only | 252 | +28.9 | +106.7% | 1.135 | 54.4% | -35.8% | 1.13 |
| top5_long_bottom5_short | 252 | +11.8 | +34.4% | 0.938 | 53.6% | -20.8% | 0.94 |
| universe_equal_weight_long | 252 | +3.2 | +8.5% | 0.589 | 52.0% | -10.7% | 0.59 |
| spy_same_horizon | 252 | -0.1 | -0.3% | -0.019 | 49.2% | -13.6% | -0.02 |

## Reference: Qlib TopkDropout portfolio backtest (long only, close-to-close)

TopkDropout topk=30 n_drop=3, deal at close, 5+5 bps, benchmark SPY

- Annualized excess return vs SPY: +32.2%
- Information ratio: 0.936
- Max drawdown (excess): -22.9%

## Monthly decile long-short, net

| Month | Return |
|---|---|
| 2025-11 | +1.19% |
| 2025-12 | +1.38% |
| 2026-01 | +0.08% |
| 2026-02 | -1.87% |
| 2026-03 | +0.81% |
| 2026-04 | +3.69% |
| 2026-05 | +5.26% |
| 2026-06 | -4.91% |
| 2026-07 | +1.10% |
| 2026-08 | -2.07% |
| 2026-09 | +3.23% |
| 2026-10 | -6.65% |
| 2026-11 | -1.89% |

_Research output, not investment advice. Survivorship: the universe is current index membership._
