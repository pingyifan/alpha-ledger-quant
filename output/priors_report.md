# Playbook priors, backtested on the full panel

901 tickers, 2016-01-04 to 2026-11-20, 2,347,450 stock-days (2,296,183 pass the ledger's price and liquidity filter). Every row measures the **open-to-close return of the session after the condition is known**, before costs; the ledger pays about 4 bps per round trip. Continuation = share of sessions where the open-to-close move had the same sign as the gap or the prior move.

## Verdicts on the playbook's priors

| Prior | Verdict |
|---|---|
| long a stock that gapped up 2-5% (continuation) | no reliable edge (mean +1.3 bps, t = 1.02, n = 63,103) |
| long a stock that gapped up 5%+ (continuation) | supported: +23.5 bps/session for that side, clears 4 bps costs (t = 5.32, n = 12,729) |
| short a stock that gapped down 2-5% (continuation) | goes the other way: -19.3 bps/session for that side (t = -14.27, n = 59,714) |
| short a stock that gapped down 5%+ (continuation) | supported: +45.4 bps/session for that side, clears 4 bps costs (t = 8.68, n = 12,055) |
| fade a +5% gap (short) | goes the other way: -23.5 bps/session for that side (t = -5.32, n = 12,729) |
| fade a -5% gap (long) | goes the other way: -45.4 bps/session for that side (t = -8.68, n = 12,055) |
| day-two fade after a +10% day (short) | no reliable edge (mean -9.8 bps, t = -1.76, n = 7,610) |
| day-two bounce after a -10% day (long) | supported: +70.9 bps/session for that side, clears 4 bps costs (t = 9.12, n = 6,123) |
| oversold bounce after a -15% three-day drop (long) | supported: +34.3 bps/session for that side, clears 4 bps costs (t = 5.06, n = 8,400) |
| 20-day momentum top decile (long) | positive but inside costs (+1.9 bps vs 4 bps, t = 4.01, n = 230,421) |
| 20-day momentum bottom decile (short) | goes the other way: -2.5 bps/session for that side (t = -4.85, n = 230,725) |

## 1. Overnight gap -> open-to-close

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | Continuation | t |
|---|---|---|---|---|---|---|---|
| gap <= -5% | full | 12,055 | -45.4 | -39.4 | 46.2% | 53.5% | -8.68 |
| -5% < gap <= -2% | full | 59,714 | +19.3 | +18.1 | 52.4% | 47.2% | 14.27 |
| -2% < gap <= -1% | full | 148,305 | +9.4 | +12.9 | 52.7% | 46.8% | 15.58 |
| -1% < gap <= -0.3% | full | 422,985 | +2.7 | +7.8 | 52.1% | 47.3% | 10.02 |
| flat (|gap| < 0.3%) | full | 869,403 | -0.1 | +2.1 | 50.5% | 48.5% | -0.78 |
| +0.3% <= gap < +1% | full | 535,782 | +0.3 | +0.0 | 49.6% | 49.6% | 1.29 |
| +1% <= gap < +2% | full | 172,107 | +6.0 | +3.8 | 50.7% | 50.7% | 11.04 |
| +2% <= gap < +5% | full | 63,103 | +1.3 | -6.0 | 48.9% | 48.9% | 1.02 |
| gap >= +5% | full | 12,729 | +23.5 | +0.0 | 49.9% | 49.9% | 5.32 |
| gap <= -5% | last_24m | 2,787 | -26.6 | -34.8 | 47.4% | 52.5% | -2.58 |
| -5% < gap <= -2% | last_24m | 14,678 | +22.0 | +33.2 | 54.7% | 45.1% | 7.73 |
| -2% < gap <= -1% | last_24m | 34,390 | +21.3 | +20.5 | 54.5% | 45.2% | 15.92 |
| -1% < gap <= -0.3% | last_24m | 87,052 | +5.5 | +7.1 | 51.9% | 47.7% | 8.7 |
| flat (|gap| < 0.3%) | last_24m | 152,275 | -1.4 | +0.0 | 49.5% | 48.3% | -3.42 |
| +0.3% <= gap < +1% | last_24m | 100,352 | -3.8 | -5.8 | 48.1% | 48.1% | -6.74 |
| +1% <= gap < +2% | last_24m | 39,324 | -3.4 | -7.6 | 48.2% | 48.2% | -2.96 |
| +2% <= gap < +5% | last_24m | 15,845 | -30.7 | -32.9 | 44.9% | 44.9% | -12.14 |
| gap >= +5% | last_24m | 3,022 | -49.5 | -55.8 | 43.4% | 43.4% | -5.75 |
| gap <= -5% | last_12m | 1,368 | +10.2 | +6.5 | 50.6% | 49.2% | 0.73 |
| -5% < gap <= -2% | last_12m | 7,672 | +11.7 | +24.4 | 53.4% | 46.2% | 3.08 |
| -2% < gap <= -1% | last_12m | 18,953 | +5.5 | +13.0 | 52.7% | 46.9% | 3.21 |
| -1% < gap <= -0.3% | last_12m | 44,062 | +1.9 | +4.6 | 51.1% | 48.5% | 2.09 |
| flat (|gap| < 0.3%) | last_12m | 70,160 | -1.6 | -2.1 | 49.1% | 48.3% | -2.41 |
| +0.3% <= gap < +1% | last_12m | 49,476 | -3.4 | -8.0 | 47.5% | 47.5% | -4.04 |
| +1% <= gap < +2% | last_12m | 23,329 | -3.5 | -12.4 | 47.2% | 47.2% | -2.31 |
| +2% <= gap < +5% | last_12m | 9,167 | -0.4 | -11.3 | 48.2% | 48.2% | -0.14 |
| gap >= +5% | last_12m | 1,656 | -20.8 | -34.0 | 45.8% | 45.8% | -1.81 |

## 2. Day two after a big close-to-close move

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | Continuation | t |
|---|---|---|---|---|---|---|---|
| yesterday +10% or more | full | 7,610 | -9.8 | -14.3 | 48.1% | 48.1% | -1.76 |
| yesterday +5% to +10% | full | 38,069 | +0.3 | -1.4 | 49.5% | 49.5% | 0.21 |
| yesterday -5% to -10% | full | 36,086 | +19.3 | +15.7 | 52.1% | 47.5% | 10.16 |
| yesterday -10% or worse | full | 6,123 | +70.9 | +43.3 | 54.0% | 45.7% | 9.12 |
| yesterday +10% or more | last_24m | 1,775 | -46.9 | -53.4 | 43.5% | 43.5% | -4.78 |
| yesterday +5% to +10% | last_24m | 9,108 | +9.3 | +3.9 | 50.4% | 50.4% | 2.81 |
| yesterday -5% to -10% | last_24m | 8,617 | +30.1 | +21.7 | 53.4% | 46.4% | 7.51 |
| yesterday -10% or worse | last_24m | 1,508 | -9.0 | -4.1 | 49.1% | 50.7% | -0.76 |
| yesterday +10% or more | last_12m | 870 | +26.6 | +19.8 | 52.1% | 52.1% | 1.81 |
| yesterday +5% to +10% | last_12m | 5,559 | +23.9 | +23.0 | 53.1% | 53.1% | 5.47 |
| yesterday -5% to -10% | last_12m | 4,782 | -9.0 | -3.7 | 49.4% | 50.4% | -1.79 |
| yesterday -10% or worse | last_12m | 731 | -54.3 | -45.5 | 45.7% | 54.3% | -3.11 |

## 3. Three-day moves

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| 3-day return <= -15% | full | 8,400 | +34.3 | +11.8 | 50.9% | 5.06 |
| 3-day return -15% to -10% | full | 20,120 | +18.1 | +9.2 | 51.1% | 6.4 |
| 3-day return >= +15% | full | 11,322 | +0.5 | -4.1 | 49.3% | 0.12 |
| 3-day return <= -15% | last_24m | 2,114 | +12.3 | -6.7 | 49.2% | 1.08 |
| 3-day return -15% to -10% | last_24m | 5,043 | +19.1 | -2.6 | 49.6% | 3.15 |
| 3-day return >= +15% | last_24m | 2,644 | +9.5 | +4.7 | 50.6% | 1.23 |
| 3-day return <= -15% | last_12m | 952 | +27.3 | +12.2 | 51.0% | 1.94 |
| 3-day return -15% to -10% | last_12m | 2,658 | -15.9 | -17.7 | 46.9% | -2.26 |
| 3-day return >= +15% | last_12m | 1,537 | +23.1 | +17.9 | 52.6% | 2.22 |

## 4. 20-day momentum deciles

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| momentum top decile (20d) | full | 230,421 | +1.9 | +2.5 | 50.4% | 4.01 |
| momentum bottom decile (20d) | full | 230,725 | +2.5 | +1.6 | 50.2% | 4.85 |
| momentum top decile (20d) | last_24m | 45,090 | +1.4 | +1.2 | 50.1% | 1.14 |
| momentum bottom decile (20d) | last_24m | 45,179 | -1.3 | -1.4 | 49.5% | -1.04 |
| momentum top decile (20d) | last_12m | 22,590 | +5.1 | +0.0 | 49.9% | 2.82 |
| momentum bottom decile (20d) | last_12m | 22,679 | -4.1 | -2.1 | 49.3% | -2.3 |

## 5. Base rate: share of tradable stock-days that closed above the open

| Year | n | Share up | Mean OC (bps) |
|---|---|---|---|
| 2016 | 176,753 | 52.8% | +10.4 |
| 2017 | 197,549 | 51.4% | +2.6 |
| 2018 | 201,342 | 49.4% | -6.4 |
| 2019 | 205,494 | 52.7% | +6.7 |
| 2020 | 210,532 | 49.7% | +0.6 |
| 2021 | 216,688 | 50.2% | +0.7 |
| 2022 | 218,418 | 50.0% | +1.2 |
| 2023 | 219,501 | 51.5% | +6.0 |
| 2024 | 224,317 | 50.3% | -0.9 |
| 2025 | 224,018 | 51.0% | +4.2 |
| 2026 | 201,571 | 49.0% | -2.2 |

## 6. SPY conditionals

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| SPY all sessions | full | 2,738 | +1.8 | +5.2 | 53.9% | 1.12 |
| SPY gap >= +0.5% | full | 432 | +8.6 | +22.3 | 60.0% | 1.71 |
| SPY gap <= -0.5% | full | 349 | +5.7 | +6.8 | 53.6% | 0.83 |
| SPY after 3 up days | full | 439 | +1.4 | +4.5 | 52.8% | 0.55 |
| SPY after a -1% day | full | 300 | +7.2 | +1.0 | 51.7% | 0.91 |
| SPY all sessions | last_24m | 501 | +0.0 | +3.2 | 51.9% | 0.0 |
| SPY gap >= +0.5% | last_24m | 80 | -10.6 | -6.4 | 46.2% | -1.0 |
| SPY gap <= -0.5% | last_24m | 66 | +18.1 | +0.7 | 51.5% | 0.86 |
| SPY after 3 up days | last_24m | 82 | +2.0 | +1.7 | 51.2% | 0.33 |
| SPY after a -1% day | last_24m | 58 | +33.8 | +6.9 | 58.6% | 1.41 |
| SPY all sessions | last_12m | 251 | -2.3 | +0.9 | 51.0% | -0.51 |
| SPY gap >= +0.5% | last_12m | 43 | -1.4 | -7.2 | 44.2% | -0.12 |
| SPY gap <= -0.5% | last_12m | 31 | -1.1 | -2.6 | 48.4% | -0.08 |
| SPY after 3 up days | last_12m | 35 | +4.2 | +7.7 | 57.1% | 0.51 |
| SPY after a -1% day | last_12m | 28 | -10.7 | -11.7 | 46.4% | -0.56 |

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
| 2026 | 224 | 50.4% | -3.6 |

_Current index membership (survivorship bias favours longs slightly). Research output, not investment advice._
