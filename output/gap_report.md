# Gap model (open-aware direction) — data to 2026-11-24

P(open-to-close return beats the day's median) from what is known at the 9:30 open: the overnight gap (raw, vs SPY, vs the stock's ATR), yesterday's move, 5/20/60-day momentum, volume, range position, SPY's gap and momentum, the market's and the sector's median gap, day of week.

## Walk-forward by year (train on earlier years, test on the year shown; tradable names only; before costs)

| year | rows | AUC (vs median) | AUC (abs) | top-3 long / short hit | top-5 long hit / bps | bottom-5 short hit / bps | D10−D1 bps/day |
|---|---|---|---|---|---|---|---|
| 2021 | 215,907 | 0.538 | 0.530 | 0.575 / 0.586 | 0.587 / 30.6 | 0.574 / 40.1 | 36.8 |
| 2022 | 218,282 | 0.522 | 0.523 | 0.534 / 0.562 | 0.538 / 1.1 | 0.555 / 28.4 | 13.5 |
| 2023 | 219,148 | 0.525 | 0.516 | 0.572 / 0.525 | 0.563 / 10.4 | 0.541 / 13.7 | 14.2 |
| 2024 | 224,023 | 0.531 | 0.527 | 0.605 / 0.566 | 0.581 / 25.5 | 0.562 / 20.5 | 16.8 |
| 2025 | 223,902 | 0.531 | 0.523 | 0.581 / 0.584 | 0.574 / 33.7 | 0.578 / 32.8 | 18.9 |
| 2026 | 203,261 | 0.521 | 0.518 | 0.587 / 0.583 | 0.588 / 25.4 | 0.585 / 35.5 | 16.2 |

## Pooled out-of-sample

- p0.55: {'coverage': 0.052, 'n': 67842, 'hit_rate': 0.5445, 'mean_bps': 19.4, 'longs': 38096, 'shorts': 29746}
- p0.57: {'coverage': 0.0091, 'n': 11823, 'hit_rate': 0.5601, 'mean_bps': 36.8, 'longs': 6834, 'shorts': 4989}
- p0.60: {'coverage': 0.0006, 'n': 844, 'hit_rate': 0.5853, 'mean_bps': 66.8, 'longs': 482, 'shorts': 362}
- p0.63: {'coverage': 0.0, 'n': 24, 'hit_rate': 0.6667, 'mean_bps': 225.9, 'longs': 13, 'shorts': 11}
- top3: {'k': 3, 'days': 1481, 'long_hit_rate': 0.5755, 'short_hit_rate': 0.5674, 'long_bps': 22.4, 'short_bps': 32.5, 'ls_bps': 27.5}
- topk: {'k': 5, 'days': 1481, 'long_hit_rate': 0.5716, 'short_hit_rate': 0.5653, 'long_bps': 21.0, 'short_bps': 28.4, 'ls_bps': 24.7}
- top10: {'k': 10, 'days': 1481, 'long_hit_rate': 0.5662, 'short_hit_rate': 0.5523, 'long_bps': 20.8, 'short_bps': 20.0, 'ls_bps': 20.4}
- decile_spread_bps: 19.4
- auc_rel: 0.5282
- base_up_rate: 0.504
- accuracy_at_half: 0.5164
- auc: 0.5231

## Calibration (out of sample): predicted P(up) bin -> observed up rate

| bin | n | mean p | up rate |
|---|---|---|---|
| 0.00–0.40 | 362 | 0.390 | 0.472 |
| 0.40–0.45 | 29,384 | 0.440 | 0.474 |
| 0.45–0.48 | 293,809 | 0.469 | 0.480 |
| 0.48–0.50 | 375,635 | 0.490 | 0.496 |
| 0.50–0.52 | 331,181 | 0.509 | 0.512 |
| 0.52–0.55 | 236,056 | 0.532 | 0.530 |
| 0.55–0.60 | 37,614 | 0.561 | 0.558 |
| 0.60–1.00 | 482 | 0.610 | 0.629 |

Gate: pooled walk-forward top-5 long hit rate >= 0.55 AND top-5 short hit rate >= 0.53 AND long-short >= +10 bps/day before costs, and the latest test year's top-5 long >= 0.53 → **PASS**

Top features by gain: sector_gap_med (26930), gap_idio (26693), gap_z (16722), mkt_gap_med (15490), sector_id (13255), spy_gap (11894), spy_mom5 (10358), spy_cc_prev (9768)
