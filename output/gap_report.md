# Gap model (open-aware direction) — data to 2026-11-04

P(open-to-close return beats the day's median) from what is known at the 9:30 open: the overnight gap (raw, vs SPY, vs the stock's ATR), yesterday's move, 5/20/60-day momentum, volume, range position, SPY's gap and momentum, the market's and the sector's median gap, day of week.

## Walk-forward by year (train on earlier years, test on the year shown; tradable names only; before costs)

| year | rows | AUC (vs median) | AUC (abs) | top-3 long / short hit | top-5 long hit / bps | bottom-5 short hit / bps | D10−D1 bps/day |
|---|---|---|---|---|---|---|---|
| 2021 | 216,664 | 0.539 | 0.533 | 0.573 / 0.597 | 0.576 / 28.8 | 0.588 / 45.4 | 38.3 |
| 2022 | 219,035 | 0.524 | 0.527 | 0.544 / 0.566 | 0.544 / 3.2 | 0.554 / 16.8 | 15.5 |
| 2023 | 219,898 | 0.525 | 0.518 | 0.575 / 0.541 | 0.566 / 16.7 | 0.530 / 4.0 | 15.7 |
| 2024 | 224,765 | 0.531 | 0.527 | 0.597 / 0.545 | 0.585 / 28.0 | 0.542 / 15.1 | 16.8 |
| 2025 | 224,391 | 0.532 | 0.523 | 0.584 / 0.585 | 0.583 / 38.4 | 0.568 / 27.1 | 18.3 |
| 2026 | 190,862 | 0.523 | 0.517 | 0.577 / 0.591 | 0.568 / 21.7 | 0.550 / 22.6 | 15.2 |

## Pooled out-of-sample

- p0.55: {'coverage': 0.0625, 'n': 80983, 'hit_rate': 0.5443, 'mean_bps': 18.9, 'longs': 43835, 'shorts': 37148}
- p0.57: {'coverage': 0.0128, 'n': 16575, 'hit_rate': 0.5636, 'mean_bps': 35.3, 'longs': 8909, 'shorts': 7666}
- p0.60: {'coverage': 0.0014, 'n': 1841, 'hit_rate': 0.6013, 'mean_bps': 67.8, 'longs': 973, 'shorts': 868}
- p0.63: {'coverage': 0.0001, 'n': 185, 'hit_rate': 0.6432, 'mean_bps': 119.0, 'longs': 106, 'shorts': 79}
- top3: {'k': 3, 'days': 1467, 'long_hit_rate': 0.5749, 'short_hit_rate': 0.5703, 'long_bps': 26.7, 'short_bps': 27.7, 'ls_bps': 27.2}
- topk: {'k': 5, 'days': 1467, 'long_hit_rate': 0.5706, 'short_hit_rate': 0.5556, 'long_bps': 22.8, 'short_bps': 21.9, 'ls_bps': 22.3}
- top10: {'k': 10, 'days': 1467, 'long_hit_rate': 0.5681, 'short_hit_rate': 0.5473, 'long_bps': 21.1, 'short_bps': 16.2, 'ls_bps': 18.7}
- decile_spread_bps: 20.0
- auc_rel: 0.5289
- base_up_rate: 0.5048
- accuracy_at_half: 0.518
- auc: 0.5243

## Calibration (out of sample): predicted P(up) bin -> observed up rate

| bin | n | mean p | up rate |
|---|---|---|---|
| 0.00–0.40 | 868 | 0.387 | 0.433 |
| 0.40–0.45 | 36,280 | 0.439 | 0.472 |
| 0.45–0.48 | 290,318 | 0.469 | 0.480 |
| 0.48–0.50 | 360,870 | 0.490 | 0.495 |
| 0.50–0.52 | 325,800 | 0.509 | 0.514 |
| 0.52–0.55 | 237,644 | 0.532 | 0.532 |
| 0.55–0.60 | 42,862 | 0.562 | 0.556 |
| 0.60–1.00 | 973 | 0.613 | 0.632 |

Gate: pooled walk-forward top-5 long hit rate >= 0.55 AND top-5 short hit rate >= 0.53 AND long-short >= +10 bps/day before costs, and the latest test year's top-5 long >= 0.53 → **PASS**

Top features by gain: gap_idio (27611), sector_gap_med (27021), gap_z (17272), sector_id (15235), mkt_gap_med (14418), spy_gap (12603), spy_mom5 (12004), spy_cc_prev (10882)
