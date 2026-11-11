# Gap model (open-aware direction) — data to 2026-11-10

P(open-to-close return beats the day's median) from what is known at the 9:30 open: the overnight gap (raw, vs SPY, vs the stock's ATR), yesterday's move, 5/20/60-day momentum, volume, range position, SPY's gap and momentum, the market's and the sector's median gap, day of week.

## Walk-forward by year (train on earlier years, test on the year shown; tradable names only; before costs)

| year | rows | AUC (vs median) | AUC (abs) | top-3 long / short hit | top-5 long hit / bps | bottom-5 short hit / bps | D10−D1 bps/day |
|---|---|---|---|---|---|---|---|
| 2021 | 216,160 | 0.539 | 0.529 | 0.587 / 0.564 | 0.587 / 29.4 | 0.568 / 39.7 | 37.7 |
| 2022 | 218,533 | 0.525 | 0.527 | 0.540 / 0.570 | 0.543 / 3.5 | 0.568 / 29.3 | 17.9 |
| 2023 | 219,398 | 0.524 | 0.515 | 0.584 / 0.531 | 0.576 / 18.4 | 0.541 / 10.8 | 14.8 |
| 2024 | 224,261 | 0.531 | 0.528 | 0.615 / 0.526 | 0.595 / 29.0 | 0.532 / 5.5 | 17.4 |
| 2025 | 223,891 | 0.532 | 0.523 | 0.583 / 0.595 | 0.573 / 38.1 | 0.581 / 38.4 | 19.9 |
| 2026 | 194,038 | 0.522 | 0.518 | 0.602 / 0.597 | 0.581 / 28.3 | 0.583 / 35.8 | 15.6 |

## Pooled out-of-sample

- p0.55: {'coverage': 0.0784, 'n': 101578, 'hit_rate': 0.5428, 'mean_bps': 17.8, 'longs': 53054, 'shorts': 48524}
- p0.57: {'coverage': 0.0186, 'n': 24126, 'hit_rate': 0.5598, 'mean_bps': 29.4, 'longs': 12803, 'shorts': 11323}
- p0.60: {'coverage': 0.0027, 'n': 3446, 'hit_rate': 0.5966, 'mean_bps': 54.0, 'longs': 1742, 'shorts': 1704}
- p0.63: {'coverage': 0.0004, 'n': 501, 'hit_rate': 0.6587, 'mean_bps': 99.0, 'longs': 246, 'shorts': 255}
- top3: {'k': 3, 'days': 1471, 'long_hit_rate': 0.5849, 'short_hit_rate': 0.5629, 'long_bps': 29.6, 'short_bps': 28.5, 'ls_bps': 29.0}
- topk: {'k': 5, 'days': 1471, 'long_hit_rate': 0.5757, 'short_hit_rate': 0.5617, 'long_bps': 24.4, 'short_bps': 26.4, 'ls_bps': 25.4}
- top10: {'k': 10, 'days': 1471, 'long_hit_rate': 0.5668, 'short_hit_rate': 0.5504, 'long_bps': 20.8, 'short_bps': 20.0, 'ls_bps': 20.4}
- decile_spread_bps: 20.6
- auc_rel: 0.529
- base_up_rate: 0.5049
- accuracy_at_half: 0.5171
- auc: 0.5238

## Calibration (out of sample): predicted P(up) bin -> observed up rate

| bin | n | mean p | up rate |
|---|---|---|---|
| 0.00–0.40 | 1,704 | 0.384 | 0.406 |
| 0.40–0.45 | 46,820 | 0.438 | 0.474 |
| 0.45–0.48 | 298,625 | 0.468 | 0.482 |
| 0.48–0.50 | 344,350 | 0.490 | 0.496 |
| 0.50–0.52 | 310,824 | 0.509 | 0.512 |
| 0.52–0.55 | 240,904 | 0.532 | 0.531 |
| 0.55–0.60 | 51,312 | 0.563 | 0.554 |
| 0.60–1.00 | 1,742 | 0.615 | 0.599 |

Gate: pooled walk-forward top-5 long hit rate >= 0.55 AND top-5 short hit rate >= 0.53 AND long-short >= +10 bps/day before costs, and the latest test year's top-5 long >= 0.53 → **PASS**

Top features by gain: sector_gap_med (29737), gap_idio (27274), mkt_gap_med (17919), gap_z (17402), sector_id (15801), spy_gap (13488), spy_cc_prev (13364), spy_mom5 (12549)
