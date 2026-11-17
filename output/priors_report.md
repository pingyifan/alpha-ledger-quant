# Playbook priors, backtested on the full panel

898 tickers, 2016-01-04 to 2026-11-16, 2,338,019 stock-days (2,287,367 pass the ledger's price and liquidity filter). Every row measures the **open-to-close return of the session after the condition is known**, before costs; the ledger pays about 4 bps per round trip. Continuation = share of sessions where the open-to-close move had the same sign as the gap or the prior move.

## Verdicts on the playbook's priors

| Prior | Verdict |
|---|---|
| long a stock that gapped up 2-5% (continuation) | no reliable edge (mean +2.1 bps, t = 1.67, n = 62,843) |
| long a stock that gapped up 5%+ (continuation) | supported: +23.9 bps/session for that side, clears 4 bps costs (t = 5.42, n = 12,695) |
| short a stock that gapped down 2-5% (continuation) | goes the other way: -20.2 bps/session for that side (t = -14.95, n = 59,497) |
| short a stock that gapped down 5%+ (continuation) | supported: +45.5 bps/session for that side, clears 4 bps costs (t = 8.68, n = 12,038) |
| fade a +5% gap (short) | goes the other way: -23.9 bps/session for that side (t = -5.42, n = 12,695) |
| fade a -5% gap (long) | goes the other way: -45.5 bps/session for that side (t = -8.68, n = 12,038) |
| day-two fade after a +10% day (short) | no reliable edge (mean -9.8 bps, t = -1.75, n = 7,593) |
| day-two bounce after a -10% day (long) | supported: +70.8 bps/session for that side, clears 4 bps costs (t = 9.09, n = 6,109) |
| oversold bounce after a -15% three-day drop (long) | supported: +34.4 bps/session for that side, clears 4 bps costs (t = 5.06, n = 8,376) |
| 20-day momentum top decile (long) | positive but inside costs (+2.1 bps vs 4 bps, t = 4.32, n = 229,632) |
| 20-day momentum bottom decile (short) | goes the other way: -2.9 bps/session for that side (t = -5.76, n = 229,909) |

## 1. Overnight gap -> open-to-close

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | Continuation | t |
|---|---|---|---|---|---|---|---|
| gap <= -5% | full | 12,038 | -45.5 | -39.4 | 46.2% | 53.5% | -8.68 |
| -5% < gap <= -2% | full | 59,497 | +20.2 | +18.6 | 52.5% | 47.1% | 14.95 |
| -2% < gap <= -1% | full | 147,539 | +9.8 | +13.2 | 52.8% | 46.8% | 16.13 |
| -1% < gap <= -0.3% | full | 420,901 | +2.9 | +7.9 | 52.1% | 47.3% | 10.77 |
| flat (|gap| < 0.3%) | full | 866,385 | -0.0 | +2.1 | 50.5% | 48.5% | -0.2 |
| +0.3% <= gap < +1% | full | 534,020 | +0.4 | +0.0 | 49.6% | 49.6% | 1.94 |
| +1% <= gap < +2% | full | 171,449 | +6.3 | +4.1 | 50.7% | 50.7% | 11.6 |
| +2% <= gap < +5% | full | 62,843 | +2.1 | -5.4 | 49.0% | 49.0% | 1.67 |
| gap >= +5% | full | 12,695 | +23.9 | +0.0 | 49.9% | 49.9% | 5.42 |
| gap <= -5% | last_24m | 2,783 | -27.0 | -34.2 | 47.4% | 52.5% | -2.61 |
| -5% < gap <= -2% | last_24m | 14,555 | +26.0 | +35.7 | 55.0% | 44.7% | 9.16 |
| -2% < gap <= -1% | last_24m | 34,229 | +24.1 | +22.9 | 55.0% | 44.7% | 18.08 |
| -1% < gap <= -0.3% | last_24m | 86,413 | +7.0 | +8.5 | 52.3% | 47.3% | 11.01 |
| flat (|gap| < 0.3%) | last_24m | 151,983 | -0.7 | +0.0 | 49.8% | 48.3% | -1.55 |
| +0.3% <= gap < +1% | last_24m | 99,889 | -2.9 | -5.1 | 48.3% | 48.3% | -5.19 |
| +1% <= gap < +2% | last_24m | 38,967 | -2.1 | -6.4 | 48.5% | 48.5% | -1.8 |
| +2% <= gap < +5% | last_24m | 15,678 | -27.7 | -30.9 | 45.1% | 45.1% | -10.93 |
| gap >= +5% | last_24m | 3,006 | -46.8 | -52.9 | 43.6% | 43.6% | -5.43 |
| gap <= -5% | last_12m | 1,367 | +10.2 | +6.0 | 50.5% | 49.2% | 0.73 |
| -5% < gap <= -2% | last_12m | 7,596 | +18.6 | +28.2 | 54.0% | 45.6% | 4.96 |
| -2% < gap <= -1% | last_12m | 18,619 | +8.3 | +15.4 | 53.2% | 46.4% | 4.87 |
| -1% < gap <= -0.3% | last_12m | 43,418 | +3.0 | +5.7 | 51.4% | 48.2% | 3.29 |
| flat (|gap| < 0.3%) | last_12m | 70,560 | -1.4 | -1.9 | 49.1% | 48.1% | -2.08 |
| +0.3% <= gap < +1% | last_12m | 49,501 | -2.9 | -7.6 | 47.6% | 47.6% | -3.47 |
| +1% <= gap < +2% | last_12m | 23,251 | -4.2 | -12.3 | 47.2% | 47.2% | -2.73 |
| +2% <= gap < +5% | last_12m | 9,119 | -2.6 | -11.5 | 48.1% | 48.1% | -0.8 |
| gap >= +5% | last_12m | 1,648 | -24.5 | -34.0 | 45.8% | 45.8% | -2.1 |

## 2. Day two after a big close-to-close move

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | Continuation | t |
|---|---|---|---|---|---|---|---|
| yesterday +10% or more | full | 7,593 | -9.8 | -14.3 | 48.1% | 48.1% | -1.75 |
| yesterday +5% to +10% | full | 37,971 | +0.5 | -1.2 | 49.5% | 49.5% | 0.3 |
| yesterday -5% to -10% | full | 35,863 | +20.2 | +16.6 | 52.2% | 47.4% | 10.59 |
| yesterday -10% or worse | full | 6,109 | +70.8 | +43.5 | 54.0% | 45.6% | 9.09 |
| yesterday +10% or more | last_24m | 1,771 | -47.6 | -53.4 | 43.5% | 43.5% | -4.83 |
| yesterday +5% to +10% | last_24m | 9,068 | +10.3 | +4.5 | 50.6% | 50.6% | 3.11 |
| yesterday -5% to -10% | last_24m | 8,474 | +34.3 | +25.3 | 53.9% | 45.9% | 8.5 |
| yesterday -10% or worse | last_24m | 1,504 | -9.1 | -3.7 | 49.3% | 50.5% | -0.76 |
| yesterday +10% or more | last_12m | 862 | +28.8 | +20.6 | 52.2% | 52.2% | 1.95 |
| yesterday +5% to +10% | last_12m | 5,516 | +23.3 | +23.7 | 53.2% | 53.2% | 5.32 |
| yesterday -5% to -10% | last_12m | 4,651 | -2.7 | +2.8 | 50.4% | 49.4% | -0.53 |
| yesterday -10% or worse | last_12m | 726 | -54.7 | -45.7 | 45.7% | 54.3% | -3.11 |

## 3. Three-day moves

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| 3-day return <= -15% | full | 8,376 | +34.4 | +12.1 | 51.0% | 5.06 |
| 3-day return -15% to -10% | full | 19,949 | +19.6 | +10.7 | 51.2% | 6.91 |
| 3-day return >= +15% | full | 11,306 | +0.6 | -4.1 | 49.3% | 0.14 |
| 3-day return <= -15% | last_24m | 2,119 | +13.8 | -6.7 | 49.3% | 1.2 |
| 3-day return -15% to -10% | last_24m | 4,928 | +25.9 | +3.0 | 50.3% | 4.23 |
| 3-day return >= +15% | last_24m | 2,637 | +10.2 | +5.2 | 50.7% | 1.32 |
| 3-day return <= -15% | last_12m | 939 | +29.5 | +21.2 | 51.4% | 2.07 |
| 3-day return -15% to -10% | last_12m | 2,557 | -5.3 | -10.6 | 48.3% | -0.74 |
| 3-day return >= +15% | last_12m | 1,528 | +23.5 | +18.9 | 52.8% | 2.24 |

## 4. 20-day momentum deciles

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| momentum top decile (20d) | full | 229,632 | +2.1 | +2.6 | 50.4% | 4.32 |
| momentum bottom decile (20d) | full | 229,909 | +2.9 | +1.9 | 50.2% | 5.76 |
| momentum top decile (20d) | last_24m | 44,997 | +2.6 | +2.3 | 50.4% | 2.14 |
| momentum bottom decile (20d) | last_24m | 45,000 | +1.3 | +0.0 | 49.9% | 1.02 |
| momentum top decile (20d) | last_12m | 22,590 | +4.9 | +0.0 | 50.0% | 2.72 |
| momentum bottom decile (20d) | last_12m | 22,590 | -2.3 | -1.3 | 49.5% | -1.29 |

## 5. Base rate: share of tradable stock-days that closed above the open

| Year | n | Share up | Mean OC (bps) |
|---|---|---|---|
| 2016 | 176,521 | 52.8% | +10.4 |
| 2017 | 197,277 | 51.4% | +2.6 |
| 2018 | 200,894 | 49.4% | -6.4 |
| 2019 | 204,990 | 52.7% | +6.6 |
| 2020 | 210,026 | 49.7% | +0.6 |
| 2021 | 216,184 | 50.2% | +0.7 |
| 2022 | 217,916 | 50.0% | +1.2 |
| 2023 | 219,001 | 51.5% | +6.0 |
| 2024 | 223,813 | 50.3% | -0.9 |
| 2025 | 223,437 | 51.0% | +4.2 |
| 2026 | 197,308 | 49.5% | +0.0 |

## 6. SPY conditionals

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| SPY all sessions | full | 2,734 | +2.1 | +5.4 | 53.9% | 1.29 |
| SPY gap >= +0.5% | full | 431 | +9.3 | +22.3 | 60.1% | 1.87 |
| SPY gap <= -0.5% | full | 349 | +5.7 | +6.8 | 53.6% | 0.83 |
| SPY after 3 up days | full | 439 | +1.4 | +4.5 | 52.8% | 0.55 |
| SPY after a -1% day | full | 297 | +8.8 | +1.1 | 52.2% | 1.12 |
| SPY all sessions | last_24m | 500 | +1.8 | +4.8 | 52.6% | 0.44 |
| SPY gap >= +0.5% | last_24m | 79 | -7.0 | -5.6 | 46.8% | -0.69 |
| SPY gap <= -0.5% | last_24m | 67 | +19.2 | +0.9 | 52.2% | 0.93 |
| SPY after 3 up days | last_24m | 82 | +2.0 | +1.7 | 51.2% | 0.33 |
| SPY after a -1% day | last_24m | 56 | +43.7 | +23.2 | 62.5% | 1.84 |
| SPY all sessions | last_12m | 251 | -0.8 | +2.6 | 51.4% | -0.18 |
| SPY gap >= +0.5% | last_12m | 43 | -1.7 | -7.2 | 44.2% | -0.14 |
| SPY gap <= -0.5% | last_12m | 32 | -2.1 | -2.8 | 46.9% | -0.16 |
| SPY after 3 up days | last_12m | 35 | +4.2 | +7.7 | 57.1% | 0.51 |
| SPY after a -1% day | last_12m | 25 | +6.3 | +0.9 | 52.0% | 0.38 |

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
| 2026 | 220 | 51.4% | -0.3 |

_Current index membership (survivorship bias favours longs slightly). Research output, not investment advice._
