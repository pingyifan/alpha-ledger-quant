# Playbook priors, backtested on the full panel

902 tickers, 2016-01-04 to 2026-10-23, 2,332,237 stock-days (2,283,340 pass the ledger's price and liquidity filter). Every row measures the **open-to-close return of the session after the condition is known**, before costs; the ledger pays about 4 bps per round trip. Continuation = share of sessions where the open-to-close move had the same sign as the gap or the prior move.

## Verdicts on the playbook's priors

| Prior | Verdict |
|---|---|
| long a stock that gapped up 2-5% (continuation) | no reliable edge (mean +0.8 bps, t = 0.66, n = 62,177) |
| long a stock that gapped up 5%+ (continuation) | supported: +24.4 bps/session for that side, clears 4 bps costs (t = 5.46, n = 12,525) |
| short a stock that gapped down 2-5% (continuation) | goes the other way: -20.9 bps/session for that side (t = -15.44, n = 58,960) |
| short a stock that gapped down 5%+ (continuation) | supported: +43.9 bps/session for that side, clears 4 bps costs (t = 8.3, n = 11,834) |
| fade a +5% gap (short) | goes the other way: -24.4 bps/session for that side (t = -5.46, n = 12,525) |
| fade a -5% gap (long) | goes the other way: -43.9 bps/session for that side (t = -8.3, n = 11,834) |
| day-two fade after a +10% day (short) | no reliable edge (mean -10.7 bps, t = -1.9, n = 7,539) |
| day-two bounce after a -10% day (long) | supported: +80.1 bps/session for that side, clears 4 bps costs (t = 10.15, n = 5,995) |
| oversold bounce after a -15% three-day drop (long) | supported: +35.2 bps/session for that side, clears 4 bps costs (t = 5.09, n = 8,205) |
| 20-day momentum top decile (long) | positive but inside costs (+2.1 bps vs 4 bps, t = 4.37, n = 229,184) |
| 20-day momentum bottom decile (short) | goes the other way: -3.1 bps/session for that side (t = -6.06, n = 229,413) |

## 1. Overnight gap -> open-to-close

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | Continuation | t |
|---|---|---|---|---|---|---|---|
| gap <= -5% | full | 11,834 | -43.9 | -38.7 | 46.4% | 53.4% | -8.3 |
| -5% < gap <= -2% | full | 58,960 | +20.9 | +18.8 | 52.5% | 47.1% | 15.44 |
| -2% < gap <= -1% | full | 146,730 | +9.9 | +13.1 | 52.7% | 46.8% | 16.3 |
| -1% < gap <= -0.3% | full | 420,604 | +2.9 | +7.9 | 52.1% | 47.3% | 10.98 |
| flat (|gap| < 0.3%) | full | 867,633 | +0.0 | +2.2 | 50.5% | 48.5% | 0.29 |
| +0.3% <= gap < +1% | full | 533,130 | +0.5 | +0.0 | 49.6% | 49.6% | 2.3 |
| +1% <= gap < +2% | full | 169,747 | +6.4 | +4.1 | 50.7% | 50.7% | 11.76 |
| +2% <= gap < +5% | full | 62,177 | +0.8 | -6.9 | 48.8% | 48.8% | 0.66 |
| gap >= +5% | full | 12,525 | +24.4 | +0.0 | 49.9% | 49.9% | 5.46 |
| gap <= -5% | last_24m | 2,670 | -19.0 | -25.7 | 48.2% | 51.7% | -1.81 |
| -5% < gap <= -2% | last_24m | 14,038 | +28.7 | +37.6 | 55.2% | 44.5% | 10.0 |
| -2% < gap <= -1% | last_24m | 33,581 | +24.1 | +22.0 | 54.8% | 44.9% | 17.86 |
| -1% < gap <= -0.3% | last_24m | 87,388 | +6.8 | +7.9 | 52.2% | 47.4% | 10.9 |
| flat (|gap| < 0.3%) | last_24m | 155,499 | -0.6 | +0.0 | 49.7% | 48.3% | -1.42 |
| +0.3% <= gap < +1% | last_24m | 101,070 | -3.2 | -5.4 | 48.2% | 48.2% | -5.68 |
| +1% <= gap < +2% | last_24m | 37,711 | -2.4 | -7.4 | 48.3% | 48.3% | -2.04 |
| +2% <= gap < +5% | last_24m | 15,333 | -32.6 | -34.6 | 44.5% | 44.5% | -12.77 |
| gap >= +5% | last_24m | 3,109 | -34.8 | -42.5 | 45.0% | 45.0% | -4.1 |
| gap <= -5% | last_12m | 1,253 | +40.4 | +18.6 | 52.3% | 47.6% | 2.79 |
| -5% < gap <= -2% | last_12m | 7,250 | +28.4 | +34.0 | 54.8% | 44.9% | 7.51 |
| -2% < gap <= -1% | last_12m | 18,407 | +8.1 | +13.5 | 52.9% | 46.8% | 4.73 |
| -1% < gap <= -0.3% | last_12m | 45,012 | +2.3 | +4.8 | 51.2% | 48.4% | 2.54 |
| flat (|gap| < 0.3%) | last_12m | 72,940 | -0.5 | -0.8 | 49.4% | 48.3% | -0.72 |
| +0.3% <= gap < +1% | last_12m | 49,246 | -1.6 | -6.8 | 47.8% | 47.8% | -1.91 |
| +1% <= gap < +2% | last_12m | 21,838 | -5.6 | -15.5 | 46.5% | 46.5% | -3.6 |
| +2% <= gap < +5% | last_12m | 8,534 | -14.7 | -23.1 | 46.3% | 46.3% | -4.38 |
| gap >= +5% | last_12m | 1,537 | -24.2 | -33.8 | 45.9% | 45.9% | -1.93 |

## 2. Day two after a big close-to-close move

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | Continuation | t |
|---|---|---|---|---|---|---|---|
| yesterday +10% or more | full | 7,539 | -10.7 | -15.5 | 48.0% | 48.0% | -1.9 |
| yesterday +5% to +10% | full | 37,518 | +0.5 | -1.1 | 49.5% | 49.5% | 0.32 |
| yesterday -5% to -10% | full | 35,591 | +22.3 | +17.8 | 52.4% | 47.2% | 11.7 |
| yesterday -10% or worse | full | 5,995 | +80.1 | +51.5 | 54.8% | 44.9% | 10.15 |
| yesterday +10% or more | last_24m | 1,822 | -56.8 | -67.3 | 42.0% | 42.0% | -5.98 |
| yesterday +5% to +10% | last_24m | 8,823 | +10.8 | +3.6 | 50.4% | 50.4% | 3.25 |
| yesterday -5% to -10% | last_24m | 8,235 | +42.7 | +29.0 | 54.6% | 45.2% | 10.62 |
| yesterday -10% or worse | last_24m | 1,418 | +13.3 | +8.4 | 50.8% | 48.9% | 1.1 |
| yesterday +10% or more | last_12m | 830 | +24.0 | +21.1 | 52.4% | 52.4% | 1.62 |
| yesterday +5% to +10% | last_12m | 5,150 | +25.2 | +24.3 | 53.5% | 53.5% | 5.66 |
| yesterday -5% to -10% | last_12m | 4,479 | +18.2 | +16.4 | 52.5% | 47.3% | 3.6 |
| yesterday -10% or worse | last_12m | 641 | -2.7 | -3.1 | 49.5% | 50.4% | -0.14 |

## 3. Three-day moves

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| 3-day return <= -15% | full | 8,205 | +35.2 | +11.5 | 50.9% | 5.09 |
| 3-day return -15% to -10% | full | 19,735 | +20.4 | +10.9 | 51.3% | 7.17 |
| 3-day return >= +15% | full | 11,212 | -0.8 | -5.4 | 49.1% | -0.21 |
| 3-day return <= -15% | last_24m | 1,974 | +8.0 | -13.0 | 48.4% | 0.67 |
| 3-day return -15% to -10% | last_24m | 4,745 | +27.2 | +2.7 | 50.3% | 4.37 |
| 3-day return >= +15% | last_24m | 2,649 | +6.4 | +0.6 | 50.0% | 0.83 |
| 3-day return <= -15% | last_12m | 825 | +28.7 | -2.6 | 49.7% | 1.96 |
| 3-day return -15% to -10% | last_12m | 2,421 | -2.0 | -12.5 | 48.2% | -0.28 |
| 3-day return >= +15% | last_12m | 1,481 | +17.1 | +10.9 | 51.9% | 1.59 |

## 4. 20-day momentum deciles

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| momentum top decile (20d) | full | 229,184 | +2.1 | +2.5 | 50.4% | 4.37 |
| momentum bottom decile (20d) | full | 229,413 | +3.1 | +1.8 | 50.2% | 6.06 |
| momentum top decile (20d) | last_24m | 45,159 | +2.5 | +1.6 | 50.2% | 2.09 |
| momentum bottom decile (20d) | last_24m | 45,174 | +1.5 | +0.0 | 49.7% | 1.23 |
| momentum top decile (20d) | last_12m | 22,659 | +5.0 | +0.0 | 49.8% | 2.74 |
| momentum bottom decile (20d) | last_12m | 22,674 | -1.8 | -2.9 | 49.1% | -1.06 |

## 5. Base rate: share of tradable stock-days that closed above the open

| Year | n | Share up | Mean OC (bps) |
|---|---|---|---|
| 2016 | 177,050 | 52.8% | +10.4 |
| 2017 | 197,848 | 51.4% | +2.7 |
| 2018 | 201,844 | 49.3% | -6.5 |
| 2019 | 205,998 | 52.7% | +6.7 |
| 2020 | 211,038 | 49.6% | +0.6 |
| 2021 | 217,192 | 50.2% | +0.7 |
| 2022 | 218,920 | 50.0% | +1.2 |
| 2023 | 220,147 | 51.5% | +6.0 |
| 2024 | 225,057 | 50.3% | -0.9 |
| 2025 | 224,491 | 51.0% | +4.2 |
| 2026 | 183,755 | 49.5% | +0.7 |

## 6. SPY conditionals

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| SPY all sessions | full | 2,718 | +2.2 | +5.1 | 53.9% | 1.39 |
| SPY gap >= +0.5% | full | 428 | +8.8 | +21.9 | 59.8% | 1.76 |
| SPY gap <= -0.5% | full | 345 | +6.2 | +6.8 | 53.6% | 0.89 |
| SPY after 3 up days | full | 438 | +1.4 | +4.4 | 52.7% | 0.55 |
| SPY after a -1% day | full | 295 | +9.2 | +1.1 | 52.2% | 1.16 |
| SPY all sessions | last_24m | 501 | +2.1 | +2.0 | 51.3% | 0.54 |
| SPY gap >= +0.5% | last_24m | 78 | -10.1 | -8.5 | 44.9% | -1.01 |
| SPY gap <= -0.5% | last_24m | 65 | +19.0 | +0.5 | 50.8% | 0.89 |
| SPY after 3 up days | last_24m | 84 | +1.7 | -0.4 | 50.0% | 0.28 |
| SPY after a -1% day | last_24m | 55 | +46.1 | +32.9 | 61.8% | 1.91 |
| SPY all sessions | last_12m | 251 | +0.5 | +0.1 | 50.2% | 0.12 |
| SPY gap >= +0.5% | last_12m | 45 | -6.1 | -9.8 | 42.2% | -0.54 |
| SPY gap <= -0.5% | last_12m | 31 | +3.1 | -3.0 | 45.2% | 0.24 |
| SPY after 3 up days | last_12m | 39 | -2.2 | +0.1 | 51.3% | -0.26 |
| SPY after a -1% day | last_12m | 27 | +14.3 | +0.9 | 55.6% | 0.94 |

| Year | n | SPY share up (open-to-close) | Mean OC (bps) |
|---|---|---|---|
| 2016 | 252 | 55.2% | +6.0 |
| 2017 | 251 | 53.4% | +2.3 |
| 2018 | 251 | 50.6% | -6.8 |
| 2019 | 252 | 54.8% | +5.4 |
| 2020 | 253 | 58.1% | +2.0 |
| 2021 | 252 | 54.4% | +3.8 |
| 2022 | 251 | 50.6% | -1.5 |
| 2023 | 250 | 58.8% | +7.3 |
| 2024 | 252 | 53.6% | +0.5 |
| 2025 | 250 | 52.4% | +3.9 |
| 2026 | 204 | 50.0% | +1.6 |

_Current index membership (survivorship bias favours longs slightly). Research output, not investment advice._
