# Playbook priors, backtested on the full panel

901 tickers, 2016-01-04 to 2026-11-11, 2,343,518 stock-days (2,292,291 pass the ledger's price and liquidity filter). Every row measures the **open-to-close return of the session after the condition is known**, before costs; the ledger pays about 4 bps per round trip. Continuation = share of sessions where the open-to-close move had the same sign as the gap or the prior move.

## Verdicts on the playbook's priors

| Prior | Verdict |
|---|---|
| long a stock that gapped up 2-5% (continuation) | no reliable edge (mean +2.2 bps, t = 1.73, n = 62,925) |
| long a stock that gapped up 5%+ (continuation) | supported: +24.1 bps/session for that side, clears 4 bps costs (t = 5.46, n = 12,705) |
| short a stock that gapped down 2-5% (continuation) | goes the other way: -20.1 bps/session for that side (t = -14.9, n = 59,462) |
| short a stock that gapped down 5%+ (continuation) | supported: +46.4 bps/session for that side, clears 4 bps costs (t = 8.84, n = 12,004) |
| fade a +5% gap (short) | goes the other way: -24.1 bps/session for that side (t = -5.46, n = 12,705) |
| fade a -5% gap (long) | goes the other way: -46.4 bps/session for that side (t = -8.84, n = 12,004) |
| day-two fade after a +10% day (short) | no reliable edge (mean -10.6 bps, t = -1.9, n = 7,592) |
| day-two bounce after a -10% day (long) | supported: +71.2 bps/session for that side, clears 4 bps costs (t = 9.15, n = 6,117) |
| oversold bounce after a -15% three-day drop (long) | supported: +34.9 bps/session for that side, clears 4 bps costs (t = 5.13, n = 8,387) |
| 20-day momentum top decile (long) | positive but inside costs (+2.1 bps vs 4 bps, t = 4.48, n = 230,006) |
| 20-day momentum bottom decile (short) | goes the other way: -2.9 bps/session for that side (t = -5.68, n = 230,377) |

## 1. Overnight gap -> open-to-close

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | Continuation | t |
|---|---|---|---|---|---|---|---|
| gap <= -5% | full | 12,004 | -46.4 | -40.3 | 46.2% | 53.5% | -8.84 |
| -5% < gap <= -2% | full | 59,462 | +20.1 | +18.6 | 52.5% | 47.1% | 14.9 |
| -2% < gap <= -1% | full | 147,647 | +10.0 | +13.3 | 52.8% | 46.8% | 16.48 |
| -1% < gap <= -0.3% | full | 421,934 | +3.0 | +8.0 | 52.2% | 47.3% | 11.01 |
| flat (|gap| < 0.3%) | full | 869,364 | +0.0 | +2.2 | 50.5% | 48.5% | 0.28 |
| +0.3% <= gap < +1% | full | 534,737 | +0.6 | +0.0 | 49.7% | 49.7% | 2.42 |
| +1% <= gap < +2% | full | 171,513 | +6.5 | +4.3 | 50.8% | 50.8% | 11.95 |
| +2% <= gap < +5% | full | 62,925 | +2.2 | -5.3 | 49.0% | 49.0% | 1.73 |
| gap >= +5% | full | 12,705 | +24.1 | +0.0 | 49.9% | 49.9% | 5.46 |
| gap <= -5% | last_24m | 2,744 | -31.2 | -39.4 | 47.2% | 52.7% | -2.98 |
| -5% < gap <= -2% | last_24m | 14,477 | +25.7 | +35.9 | 55.1% | 44.7% | 9.01 |
| -2% < gap <= -1% | last_24m | 34,288 | +24.4 | +23.2 | 55.0% | 44.6% | 18.25 |
| -1% < gap <= -0.3% | last_24m | 87,219 | +6.7 | +8.2 | 52.2% | 47.3% | 10.61 |
| flat (|gap| < 0.3%) | last_24m | 153,572 | -1.0 | +0.0 | 49.7% | 48.3% | -2.28 |
| +0.3% <= gap < +1% | last_24m | 100,016 | -2.9 | -5.0 | 48.3% | 48.3% | -5.16 |
| +1% <= gap < +2% | last_24m | 38,847 | -1.6 | -5.6 | 48.6% | 48.6% | -1.43 |
| +2% <= gap < +5% | last_24m | 15,695 | -27.6 | -30.9 | 45.1% | 45.1% | -10.93 |
| gap >= +5% | last_24m | 3,022 | -47.2 | -52.7 | 43.6% | 43.6% | -5.5 |
| gap <= -5% | last_12m | 1,326 | +9.2 | +5.3 | 50.4% | 49.4% | 0.63 |
| -5% < gap <= -2% | last_12m | 7,595 | +21.7 | +31.5 | 54.6% | 45.0% | 5.75 |
| -2% < gap <= -1% | last_12m | 18,747 | +9.2 | +16.8 | 53.5% | 46.2% | 5.43 |
| -1% < gap <= -0.3% | last_12m | 43,998 | +2.8 | +5.4 | 51.4% | 48.3% | 3.04 |
| flat (|gap| < 0.3%) | last_12m | 71,259 | -0.9 | -1.4 | 49.3% | 48.2% | -1.46 |
| +0.3% <= gap < +1% | last_12m | 49,070 | -1.7 | -6.1 | 48.0% | 48.0% | -1.99 |
| +1% <= gap < +2% | last_12m | 23,057 | -3.0 | -11.2 | 47.5% | 47.5% | -1.97 |
| +2% <= gap < +5% | last_12m | 9,114 | -2.3 | -11.4 | 48.2% | 48.2% | -0.71 |
| gap >= +5% | last_12m | 1,654 | -23.9 | -33.7 | 45.8% | 45.8% | -2.06 |

## 2. Day two after a big close-to-close move

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | Continuation | t |
|---|---|---|---|---|---|---|---|
| yesterday +10% or more | full | 7,592 | -10.6 | -15.0 | 48.0% | 48.0% | -1.9 |
| yesterday +5% to +10% | full | 37,997 | +0.2 | -1.5 | 49.5% | 49.5% | 0.15 |
| yesterday -5% to -10% | full | 35,900 | +20.2 | +16.7 | 52.2% | 47.4% | 10.62 |
| yesterday -10% or worse | full | 6,117 | +71.2 | +44.2 | 54.1% | 45.6% | 9.15 |
| yesterday +10% or more | last_24m | 1,768 | -49.5 | -56.5 | 43.2% | 43.2% | -5.03 |
| yesterday +5% to +10% | last_24m | 9,078 | +9.2 | +3.9 | 50.5% | 50.5% | 2.77 |
| yesterday -5% to -10% | last_24m | 8,508 | +33.8 | +25.0 | 53.9% | 45.9% | 8.4 |
| yesterday -10% or worse | last_24m | 1,515 | -11.9 | -4.4 | 49.0% | 50.8% | -1.0 |
| yesterday +10% or more | last_12m | 854 | +23.2 | +12.4 | 51.4% | 51.4% | 1.57 |
| yesterday +5% to +10% | last_12m | 5,517 | +21.6 | +21.0 | 52.9% | 52.9% | 4.94 |
| yesterday -5% to -10% | last_12m | 4,686 | +1.0 | +5.3 | 51.0% | 48.9% | 0.2 |
| yesterday -10% or worse | last_12m | 730 | -46.6 | -36.8 | 46.2% | 53.8% | -2.61 |

## 3. Three-day moves

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| 3-day return <= -15% | full | 8,387 | +34.9 | +12.4 | 51.0% | 5.13 |
| 3-day return -15% to -10% | full | 19,969 | +19.6 | +10.7 | 51.2% | 6.92 |
| 3-day return >= +15% | full | 11,277 | -0.4 | -5.0 | 49.2% | -0.1 |
| 3-day return <= -15% | last_24m | 2,135 | +12.6 | -7.0 | 49.1% | 1.1 |
| 3-day return -15% to -10% | last_24m | 4,953 | +25.1 | +2.1 | 50.2% | 4.11 |
| 3-day return >= +15% | last_24m | 2,636 | +5.0 | +1.1 | 50.1% | 0.65 |
| 3-day return <= -15% | last_12m | 940 | +34.0 | +22.6 | 51.6% | 2.36 |
| 3-day return -15% to -10% | last_12m | 2,567 | -1.1 | -7.1 | 48.9% | -0.15 |
| 3-day return >= +15% | last_12m | 1,500 | +15.7 | +10.1 | 51.7% | 1.48 |

## 4. 20-day momentum deciles

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| momentum top decile (20d) | full | 230,006 | +2.1 | +2.7 | 50.5% | 4.48 |
| momentum bottom decile (20d) | full | 230,377 | +2.9 | +1.9 | 50.2% | 5.68 |
| momentum top decile (20d) | last_24m | 45,090 | +2.4 | +2.1 | 50.3% | 1.94 |
| momentum bottom decile (20d) | last_24m | 45,173 | +0.7 | +0.0 | 49.7% | 0.55 |
| momentum top decile (20d) | last_12m | 22,590 | +5.4 | +1.1 | 50.1% | 2.96 |
| momentum bottom decile (20d) | last_12m | 22,673 | -2.2 | -1.3 | 49.5% | -1.22 |

## 5. Base rate: share of tradable stock-days that closed above the open

| Year | n | Share up | Mean OC (bps) |
|---|---|---|---|
| 2016 | 176,985 | 52.8% | +10.4 |
| 2017 | 197,803 | 51.4% | +2.6 |
| 2018 | 201,593 | 49.4% | -6.4 |
| 2019 | 205,746 | 52.6% | +6.7 |
| 2020 | 210,784 | 49.7% | +0.6 |
| 2021 | 216,939 | 50.2% | +0.7 |
| 2022 | 218,669 | 50.0% | +1.2 |
| 2023 | 219,751 | 51.5% | +6.0 |
| 2024 | 224,569 | 50.3% | -0.9 |
| 2025 | 224,187 | 51.0% | +4.2 |
| 2026 | 195,265 | 49.8% | +1.0 |

## 6. SPY conditionals

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| SPY all sessions | full | 2,731 | +2.1 | +5.4 | 54.0% | 1.33 |
| SPY gap >= +0.5% | full | 431 | +9.3 | +22.3 | 60.1% | 1.87 |
| SPY gap <= -0.5% | full | 347 | +6.0 | +6.8 | 53.6% | 0.87 |
| SPY after 3 up days | full | 439 | +1.4 | +4.5 | 52.8% | 0.55 |
| SPY after a -1% day | full | 297 | +8.8 | +1.1 | 52.2% | 1.12 |
| SPY all sessions | last_24m | 501 | +1.8 | +4.5 | 52.3% | 0.43 |
| SPY gap >= +0.5% | last_24m | 79 | -7.0 | -5.6 | 46.8% | -0.69 |
| SPY gap <= -0.5% | last_24m | 66 | +19.8 | +0.7 | 51.5% | 0.95 |
| SPY after 3 up days | last_24m | 83 | +1.6 | +0.1 | 50.6% | 0.27 |
| SPY after a -1% day | last_24m | 56 | +43.7 | +23.2 | 62.5% | 1.84 |
| SPY all sessions | last_12m | 251 | -0.3 | +2.6 | 51.4% | -0.07 |
| SPY gap >= +0.5% | last_12m | 43 | -1.7 | -7.2 | 44.2% | -0.14 |
| SPY gap <= -0.5% | last_12m | 31 | +3.9 | -2.6 | 48.4% | 0.3 |
| SPY after 3 up days | last_12m | 37 | +0.0 | +7.4 | 54.0% | 0.01 |
| SPY after a -1% day | last_12m | 26 | +9.8 | +0.9 | 53.8% | 0.61 |

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
| 2026 | 217 | 51.6% | +0.5 |

_Current index membership (survivorship bias favours longs slightly). Research output, not investment advice._
