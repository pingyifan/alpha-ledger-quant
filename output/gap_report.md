# Gap model (open-aware direction) — data to 2026-11-17

P(open-to-close return beats the day's median) from what is known at the 9:30 open: the overnight gap (raw, vs SPY, vs the stock's ATR), yesterday's move, 5/20/60-day momentum, volume, range position, SPY's gap and momentum, the market's and the sector's median gap, day of week.

## Walk-forward by year (train on earlier years, test on the year shown; tradable names only; before costs)

| year | rows | AUC (vs median) | AUC (abs) | top-3 long / short hit | top-5 long hit / bps | bottom-5 short hit / bps | D10−D1 bps/day |
|---|---|---|---|---|---|---|---|
| 2021 | 215,404 | 0.537 | 0.530 | 0.574 / 0.594 | 0.579 / 28.6 | 0.576 / 46.7 | 37.6 |
| 2022 | 217,780 | 0.522 | 0.527 | 0.519 / 0.558 | 0.538 / 3.0 | 0.553 / 23.1 | 13.2 |
| 2023 | 218,648 | 0.526 | 0.517 | 0.567 / 0.552 | 0.562 / 13.2 | 0.542 / 5.8 | 14.8 |
| 2024 | 223,521 | 0.530 | 0.527 | 0.606 / 0.540 | 0.589 / 31.7 | 0.548 / 10.7 | 16.2 |
| 2025 | 223,336 | 0.532 | 0.522 | 0.585 / 0.596 | 0.578 / 31.5 | 0.582 / 33.6 | 18.1 |
| 2026 | 198,096 | 0.521 | 0.518 | 0.582 / 0.590 | 0.567 / 22.2 | 0.567 / 22.4 | 15.1 |

## Pooled out-of-sample

- p0.55: {'coverage': 0.0636, 'n': 82530, 'hit_rate': 0.5454, 'mean_bps': 18.9, 'longs': 44634, 'shorts': 37896}
- p0.57: {'coverage': 0.0138, 'n': 17882, 'hit_rate': 0.5569, 'mean_bps': 32.5, 'longs': 9288, 'shorts': 8594}
- p0.60: {'coverage': 0.002, 'n': 2531, 'hit_rate': 0.5899, 'mean_bps': 53.1, 'longs': 1180, 'shorts': 1351}
- p0.63: {'coverage': 0.0002, 'n': 268, 'hit_rate': 0.6381, 'mean_bps': 110.6, 'longs': 136, 'shorts': 132}
- top3: {'k': 3, 'days': 1476, 'long_hit_rate': 0.572, 'short_hit_rate': 0.5711, 'long_bps': 24.6, 'short_bps': 27.3, 'ls_bps': 26.0}
- topk: {'k': 5, 'days': 1476, 'long_hit_rate': 0.5686, 'short_hit_rate': 0.5614, 'long_bps': 21.7, 'short_bps': 23.7, 'ls_bps': 22.7}
- top10: {'k': 10, 'days': 1476, 'long_hit_rate': 0.5639, 'short_hit_rate': 0.5479, 'long_bps': 18.9, 'short_bps': 18.5, 'ls_bps': 18.7}
- decile_spread_bps: 19.2
- auc_rel: 0.528
- base_up_rate: 0.5043
- accuracy_at_half: 0.5171
- auc: 0.5236

## Calibration (out of sample): predicted P(up) bin -> observed up rate

| bin | n | mean p | up rate |
|---|---|---|---|
| 0.00–0.40 | 1,351 | 0.387 | 0.429 |
| 0.40–0.45 | 36,545 | 0.438 | 0.471 |
| 0.45–0.48 | 289,048 | 0.469 | 0.481 |
| 0.48–0.50 | 361,993 | 0.490 | 0.495 |
| 0.50–0.52 | 324,175 | 0.509 | 0.512 |
| 0.52–0.55 | 239,039 | 0.532 | 0.531 |
| 0.55–0.60 | 43,454 | 0.562 | 0.557 |
| 0.60–1.00 | 1,180 | 0.614 | 0.611 |

Gate: pooled walk-forward top-5 long hit rate >= 0.55 AND top-5 short hit rate >= 0.53 AND long-short >= +10 bps/day before costs, and the latest test year's top-5 long >= 0.53 → **PASS**

Top features by gain: gap_idio (27060), sector_gap_med (25639), gap_z (17034), mkt_gap_med (14035), sector_id (13027), spy_gap (11299), spy_cc_prev (11105), gap (9186)
