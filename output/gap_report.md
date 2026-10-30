# Gap model (open-aware direction) — data to 2026-10-28

P(open-to-close return beats the day's median) from what is known at the 9:30 open: the overnight gap (raw, vs SPY, vs the stock's ATR), yesterday's move, 5/20/60-day momentum, volume, range position, SPY's gap and momentum, the market's and the sector's median gap, day of week.

## Walk-forward by year (train on earlier years, test on the year shown; tradable names only; before costs)

| year | rows | AUC (vs median) | AUC (abs) | top-3 long / short hit | top-5 long hit / bps | bottom-5 short hit / bps | D10−D1 bps/day |
|---|---|---|---|---|---|---|---|
| 2021 | 216,412 | 0.538 | 0.531 | 0.566 / 0.582 | 0.578 / 25.9 | 0.571 / 38.7 | 37.3 |
| 2022 | 218,784 | 0.524 | 0.523 | 0.522 / 0.538 | 0.526 / -5.5 | 0.547 / 18.5 | 17.5 |
| 2023 | 219,753 | 0.525 | 0.516 | 0.548 / 0.529 | 0.554 / 10.7 | 0.535 / 11.3 | 16.5 |
| 2024 | 224,765 | 0.532 | 0.529 | 0.626 / 0.553 | 0.594 / 30.0 | 0.548 / 14.2 | 18.1 |
| 2025 | 224,391 | 0.531 | 0.524 | 0.593 / 0.569 | 0.577 / 38.1 | 0.562 / 23.9 | 17.9 |
| 2026 | 186,351 | 0.523 | 0.517 | 0.573 / 0.586 | 0.587 / 26.7 | 0.556 / 28.5 | 17.3 |

## Pooled out-of-sample

- p0.55: {'coverage': 0.0548, 'n': 70751, 'hit_rate': 0.5462, 'mean_bps': 19.6, 'longs': 39302, 'shorts': 31449}
- p0.57: {'coverage': 0.0092, 'n': 11881, 'hit_rate': 0.5683, 'mean_bps': 40.4, 'longs': 6758, 'shorts': 5123}
- p0.60: {'coverage': 0.0007, 'n': 927, 'hit_rate': 0.6397, 'mean_bps': 84.3, 'longs': 566, 'shorts': 361}
- p0.63: {'coverage': 0.0001, 'n': 67, 'hit_rate': 0.7313, 'mean_bps': 225.2, 'longs': 56, 'shorts': 11}
- top3: {'k': 3, 'days': 1462, 'long_hit_rate': 0.5714, 'short_hit_rate': 0.5588, 'long_bps': 22.7, 'short_bps': 27.4, 'ls_bps': 25.0}
- topk: {'k': 5, 'days': 1462, 'long_hit_rate': 0.5688, 'short_hit_rate': 0.5531, 'long_bps': 20.8, 'short_bps': 22.3, 'ls_bps': 21.6}
- top10: {'k': 10, 'days': 1462, 'long_hit_rate': 0.5659, 'short_hit_rate': 0.5434, 'long_bps': 21.3, 'short_bps': 15.2, 'ls_bps': 18.3}
- decile_spread_bps: 20.8
- auc_rel: 0.5289
- base_up_rate: 0.5047
- accuracy_at_half: 0.517
- auc: 0.5237

## Calibration (out of sample): predicted P(up) bin -> observed up rate

| bin | n | mean p | up rate |
|---|---|---|---|
| 0.00–0.40 | 361 | 0.391 | 0.404 |
| 0.40–0.45 | 31,088 | 0.440 | 0.470 |
| 0.45–0.48 | 288,826 | 0.469 | 0.480 |
| 0.48–0.50 | 369,267 | 0.490 | 0.496 |
| 0.50–0.52 | 328,162 | 0.509 | 0.514 |
| 0.52–0.55 | 233,450 | 0.532 | 0.531 |
| 0.55–0.60 | 38,736 | 0.561 | 0.557 |
| 0.60–1.00 | 566 | 0.613 | 0.668 |

Gate: pooled walk-forward top-5 long hit rate >= 0.55 AND top-5 short hit rate >= 0.53 AND long-short >= +10 bps/day before costs, and the latest test year's top-5 long >= 0.53 → **PASS**

Top features by gain: sector_gap_med (28361), gap_idio (27551), gap_z (17077), sector_id (15290), mkt_gap_med (14805), spy_gap (11982), spy_cc_prev (11562), spy_mom5 (11078)
