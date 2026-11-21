# Gap model (open-aware direction) — data to 2026-11-20

P(open-to-close return beats the day's median) from what is known at the 9:30 open: the overnight gap (raw, vs SPY, vs the stock's ATR), yesterday's move, 5/20/60-day momentum, volume, range position, SPY's gap and momentum, the market's and the sector's median gap, day of week.

## Walk-forward by year (train on earlier years, test on the year shown; tradable names only; before costs)

| year | rows | AUC (vs median) | AUC (abs) | top-3 long / short hit | top-5 long hit / bps | bottom-5 short hit / bps | D10−D1 bps/day |
|---|---|---|---|---|---|---|---|
| 2021 | 215,908 | 0.539 | 0.530 | 0.570 / 0.597 | 0.569 / 20.8 | 0.573 / 36.3 | 38.1 |
| 2022 | 218,282 | 0.523 | 0.524 | 0.523 / 0.562 | 0.527 / -5.2 | 0.551 / 25.1 | 14.9 |
| 2023 | 219,148 | 0.524 | 0.516 | 0.573 / 0.543 | 0.558 / 8.5 | 0.538 / 7.1 | 13.3 |
| 2024 | 224,025 | 0.530 | 0.526 | 0.601 / 0.549 | 0.591 / 24.7 | 0.547 / 13.3 | 16.4 |
| 2025 | 223,902 | 0.530 | 0.524 | 0.589 / 0.599 | 0.582 / 31.5 | 0.574 / 23.2 | 19.2 |
| 2026 | 201,461 | 0.521 | 0.519 | 0.600 / 0.595 | 0.582 / 23.3 | 0.577 / 33.1 | 16.9 |

## Pooled out-of-sample

- p0.55: {'coverage': 0.0537, 'n': 69920, 'hit_rate': 0.5459, 'mean_bps': 20.1, 'longs': 37999, 'shorts': 31921}
- p0.57: {'coverage': 0.0092, 'n': 12021, 'hit_rate': 0.5732, 'mean_bps': 44.1, 'longs': 6564, 'shorts': 5457}
- p0.60: {'coverage': 0.0007, 'n': 928, 'hit_rate': 0.6584, 'mean_bps': 113.8, 'longs': 519, 'shorts': 409}
- p0.63: {'coverage': 0.0, 'n': 46, 'hit_rate': 0.7391, 'mean_bps': 214.4, 'longs': 30, 'shorts': 16}
- top3: {'k': 3, 'days': 1479, 'long_hit_rate': 0.5756, 'short_hit_rate': 0.5736, 'long_bps': 17.3, 'short_bps': 29.6, 'ls_bps': 23.5}
- topk: {'k': 5, 'days': 1479, 'long_hit_rate': 0.5678, 'short_hit_rate': 0.5597, 'long_bps': 17.2, 'short_bps': 22.8, 'ls_bps': 20.0}
- top10: {'k': 10, 'days': 1479, 'long_hit_rate': 0.5652, 'short_hit_rate': 0.5508, 'long_bps': 20.4, 'short_bps': 19.0, 'ls_bps': 19.7}
- decile_spread_bps: 19.8
- auc_rel: 0.5283
- base_up_rate: 0.5038
- accuracy_at_half: 0.5164
- auc: 0.5234

## Calibration (out of sample): predicted P(up) bin -> observed up rate

| bin | n | mean p | up rate |
|---|---|---|---|
| 0.00–0.40 | 409 | 0.391 | 0.333 |
| 0.40–0.45 | 31,512 | 0.439 | 0.465 |
| 0.45–0.48 | 291,687 | 0.469 | 0.481 |
| 0.48–0.50 | 374,800 | 0.490 | 0.496 |
| 0.50–0.52 | 330,680 | 0.509 | 0.511 |
| 0.52–0.55 | 235,639 | 0.532 | 0.531 |
| 0.55–0.60 | 37,480 | 0.561 | 0.552 |
| 0.60–1.00 | 519 | 0.610 | 0.651 |

Gate: pooled walk-forward top-5 long hit rate >= 0.55 AND top-5 short hit rate >= 0.53 AND long-short >= +10 bps/day before costs, and the latest test year's top-5 long >= 0.53 → **PASS**

Top features by gain: gap_idio (27554), sector_gap_med (27099), gap_z (17425), mkt_gap_med (15209), sector_id (14949), spy_gap (13298), spy_cc_prev (10439), spy_mom5 (9898)
