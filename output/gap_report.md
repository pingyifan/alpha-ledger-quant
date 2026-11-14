# Gap model (open-aware direction) — data to 2026-11-13

P(open-to-close return beats the day's median) from what is known at the 9:30 open: the overnight gap (raw, vs SPY, vs the stock's ATR), yesterday's move, 5/20/60-day momentum, volume, range position, SPY's gap and momentum, the market's and the sector's median gap, day of week.

## Walk-forward by year (train on earlier years, test on the year shown; tradable names only; before costs)

| year | rows | AUC (vs median) | AUC (abs) | top-3 long / short hit | top-5 long hit / bps | bottom-5 short hit / bps | D10−D1 bps/day |
|---|---|---|---|---|---|---|---|
| 2021 | 216,160 | 0.538 | 0.530 | 0.570 / 0.601 | 0.584 / 29.8 | 0.579 / 51.5 | 38.6 |
| 2022 | 218,533 | 0.524 | 0.527 | 0.530 / 0.575 | 0.526 / 1.0 | 0.560 / 28.4 | 18.1 |
| 2023 | 219,398 | 0.524 | 0.516 | 0.568 / 0.543 | 0.562 / 14.8 | 0.537 / 7.2 | 14.4 |
| 2024 | 224,277 | 0.531 | 0.527 | 0.622 / 0.561 | 0.592 / 24.0 | 0.550 / 19.0 | 16.7 |
| 2025 | 224,086 | 0.532 | 0.525 | 0.607 / 0.587 | 0.588 / 38.2 | 0.565 / 27.4 | 19.0 |
| 2026 | 196,957 | 0.523 | 0.518 | 0.563 / 0.580 | 0.577 / 21.8 | 0.558 / 29.3 | 13.1 |

## Pooled out-of-sample

- p0.55: {'coverage': 0.0668, 'n': 86776, 'hit_rate': 0.5433, 'mean_bps': 18.3, 'longs': 46411, 'shorts': 40365}
- p0.57: {'coverage': 0.0161, 'n': 20947, 'hit_rate': 0.5586, 'mean_bps': 31.0, 'longs': 10757, 'shorts': 10190}
- p0.60: {'coverage': 0.0024, 'n': 3121, 'hit_rate': 0.587, 'mean_bps': 53.2, 'longs': 1561, 'shorts': 1560}
- p0.63: {'coverage': 0.0003, 'n': 409, 'hit_rate': 0.6455, 'mean_bps': 95.8, 'longs': 207, 'shorts': 202}
- top3: {'k': 3, 'days': 1474, 'long_hit_rate': 0.5769, 'short_hit_rate': 0.5742, 'long_bps': 23.1, 'short_bps': 33.3, 'ls_bps': 28.2}
- topk: {'k': 5, 'days': 1474, 'long_hit_rate': 0.5715, 'short_hit_rate': 0.5582, 'long_bps': 21.6, 'short_bps': 27.1, 'ls_bps': 24.4}
- top10: {'k': 10, 'days': 1474, 'long_hit_rate': 0.5678, 'short_hit_rate': 0.5488, 'long_bps': 22.0, 'short_bps': 20.1, 'ls_bps': 21.0}
- decile_spread_bps: 20.0
- auc_rel: 0.5288
- base_up_rate: 0.5047
- accuracy_at_half: 0.5174
- auc: 0.5242

## Calibration (out of sample): predicted P(up) bin -> observed up rate

| bin | n | mean p | up rate |
|---|---|---|---|
| 0.00–0.40 | 1,560 | 0.385 | 0.435 |
| 0.40–0.45 | 38,805 | 0.437 | 0.473 |
| 0.45–0.48 | 291,370 | 0.469 | 0.481 |
| 0.48–0.50 | 359,717 | 0.490 | 0.496 |
| 0.50–0.52 | 322,803 | 0.509 | 0.512 |
| 0.52–0.55 | 238,745 | 0.532 | 0.533 |
| 0.55–0.60 | 44,850 | 0.562 | 0.554 |
| 0.60–1.00 | 1,561 | 0.615 | 0.609 |

Gate: pooled walk-forward top-5 long hit rate >= 0.55 AND top-5 short hit rate >= 0.53 AND long-short >= +10 bps/day before costs, and the latest test year's top-5 long >= 0.53 → **PASS**

Top features by gain: sector_gap_med (28726), gap_idio (27298), gap_z (16534), sector_id (15554), mkt_gap_med (14759), spy_gap (13880), spy_cc_prev (12269), spy_mom5 (10637)
