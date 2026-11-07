# Gap model (open-aware direction) — data to 2026-11-06

P(open-to-close return beats the day's median) from what is known at the 9:30 open: the overnight gap (raw, vs SPY, vs the stock's ATR), yesterday's move, 5/20/60-day momentum, volume, range position, SPY's gap and momentum, the market's and the sector's median gap, day of week.

## Walk-forward by year (train on earlier years, test on the year shown; tradable names only; before costs)

| year | rows | AUC (vs median) | AUC (abs) | top-3 long / short hit | top-5 long hit / bps | bottom-5 short hit / bps | D10−D1 bps/day |
|---|---|---|---|---|---|---|---|
| 2021 | 216,664 | 0.538 | 0.532 | 0.564 / 0.579 | 0.567 / 22.6 | 0.574 / 40.5 | 36.4 |
| 2022 | 219,035 | 0.522 | 0.526 | 0.538 / 0.555 | 0.543 / 3.8 | 0.551 / 18.9 | 13.6 |
| 2023 | 219,898 | 0.525 | 0.519 | 0.568 / 0.529 | 0.574 / 30.5 | 0.527 / 8.7 | 15.7 |
| 2024 | 224,765 | 0.531 | 0.528 | 0.609 / 0.554 | 0.591 / 26.5 | 0.552 / 17.6 | 16.6 |
| 2025 | 224,391 | 0.531 | 0.520 | 0.604 / 0.591 | 0.598 / 43.8 | 0.578 / 28.7 | 18.6 |
| 2026 | 192,666 | 0.521 | 0.518 | 0.590 / 0.573 | 0.588 / 24.5 | 0.544 / 20.6 | 13.2 |

## Pooled out-of-sample

- p0.55: {'coverage': 0.056, 'n': 72656, 'hit_rate': 0.5472, 'mean_bps': 19.5, 'longs': 40059, 'shorts': 32597}
- p0.57: {'coverage': 0.0099, 'n': 12832, 'hit_rate': 0.5712, 'mean_bps': 41.2, 'longs': 7103, 'shorts': 5729}
- p0.60: {'coverage': 0.0008, 'n': 1067, 'hit_rate': 0.6373, 'mean_bps': 83.5, 'longs': 606, 'shorts': 461}
- p0.63: {'coverage': 0.0001, 'n': 98, 'hit_rate': 0.7041, 'mean_bps': 145.7, 'longs': 65, 'shorts': 33}
- top3: {'k': 3, 'days': 1469, 'long_hit_rate': 0.5784, 'short_hit_rate': 0.5634, 'long_bps': 26.2, 'short_bps': 28.5, 'ls_bps': 27.4}
- topk: {'k': 5, 'days': 1469, 'long_hit_rate': 0.5766, 'short_hit_rate': 0.5544, 'long_bps': 25.3, 'short_bps': 22.6, 'ls_bps': 23.9}
- top10: {'k': 10, 'days': 1469, 'long_hit_rate': 0.5691, 'short_hit_rate': 0.5457, 'long_bps': 21.8, 'short_bps': 17.8, 'ls_bps': 19.8}
- decile_spread_bps: 19.1
- auc_rel: 0.5284
- base_up_rate: 0.5046
- accuracy_at_half: 0.5171
- auc: 0.524

## Calibration (out of sample): predicted P(up) bin -> observed up rate

| bin | n | mean p | up rate |
|---|---|---|---|
| 0.00–0.40 | 461 | 0.389 | 0.386 |
| 0.40–0.45 | 32,136 | 0.439 | 0.467 |
| 0.45–0.48 | 293,643 | 0.469 | 0.481 |
| 0.48–0.50 | 366,186 | 0.490 | 0.496 |
| 0.50–0.52 | 329,293 | 0.509 | 0.513 |
| 0.52–0.55 | 235,641 | 0.532 | 0.532 |
| 0.55–0.60 | 39,453 | 0.561 | 0.556 |
| 0.60–1.00 | 606 | 0.613 | 0.655 |

Gate: pooled walk-forward top-5 long hit rate >= 0.55 AND top-5 short hit rate >= 0.53 AND long-short >= +10 bps/day before costs, and the latest test year's top-5 long >= 0.53 → **PASS**

Top features by gain: sector_gap_med (27946), gap_idio (27298), gap_z (16834), sector_id (15263), mkt_gap_med (15212), spy_gap (12435), spy_mom5 (11175), spy_cc_prev (10499)
