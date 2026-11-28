# Gap model (open-aware direction) — data to 2026-11-27

P(open-to-close return beats the day's median) from what is known at the 9:30 open: the overnight gap (raw, vs SPY, vs the stock's ATR), yesterday's move, 5/20/60-day momentum, volume, range position, SPY's gap and momentum, the market's and the sector's median gap, day of week.

## Walk-forward by year (train on earlier years, test on the year shown; tradable names only; before costs)

| year | rows | AUC (vs median) | AUC (abs) | top-3 long / short hit | top-5 long hit / bps | bottom-5 short hit / bps | D10−D1 bps/day |
|---|---|---|---|---|---|---|---|
| 2021 | 215,908 | 0.539 | 0.531 | 0.568 / 0.590 | 0.586 / 32.5 | 0.586 / 42.3 | 37.2 |
| 2022 | 218,282 | 0.523 | 0.525 | 0.539 / 0.550 | 0.543 / 2.9 | 0.559 / 26.4 | 15.4 |
| 2023 | 219,148 | 0.524 | 0.516 | 0.556 / 0.533 | 0.558 / 13.4 | 0.527 / 6.4 | 13.4 |
| 2024 | 224,023 | 0.529 | 0.526 | 0.578 / 0.552 | 0.578 / 17.0 | 0.559 / 15.7 | 16.7 |
| 2025 | 223,902 | 0.530 | 0.523 | 0.591 / 0.595 | 0.579 / 24.3 | 0.586 / 31.3 | 17.3 |
| 2026 | 205,061 | 0.522 | 0.519 | 0.588 / 0.591 | 0.591 / 27.5 | 0.563 / 31.0 | 14.7 |

## Pooled out-of-sample

- p0.55: {'coverage': 0.0705, 'n': 92039, 'hit_rate': 0.5436, 'mean_bps': 17.3, 'longs': 48913, 'shorts': 43126}
- p0.57: {'coverage': 0.0147, 'n': 19202, 'hit_rate': 0.5578, 'mean_bps': 31.2, 'longs': 10030, 'shorts': 9172}
- p0.60: {'coverage': 0.0016, 'n': 2144, 'hit_rate': 0.5816, 'mean_bps': 64.1, 'longs': 1120, 'shorts': 1024}
- p0.63: {'coverage': 0.0001, 'n': 157, 'hit_rate': 0.5669, 'mean_bps': 104.5, 'longs': 94, 'shorts': 63}
- top3: {'k': 3, 'days': 1483, 'long_hit_rate': 0.5696, 'short_hit_rate': 0.568, 'long_bps': 20.6, 'short_bps': 26.9, 'ls_bps': 23.8}
- topk: {'k': 5, 'days': 1483, 'long_hit_rate': 0.5724, 'short_hit_rate': 0.5635, 'long_bps': 19.5, 'short_bps': 25.4, 'ls_bps': 22.5}
- top10: {'k': 10, 'days': 1483, 'long_hit_rate': 0.5674, 'short_hit_rate': 0.5485, 'long_bps': 19.5, 'short_bps': 18.4, 'ls_bps': 19.0}
- decile_spread_bps: 19.1
- auc_rel: 0.5281
- base_up_rate: 0.5044
- accuracy_at_half: 0.5166
- auc: 0.5236

## Calibration (out of sample): predicted P(up) bin -> observed up rate

| bin | n | mean p | up rate |
|---|---|---|---|
| 0.00–0.40 | 1,024 | 0.389 | 0.428 |
| 0.40–0.45 | 42,102 | 0.438 | 0.471 |
| 0.45–0.48 | 297,891 | 0.469 | 0.482 |
| 0.48–0.50 | 358,163 | 0.490 | 0.497 |
| 0.50–0.52 | 318,096 | 0.509 | 0.511 |
| 0.52–0.55 | 240,135 | 0.532 | 0.532 |
| 0.55–0.60 | 47,793 | 0.562 | 0.555 |
| 0.60–1.00 | 1,120 | 0.613 | 0.590 |

Gate: pooled walk-forward top-5 long hit rate >= 0.55 AND top-5 short hit rate >= 0.53 AND long-short >= +10 bps/day before costs, and the latest test year's top-5 long >= 0.53 → **PASS**

Top features by gain: sector_gap_med (29567), gap_idio (27935), mkt_gap_med (19091), gap_z (17719), sector_id (16367), spy_gap (15279), spy_cc_prev (13033), spy_mom5 (12522)
