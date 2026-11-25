# Playbook priors, backtested on the full panel

901 tickers, 2016-01-04 to 2026-11-24, 2,349,250 stock-days (2,297,983 pass the ledger's price and liquidity filter). Every row measures the **open-to-close return of the session after the condition is known**, before costs; the ledger pays about 4 bps per round trip. Continuation = share of sessions where the open-to-close move had the same sign as the gap or the prior move.

## Verdicts on the playbook's priors

| Prior | Verdict |
|---|---|
| long a stock that gapped up 2-5% (continuation) | no reliable edge (mean +1.4 bps, t = 1.12, n = 63,355) |
| long a stock that gapped up 5%+ (continuation) | supported: +21.7 bps/session for that side, clears 4 bps costs (t = 4.97, n = 12,906) |
| short a stock that gapped down 2-5% (continuation) | goes the other way: -18.9 bps/session for that side (t = -13.97, n = 59,797) |
| short a stock that gapped down 5%+ (continuation) | supported: +45.8 bps/session for that side, clears 4 bps costs (t = 8.76, n = 12,071) |
| fade a +5% gap (short) | goes the other way: -21.7 bps/session for that side (t = -4.97, n = 12,906) |
| fade a -5% gap (long) | goes the other way: -45.8 bps/session for that side (t = -8.76, n = 12,071) |
| day-two fade after a +10% day (short) | supported: +12.8 bps/session for that side, clears 4 bps costs (t = 2.31, n = 7,664) |
| day-two bounce after a -10% day (long) | supported: +68.6 bps/session for that side, clears 4 bps costs (t = 8.87, n = 6,163) |
| oversold bounce after a -15% three-day drop (long) | supported: +33.8 bps/session for that side, clears 4 bps costs (t = 4.99, n = 8,419) |
| 20-day momentum top decile (long) | positive but inside costs (+2.0 bps vs 4 bps, t = 4.15, n = 230,604) |
| 20-day momentum bottom decile (short) | goes the other way: -2.4 bps/session for that side (t = -4.71, n = 230,904) |

## 1. Overnight gap -> open-to-close

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | Continuation | t |
|---|---|---|---|---|---|---|---|
| gap <= -5% | full | 12,071 | -45.8 | -39.8 | 46.2% | 53.5% | -8.76 |
| -5% < gap <= -2% | full | 59,797 | +18.9 | +17.8 | 52.4% | 47.2% | 13.97 |
| -2% < gap <= -1% | full | 148,469 | +9.4 | +13.0 | 52.7% | 46.8% | 15.66 |
| -1% < gap <= -0.3% | full | 423,326 | +2.8 | +7.8 | 52.1% | 47.3% | 10.35 |
| flat (|gap| < 0.3%) | full | 869,784 | -0.1 | +2.1 | 50.5% | 48.5% | -0.48 |
| +0.3% <= gap < +1% | full | 535,995 | +0.3 | +0.0 | 49.6% | 49.6% | 1.5 |
| +1% <= gap < +2% | full | 172,280 | +6.0 | +3.8 | 50.7% | 50.7% | 11.14 |
| +2% <= gap < +5% | full | 63,355 | +1.4 | -5.7 | 48.9% | 48.9% | 1.12 |
| gap >= +5% | full | 12,906 | +21.7 | -2.5 | 49.6% | 49.6% | 4.97 |
| gap <= -5% | last_24m | 2,795 | -29.1 | -37.4 | 47.2% | 52.7% | -2.82 |
| -5% < gap <= -2% | last_24m | 14,760 | +20.3 | +31.4 | 54.4% | 45.3% | 7.15 |
| -2% < gap <= -1% | last_24m | 34,531 | +21.4 | +20.7 | 54.5% | 45.1% | 16.04 |
| -1% < gap <= -0.3% | last_24m | 87,253 | +5.7 | +7.3 | 52.0% | 47.6% | 9.07 |
| flat (|gap| < 0.3%) | last_24m | 151,891 | -1.7 | -0.7 | 49.5% | 48.2% | -4.0 |
| +0.3% <= gap < +1% | last_24m | 99,877 | -4.2 | -6.2 | 48.0% | 48.0% | -7.3 |
| +1% <= gap < +2% | last_24m | 39,375 | -3.5 | -7.8 | 48.1% | 48.1% | -3.09 |
| +2% <= gap < +5% | last_24m | 16,064 | -30.1 | -31.3 | 45.0% | 45.0% | -12.09 |
| gap >= +5% | last_24m | 3,191 | -53.0 | -59.1 | 42.8% | 42.8% | -6.47 |
| gap <= -5% | last_12m | 1,379 | +6.2 | +3.8 | 50.2% | 49.5% | 0.44 |
| -5% < gap <= -2% | last_12m | 7,754 | +8.8 | +22.4 | 53.0% | 46.7% | 2.32 |
| -2% < gap <= -1% | last_12m | 19,085 | +5.8 | +13.3 | 52.8% | 46.8% | 3.4 |
| -1% < gap <= -0.3% | last_12m | 44,162 | +2.5 | +5.1 | 51.2% | 48.4% | 2.7 |
| flat (|gap| < 0.3%) | last_12m | 69,760 | -1.9 | -2.2 | 49.1% | 48.1% | -2.94 |
| +0.3% <= gap < +1% | last_12m | 49,113 | -4.9 | -8.9 | 47.3% | 47.3% | -5.85 |
| +1% <= gap < +2% | last_12m | 23,372 | -4.3 | -12.6 | 47.1% | 47.1% | -2.84 |
| +2% <= gap < +5% | last_12m | 9,395 | -0.9 | -10.7 | 48.3% | 48.3% | -0.28 |
| gap >= +5% | last_12m | 1,826 | -29.7 | -38.3 | 44.4% | 44.4% | -2.81 |

## 2. Day two after a big close-to-close move

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | Continuation | t |
|---|---|---|---|---|---|---|---|
| yesterday +10% or more | full | 7,664 | -12.8 | -17.0 | 47.8% | 47.8% | -2.31 |
| yesterday +5% to +10% | full | 38,213 | +0.2 | -1.7 | 49.5% | 49.5% | 0.13 |
| yesterday -5% to -10% | full | 36,189 | +19.0 | +15.4 | 52.0% | 47.6% | 10.05 |
| yesterday -10% or worse | full | 6,163 | +68.6 | +41.1 | 53.8% | 45.9% | 8.87 |
| yesterday +10% or more | last_24m | 1,822 | -59.8 | -64.3 | 42.4% | 42.4% | -6.15 |
| yesterday +5% to +10% | last_24m | 9,229 | +8.4 | +2.7 | 50.2% | 50.2% | 2.54 |
| yesterday -5% to -10% | last_24m | 8,714 | +28.5 | +20.6 | 53.1% | 46.7% | 7.2 |
| yesterday -10% or worse | last_24m | 1,546 | -16.1 | -10.8 | 48.3% | 51.5% | -1.37 |
| yesterday +10% or more | last_12m | 922 | -0.5 | -1.4 | 49.6% | 49.6% | -0.04 |
| yesterday +5% to +10% | last_12m | 5,622 | +21.1 | +17.4 | 52.5% | 52.5% | 4.85 |
| yesterday -5% to -10% | last_12m | 4,834 | -11.5 | -6.4 | 48.9% | 50.9% | -2.29 |
| yesterday -10% or worse | last_12m | 763 | -65.7 | -52.6 | 44.3% | 55.7% | -3.86 |

## 3. Three-day moves

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| 3-day return <= -15% | full | 8,419 | +33.8 | +11.1 | 50.8% | 4.99 |
| 3-day return -15% to -10% | full | 20,193 | +17.6 | +8.8 | 51.0% | 6.24 |
| 3-day return >= +15% | full | 11,321 | +0.5 | -4.1 | 49.3% | 0.12 |
| 3-day return <= -15% | last_24m | 2,131 | +10.2 | -7.4 | 48.9% | 0.9 |
| 3-day return -15% to -10% | last_24m | 5,113 | +17.0 | -3.9 | 49.3% | 2.84 |
| 3-day return >= +15% | last_24m | 2,635 | +9.0 | +4.7 | 50.6% | 1.17 |
| 3-day return <= -15% | last_12m | 964 | +22.0 | +5.8 | 50.4% | 1.58 |
| 3-day return -15% to -10% | last_12m | 2,714 | -18.9 | -20.1 | 46.5% | -2.73 |
| 3-day return >= +15% | last_12m | 1,537 | +23.1 | +17.9 | 52.6% | 2.22 |

## 4. 20-day momentum deciles

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| momentum top decile (20d) | full | 230,604 | +2.0 | +2.5 | 50.4% | 4.15 |
| momentum bottom decile (20d) | full | 230,904 | +2.4 | +1.6 | 50.2% | 4.71 |
| momentum top decile (20d) | last_24m | 45,090 | +1.3 | +1.3 | 50.1% | 1.11 |
| momentum bottom decile (20d) | last_24m | 45,179 | -2.2 | -2.1 | 49.3% | -1.74 |
| momentum top decile (20d) | last_12m | 22,590 | +4.7 | +0.0 | 49.9% | 2.62 |
| momentum bottom decile (20d) | last_12m | 22,679 | -6.3 | -3.3 | 49.1% | -3.49 |

## 5. Base rate: share of tradable stock-days that closed above the open

| Year | n | Share up | Mean OC (bps) |
|---|---|---|---|
| 2016 | 176,753 | 52.8% | +10.4 |
| 2017 | 197,552 | 51.4% | +2.6 |
| 2018 | 201,342 | 49.4% | -6.4 |
| 2019 | 205,494 | 52.7% | +6.7 |
| 2020 | 210,532 | 49.7% | +0.6 |
| 2021 | 216,687 | 50.2% | +0.7 |
| 2022 | 218,418 | 50.0% | +1.2 |
| 2023 | 219,501 | 51.5% | +6.0 |
| 2024 | 224,315 | 50.3% | -0.9 |
| 2025 | 224,018 | 51.0% | +4.2 |
| 2026 | 203,371 | 49.2% | -1.8 |

## 6. SPY conditionals

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| SPY all sessions | full | 2,740 | +1.8 | +5.2 | 53.9% | 1.12 |
| SPY gap >= +0.5% | full | 433 | +8.5 | +22.3 | 59.8% | 1.7 |
| SPY gap <= -0.5% | full | 350 | +5.8 | +7.4 | 53.7% | 0.86 |
| SPY after 3 up days | full | 439 | +1.4 | +4.5 | 52.8% | 0.55 |
| SPY after a -1% day | full | 301 | +7.1 | +1.0 | 51.5% | 0.9 |
| SPY all sessions | last_24m | 501 | -0.0 | +3.2 | 51.7% | -0.0 |
| SPY gap >= +0.5% | last_24m | 81 | -10.8 | -7.2 | 45.7% | -1.03 |
| SPY gap <= -0.5% | last_24m | 67 | +18.5 | +0.9 | 52.2% | 0.9 |
| SPY after 3 up days | last_24m | 80 | +1.6 | -0.4 | 50.0% | 0.25 |
| SPY after a -1% day | last_24m | 59 | +32.7 | +6.4 | 57.6% | 1.39 |
| SPY all sessions | last_12m | 251 | -2.8 | +0.9 | 50.6% | -0.63 |
| SPY gap >= +0.5% | last_12m | 43 | -4.2 | -9.8 | 41.9% | -0.35 |
| SPY gap <= -0.5% | last_12m | 32 | +0.5 | -1.0 | 50.0% | 0.04 |
| SPY after 3 up days | last_12m | 35 | +4.2 | +7.7 | 57.1% | 0.51 |
| SPY after a -1% day | last_12m | 28 | -13.9 | -14.8 | 42.9% | -0.73 |

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
| 2026 | 226 | 50.4% | -3.5 |

_Current index membership (survivorship bias favours longs slightly). Research output, not investment advice._
