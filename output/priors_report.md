# Playbook priors, backtested on the full panel

902 tickers, 2016-01-04 to 2026-10-20, 2,329,531 stock-days (2,280,634 pass the ledger's price and liquidity filter). Every row measures the **open-to-close return of the session after the condition is known**, before costs; the ledger pays about 4 bps per round trip. Continuation = share of sessions where the open-to-close move had the same sign as the gap or the prior move.

## Verdicts on the playbook's priors

| Prior | Verdict |
|---|---|
| long a stock that gapped up 2-5% (continuation) | no reliable edge (mean +0.8 bps, t = 0.66, n = 62,096) |
| long a stock that gapped up 5%+ (continuation) | supported: +24.8 bps/session for that side, clears 4 bps costs (t = 5.53, n = 12,513) |
| short a stock that gapped down 2-5% (continuation) | goes the other way: -21.3 bps/session for that side (t = -15.7, n = 58,799) |
| short a stock that gapped down 5%+ (continuation) | supported: +43.2 bps/session for that side, clears 4 bps costs (t = 8.15, n = 11,790) |
| fade a +5% gap (short) | goes the other way: -24.8 bps/session for that side (t = -5.53, n = 12,513) |
| fade a -5% gap (long) | goes the other way: -43.2 bps/session for that side (t = -8.15, n = 11,790) |
| day-two fade after a +10% day (short) | no reliable edge (mean -10.7 bps, t = -1.91, n = 7,535) |
| day-two bounce after a -10% day (long) | supported: +79.9 bps/session for that side, clears 4 bps costs (t = 10.08, n = 5,964) |
| oversold bounce after a -15% three-day drop (long) | supported: +35.1 bps/session for that side, clears 4 bps costs (t = 5.07, n = 8,202) |
| 20-day momentum top decile (long) | positive but inside costs (+2.1 bps vs 4 bps, t = 4.35, n = 228,911) |
| 20-day momentum bottom decile (short) | goes the other way: -3.2 bps/session for that side (t = -6.18, n = 229,140) |

## 1. Overnight gap -> open-to-close

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | Continuation | t |
|---|---|---|---|---|---|---|---|
| gap <= -5% | full | 11,790 | -43.2 | -38.0 | 46.4% | 53.3% | -8.15 |
| -5% < gap <= -2% | full | 58,799 | +21.3 | +19.1 | 52.6% | 47.0% | 15.7 |
| -2% < gap <= -1% | full | 146,389 | +9.8 | +13.1 | 52.7% | 46.8% | 16.18 |
| -1% < gap <= -0.3% | full | 419,902 | +2.9 | +7.9 | 52.1% | 47.3% | 10.82 |
| flat (|gap| < 0.3%) | full | 866,993 | +0.0 | +2.2 | 50.5% | 48.5% | 0.12 |
| +0.3% <= gap < +1% | full | 532,586 | +0.4 | +0.0 | 49.6% | 49.6% | 1.92 |
| +1% <= gap < +2% | full | 169,566 | +6.4 | +4.1 | 50.7% | 50.7% | 11.66 |
| +2% <= gap < +5% | full | 62,096 | +0.8 | -6.9 | 48.8% | 48.8% | 0.66 |
| gap >= +5% | full | 12,513 | +24.8 | +0.0 | 50.0% | 50.0% | 5.53 |
| gap <= -5% | last_24m | 2,635 | -15.1 | -18.7 | 48.6% | 51.3% | -1.44 |
| -5% < gap <= -2% | last_24m | 13,916 | +30.1 | +38.8 | 55.4% | 44.4% | 10.47 |
| -2% < gap <= -1% | last_24m | 33,375 | +23.8 | +21.6 | 54.7% | 45.0% | 17.58 |
| -1% < gap <= -0.3% | last_24m | 87,743 | +6.2 | +7.5 | 52.1% | 47.5% | 9.93 |
| flat (|gap| < 0.3%) | last_24m | 156,048 | -1.0 | +0.0 | 49.6% | 48.4% | -2.45 |
| +0.3% <= gap < +1% | last_24m | 100,712 | -3.7 | -5.7 | 48.1% | 48.1% | -6.66 |
| +1% <= gap < +2% | last_24m | 37,571 | -2.8 | -7.5 | 48.2% | 48.2% | -2.38 |
| +2% <= gap < +5% | last_24m | 15,278 | -32.7 | -34.7 | 44.5% | 44.5% | -12.78 |
| gap >= +5% | last_24m | 3,103 | -33.6 | -41.4 | 45.1% | 45.1% | -3.95 |
| gap <= -5% | last_12m | 1,223 | +52.0 | +31.6 | 53.2% | 46.6% | 3.58 |
| -5% < gap <= -2% | last_12m | 7,149 | +31.7 | +36.4 | 55.2% | 44.5% | 8.36 |
| -2% < gap <= -1% | last_12m | 18,156 | +7.6 | +13.2 | 52.8% | 46.9% | 4.4 |
| -1% < gap <= -0.3% | last_12m | 44,777 | +2.1 | +4.9 | 51.2% | 48.4% | 2.32 |
| flat (|gap| < 0.3%) | last_12m | 73,552 | -0.6 | -1.0 | 49.4% | 48.2% | -0.92 |
| +0.3% <= gap < +1% | last_12m | 49,309 | -2.6 | -7.5 | 47.6% | 47.6% | -3.11 |
| +1% <= gap < +2% | last_12m | 21,771 | -6.2 | -15.9 | 46.4% | 46.4% | -3.99 |
| +2% <= gap < +5% | last_12m | 8,525 | -14.4 | -23.2 | 46.2% | 46.2% | -4.27 |
| gap >= +5% | last_12m | 1,543 | -18.5 | -27.8 | 46.4% | 46.4% | -1.48 |

## 2. Day two after a big close-to-close move

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | Continuation | t |
|---|---|---|---|---|---|---|---|
| yesterday +10% or more | full | 7,535 | -10.7 | -16.1 | 48.0% | 48.0% | -1.91 |
| yesterday +5% to +10% | full | 37,407 | +0.6 | -0.7 | 49.6% | 49.6% | 0.39 |
| yesterday -5% to -10% | full | 35,501 | +22.2 | +17.7 | 52.4% | 47.3% | 11.63 |
| yesterday -10% or worse | full | 5,964 | +79.9 | +51.1 | 54.7% | 45.0% | 10.08 |
| yesterday +10% or more | last_24m | 1,821 | -57.1 | -67.6 | 41.9% | 41.9% | -6.01 |
| yesterday +5% to +10% | last_24m | 8,729 | +11.2 | +4.1 | 50.6% | 50.6% | 3.37 |
| yesterday -5% to -10% | last_24m | 8,166 | +42.3 | +28.7 | 54.5% | 45.3% | 10.48 |
| yesterday -10% or worse | last_24m | 1,390 | +11.4 | +6.7 | 50.6% | 49.1% | 0.92 |
| yesterday +10% or more | last_12m | 833 | +24.0 | +22.6 | 52.5% | 52.5% | 1.6 |
| yesterday +5% to +10% | last_12m | 5,061 | +26.5 | +25.6 | 53.8% | 53.8% | 5.91 |
| yesterday -5% to -10% | last_12m | 4,417 | +18.8 | +15.6 | 52.4% | 47.4% | 3.67 |
| yesterday -10% or worse | last_12m | 619 | -6.2 | -7.0 | 48.9% | 50.9% | -0.32 |

## 3. Three-day moves

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| 3-day return <= -15% | full | 8,202 | +35.1 | +11.2 | 50.8% | 5.07 |
| 3-day return -15% to -10% | full | 19,704 | +20.5 | +10.9 | 51.3% | 7.17 |
| 3-day return >= +15% | full | 11,208 | -0.8 | -5.2 | 49.1% | -0.2 |
| 3-day return <= -15% | last_24m | 1,973 | +7.7 | -13.4 | 48.4% | 0.65 |
| 3-day return -15% to -10% | last_24m | 4,727 | +27.1 | +2.4 | 50.2% | 4.35 |
| 3-day return >= +15% | last_24m | 2,645 | +6.7 | +1.0 | 50.1% | 0.86 |
| 3-day return <= -15% | last_12m | 827 | +29.4 | -2.9 | 49.6% | 2.01 |
| 3-day return -15% to -10% | last_12m | 2,400 | -1.9 | -12.6 | 48.2% | -0.26 |
| 3-day return >= +15% | last_12m | 1,486 | +17.4 | +12.2 | 52.0% | 1.61 |

## 4. 20-day momentum deciles

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| momentum top decile (20d) | full | 228,911 | +2.1 | +2.5 | 50.4% | 4.35 |
| momentum bottom decile (20d) | full | 229,140 | +3.2 | +1.9 | 50.2% | 6.18 |
| momentum top decile (20d) | last_24m | 45,156 | +2.3 | +1.5 | 50.2% | 1.9 |
| momentum bottom decile (20d) | last_24m | 45,171 | +1.5 | -0.2 | 49.6% | 1.25 |
| momentum top decile (20d) | last_12m | 22,656 | +4.7 | +0.0 | 49.8% | 2.58 |
| momentum bottom decile (20d) | last_12m | 22,671 | -0.9 | -2.4 | 49.2% | -0.52 |

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
| 2026 | 181,049 | 49.5% | +0.3 |

## 6. SPY conditionals

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| SPY all sessions | full | 2,715 | +2.2 | +5.1 | 53.8% | 1.39 |
| SPY gap >= +0.5% | full | 428 | +8.8 | +21.9 | 59.8% | 1.76 |
| SPY gap <= -0.5% | full | 343 | +6.3 | +8.0 | 53.6% | 0.91 |
| SPY after 3 up days | full | 437 | +1.5 | +4.5 | 52.9% | 0.57 |
| SPY after a -1% day | full | 294 | +9.2 | +2.2 | 52.0% | 1.16 |
| SPY all sessions | last_24m | 501 | +2.1 | +2.0 | 51.1% | 0.53 |
| SPY gap >= +0.5% | last_24m | 78 | -10.1 | -8.5 | 44.9% | -1.01 |
| SPY gap <= -0.5% | last_24m | 63 | +20.1 | +0.5 | 50.8% | 0.91 |
| SPY after 3 up days | last_24m | 84 | +2.0 | -0.4 | 50.0% | 0.34 |
| SPY after a -1% day | last_24m | 54 | +46.9 | +34.5 | 61.1% | 1.91 |
| SPY all sessions | last_12m | 251 | +0.5 | -0.8 | 49.8% | 0.12 |
| SPY gap >= +0.5% | last_12m | 45 | -6.1 | -9.8 | 42.2% | -0.54 |
| SPY gap <= -0.5% | last_12m | 29 | +4.4 | -3.0 | 44.8% | 0.32 |
| SPY after 3 up days | last_12m | 38 | -1.4 | +1.7 | 52.6% | -0.16 |
| SPY after a -1% day | last_12m | 26 | +14.8 | +3.3 | 53.8% | 0.94 |

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
| 2026 | 201 | 49.8% | +1.6 |

_Current index membership (survivorship bias favours longs slightly). Research output, not investment advice._
