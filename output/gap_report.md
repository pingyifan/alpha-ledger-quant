# Gap model (open-aware direction) — data to 2026-11-09

P(open-to-close return beats the day's median) from what is known at the 9:30 open: the overnight gap (raw, vs SPY, vs the stock's ATR), yesterday's move, 5/20/60-day momentum, volume, range position, SPY's gap and momentum, the market's and the sector's median gap, day of week.

## Walk-forward by year (train on earlier years, test on the year shown; tradable names only; before costs)

| year | rows | AUC (vs median) | AUC (abs) | top-3 long / short hit | top-5 long hit / bps | bottom-5 short hit / bps | D10−D1 bps/day |
|---|---|---|---|---|---|---|---|
| 2021 | 216,160 | 0.539 | 0.531 | 0.586 / 0.587 | 0.579 / 29.0 | 0.586 / 51.5 | 39.6 |
| 2022 | 218,533 | 0.524 | 0.526 | 0.530 / 0.579 | 0.537 / -0.8 | 0.555 / 24.5 | 16.3 |
| 2023 | 219,398 | 0.524 | 0.516 | 0.588 / 0.517 | 0.569 / 18.8 | 0.530 / 7.8 | 13.6 |
| 2024 | 224,261 | 0.531 | 0.528 | 0.605 / 0.549 | 0.581 / 23.5 | 0.547 / 18.9 | 17.4 |
| 2025 | 223,891 | 0.531 | 0.523 | 0.561 / 0.603 | 0.572 / 28.5 | 0.586 / 37.6 | 18.1 |
| 2026 | 193,138 | 0.522 | 0.518 | 0.594 / 0.564 | 0.584 / 27.1 | 0.567 / 30.5 | 13.5 |

## Pooled out-of-sample

- p0.55: {'coverage': 0.0592, 'n': 76645, 'hit_rate': 0.5461, 'mean_bps': 19.5, 'longs': 42657, 'shorts': 33988}
- p0.57: {'coverage': 0.012, 'n': 15563, 'hit_rate': 0.5642, 'mean_bps': 34.7, 'longs': 8444, 'shorts': 7119}
- p0.60: {'coverage': 0.0015, 'n': 1945, 'hit_rate': 0.6051, 'mean_bps': 55.3, 'longs': 1064, 'shorts': 881}
- p0.63: {'coverage': 0.0002, 'n': 225, 'hit_rate': 0.6756, 'mean_bps': 138.9, 'longs': 127, 'shorts': 98}
- top3: {'k': 3, 'days': 1470, 'long_hit_rate': 0.5769, 'short_hit_rate': 0.5667, 'long_bps': 22.1, 'short_bps': 33.8, 'ls_bps': 27.9}
- topk: {'k': 5, 'days': 1470, 'long_hit_rate': 0.5701, 'short_hit_rate': 0.5616, 'long_bps': 20.9, 'short_bps': 28.4, 'ls_bps': 24.6}
- top10: {'k': 10, 'days': 1470, 'long_hit_rate': 0.5634, 'short_hit_rate': 0.5514, 'long_bps': 19.8, 'short_bps': 21.3, 'ls_bps': 20.5}
- decile_spread_bps: 19.8
- auc_rel: 0.5288
- base_up_rate: 0.5048
- accuracy_at_half: 0.5174
- auc: 0.5241

## Calibration (out of sample): predicted P(up) bin -> observed up rate

| bin | n | mean p | up rate |
|---|---|---|---|
| 0.00–0.40 | 881 | 0.386 | 0.412 |
| 0.40–0.45 | 33,107 | 0.439 | 0.466 |
| 0.45–0.48 | 292,892 | 0.469 | 0.482 |
| 0.48–0.50 | 365,678 | 0.490 | 0.495 |
| 0.50–0.52 | 325,056 | 0.509 | 0.514 |
| 0.52–0.55 | 235,110 | 0.532 | 0.532 |
| 0.55–0.60 | 41,593 | 0.561 | 0.553 |
| 0.60–1.00 | 1,064 | 0.615 | 0.619 |

Gate: pooled walk-forward top-5 long hit rate >= 0.55 AND top-5 short hit rate >= 0.53 AND long-short >= +10 bps/day before costs, and the latest test year's top-5 long >= 0.53 → **PASS**

Top features by gain: gap_idio (26794), sector_gap_med (26006), gap_z (16479), mkt_gap_med (14491), sector_id (13079), spy_gap (12259), spy_mom5 (10776), spy_cc_prev (9388)
