# Gap model (open-aware direction) — data to 2026-11-05

P(open-to-close return beats the day's median) from what is known at the 9:30 open: the overnight gap (raw, vs SPY, vs the stock's ATR), yesterday's move, 5/20/60-day momentum, volume, range position, SPY's gap and momentum, the market's and the sector's median gap, day of week.

## Walk-forward by year (train on earlier years, test on the year shown; tradable names only; before costs)

| year | rows | AUC (vs median) | AUC (abs) | top-3 long / short hit | top-5 long hit / bps | bottom-5 short hit / bps | D10−D1 bps/day |
|---|---|---|---|---|---|---|---|
| 2021 | 216,412 | 0.537 | 0.530 | 0.591 / 0.585 | 0.587 / 37.4 | 0.582 / 40.5 | 37.3 |
| 2022 | 218,784 | 0.524 | 0.529 | 0.539 / 0.542 | 0.522 / 2.8 | 0.565 / 21.9 | 15.3 |
| 2023 | 219,648 | 0.524 | 0.517 | 0.579 / 0.544 | 0.570 / 16.1 | 0.536 / 14.1 | 13.4 |
| 2024 | 224,513 | 0.531 | 0.528 | 0.605 / 0.557 | 0.591 / 24.8 | 0.556 / 11.3 | 16.9 |
| 2025 | 224,141 | 0.532 | 0.526 | 0.607 / 0.593 | 0.590 / 30.9 | 0.578 / 30.1 | 18.6 |
| 2026 | 191,551 | 0.520 | 0.517 | 0.593 / 0.585 | 0.580 / 25.1 | 0.574 / 34.0 | 13.0 |

## Pooled out-of-sample

- p0.55: {'coverage': 0.0687, 'n': 88949, 'hit_rate': 0.5448, 'mean_bps': 20.1, 'longs': 47913, 'shorts': 41036}
- p0.57: {'coverage': 0.014, 'n': 18075, 'hit_rate': 0.5664, 'mean_bps': 41.3, 'longs': 9820, 'shorts': 8255}
- p0.60: {'coverage': 0.0014, 'n': 1872, 'hit_rate': 0.64, 'mean_bps': 90.8, 'longs': 1080, 'shorts': 792}
- p0.63: {'coverage': 0.0001, 'n': 162, 'hit_rate': 0.6852, 'mean_bps': 181.1, 'longs': 101, 'shorts': 61}
- top3: {'k': 3, 'days': 1468, 'long_hit_rate': 0.5854, 'short_hit_rate': 0.5672, 'long_bps': 27.4, 'short_bps': 26.5, 'ls_bps': 26.9}
- topk: {'k': 5, 'days': 1468, 'long_hit_rate': 0.573, 'short_hit_rate': 0.5647, 'long_bps': 22.8, 'short_bps': 25.1, 'ls_bps': 24.0}
- top10: {'k': 10, 'days': 1468, 'long_hit_rate': 0.5662, 'short_hit_rate': 0.5504, 'long_bps': 20.1, 'short_bps': 18.2, 'ls_bps': 19.2}
- decile_spread_bps: 19.2
- auc_rel: 0.5284
- base_up_rate: 0.5045
- accuracy_at_half: 0.5177
- auc: 0.5249

## Calibration (out of sample): predicted P(up) bin -> observed up rate

| bin | n | mean p | up rate |
|---|---|---|---|
| 0.00–0.40 | 792 | 0.388 | 0.379 |
| 0.40–0.45 | 40,244 | 0.439 | 0.471 |
| 0.45–0.48 | 292,801 | 0.469 | 0.480 |
| 0.48–0.50 | 355,040 | 0.490 | 0.496 |
| 0.50–0.52 | 318,012 | 0.509 | 0.512 |
| 0.52–0.55 | 240,247 | 0.532 | 0.533 |
| 0.55–0.60 | 46,833 | 0.562 | 0.554 |
| 0.60–1.00 | 1,080 | 0.613 | 0.654 |

Gate: pooled walk-forward top-5 long hit rate >= 0.55 AND top-5 short hit rate >= 0.53 AND long-short >= +10 bps/day before costs, and the latest test year's top-5 long >= 0.53 → **PASS**

Top features by gain: sector_gap_med (28083), gap_idio (26917), gap_z (16605), mkt_gap_med (16258), sector_id (16034), spy_cc_prev (12091), spy_gap (11321), spy_mom5 (10636)
