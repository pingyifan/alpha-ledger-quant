# Playbook priors, backtested on the full panel

901 tickers, 2016-01-04 to 2026-11-13, 2,345,320 stock-days (2,294,094 pass the ledger's price and liquidity filter). Every row measures the **open-to-close return of the session after the condition is known**, before costs; the ledger pays about 4 bps per round trip. Continuation = share of sessions where the open-to-close move had the same sign as the gap or the prior move.

## Verdicts on the playbook's priors

| Prior | Verdict |
|---|---|
| long a stock that gapped up 2-5% (continuation) | no reliable edge (mean +2.1 bps, t = 1.68, n = 62,953) |
| long a stock that gapped up 5%+ (continuation) | supported: +24.0 bps/session for that side, clears 4 bps costs (t = 5.44, n = 12,707) |
| short a stock that gapped down 2-5% (continuation) | goes the other way: -20.2 bps/session for that side (t = -15.01, n = 59,540) |
| short a stock that gapped down 5%+ (continuation) | supported: +45.6 bps/session for that side, clears 4 bps costs (t = 8.7, n = 12,028) |
| fade a +5% gap (short) | goes the other way: -24.0 bps/session for that side (t = -5.44, n = 12,707) |
| fade a -5% gap (long) | goes the other way: -45.6 bps/session for that side (t = -8.7, n = 12,028) |
| day-two fade after a +10% day (short) | no reliable edge (mean -10.0 bps, t = -1.79, n = 7,601) |
| day-two bounce after a -10% day (long) | supported: +71.4 bps/session for that side, clears 4 bps costs (t = 9.18, n = 6,124) |
| oversold bounce after a -15% three-day drop (long) | supported: +35.0 bps/session for that side, clears 4 bps costs (t = 5.15, n = 8,393) |
| 20-day momentum top decile (long) | positive but inside costs (+2.0 bps vs 4 bps, t = 4.3, n = 230,186) |
| 20-day momentum bottom decile (short) | goes the other way: -2.9 bps/session for that side (t = -5.73, n = 230,560) |

## 1. Overnight gap -> open-to-close

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | Continuation | t |
|---|---|---|---|---|---|---|---|
| gap <= -5% | full | 12,028 | -45.6 | -39.6 | 46.2% | 53.5% | -8.7 |
| -5% < gap <= -2% | full | 59,540 | +20.2 | +18.7 | 52.5% | 47.1% | 15.01 |
| -2% < gap <= -1% | full | 147,755 | +9.9 | +13.3 | 52.8% | 46.8% | 16.41 |
| -1% < gap <= -0.3% | full | 422,093 | +2.9 | +7.9 | 52.1% | 47.3% | 10.88 |
| flat (|gap| < 0.3%) | full | 869,748 | +0.0 | +2.2 | 50.5% | 48.5% | 0.07 |
| +0.3% <= gap < +1% | full | 535,555 | +0.5 | +0.0 | 49.6% | 49.6% | 2.03 |
| +1% <= gap < +2% | full | 171,715 | +6.3 | +4.1 | 50.7% | 50.7% | 11.7 |
| +2% <= gap < +5% | full | 62,953 | +2.1 | -5.4 | 49.0% | 49.0% | 1.68 |
| gap >= +5% | full | 12,707 | +24.0 | +0.0 | 49.9% | 49.9% | 5.44 |
| gap <= -5% | last_24m | 2,764 | -27.8 | -34.9 | 47.5% | 52.4% | -2.67 |
| -5% < gap <= -2% | last_24m | 14,532 | +26.4 | +36.7 | 55.1% | 44.6% | 9.28 |
| -2% < gap <= -1% | last_24m | 34,309 | +24.3 | +23.2 | 55.0% | 44.6% | 18.17 |
| -1% < gap <= -0.3% | last_24m | 86,965 | +6.8 | +8.3 | 52.3% | 47.3% | 10.77 |
| flat (|gap| < 0.3%) | last_24m | 153,211 | -1.0 | +0.0 | 49.7% | 48.3% | -2.3 |
| +0.3% <= gap < +1% | last_24m | 100,404 | -3.1 | -5.2 | 48.3% | 48.3% | -5.49 |
| +1% <= gap < +2% | last_24m | 38,980 | -2.0 | -6.3 | 48.5% | 48.5% | -1.7 |
| +2% <= gap < +5% | last_24m | 15,709 | -27.8 | -31.0 | 45.1% | 45.1% | -10.99 |
| gap >= +5% | last_24m | 3,018 | -46.9 | -52.9 | 43.6% | 43.6% | -5.46 |
| gap <= -5% | last_12m | 1,348 | +15.9 | +11.0 | 51.1% | 48.7% | 1.11 |
| -5% < gap <= -2% | last_12m | 7,661 | +23.7 | +33.2 | 54.9% | 44.8% | 6.33 |
| -2% < gap <= -1% | last_12m | 18,751 | +9.9 | +17.3 | 53.6% | 46.1% | 5.86 |
| -1% < gap <= -0.3% | last_12m | 43,694 | +3.4 | +6.1 | 51.6% | 48.1% | 3.78 |
| flat (|gap| < 0.3%) | last_12m | 70,838 | -1.1 | -1.7 | 49.2% | 48.1% | -1.74 |
| +0.3% <= gap < +1% | last_12m | 49,570 | -2.6 | -7.3 | 47.7% | 47.7% | -3.14 |
| +1% <= gap < +2% | last_12m | 23,192 | -3.9 | -12.3 | 47.2% | 47.2% | -2.57 |
| +2% <= gap < +5% | last_12m | 9,123 | -2.4 | -11.5 | 48.2% | 48.2% | -0.75 |
| gap >= +5% | last_12m | 1,651 | -24.4 | -33.8 | 45.8% | 45.8% | -2.1 |

## 2. Day two after a big close-to-close move

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | Continuation | t |
|---|---|---|---|---|---|---|---|
| yesterday +10% or more | full | 7,601 | -10.0 | -14.4 | 48.1% | 48.1% | -1.79 |
| yesterday +5% to +10% | full | 38,034 | +0.5 | -1.2 | 49.5% | 49.5% | 0.29 |
| yesterday -5% to -10% | full | 35,917 | +20.2 | +16.7 | 52.2% | 47.4% | 10.6 |
| yesterday -10% or worse | full | 6,124 | +71.4 | +44.6 | 54.1% | 45.6% | 9.18 |
| yesterday +10% or more | last_24m | 1,773 | -47.6 | -53.5 | 43.4% | 43.4% | -4.84 |
| yesterday +5% to +10% | last_24m | 9,096 | +10.1 | +4.4 | 50.6% | 50.6% | 3.05 |
| yesterday -5% to -10% | last_24m | 8,506 | +33.9 | +25.2 | 53.9% | 45.9% | 8.4 |
| yesterday -10% or worse | last_24m | 1,517 | -10.2 | -4.1 | 49.2% | 50.6% | -0.86 |
| yesterday +10% or more | last_12m | 863 | +28.4 | +20.3 | 52.1% | 52.1% | 1.92 |
| yesterday +5% to +10% | last_12m | 5,535 | +23.3 | +23.6 | 53.1% | 53.1% | 5.33 |
| yesterday -5% to -10% | last_12m | 4,694 | +1.1 | +5.0 | 50.9% | 48.9% | 0.22 |
| yesterday -10% or worse | last_12m | 735 | -44.5 | -32.8 | 46.4% | 53.6% | -2.5 |

## 3. Three-day moves

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| 3-day return <= -15% | full | 8,393 | +35.0 | +12.5 | 51.0% | 5.15 |
| 3-day return -15% to -10% | full | 19,976 | +19.6 | +10.6 | 51.2% | 6.9 |
| 3-day return >= +15% | full | 11,313 | +0.5 | -4.1 | 49.3% | 0.13 |
| 3-day return <= -15% | last_24m | 2,132 | +13.0 | -6.8 | 49.2% | 1.14 |
| 3-day return -15% to -10% | last_24m | 4,948 | +25.4 | +2.6 | 50.3% | 4.16 |
| 3-day return >= +15% | last_24m | 2,643 | +9.2 | +4.7 | 50.6% | 1.18 |
| 3-day return <= -15% | last_12m | 944 | +34.9 | +23.5 | 51.8% | 2.43 |
| 3-day return -15% to -10% | last_12m | 2,579 | -1.4 | -7.7 | 48.8% | -0.2 |
| 3-day return >= +15% | last_12m | 1,531 | +22.8 | +17.9 | 52.6% | 2.18 |

## 4. 20-day momentum deciles

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| momentum top decile (20d) | full | 230,186 | +2.0 | +2.6 | 50.4% | 4.3 |
| momentum bottom decile (20d) | full | 230,560 | +2.9 | +1.9 | 50.2% | 5.73 |
| momentum top decile (20d) | last_24m | 45,090 | +2.2 | +1.9 | 50.3% | 1.77 |
| momentum bottom decile (20d) | last_24m | 45,175 | +1.2 | +0.0 | 49.8% | 0.99 |
| momentum top decile (20d) | last_12m | 22,590 | +5.4 | +1.0 | 50.1% | 2.98 |
| momentum bottom decile (20d) | last_12m | 22,675 | -1.3 | +0.0 | 49.7% | -0.72 |

## 5. Base rate: share of tradable stock-days that closed above the open

| Year | n | Share up | Mean OC (bps) |
|---|---|---|---|
| 2016 | 176,985 | 52.8% | +10.4 |
| 2017 | 197,803 | 51.4% | +2.6 |
| 2018 | 201,593 | 49.4% | -6.4 |
| 2019 | 205,746 | 52.6% | +6.7 |
| 2020 | 210,784 | 49.7% | +0.6 |
| 2021 | 216,940 | 50.2% | +0.7 |
| 2022 | 218,669 | 50.0% | +1.2 |
| 2023 | 219,751 | 51.5% | +6.0 |
| 2024 | 224,569 | 50.3% | -0.9 |
| 2025 | 224,187 | 51.0% | +4.2 |
| 2026 | 197,067 | 49.6% | +0.5 |

## 6. SPY conditionals

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| SPY all sessions | full | 2,733 | +2.1 | +5.4 | 54.0% | 1.32 |
| SPY gap >= +0.5% | full | 431 | +9.3 | +22.3 | 60.1% | 1.87 |
| SPY gap <= -0.5% | full | 348 | +6.1 | +7.4 | 53.7% | 0.89 |
| SPY after 3 up days | full | 439 | +1.4 | +4.5 | 52.8% | 0.55 |
| SPY after a -1% day | full | 297 | +8.8 | +1.1 | 52.2% | 1.12 |
| SPY all sessions | last_24m | 501 | +1.8 | +4.5 | 52.5% | 0.43 |
| SPY gap >= +0.5% | last_24m | 79 | -7.0 | -5.6 | 46.8% | -0.69 |
| SPY gap <= -0.5% | last_24m | 67 | +20.1 | +0.9 | 52.2% | 0.98 |
| SPY after 3 up days | last_24m | 82 | +2.0 | +1.7 | 51.2% | 0.33 |
| SPY after a -1% day | last_24m | 56 | +43.7 | +23.2 | 62.5% | 1.84 |
| SPY all sessions | last_12m | 251 | +0.1 | +3.2 | 51.8% | 0.03 |
| SPY gap >= +0.5% | last_12m | 43 | -1.7 | -7.2 | 44.2% | -0.14 |
| SPY gap <= -0.5% | last_12m | 32 | +5.1 | -1.0 | 50.0% | 0.4 |
| SPY after 3 up days | last_12m | 35 | +4.2 | +7.7 | 57.1% | 0.51 |
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
| 2026 | 219 | 51.6% | +0.3 |

_Current index membership (survivorship bias favours longs slightly). Research output, not investment advice._
