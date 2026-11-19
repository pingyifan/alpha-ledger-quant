# Gap model (open-aware direction) — data to 2026-11-18

P(open-to-close return beats the day's median) from what is known at the 9:30 open: the overnight gap (raw, vs SPY, vs the stock's ATR), yesterday's move, 5/20/60-day momentum, volume, range position, SPY's gap and momentum, the market's and the sector's median gap, day of week.

## Walk-forward by year (train on earlier years, test on the year shown; tradable names only; before costs)

| year | rows | AUC (vs median) | AUC (abs) | top-3 long / short hit | top-5 long hit / bps | bottom-5 short hit / bps | D10−D1 bps/day |
|---|---|---|---|---|---|---|---|
| 2021 | 215,908 | 0.539 | 0.532 | 0.577 / 0.586 | 0.585 / 33.7 | 0.582 / 41.7 | 36.4 |
| 2022 | 218,282 | 0.522 | 0.524 | 0.544 / 0.559 | 0.547 / 2.9 | 0.537 / 14.4 | 15.0 |
| 2023 | 219,148 | 0.524 | 0.517 | 0.580 / 0.540 | 0.573 / 14.9 | 0.533 / 9.3 | 14.2 |
| 2024 | 224,025 | 0.530 | 0.527 | 0.599 / 0.556 | 0.580 / 21.7 | 0.552 / 11.8 | 16.5 |
| 2025 | 223,754 | 0.531 | 0.523 | 0.591 / 0.561 | 0.576 / 31.6 | 0.578 / 25.3 | 17.3 |
| 2026 | 199,438 | 0.521 | 0.518 | 0.581 / 0.578 | 0.571 / 25.2 | 0.579 / 35.2 | 14.7 |

## Pooled out-of-sample

- p0.55: {'coverage': 0.0627, 'n': 81512, 'hit_rate': 0.545, 'mean_bps': 19.8, 'longs': 44771, 'shorts': 36741}
- p0.57: {'coverage': 0.0123, 'n': 16028, 'hit_rate': 0.5637, 'mean_bps': 40.6, 'longs': 8929, 'shorts': 7099}
- p0.60: {'coverage': 0.0012, 'n': 1506, 'hit_rate': 0.6069, 'mean_bps': 83.3, 'longs': 825, 'shorts': 681}
- p0.63: {'coverage': 0.0001, 'n': 78, 'hit_rate': 0.6795, 'mean_bps': 165.2, 'longs': 55, 'shorts': 23}
- top3: {'k': 3, 'days': 1477, 'long_hit_rate': 0.5787, 'short_hit_rate': 0.5631, 'long_bps': 23.7, 'short_bps': 25.2, 'ls_bps': 24.5}
- topk: {'k': 5, 'days': 1477, 'long_hit_rate': 0.5721, 'short_hit_rate': 0.5598, 'long_bps': 21.6, 'short_bps': 22.7, 'ls_bps': 22.2}
- top10: {'k': 10, 'days': 1477, 'long_hit_rate': 0.5667, 'short_hit_rate': 0.5466, 'long_bps': 21.3, 'short_bps': 18.1, 'ls_bps': 19.7}
- decile_spread_bps: 19.0
- auc_rel: 0.528
- base_up_rate: 0.5044
- accuracy_at_half: 0.5169
- auc: 0.5239

## Calibration (out of sample): predicted P(up) bin -> observed up rate

| bin | n | mean p | up rate |
|---|---|---|---|
| 0.00–0.40 | 681 | 0.389 | 0.410 |
| 0.40–0.45 | 36,060 | 0.439 | 0.473 |
| 0.45–0.48 | 295,385 | 0.469 | 0.481 |
| 0.48–0.50 | 364,689 | 0.490 | 0.496 |
| 0.50–0.52 | 321,366 | 0.509 | 0.512 |
| 0.52–0.55 | 237,603 | 0.532 | 0.531 |
| 0.55–0.60 | 43,946 | 0.562 | 0.558 |
| 0.60–1.00 | 825 | 0.612 | 0.621 |

Gate: pooled walk-forward top-5 long hit rate >= 0.55 AND top-5 short hit rate >= 0.53 AND long-short >= +10 bps/day before costs, and the latest test year's top-5 long >= 0.53 → **PASS**

Top features by gain: sector_gap_med (28637), gap_idio (27590), mkt_gap_med (17294), gap_z (17229), sector_id (15156), spy_gap (13779), spy_mom5 (12819), spy_cc_prev (12012)
