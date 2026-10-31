# Gap model (open-aware direction) — data to 2026-10-30

P(open-to-close return beats the day's median) from what is known at the 9:30 open: the overnight gap (raw, vs SPY, vs the stock's ATR), yesterday's move, 5/20/60-day momentum, volume, range position, SPY's gap and momentum, the market's and the sector's median gap, day of week.

## Walk-forward by year (train on earlier years, test on the year shown; tradable names only; before costs)

| year | rows | AUC (vs median) | AUC (abs) | top-3 long / short hit | top-5 long hit / bps | bottom-5 short hit / bps | D10−D1 bps/day |
|---|---|---|---|---|---|---|---|
| 2021 | 216,411 | 0.538 | 0.532 | 0.557 / 0.591 | 0.581 / 31.9 | 0.580 / 40.3 | 38.2 |
| 2022 | 218,784 | 0.524 | 0.528 | 0.519 / 0.550 | 0.534 / 0.7 | 0.555 / 21.0 | 17.4 |
| 2023 | 219,753 | 0.525 | 0.516 | 0.585 / 0.535 | 0.574 / 21.1 | 0.530 / 6.4 | 14.7 |
| 2024 | 224,765 | 0.532 | 0.531 | 0.587 / 0.558 | 0.590 / 30.4 | 0.558 / 16.9 | 17.9 |
| 2025 | 224,391 | 0.531 | 0.522 | 0.597 / 0.587 | 0.588 / 40.1 | 0.574 / 23.6 | 17.8 |
| 2026 | 188,155 | 0.523 | 0.517 | 0.590 / 0.549 | 0.595 / 32.3 | 0.562 / 23.2 | 16.5 |

## Pooled out-of-sample

- p0.55: {'coverage': 0.0649, 'n': 83913, 'hit_rate': 0.5455, 'mean_bps': 19.1, 'longs': 45894, 'shorts': 38019}
- p0.57: {'coverage': 0.0145, 'n': 18792, 'hit_rate': 0.5643, 'mean_bps': 34.5, 'longs': 10074, 'shorts': 8718}
- p0.60: {'coverage': 0.0019, 'n': 2507, 'hit_rate': 0.6127, 'mean_bps': 62.6, 'longs': 1314, 'shorts': 1193}
- p0.63: {'coverage': 0.0002, 'n': 319, 'hit_rate': 0.6489, 'mean_bps': 106.3, 'longs': 191, 'shorts': 128}
- top3: {'k': 3, 'days': 1464, 'long_hit_rate': 0.5722, 'short_hit_rate': 0.5619, 'long_bps': 25.4, 'short_bps': 24.5, 'ls_bps': 24.9}
- topk: {'k': 5, 'days': 1464, 'long_hit_rate': 0.5765, 'short_hit_rate': 0.56, 'long_bps': 25.9, 'short_bps': 21.9, 'ls_bps': 23.9}
- top10: {'k': 10, 'days': 1464, 'long_hit_rate': 0.5672, 'short_hit_rate': 0.5517, 'long_bps': 21.7, 'short_bps': 18.2, 'ls_bps': 20.0}
- decile_spread_bps: 20.4
- auc_rel: 0.529
- base_up_rate: 0.5047
- accuracy_at_half: 0.5178
- auc: 0.5246

## Calibration (out of sample): predicted P(up) bin -> observed up rate

| bin | n | mean p | up rate |
|---|---|---|---|
| 0.00–0.40 | 1,193 | 0.386 | 0.397 |
| 0.40–0.45 | 36,826 | 0.438 | 0.474 |
| 0.45–0.48 | 289,633 | 0.469 | 0.480 |
| 0.48–0.50 | 360,405 | 0.490 | 0.496 |
| 0.50–0.52 | 322,851 | 0.509 | 0.514 |
| 0.52–0.55 | 235,457 | 0.532 | 0.530 |
| 0.55–0.60 | 44,580 | 0.562 | 0.558 |
| 0.60–1.00 | 1,314 | 0.615 | 0.622 |

Gate: pooled walk-forward top-5 long hit rate >= 0.55 AND top-5 short hit rate >= 0.53 AND long-short >= +10 bps/day before costs, and the latest test year's top-5 long >= 0.53 → **PASS**

Top features by gain: sector_gap_med (27924), gap_idio (26880), gap_z (16794), sector_id (15451), mkt_gap_med (15361), spy_gap (12011), spy_cc_prev (11617), spy_mom5 (10684)
