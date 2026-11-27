# Gap model (open-aware direction) — data to 2026-11-25

P(open-to-close return beats the day's median) from what is known at the 9:30 open: the overnight gap (raw, vs SPY, vs the stock's ATR), yesterday's move, 5/20/60-day momentum, volume, range position, SPY's gap and momentum, the market's and the sector's median gap, day of week.

## Walk-forward by year (train on earlier years, test on the year shown; tradable names only; before costs)

| year | rows | AUC (vs median) | AUC (abs) | top-3 long / short hit | top-5 long hit / bps | bottom-5 short hit / bps | D10−D1 bps/day |
|---|---|---|---|---|---|---|---|
| 2021 | 215,908 | 0.538 | 0.531 | 0.569 / 0.598 | 0.587 / 33.0 | 0.577 / 44.9 | 36.5 |
| 2022 | 218,282 | 0.523 | 0.523 | 0.529 / 0.562 | 0.533 / 3.9 | 0.550 / 22.3 | 15.2 |
| 2023 | 219,148 | 0.524 | 0.516 | 0.596 / 0.555 | 0.582 / 19.9 | 0.544 / 10.9 | 14.0 |
| 2024 | 224,023 | 0.531 | 0.527 | 0.611 / 0.545 | 0.602 / 33.4 | 0.548 / 16.4 | 17.4 |
| 2025 | 223,902 | 0.531 | 0.522 | 0.591 / 0.579 | 0.575 / 33.2 | 0.574 / 32.1 | 18.5 |
| 2026 | 204,161 | 0.522 | 0.517 | 0.577 / 0.587 | 0.580 / 29.7 | 0.579 / 35.8 | 14.7 |

## Pooled out-of-sample

- p0.55: {'coverage': 0.0515, 'n': 67255, 'hit_rate': 0.5494, 'mean_bps': 22.2, 'longs': 38294, 'shorts': 28961}
- p0.57: {'coverage': 0.008, 'n': 10384, 'hit_rate': 0.5738, 'mean_bps': 47.7, 'longs': 5987, 'shorts': 4397}
- p0.60: {'coverage': 0.0005, 'n': 672, 'hit_rate': 0.6429, 'mean_bps': 90.6, 'longs': 418, 'shorts': 254}
- p0.63: {'coverage': 0.0, 'n': 35, 'hit_rate': 0.6857, 'mean_bps': 243.4, 'longs': 26, 'shorts': 9}
- top3: {'k': 3, 'days': 1482, 'long_hit_rate': 0.5787, 'short_hit_rate': 0.5706, 'long_bps': 25.9, 'short_bps': 32.7, 'ls_bps': 29.3}
- topk: {'k': 5, 'days': 1482, 'long_hit_rate': 0.5764, 'short_hit_rate': 0.5615, 'long_bps': 25.5, 'short_bps': 27.0, 'ls_bps': 26.2}
- top10: {'k': 10, 'days': 1482, 'long_hit_rate': 0.5661, 'short_hit_rate': 0.5539, 'long_bps': 21.4, 'short_bps': 22.0, 'ls_bps': 21.7}
- decile_spread_bps: 19.4
- auc_rel: 0.5284
- base_up_rate: 0.5043
- accuracy_at_half: 0.5162
- auc: 0.5227

## Calibration (out of sample): predicted P(up) bin -> observed up rate

| bin | n | mean p | up rate |
|---|---|---|---|
| 0.00–0.40 | 254 | 0.391 | 0.398 |
| 0.40–0.45 | 28,707 | 0.440 | 0.466 |
| 0.45–0.48 | 295,585 | 0.469 | 0.483 |
| 0.48–0.50 | 375,778 | 0.490 | 0.496 |
| 0.50–0.52 | 330,848 | 0.509 | 0.512 |
| 0.52–0.55 | 235,958 | 0.532 | 0.530 |
| 0.55–0.60 | 37,876 | 0.560 | 0.559 |
| 0.60–1.00 | 418 | 0.611 | 0.667 |

Gate: pooled walk-forward top-5 long hit rate >= 0.55 AND top-5 short hit rate >= 0.53 AND long-short >= +10 bps/day before costs, and the latest test year's top-5 long >= 0.53 → **PASS**

Top features by gain: gap_idio (27476), sector_gap_med (26333), mkt_gap_med (16424), gap_z (16364), sector_id (12970), spy_gap (12532), gap (10003), spy_cc_prev (9581)
