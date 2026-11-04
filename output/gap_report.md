# Gap model (open-aware direction) — data to 2026-11-03

P(open-to-close return beats the day's median) from what is known at the 9:30 open: the overnight gap (raw, vs SPY, vs the stock's ATR), yesterday's move, 5/20/60-day momentum, volume, range position, SPY's gap and momentum, the market's and the sector's median gap, day of week.

## Walk-forward by year (train on earlier years, test on the year shown; tradable names only; before costs)

| year | rows | AUC (vs median) | AUC (abs) | top-3 long / short hit | top-5 long hit / bps | bottom-5 short hit / bps | D10−D1 bps/day |
|---|---|---|---|---|---|---|---|
| 2021 | 216,412 | 0.538 | 0.533 | 0.573 / 0.579 | 0.580 / 25.9 | 0.566 / 31.7 | 36.9 |
| 2022 | 218,784 | 0.524 | 0.523 | 0.509 / 0.551 | 0.523 / -2.1 | 0.550 / 22.7 | 17.5 |
| 2023 | 219,648 | 0.525 | 0.517 | 0.571 / 0.548 | 0.565 / 12.0 | 0.542 / 2.7 | 15.0 |
| 2024 | 224,513 | 0.531 | 0.529 | 0.603 / 0.557 | 0.585 / 26.5 | 0.548 / 14.1 | 17.6 |
| 2025 | 224,141 | 0.532 | 0.524 | 0.595 / 0.593 | 0.595 / 44.6 | 0.564 / 31.7 | 19.1 |
| 2026 | 189,749 | 0.521 | 0.515 | 0.588 / 0.574 | 0.577 / 28.6 | 0.547 / 26.0 | 13.6 |

## Pooled out-of-sample

- p0.55: {'coverage': 0.053, 'n': 68523, 'hit_rate': 0.5502, 'mean_bps': 21.7, 'longs': 37993, 'shorts': 30530}
- p0.57: {'coverage': 0.0088, 'n': 11358, 'hit_rate': 0.5794, 'mean_bps': 45.4, 'longs': 6503, 'shorts': 4855}
- p0.60: {'coverage': 0.0007, 'n': 854, 'hit_rate': 0.6511, 'mean_bps': 86.5, 'longs': 541, 'shorts': 313}
- p0.63: {'coverage': 0.0, 'n': 57, 'hit_rate': 0.7544, 'mean_bps': 265.3, 'longs': 50, 'shorts': 7}
- top3: {'k': 3, 'days': 1466, 'long_hit_rate': 0.5725, 'short_hit_rate': 0.5668, 'long_bps': 20.9, 'short_bps': 27.2, 'ls_bps': 24.0}
- topk: {'k': 5, 'days': 1466, 'long_hit_rate': 0.5707, 'short_hit_rate': 0.5528, 'long_bps': 22.4, 'short_bps': 21.4, 'ls_bps': 21.9}
- top10: {'k': 10, 'days': 1466, 'long_hit_rate': 0.5664, 'short_hit_rate': 0.5472, 'long_bps': 21.4, 'short_bps': 17.6, 'ls_bps': 19.5}
- decile_spread_bps: 20.0
- auc_rel: 0.5289
- base_up_rate: 0.5048
- accuracy_at_half: 0.5173
- auc: 0.524

## Calibration (out of sample): predicted P(up) bin -> observed up rate

| bin | n | mean p | up rate |
|---|---|---|---|
| 0.00–0.40 | 313 | 0.391 | 0.390 |
| 0.40–0.45 | 30,217 | 0.440 | 0.464 |
| 0.45–0.48 | 286,606 | 0.469 | 0.481 |
| 0.48–0.50 | 376,261 | 0.490 | 0.496 |
| 0.50–0.52 | 331,885 | 0.509 | 0.514 |
| 0.52–0.55 | 229,972 | 0.532 | 0.532 |
| 0.55–0.60 | 37,452 | 0.561 | 0.560 |
| 0.60–1.00 | 541 | 0.613 | 0.675 |

Gate: pooled walk-forward top-5 long hit rate >= 0.55 AND top-5 short hit rate >= 0.53 AND long-short >= +10 bps/day before costs, and the latest test year's top-5 long >= 0.53 → **PASS**

Top features by gain: sector_gap_med (27241), gap_idio (26921), gap_z (16564), sector_id (13461), mkt_gap_med (13416), spy_gap (11583), spy_mom5 (10508), gap (9856)
