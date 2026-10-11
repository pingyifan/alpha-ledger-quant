# Playbook priors, backtested on the full panel

902 tickers, 2016-01-04 to 2026-10-09, 2,323,218 stock-days (2,274,321 pass the ledger's price and liquidity filter). Every row measures the **open-to-close return of the session after the condition is known**, before costs; the ledger pays about 4 bps per round trip. Continuation = share of sessions where the open-to-close move had the same sign as the gap or the prior move.

## Verdicts on the playbook's priors

| Prior | Verdict |
|---|---|
| long a stock that gapped up 2-5% (continuation) | no reliable edge (mean +1.0 bps, t = 0.78, n = 61,899) |
| long a stock that gapped up 5%+ (continuation) | supported: +25.1 bps/session for that side, clears 4 bps costs (t = 5.6, n = 12,495) |
| short a stock that gapped down 2-5% (continuation) | goes the other way: -21.4 bps/session for that side (t = -15.73, n = 58,530) |
| short a stock that gapped down 5%+ (continuation) | supported: +44.0 bps/session for that side, clears 4 bps costs (t = 8.3, n = 11,758) |
| fade a +5% gap (short) | goes the other way: -25.1 bps/session for that side (t = -5.6, n = 12,495) |
| fade a -5% gap (long) | goes the other way: -44.0 bps/session for that side (t = -8.3, n = 11,758) |
| day-two fade after a +10% day (short) | no reliable edge (mean -10.6 bps, t = -1.87, n = 7,530) |
| day-two bounce after a -10% day (long) | supported: +80.0 bps/session for that side, clears 4 bps costs (t = 10.08, n = 5,953) |
| oversold bounce after a -15% three-day drop (long) | supported: +36.1 bps/session for that side, clears 4 bps costs (t = 5.2, n = 8,161) |
| 20-day momentum top decile (long) | positive but inside costs (+2.2 bps vs 4 bps, t = 4.55, n = 228,275) |
| 20-day momentum bottom decile (short) | goes the other way: -3.2 bps/session for that side (t = -6.24, n = 228,503) |

## 1. Overnight gap -> open-to-close

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | Continuation | t |
|---|---|---|---|---|---|---|---|
| gap <= -5% | full | 11,758 | -44.0 | -38.9 | 46.3% | 53.4% | -8.3 |
| -5% < gap <= -2% | full | 58,530 | +21.4 | +19.0 | 52.6% | 47.0% | 15.73 |
| -2% < gap <= -1% | full | 145,836 | +9.9 | +13.1 | 52.7% | 46.8% | 16.23 |
| -1% < gap <= -0.3% | full | 418,970 | +2.9 | +7.9 | 52.1% | 47.3% | 10.72 |
| flat (|gap| < 0.3%) | full | 865,367 | -0.0 | +2.2 | 50.5% | 48.5% | -0.0 |
| +0.3% <= gap < +1% | full | 530,764 | +0.4 | +0.0 | 49.6% | 49.6% | 1.79 |
| +1% <= gap < +2% | full | 168,702 | +6.4 | +4.1 | 50.7% | 50.7% | 11.74 |
| +2% <= gap < +5% | full | 61,899 | +1.0 | -6.8 | 48.8% | 48.8% | 0.78 |
| gap >= +5% | full | 12,495 | +25.1 | +0.4 | 50.0% | 50.0% | 5.6 |
| gap <= -5% | last_24m | 2,616 | -17.5 | -24.1 | 48.3% | 51.6% | -1.66 |
| -5% < gap <= -2% | last_24m | 13,732 | +30.4 | +38.0 | 55.3% | 44.4% | 10.52 |
| -2% < gap <= -1% | last_24m | 33,092 | +24.4 | +21.9 | 54.8% | 44.9% | 18.0 |
| -1% < gap <= -0.3% | last_24m | 87,765 | +6.3 | +7.6 | 52.1% | 47.5% | 10.1 |
| flat (|gap| < 0.3%) | last_24m | 157,071 | -0.7 | +0.0 | 49.8% | 48.4% | -1.62 |
| +0.3% <= gap < +1% | last_24m | 100,728 | -3.6 | -5.5 | 48.2% | 48.2% | -6.4 |
| +1% <= gap < +2% | last_24m | 37,042 | -2.7 | -7.4 | 48.2% | 48.2% | -2.29 |
| +2% <= gap < +5% | last_24m | 15,196 | -32.7 | -34.9 | 44.5% | 44.5% | -12.7 |
| gap >= +5% | last_24m | 3,098 | -32.3 | -40.2 | 45.4% | 45.4% | -3.78 |
| gap <= -5% | last_12m | 1,199 | +44.9 | +18.6 | 52.4% | 47.5% | 3.06 |
| -5% < gap <= -2% | last_12m | 7,042 | +34.8 | +38.7 | 55.6% | 44.0% | 9.11 |
| -2% < gap <= -1% | last_12m | 18,026 | +10.2 | +15.3 | 53.3% | 46.4% | 5.9 |
| -1% < gap <= -0.3% | last_12m | 44,666 | +2.5 | +5.4 | 51.4% | 48.3% | 2.77 |
| flat (|gap| < 0.3%) | last_12m | 73,940 | -2.0 | -1.6 | 49.2% | 48.1% | -3.17 |
| +0.3% <= gap < +1% | last_12m | 49,391 | -5.2 | -8.5 | 47.4% | 47.4% | -6.32 |
| +1% <= gap < +2% | last_12m | 21,544 | -6.0 | -15.0 | 46.6% | 46.6% | -3.82 |
| +2% <= gap < +5% | last_12m | 8,599 | -12.3 | -20.4 | 46.7% | 46.7% | -3.66 |
| gap >= +5% | last_12m | 1,571 | -14.5 | -23.2 | 47.1% | 47.1% | -1.17 |

## 2. Day two after a big close-to-close move

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | Continuation | t |
|---|---|---|---|---|---|---|---|
| yesterday +10% or more | full | 7,530 | -10.6 | -15.1 | 48.0% | 48.0% | -1.87 |
| yesterday +5% to +10% | full | 37,310 | +1.0 | +0.0 | 49.6% | 49.6% | 0.6 |
| yesterday -5% to -10% | full | 35,359 | +22.1 | +17.4 | 52.3% | 47.3% | 11.53 |
| yesterday -10% or worse | full | 5,953 | +80.0 | +50.4 | 54.7% | 45.0% | 10.08 |
| yesterday +10% or more | last_24m | 1,820 | -56.6 | -67.6 | 42.1% | 42.1% | -5.95 |
| yesterday +5% to +10% | last_24m | 8,691 | +12.8 | +5.0 | 50.7% | 50.7% | 3.83 |
| yesterday -5% to -10% | last_24m | 8,056 | +42.0 | +28.0 | 54.4% | 45.4% | 10.32 |
| yesterday -10% or worse | last_24m | 1,384 | +10.0 | +5.1 | 50.4% | 49.4% | 0.81 |
| yesterday +10% or more | last_12m | 835 | +23.5 | +23.4 | 52.7% | 52.7% | 1.57 |
| yesterday +5% to +10% | last_12m | 5,083 | +32.0 | +30.6 | 54.7% | 54.7% | 7.15 |
| yesterday -5% to -10% | last_12m | 4,474 | +19.5 | +20.2 | 52.9% | 46.9% | 3.89 |
| yesterday -10% or worse | last_12m | 622 | -3.3 | -3.5 | 49.2% | 50.6% | -0.17 |

## 3. Three-day moves

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| 3-day return <= -15% | full | 8,161 | +36.1 | +12.5 | 51.0% | 5.2 |
| 3-day return -15% to -10% | full | 19,580 | +20.7 | +10.9 | 51.3% | 7.21 |
| 3-day return >= +15% | full | 11,201 | -0.7 | -5.1 | 49.1% | -0.19 |
| 3-day return <= -15% | last_24m | 1,934 | +11.1 | -8.3 | 48.9% | 0.92 |
| 3-day return -15% to -10% | last_24m | 4,621 | +27.8 | +2.3 | 50.2% | 4.41 |
| 3-day return >= +15% | last_24m | 2,650 | +7.0 | +1.1 | 50.1% | 0.91 |
| 3-day return <= -15% | last_12m | 790 | +39.4 | +19.1 | 50.9% | 2.63 |
| 3-day return -15% to -10% | last_12m | 2,326 | +0.4 | -11.9 | 48.3% | 0.06 |
| 3-day return >= +15% | last_12m | 1,499 | +15.7 | +10.9 | 51.8% | 1.47 |

## 4. 20-day momentum deciles

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| momentum top decile (20d) | full | 228,275 | +2.2 | +2.6 | 50.4% | 4.55 |
| momentum bottom decile (20d) | full | 228,503 | +3.2 | +1.9 | 50.2% | 6.24 |
| momentum top decile (20d) | last_24m | 45,150 | +3.0 | +2.0 | 50.3% | 2.49 |
| momentum bottom decile (20d) | last_24m | 45,164 | +2.1 | +0.0 | 49.8% | 1.76 |
| momentum top decile (20d) | last_12m | 22,650 | +4.0 | +0.0 | 50.0% | 2.2 |
| momentum bottom decile (20d) | last_12m | 22,664 | -0.7 | -2.0 | 49.3% | -0.39 |

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
| 2026 | 174,736 | 49.4% | +0.1 |

## 6. SPY conditionals

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| SPY all sessions | full | 2,708 | +2.3 | +5.2 | 53.9% | 1.41 |
| SPY gap >= +0.5% | full | 427 | +8.8 | +22.3 | 60.0% | 1.76 |
| SPY gap <= -0.5% | full | 343 | +6.3 | +8.0 | 53.6% | 0.91 |
| SPY after 3 up days | full | 437 | +1.5 | +4.5 | 52.9% | 0.57 |
| SPY after a -1% day | full | 292 | +9.1 | +2.2 | 52.0% | 1.13 |
| SPY all sessions | last_24m | 501 | +2.4 | +2.8 | 51.5% | 0.59 |
| SPY gap >= +0.5% | last_24m | 78 | -10.8 | -9.7 | 44.9% | -1.07 |
| SPY gap <= -0.5% | last_24m | 63 | +20.1 | +0.5 | 50.8% | 0.91 |
| SPY after 3 up days | last_24m | 84 | +2.0 | -0.4 | 50.0% | 0.34 |
| SPY after a -1% day | last_24m | 52 | +47.5 | +34.5 | 61.5% | 1.87 |
| SPY all sessions | last_12m | 251 | +0.2 | +0.1 | 50.2% | 0.05 |
| SPY gap >= +0.5% | last_12m | 46 | -5.5 | -9.7 | 43.5% | -0.49 |
| SPY gap <= -0.5% | last_12m | 30 | +6.8 | -2.8 | 46.7% | 0.5 |
| SPY after 3 up days | last_12m | 38 | -1.4 | +1.7 | 52.6% | -0.16 |
| SPY after a -1% day | last_12m | 25 | +14.3 | +5.7 | 56.0% | 0.89 |

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
| 2026 | 194 | 50.0% | +2.2 |

_Current index membership (survivorship bias favours longs slightly). Research output, not investment advice._
