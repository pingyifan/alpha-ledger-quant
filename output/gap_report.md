# Gap model (open-aware direction) — data to 2026-11-25

P(open-to-close return beats the day's median) from what is known at the 9:30 open: the overnight gap (raw, vs SPY, vs the stock's ATR), yesterday's move, 5/20/60-day momentum, volume, range position, SPY's gap and momentum, the market's and the sector's median gap, day of week.

## Walk-forward by year (train on earlier years, test on the year shown; tradable names only; before costs)

| year | rows | AUC (vs median) | AUC (abs) | top-3 long / short hit | top-5 long hit / bps | bottom-5 short hit / bps | D10−D1 bps/day |
|---|---|---|---|---|---|---|---|
| 2021 | 215,908 | 0.539 | 0.531 | 0.564 / 0.594 | 0.574 / 30.2 | 0.572 / 40.4 | 38.0 |
| 2022 | 218,282 | 0.523 | 0.526 | 0.532 / 0.547 | 0.540 / 1.0 | 0.546 / 13.0 | 16.3 |
| 2023 | 219,148 | 0.524 | 0.516 | 0.576 / 0.520 | 0.561 / 9.7 | 0.533 / 9.1 | 13.6 |
| 2024 | 224,023 | 0.530 | 0.527 | 0.601 / 0.550 | 0.594 / 29.5 | 0.541 / 11.3 | 15.6 |
| 2025 | 223,902 | 0.531 | 0.523 | 0.595 / 0.589 | 0.578 / 36.4 | 0.582 / 27.7 | 17.8 |
| 2026 | 204,161 | 0.523 | 0.517 | 0.584 / 0.568 | 0.592 / 28.1 | 0.570 / 31.7 | 16.8 |

## Pooled out-of-sample

- p0.55: {'coverage': 0.0622, 'n': 81206, 'hit_rate': 0.5468, 'mean_bps': 19.5, 'longs': 44313, 'shorts': 36893}
- p0.57: {'coverage': 0.0103, 'n': 13434, 'hit_rate': 0.5683, 'mean_bps': 40.5, 'longs': 7569, 'shorts': 5865}
- p0.60: {'coverage': 0.0008, 'n': 1027, 'hit_rate': 0.6407, 'mean_bps': 107.5, 'longs': 606, 'shorts': 421}
- p0.63: {'coverage': 0.0, 'n': 42, 'hit_rate': 0.7381, 'mean_bps': 222.0, 'longs': 25, 'shorts': 17}
- top3: {'k': 3, 'days': 1482, 'long_hit_rate': 0.5751, 'short_hit_rate': 0.5614, 'long_bps': 22.2, 'short_bps': 26.7, 'ls_bps': 24.4}
- topk: {'k': 5, 'days': 1482, 'long_hit_rate': 0.573, 'short_hit_rate': 0.5571, 'long_bps': 22.4, 'short_bps': 22.1, 'ls_bps': 22.2}
- top10: {'k': 10, 'days': 1482, 'long_hit_rate': 0.5694, 'short_hit_rate': 0.547, 'long_bps': 21.4, 'short_bps': 17.4, 'ls_bps': 19.4}
- decile_spread_bps: 19.6
- auc_rel: 0.5286
- base_up_rate: 0.5043
- accuracy_at_half: 0.5168
- auc: 0.5237

## Calibration (out of sample): predicted P(up) bin -> observed up rate

| bin | n | mean p | up rate |
|---|---|---|---|
| 0.00–0.40 | 421 | 0.390 | 0.380 |
| 0.40–0.45 | 36,472 | 0.440 | 0.468 |
| 0.45–0.48 | 301,127 | 0.469 | 0.481 |
| 0.48–0.50 | 362,229 | 0.490 | 0.496 |
| 0.50–0.52 | 319,940 | 0.509 | 0.512 |
| 0.52–0.55 | 240,922 | 0.532 | 0.530 |
| 0.55–0.60 | 43,707 | 0.561 | 0.557 |
| 0.60–1.00 | 606 | 0.611 | 0.655 |

Gate: pooled walk-forward top-5 long hit rate >= 0.55 AND top-5 short hit rate >= 0.53 AND long-short >= +10 bps/day before costs, and the latest test year's top-5 long >= 0.53 → **PASS**

Top features by gain: sector_gap_med (28077), gap_idio (27438), mkt_gap_med (18032), gap_z (17206), sector_id (15197), spy_gap (13770), spy_mom5 (11457), spy_cc_prev (11374)
