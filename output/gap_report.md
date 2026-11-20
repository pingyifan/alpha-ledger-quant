# Gap model (open-aware direction) — data to 2026-11-19

P(open-to-close return beats the day's median) from what is known at the 9:30 open: the overnight gap (raw, vs SPY, vs the stock's ATR), yesterday's move, 5/20/60-day momentum, volume, range position, SPY's gap and momentum, the market's and the sector's median gap, day of week.

## Walk-forward by year (train on earlier years, test on the year shown; tradable names only; before costs)

| year | rows | AUC (vs median) | AUC (abs) | top-3 long / short hit | top-5 long hit / bps | bottom-5 short hit / bps | D10−D1 bps/day |
|---|---|---|---|---|---|---|---|
| 2021 | 215,656 | 0.537 | 0.531 | 0.570 / 0.575 | 0.581 / 29.5 | 0.569 / 32.2 | 36.5 |
| 2022 | 218,031 | 0.524 | 0.527 | 0.536 / 0.571 | 0.538 / 5.1 | 0.548 / 20.5 | 15.2 |
| 2023 | 218,898 | 0.525 | 0.517 | 0.585 / 0.519 | 0.579 / 16.6 | 0.520 / -0.5 | 14.2 |
| 2024 | 223,773 | 0.530 | 0.527 | 0.610 / 0.553 | 0.591 / 28.0 | 0.544 / 14.5 | 16.7 |
| 2025 | 223,652 | 0.531 | 0.524 | 0.595 / 0.561 | 0.587 / 36.2 | 0.562 / 26.3 | 16.6 |
| 2026 | 200,155 | 0.523 | 0.517 | 0.604 / 0.607 | 0.593 / 33.6 | 0.587 / 31.3 | 17.1 |

## Pooled out-of-sample

- p0.55: {'coverage': 0.0588, 'n': 76478, 'hit_rate': 0.5453, 'mean_bps': 19.9, 'longs': 42173, 'shorts': 34305}
- p0.57: {'coverage': 0.0117, 'n': 15266, 'hit_rate': 0.5601, 'mean_bps': 32.0, 'longs': 8456, 'shorts': 6810}
- p0.60: {'coverage': 0.0013, 'n': 1655, 'hit_rate': 0.6157, 'mean_bps': 63.6, 'longs': 926, 'shorts': 729}
- p0.63: {'coverage': 0.0001, 'n': 145, 'hit_rate': 0.6138, 'mean_bps': 108.2, 'longs': 89, 'shorts': 56}
- top3: {'k': 3, 'days': 1478, 'long_hit_rate': 0.583, 'short_hit_rate': 0.5636, 'long_bps': 26.5, 'short_bps': 23.8, 'ls_bps': 25.1}
- topk: {'k': 5, 'days': 1478, 'long_hit_rate': 0.5778, 'short_hit_rate': 0.5545, 'long_bps': 24.7, 'short_bps': 20.5, 'ls_bps': 22.6}
- top10: {'k': 10, 'days': 1478, 'long_hit_rate': 0.5681, 'short_hit_rate': 0.5473, 'long_bps': 20.8, 'short_bps': 18.8, 'ls_bps': 19.8}
- decile_spread_bps: 19.4
- auc_rel: 0.5285
- base_up_rate: 0.5041
- accuracy_at_half: 0.5169
- auc: 0.5239

## Calibration (out of sample): predicted P(up) bin -> observed up rate

| bin | n | mean p | up rate |
|---|---|---|---|
| 0.00–0.40 | 729 | 0.388 | 0.401 |
| 0.40–0.45 | 33,576 | 0.439 | 0.471 |
| 0.45–0.48 | 288,244 | 0.469 | 0.480 |
| 0.48–0.50 | 370,278 | 0.490 | 0.496 |
| 0.50–0.52 | 329,218 | 0.509 | 0.511 |
| 0.52–0.55 | 235,947 | 0.532 | 0.532 |
| 0.55–0.60 | 41,247 | 0.561 | 0.556 |
| 0.60–1.00 | 926 | 0.613 | 0.628 |

Gate: pooled walk-forward top-5 long hit rate >= 0.55 AND top-5 short hit rate >= 0.53 AND long-short >= +10 bps/day before costs, and the latest test year's top-5 long >= 0.53 → **PASS**

Top features by gain: sector_gap_med (27322), gap_idio (27145), gap_z (16544), mkt_gap_med (16175), sector_id (14635), spy_gap (11908), spy_cc_prev (11483), spy_mom5 (10052)
