# Gap model (open-aware direction) — data to 2026-11-16

P(open-to-close return beats the day's median) from what is known at the 9:30 open: the overnight gap (raw, vs SPY, vs the stock's ATR), yesterday's move, 5/20/60-day momentum, volume, range position, SPY's gap and momentum, the market's and the sector's median gap, day of week.

## Walk-forward by year (train on earlier years, test on the year shown; tradable names only; before costs)

| year | rows | AUC (vs median) | AUC (abs) | top-3 long / short hit | top-5 long hit / bps | bottom-5 short hit / bps | D10−D1 bps/day |
|---|---|---|---|---|---|---|---|
| 2021 | 215,404 | 0.537 | 0.531 | 0.579 / 0.577 | 0.579 / 30.1 | 0.578 / 42.3 | 38.0 |
| 2022 | 217,780 | 0.523 | 0.527 | 0.542 / 0.563 | 0.535 / 1.3 | 0.549 / 22.9 | 14.5 |
| 2023 | 218,648 | 0.525 | 0.515 | 0.564 / 0.532 | 0.567 / 12.9 | 0.527 / 3.2 | 14.6 |
| 2024 | 223,521 | 0.533 | 0.529 | 0.595 / 0.558 | 0.579 / 21.8 | 0.555 / 17.9 | 17.9 |
| 2025 | 223,336 | 0.532 | 0.524 | 0.583 / 0.591 | 0.587 / 35.7 | 0.564 / 29.6 | 19.5 |
| 2026 | 197,198 | 0.521 | 0.516 | 0.574 / 0.565 | 0.577 / 20.8 | 0.568 / 28.9 | 11.7 |

## Pooled out-of-sample

- p0.55: {'coverage': 0.0627, 'n': 81285, 'hit_rate': 0.5446, 'mean_bps': 20.2, 'longs': 43489, 'shorts': 37796}
- p0.57: {'coverage': 0.0135, 'n': 17505, 'hit_rate': 0.5693, 'mean_bps': 34.7, 'longs': 8877, 'shorts': 8628}
- p0.60: {'coverage': 0.0018, 'n': 2329, 'hit_rate': 0.5955, 'mean_bps': 47.5, 'longs': 1152, 'shorts': 1177}
- p0.63: {'coverage': 0.0002, 'n': 291, 'hit_rate': 0.6495, 'mean_bps': 101.9, 'longs': 157, 'shorts': 134}
- top3: {'k': 3, 'days': 1475, 'long_hit_rate': 0.5729, 'short_hit_rate': 0.5643, 'long_bps': 24.1, 'short_bps': 27.4, 'ls_bps': 25.8}
- topk: {'k': 5, 'days': 1475, 'long_hit_rate': 0.5704, 'short_hit_rate': 0.5566, 'long_bps': 20.4, 'short_bps': 24.0, 'ls_bps': 22.2}
- top10: {'k': 10, 'days': 1475, 'long_hit_rate': 0.5654, 'short_hit_rate': 0.5508, 'long_bps': 20.6, 'short_bps': 18.5, 'ls_bps': 19.6}
- decile_spread_bps: 19.4
- auc_rel: 0.5287
- base_up_rate: 0.5045
- accuracy_at_half: 0.5175
- auc: 0.5239

## Calibration (out of sample): predicted P(up) bin -> observed up rate

| bin | n | mean p | up rate |
|---|---|---|---|
| 0.00–0.40 | 1,177 | 0.386 | 0.409 |
| 0.40–0.45 | 36,619 | 0.438 | 0.473 |
| 0.45–0.48 | 291,069 | 0.469 | 0.481 |
| 0.48–0.50 | 362,271 | 0.490 | 0.495 |
| 0.50–0.52 | 323,784 | 0.509 | 0.513 |
| 0.52–0.55 | 237,478 | 0.532 | 0.531 |
| 0.55–0.60 | 42,337 | 0.561 | 0.557 |
| 0.60–1.00 | 1,152 | 0.615 | 0.600 |

Gate: pooled walk-forward top-5 long hit rate >= 0.55 AND top-5 short hit rate >= 0.53 AND long-short >= +10 bps/day before costs, and the latest test year's top-5 long >= 0.53 → **PASS**

Top features by gain: sector_gap_med (27648), gap_idio (27438), gap_z (16295), mkt_gap_med (15702), sector_id (13982), spy_gap (12393), spy_mom5 (10682), spy_cc_prev (10334)
