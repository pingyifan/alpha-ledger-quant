# Gap model (open-aware direction) — data to 2026-11-12

P(open-to-close return beats the day's median) from what is known at the 9:30 open: the overnight gap (raw, vs SPY, vs the stock's ATR), yesterday's move, 5/20/60-day momentum, volume, range position, SPY's gap and momentum, the market's and the sector's median gap, day of week.

## Walk-forward by year (train on earlier years, test on the year shown; tradable names only; before costs)

| year | rows | AUC (vs median) | AUC (abs) | top-3 long / short hit | top-5 long hit / bps | bottom-5 short hit / bps | D10−D1 bps/day |
|---|---|---|---|---|---|---|---|
| 2021 | 216,412 | 0.538 | 0.531 | 0.561 / 0.591 | 0.584 / 26.8 | 0.576 / 38.5 | 36.3 |
| 2022 | 218,784 | 0.523 | 0.525 | 0.531 / 0.539 | 0.531 / 1.1 | 0.530 / 13.1 | 14.7 |
| 2023 | 219,648 | 0.524 | 0.515 | 0.572 / 0.544 | 0.554 / 13.7 | 0.532 / 4.8 | 15.2 |
| 2024 | 224,529 | 0.531 | 0.529 | 0.605 / 0.558 | 0.586 / 24.1 | 0.536 / 9.0 | 17.4 |
| 2025 | 224,336 | 0.530 | 0.523 | 0.593 / 0.584 | 0.587 / 33.3 | 0.574 / 26.2 | 17.2 |
| 2026 | 196,274 | 0.520 | 0.515 | 0.577 / 0.563 | 0.598 / 37.1 | 0.546 / 13.2 | 13.9 |

## Pooled out-of-sample

- p0.55: {'coverage': 0.0608, 'n': 79045, 'hit_rate': 0.5438, 'mean_bps': 19.1, 'longs': 43184, 'shorts': 35861}
- p0.57: {'coverage': 0.0117, 'n': 15193, 'hit_rate': 0.5615, 'mean_bps': 37.3, 'longs': 8476, 'shorts': 6717}
- p0.60: {'coverage': 0.0012, 'n': 1580, 'hit_rate': 0.6278, 'mean_bps': 69.7, 'longs': 882, 'shorts': 698}
- p0.63: {'coverage': 0.0001, 'n': 190, 'hit_rate': 0.6947, 'mean_bps': 115.7, 'longs': 116, 'shorts': 74}
- top3: {'k': 3, 'days': 1473, 'long_hit_rate': 0.573, 'short_hit_rate': 0.5632, 'long_bps': 21.8, 'short_bps': 22.7, 'ls_bps': 22.2}
- topk: {'k': 5, 'days': 1473, 'long_hit_rate': 0.5728, 'short_hit_rate': 0.5492, 'long_bps': 22.4, 'short_bps': 17.6, 'ls_bps': 20.0}
- top10: {'k': 10, 'days': 1473, 'long_hit_rate': 0.5694, 'short_hit_rate': 0.5451, 'long_bps': 23.2, 'short_bps': 17.3, 'ls_bps': 20.3}
- decile_spread_bps: 19.1
- auc_rel: 0.5281
- base_up_rate: 0.5048
- accuracy_at_half: 0.5164
- auc: 0.5232

## Calibration (out of sample): predicted P(up) bin -> observed up rate

| bin | n | mean p | up rate |
|---|---|---|---|
| 0.00–0.40 | 698 | 0.387 | 0.371 |
| 0.40–0.45 | 35,163 | 0.439 | 0.471 |
| 0.45–0.48 | 291,338 | 0.469 | 0.482 |
| 0.48–0.50 | 366,849 | 0.490 | 0.496 |
| 0.50–0.52 | 326,157 | 0.509 | 0.512 |
| 0.52–0.55 | 236,594 | 0.532 | 0.532 |
| 0.55–0.60 | 42,302 | 0.561 | 0.553 |
| 0.60–1.00 | 882 | 0.614 | 0.627 |

Gate: pooled walk-forward top-5 long hit rate >= 0.55 AND top-5 short hit rate >= 0.53 AND long-short >= +10 bps/day before costs, and the latest test year's top-5 long >= 0.53 → **PASS**

Top features by gain: gap_idio (27448), sector_gap_med (27262), gap_z (16998), mkt_gap_med (16371), sector_id (14214), spy_gap (12133), spy_cc_prev (11309), spy_mom5 (10770)
