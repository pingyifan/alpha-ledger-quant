# Gap model (open-aware direction) — data to 2026-11-11

P(open-to-close return beats the day's median) from what is known at the 9:30 open: the overnight gap (raw, vs SPY, vs the stock's ATR), yesterday's move, 5/20/60-day momentum, volume, range position, SPY's gap and momentum, the market's and the sector's median gap, day of week.

## Walk-forward by year (train on earlier years, test on the year shown; tradable names only; before costs)

| year | rows | AUC (vs median) | AUC (abs) | top-3 long / short hit | top-5 long hit / bps | bottom-5 short hit / bps | D10−D1 bps/day |
|---|---|---|---|---|---|---|---|
| 2021 | 216,159 | 0.538 | 0.529 | 0.565 / 0.590 | 0.577 / 28.7 | 0.576 / 41.3 | 36.5 |
| 2022 | 218,533 | 0.524 | 0.527 | 0.527 / 0.576 | 0.529 / -5.3 | 0.561 / 24.3 | 16.1 |
| 2023 | 219,398 | 0.525 | 0.516 | 0.575 / 0.512 | 0.578 / 19.3 | 0.522 / 1.1 | 13.7 |
| 2024 | 224,277 | 0.531 | 0.529 | 0.626 / 0.568 | 0.590 / 27.2 | 0.552 / 17.4 | 18.2 |
| 2025 | 224,086 | 0.532 | 0.523 | 0.580 / 0.585 | 0.574 / 40.1 | 0.584 / 33.5 | 18.9 |
| 2026 | 195,155 | 0.521 | 0.517 | 0.611 / 0.521 | 0.607 / 42.6 | 0.531 / 16.5 | 13.9 |

## Pooled out-of-sample

- p0.55: {'coverage': 0.0606, 'n': 78611, 'hit_rate': 0.5452, 'mean_bps': 19.3, 'longs': 42588, 'shorts': 36023}
- p0.57: {'coverage': 0.0117, 'n': 15204, 'hit_rate': 0.5602, 'mean_bps': 36.2, 'longs': 7973, 'shorts': 7231}
- p0.60: {'coverage': 0.0013, 'n': 1634, 'hit_rate': 0.6083, 'mean_bps': 82.3, 'longs': 892, 'shorts': 742}
- p0.63: {'coverage': 0.0001, 'n': 96, 'hit_rate': 0.6771, 'mean_bps': 170.7, 'longs': 57, 'shorts': 39}
- top3: {'k': 3, 'days': 1472, 'long_hit_rate': 0.5799, 'short_hit_rate': 0.5596, 'long_bps': 25.6, 'short_bps': 23.6, 'ls_bps': 24.6}
- topk: {'k': 5, 'days': 1472, 'long_hit_rate': 0.575, 'short_hit_rate': 0.5548, 'long_bps': 25.0, 'short_bps': 22.5, 'ls_bps': 23.8}
- top10: {'k': 10, 'days': 1472, 'long_hit_rate': 0.5681, 'short_hit_rate': 0.5467, 'long_bps': 21.2, 'short_bps': 16.7, 'ls_bps': 19.0}
- decile_spread_bps: 19.6
- auc_rel: 0.5288
- base_up_rate: 0.505
- accuracy_at_half: 0.5169
- auc: 0.5239

## Calibration (out of sample): predicted P(up) bin -> observed up rate

| bin | n | mean p | up rate |
|---|---|---|---|
| 0.00–0.40 | 742 | 0.389 | 0.418 |
| 0.40–0.45 | 35,281 | 0.439 | 0.472 |
| 0.45–0.48 | 294,825 | 0.469 | 0.481 |
| 0.48–0.50 | 360,915 | 0.490 | 0.497 |
| 0.50–0.52 | 323,645 | 0.509 | 0.512 |
| 0.52–0.55 | 239,612 | 0.532 | 0.532 |
| 0.55–0.60 | 41,696 | 0.561 | 0.557 |
| 0.60–1.00 | 892 | 0.612 | 0.630 |

Gate: pooled walk-forward top-5 long hit rate >= 0.55 AND top-5 short hit rate >= 0.53 AND long-short >= +10 bps/day before costs, and the latest test year's top-5 long >= 0.53 → **PASS**

Top features by gain: sector_gap_med (26974), gap_idio (26600), gap_z (17821), mkt_gap_med (15186), sector_id (14672), spy_gap (13244), spy_mom5 (11919), spy_cc_prev (11758)
