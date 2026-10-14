# Playbook priors, backtested on the full panel

902 tickers, 2016-01-04 to 2026-10-13, 2,325,021 stock-days (2,276,122 pass the ledger's price and liquidity filter). Every row measures the **open-to-close return of the session after the condition is known**, before costs; the ledger pays about 4 bps per round trip. Continuation = share of sessions where the open-to-close move had the same sign as the gap or the prior move.

## Verdicts on the playbook's priors

| Prior | Verdict |
|---|---|
| long a stock that gapped up 2-5% (continuation) | no reliable edge (mean +1.0 bps, t = 0.76, n = 61,911) |
| long a stock that gapped up 5%+ (continuation) | supported: +25.0 bps/session for that side, clears 4 bps costs (t = 5.58, n = 12,496) |
| short a stock that gapped down 2-5% (continuation) | goes the other way: -21.4 bps/session for that side (t = -15.78, n = 58,590) |
| short a stock that gapped down 5%+ (continuation) | supported: +43.8 bps/session for that side, clears 4 bps costs (t = 8.25, n = 11,764) |
| fade a +5% gap (short) | goes the other way: -25.0 bps/session for that side (t = -5.58, n = 12,496) |
| fade a -5% gap (long) | goes the other way: -43.8 bps/session for that side (t = -8.25, n = 11,764) |
| day-two fade after a +10% day (short) | no reliable edge (mean -10.8 bps, t = -1.91, n = 7,533) |
| day-two bounce after a -10% day (long) | supported: +80.1 bps/session for that side, clears 4 bps costs (t = 10.09, n = 5,955) |
| oversold bounce after a -15% three-day drop (long) | supported: +36.2 bps/session for that side, clears 4 bps costs (t = 5.2, n = 8,162) |
| 20-day momentum top decile (long) | positive but inside costs (+2.2 bps vs 4 bps, t = 4.5, n = 228,455) |
| 20-day momentum bottom decile (short) | goes the other way: -3.2 bps/session for that side (t = -6.23, n = 228,684) |

## 1. Overnight gap -> open-to-close

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | Continuation | t |
|---|---|---|---|---|---|---|---|
| gap <= -5% | full | 11,764 | -43.8 | -38.6 | 46.3% | 53.4% | -8.25 |
| -5% < gap <= -2% | full | 58,590 | +21.4 | +19.1 | 52.6% | 47.0% | 15.78 |
| -2% < gap <= -1% | full | 145,948 | +9.8 | +13.1 | 52.7% | 46.8% | 16.18 |
| -1% < gap <= -0.3% | full | 419,192 | +2.9 | +7.9 | 52.1% | 47.3% | 10.78 |
| flat (|gap| < 0.3%) | full | 865,937 | +0.0 | +2.2 | 50.5% | 48.5% | 0.04 |
| +0.3% <= gap < +1% | full | 531,400 | +0.4 | +0.0 | 49.6% | 49.6% | 1.66 |
| +1% <= gap < +2% | full | 168,884 | +6.3 | +4.0 | 50.7% | 50.7% | 11.62 |
| +2% <= gap < +5% | full | 61,911 | +1.0 | -6.8 | 48.8% | 48.8% | 0.76 |
| gap >= +5% | full | 12,496 | +25.0 | +0.0 | 50.0% | 50.0% | 5.58 |
| gap <= -5% | last_24m | 2,616 | -17.0 | -23.4 | 48.4% | 51.5% | -1.61 |
| -5% < gap <= -2% | last_24m | 13,768 | +30.6 | +38.0 | 55.3% | 44.4% | 10.6 |
| -2% < gap <= -1% | last_24m | 33,045 | +23.9 | +21.4 | 54.7% | 45.0% | 17.6 |
| -1% < gap <= -0.3% | last_24m | 87,550 | +6.1 | +7.5 | 52.1% | 47.5% | 9.79 |
| flat (|gap| < 0.3%) | last_24m | 156,944 | -0.9 | +0.0 | 49.7% | 48.4% | -2.13 |
| +0.3% <= gap < +1% | last_24m | 100,950 | -4.0 | -6.0 | 48.0% | 48.0% | -7.16 |
| +1% <= gap < +2% | last_24m | 37,180 | -3.0 | -7.7 | 48.1% | 48.1% | -2.58 |
| +2% <= gap < +5% | last_24m | 15,202 | -32.8 | -34.9 | 44.4% | 44.4% | -12.74 |
| gap >= +5% | last_24m | 3,096 | -33.1 | -40.9 | 45.2% | 45.2% | -3.88 |
| gap <= -5% | last_12m | 1,203 | +46.8 | +19.1 | 52.6% | 47.2% | 3.19 |
| -5% < gap <= -2% | last_12m | 7,093 | +35.9 | +40.3 | 55.8% | 43.9% | 9.44 |
| -2% < gap <= -1% | last_12m | 18,100 | +10.3 | +15.3 | 53.3% | 46.4% | 5.94 |
| -1% < gap <= -0.3% | last_12m | 44,731 | +3.0 | +5.6 | 51.4% | 48.2% | 3.37 |
| flat (|gap| < 0.3%) | last_12m | 73,956 | -0.6 | -0.5 | 49.5% | 48.1% | -1.03 |
| +0.3% <= gap < +1% | last_12m | 49,412 | -3.5 | -8.0 | 47.5% | 47.5% | -4.27 |
| +1% <= gap < +2% | last_12m | 21,452 | -6.6 | -16.4 | 46.3% | 46.3% | -4.18 |
| +2% <= gap < +5% | last_12m | 8,493 | -13.9 | -22.8 | 46.4% | 46.4% | -4.11 |
| gap >= +5% | last_12m | 1,545 | -16.4 | -25.8 | 46.7% | 46.7% | -1.31 |

## 2. Day two after a big close-to-close move

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | Continuation | t |
|---|---|---|---|---|---|---|---|
| yesterday +10% or more | full | 7,533 | -10.8 | -16.0 | 48.0% | 48.0% | -1.91 |
| yesterday +5% to +10% | full | 37,333 | +0.9 | +0.0 | 49.6% | 49.6% | 0.56 |
| yesterday -5% to -10% | full | 35,389 | +22.2 | +17.6 | 52.4% | 47.3% | 11.59 |
| yesterday -10% or worse | full | 5,955 | +80.1 | +51.2 | 54.7% | 45.0% | 10.09 |
| yesterday +10% or more | last_24m | 1,822 | -56.9 | -67.6 | 42.0% | 42.0% | -6.0 |
| yesterday +5% to +10% | last_24m | 8,704 | +12.2 | +4.7 | 50.7% | 50.7% | 3.67 |
| yesterday -5% to -10% | last_24m | 8,083 | +42.5 | +28.6 | 54.5% | 45.3% | 10.46 |
| yesterday -10% or worse | last_24m | 1,386 | +10.4 | +5.4 | 50.5% | 49.3% | 0.84 |
| yesterday +10% or more | last_12m | 839 | +23.6 | +23.2 | 52.6% | 52.6% | 1.58 |
| yesterday +5% to +10% | last_12m | 5,098 | +31.2 | +29.7 | 54.6% | 54.6% | 6.98 |
| yesterday -5% to -10% | last_12m | 4,366 | +18.6 | +15.8 | 52.4% | 47.4% | 3.62 |
| yesterday -10% or worse | last_12m | 616 | -3.8 | -3.5 | 49.2% | 50.6% | -0.2 |

## 3. Three-day moves

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| 3-day return <= -15% | full | 8,162 | +36.2 | +12.6 | 51.0% | 5.2 |
| 3-day return -15% to -10% | full | 19,602 | +20.8 | +10.9 | 51.3% | 7.26 |
| 3-day return >= +15% | full | 11,205 | -0.8 | -5.3 | 49.1% | -0.2 |
| 3-day return <= -15% | last_24m | 1,934 | +11.1 | -8.3 | 48.9% | 0.92 |
| 3-day return -15% to -10% | last_24m | 4,640 | +28.4 | +2.6 | 50.3% | 4.51 |
| 3-day return >= +15% | last_24m | 2,652 | +6.7 | +1.0 | 50.1% | 0.87 |
| 3-day return <= -15% | last_12m | 789 | +40.0 | +21.2 | 50.9% | 2.67 |
| 3-day return -15% to -10% | last_12m | 2,325 | +1.4 | -11.3 | 48.4% | 0.19 |
| 3-day return >= +15% | last_12m | 1,501 | +15.9 | +10.9 | 51.8% | 1.48 |

## 4. 20-day momentum deciles

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| momentum top decile (20d) | full | 228,455 | +2.2 | +2.6 | 50.4% | 4.5 |
| momentum bottom decile (20d) | full | 228,684 | +3.2 | +1.9 | 50.2% | 6.23 |
| momentum top decile (20d) | last_24m | 45,151 | +2.5 | +1.6 | 50.2% | 2.04 |
| momentum bottom decile (20d) | last_24m | 45,166 | +1.8 | +0.0 | 49.7% | 1.51 |
| momentum top decile (20d) | last_12m | 22,651 | +5.7 | +0.9 | 50.1% | 3.11 |
| momentum bottom decile (20d) | last_12m | 22,666 | +0.0 | -1.7 | 49.4% | 0.02 |

## 5. Base rate: share of tradable stock-days that closed above the open

| Year | n | Share up | Mean OC (bps) |
|---|---|---|---|
| 2016 | 177,050 | 52.8% | +10.4 |
| 2017 | 197,848 | 51.4% | +2.7 |
| 2018 | 201,844 | 49.3% | -6.5 |
| 2019 | 205,998 | 52.7% | +6.7 |
| 2020 | 211,037 | 49.6% | +0.6 |
| 2021 | 217,191 | 50.2% | +0.7 |
| 2022 | 218,920 | 50.0% | +1.2 |
| 2023 | 220,147 | 51.5% | +6.0 |
| 2024 | 225,057 | 50.3% | -0.9 |
| 2025 | 224,491 | 51.0% | +4.2 |
| 2026 | 176,539 | 49.4% | +0.0 |

## 6. SPY conditionals

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| SPY all sessions | full | 2,710 | +2.3 | +5.2 | 53.9% | 1.41 |
| SPY gap >= +0.5% | full | 427 | +8.8 | +22.3 | 60.0% | 1.76 |
| SPY gap <= -0.5% | full | 343 | +6.3 | +8.0 | 53.6% | 0.91 |
| SPY after 3 up days | full | 437 | +1.5 | +4.5 | 52.9% | 0.57 |
| SPY after a -1% day | full | 292 | +9.1 | +2.2 | 52.0% | 1.13 |
| SPY all sessions | last_24m | 501 | +2.2 | +2.6 | 51.3% | 0.56 |
| SPY gap >= +0.5% | last_24m | 78 | -10.8 | -9.7 | 44.9% | -1.07 |
| SPY gap <= -0.5% | last_24m | 63 | +20.1 | +0.5 | 50.8% | 0.91 |
| SPY after 3 up days | last_24m | 84 | +2.0 | -0.4 | 50.0% | 0.34 |
| SPY after a -1% day | last_24m | 52 | +47.5 | +34.5 | 61.5% | 1.87 |
| SPY all sessions | last_12m | 251 | +1.2 | +0.1 | 50.2% | 0.3 |
| SPY gap >= +0.5% | last_12m | 45 | -6.4 | -12.2 | 42.2% | -0.56 |
| SPY gap <= -0.5% | last_12m | 30 | +6.8 | -2.8 | 46.7% | 0.5 |
| SPY after 3 up days | last_12m | 38 | -1.4 | +1.7 | 52.6% | -0.16 |
| SPY after a -1% day | last_12m | 24 | +13.4 | +3.3 | 54.2% | 0.8 |

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
| 2026 | 196 | 50.0% | +2.2 |

_Current index membership (survivorship bias favours longs slightly). Research output, not investment advice._
