# Gap model (open-aware direction) — data to 2026-11-23

P(open-to-close return beats the day's median) from what is known at the 9:30 open: the overnight gap (raw, vs SPY, vs the stock's ATR), yesterday's move, 5/20/60-day momentum, volume, range position, SPY's gap and momentum, the market's and the sector's median gap, day of week.

## Walk-forward by year (train on earlier years, test on the year shown; tradable names only; before costs)

| year | rows | AUC (vs median) | AUC (abs) | top-3 long / short hit | top-5 long hit / bps | bottom-5 short hit / bps | D10−D1 bps/day |
|---|---|---|---|---|---|---|---|
| 2021 | 215,656 | 0.537 | 0.531 | 0.579 / 0.597 | 0.572 / 24.9 | 0.587 / 44.0 | 36.9 |
| 2022 | 218,031 | 0.524 | 0.526 | 0.550 / 0.556 | 0.537 / 5.2 | 0.550 / 20.1 | 15.5 |
| 2023 | 218,898 | 0.524 | 0.516 | 0.549 / 0.536 | 0.557 / 11.0 | 0.542 / 14.6 | 14.6 |
| 2024 | 223,771 | 0.531 | 0.529 | 0.597 / 0.552 | 0.596 / 28.5 | 0.552 / 15.5 | 17.8 |
| 2025 | 223,652 | 0.531 | 0.522 | 0.592 / 0.584 | 0.582 / 35.9 | 0.573 / 26.8 | 16.6 |
| 2026 | 202,136 | 0.522 | 0.518 | 0.569 / 0.581 | 0.561 / 13.3 | 0.561 / 21.4 | 14.7 |

## Pooled out-of-sample

- p0.55: {'coverage': 0.0576, 'n': 74994, 'hit_rate': 0.5453, 'mean_bps': 19.7, 'longs': 40675, 'shorts': 34319}
- p0.57: {'coverage': 0.0109, 'n': 14217, 'hit_rate': 0.5563, 'mean_bps': 32.6, 'longs': 7296, 'shorts': 6921}
- p0.60: {'coverage': 0.001, 'n': 1279, 'hit_rate': 0.613, 'mean_bps': 66.4, 'longs': 692, 'shorts': 587}
- p0.63: {'coverage': 0.0001, 'n': 86, 'hit_rate': 0.6744, 'mean_bps': 139.2, 'longs': 54, 'shorts': 32}
- top3: {'k': 3, 'days': 1480, 'long_hit_rate': 0.5727, 'short_hit_rate': 0.5673, 'long_bps': 23.2, 'short_bps': 27.2, 'ls_bps': 25.2}
- topk: {'k': 5, 'days': 1480, 'long_hit_rate': 0.5676, 'short_hit_rate': 0.5608, 'long_bps': 19.9, 'short_bps': 23.8, 'ls_bps': 21.8}
- top10: {'k': 10, 'days': 1480, 'long_hit_rate': 0.5642, 'short_hit_rate': 0.5501, 'long_bps': 19.9, 'short_bps': 18.1, 'ls_bps': 19.0}
- decile_spread_bps: 19.3
- auc_rel: 0.5284
- base_up_rate: 0.5039
- accuracy_at_half: 0.5174
- auc: 0.5239

## Calibration (out of sample): predicted P(up) bin -> observed up rate

| bin | n | mean p | up rate |
|---|---|---|---|
| 0.00–0.40 | 587 | 0.389 | 0.385 |
| 0.40–0.45 | 33,732 | 0.439 | 0.470 |
| 0.45–0.48 | 294,716 | 0.469 | 0.481 |
| 0.48–0.50 | 365,111 | 0.490 | 0.494 |
| 0.50–0.52 | 327,707 | 0.509 | 0.512 |
| 0.52–0.55 | 239,616 | 0.532 | 0.531 |
| 0.55–0.60 | 39,983 | 0.561 | 0.556 |
| 0.60–1.00 | 692 | 0.612 | 0.611 |

Gate: pooled walk-forward top-5 long hit rate >= 0.55 AND top-5 short hit rate >= 0.53 AND long-short >= +10 bps/day before costs, and the latest test year's top-5 long >= 0.53 → **PASS**

Top features by gain: gap_idio (26733), sector_gap_med (26138), gap_z (17267), mkt_gap_med (14411), sector_id (12867), spy_gap (10844), spy_mom5 (9983), spy_cc_prev (9723)
