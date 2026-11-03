# Gap model (open-aware direction) — data to 2026-11-02

P(open-to-close return beats the day's median) from what is known at the 9:30 open: the overnight gap (raw, vs SPY, vs the stock's ATR), yesterday's move, 5/20/60-day momentum, volume, range position, SPY's gap and momentum, the market's and the sector's median gap, day of week.

## Walk-forward by year (train on earlier years, test on the year shown; tradable names only; before costs)

| year | rows | AUC (vs median) | AUC (abs) | top-3 long / short hit | top-5 long hit / bps | bottom-5 short hit / bps | D10−D1 bps/day |
|---|---|---|---|---|---|---|---|
| 2021 | 216,412 | 0.538 | 0.532 | 0.577 / 0.594 | 0.593 / 29.9 | 0.584 / 48.8 | 38.4 |
| 2022 | 218,784 | 0.524 | 0.523 | 0.523 / 0.568 | 0.526 / -3.5 | 0.548 / 18.8 | 17.0 |
| 2023 | 219,753 | 0.525 | 0.517 | 0.568 / 0.541 | 0.565 / 11.1 | 0.538 / 2.8 | 15.6 |
| 2024 | 224,765 | 0.531 | 0.528 | 0.606 / 0.530 | 0.586 / 27.3 | 0.540 / 10.7 | 18.1 |
| 2025 | 224,391 | 0.530 | 0.522 | 0.592 / 0.584 | 0.581 / 31.6 | 0.574 / 27.5 | 17.8 |
| 2026 | 189,057 | 0.522 | 0.517 | 0.591 / 0.570 | 0.576 / 28.0 | 0.567 / 37.7 | 14.0 |

## Pooled out-of-sample

- p0.55: {'coverage': 0.058, 'n': 75021, 'hit_rate': 0.5471, 'mean_bps': 20.8, 'longs': 40971, 'shorts': 34050}
- p0.57: {'coverage': 0.0112, 'n': 14538, 'hit_rate': 0.5702, 'mean_bps': 39.1, 'longs': 7947, 'shorts': 6591}
- p0.60: {'coverage': 0.0013, 'n': 1691, 'hit_rate': 0.6286, 'mean_bps': 65.0, 'longs': 944, 'shorts': 747}
- p0.63: {'coverage': 0.0002, 'n': 212, 'hit_rate': 0.6887, 'mean_bps': 160.3, 'longs': 130, 'shorts': 82}
- top3: {'k': 3, 'days': 1465, 'long_hit_rate': 0.5757, 'short_hit_rate': 0.5645, 'long_bps': 24.1, 'short_bps': 23.5, 'ls_bps': 23.8}
- topk: {'k': 5, 'days': 1465, 'long_hit_rate': 0.5709, 'short_hit_rate': 0.5582, 'long_bps': 20.5, 'short_bps': 24.0, 'ls_bps': 22.3}
- top10: {'k': 10, 'days': 1465, 'long_hit_rate': 0.5665, 'short_hit_rate': 0.5486, 'long_bps': 20.6, 'short_bps': 17.7, 'ls_bps': 19.1}
- decile_spread_bps: 20.2
- auc_rel: 0.5286
- base_up_rate: 0.5048
- accuracy_at_half: 0.5168
- auc: 0.5233

## Calibration (out of sample): predicted P(up) bin -> observed up rate

| bin | n | mean p | up rate |
|---|---|---|---|
| 0.00–0.40 | 747 | 0.387 | 0.378 |
| 0.40–0.45 | 33,303 | 0.439 | 0.468 |
| 0.45–0.48 | 287,179 | 0.469 | 0.482 |
| 0.48–0.50 | 368,886 | 0.490 | 0.496 |
| 0.50–0.52 | 330,003 | 0.509 | 0.515 |
| 0.52–0.55 | 232,073 | 0.532 | 0.529 |
| 0.55–0.60 | 40,027 | 0.561 | 0.556 |
| 0.60–1.00 | 944 | 0.615 | 0.633 |

Gate: pooled walk-forward top-5 long hit rate >= 0.55 AND top-5 short hit rate >= 0.53 AND long-short >= +10 bps/day before costs, and the latest test year's top-5 long >= 0.53 → **PASS**

Top features by gain: gap_idio (27691), sector_gap_med (27329), gap_z (17005), sector_id (14910), mkt_gap_med (14592), spy_gap (11963), spy_mom5 (11629), spy_cc_prev (10894)
