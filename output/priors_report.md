# Playbook priors, backtested on the full panel

900 tickers, 2016-01-04 to 2026-11-09, 2,338,987 stock-days (2,290,065 pass the ledger's price and liquidity filter). Every row measures the **open-to-close return of the session after the condition is known**, before costs; the ledger pays about 4 bps per round trip. Continuation = share of sessions where the open-to-close move had the same sign as the gap or the prior move.

## Verdicts on the playbook's priors

| Prior | Verdict |
|---|---|
| long a stock that gapped up 2-5% (continuation) | no reliable edge (mean +2.3 bps, t = 1.78, n = 62,833) |
| long a stock that gapped up 5%+ (continuation) | supported: +24.2 bps/session for that side, clears 4 bps costs (t = 5.46, n = 12,640) |
| short a stock that gapped down 2-5% (continuation) | goes the other way: -20.1 bps/session for that side (t = -14.85, n = 59,350) |
| short a stock that gapped down 5%+ (continuation) | supported: +46.4 bps/session for that side, clears 4 bps costs (t = 8.84, n = 11,992) |
| fade a +5% gap (short) | goes the other way: -24.2 bps/session for that side (t = -5.46, n = 12,640) |
| fade a -5% gap (long) | goes the other way: -46.4 bps/session for that side (t = -8.84, n = 11,992) |
| day-two fade after a +10% day (short) | no reliable edge (mean -10.6 bps, t = -1.9, n = 7,562) |
| day-two bounce after a -10% day (long) | supported: +71.4 bps/session for that side, clears 4 bps costs (t = 9.17, n = 6,112) |
| oversold bounce after a -15% three-day drop (long) | supported: +34.7 bps/session for that side, clears 4 bps costs (t = 5.1, n = 8,371) |
| 20-day momentum top decile (long) | positive but inside costs (+2.1 bps vs 4 bps, t = 4.46, n = 229,826) |
| 20-day momentum bottom decile (short) | goes the other way: -2.9 bps/session for that side (t = -5.58, n = 230,115) |

## 1. Overnight gap -> open-to-close

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | Continuation | t |
|---|---|---|---|---|---|---|---|
| gap <= -5% | full | 11,992 | -46.4 | -40.4 | 46.2% | 53.5% | -8.84 |
| -5% < gap <= -2% | full | 59,350 | +20.1 | +18.5 | 52.5% | 47.1% | 14.85 |
| -2% < gap <= -1% | full | 147,281 | +9.8 | +13.2 | 52.8% | 46.8% | 16.24 |
| -1% < gap <= -0.3% | full | 421,293 | +2.9 | +7.9 | 52.1% | 47.3% | 10.67 |
| flat (|gap| < 0.3%) | full | 868,842 | +0.0 | +2.2 | 50.5% | 48.5% | 0.19 |
| +0.3% <= gap < +1% | full | 534,477 | +0.5 | +0.0 | 49.7% | 49.7% | 2.37 |
| +1% <= gap < +2% | full | 171,357 | +6.5 | +4.3 | 50.8% | 50.8% | 11.9 |
| +2% <= gap < +5% | full | 62,833 | +2.3 | -5.2 | 49.0% | 49.0% | 1.78 |
| gap >= +5% | full | 12,640 | +24.2 | +0.0 | 49.9% | 49.9% | 5.46 |
| gap <= -5% | last_24m | 2,739 | -30.7 | -39.3 | 47.3% | 52.6% | -2.93 |
| -5% < gap <= -2% | last_24m | 14,375 | +25.5 | +35.9 | 55.0% | 44.7% | 8.9 |
| -2% < gap <= -1% | last_24m | 33,931 | +23.9 | +22.5 | 54.9% | 44.8% | 17.76 |
| -1% < gap <= -0.3% | last_24m | 86,654 | +6.3 | +7.6 | 52.1% | 47.5% | 9.91 |
| flat (|gap| < 0.3%) | last_24m | 153,293 | -1.0 | +0.0 | 49.7% | 48.3% | -2.43 |
| +0.3% <= gap < +1% | last_24m | 100,088 | -3.0 | -5.0 | 48.3% | 48.3% | -5.23 |
| +1% <= gap < +2% | last_24m | 38,880 | -1.5 | -5.5 | 48.7% | 48.7% | -1.31 |
| +2% <= gap < +5% | last_24m | 15,637 | -27.5 | -30.5 | 45.2% | 45.2% | -10.82 |
| gap >= +5% | last_24m | 2,966 | -47.6 | -53.5 | 43.5% | 43.5% | -5.45 |
| gap <= -5% | last_12m | 1,322 | +8.8 | +4.4 | 50.4% | 49.5% | 0.61 |
| -5% < gap <= -2% | last_12m | 7,515 | +21.5 | +31.6 | 54.6% | 45.0% | 5.66 |
| -2% < gap <= -1% | last_12m | 18,472 | +7.8 | +14.5 | 53.1% | 46.5% | 4.54 |
| -1% < gap <= -0.3% | last_12m | 43,631 | +1.9 | +4.6 | 51.1% | 48.5% | 2.11 |
| flat (|gap| < 0.3%) | last_12m | 71,436 | -0.8 | -1.3 | 49.3% | 48.2% | -1.29 |
| +0.3% <= gap < +1% | last_12m | 49,378 | -1.4 | -5.6 | 48.2% | 48.2% | -1.64 |
| +1% <= gap < +2% | last_12m | 23,086 | -3.3 | -11.5 | 47.4% | 47.4% | -2.17 |
| +2% <= gap < +5% | last_12m | 9,124 | -2.3 | -11.4 | 48.2% | 48.2% | -0.72 |
| gap >= +5% | last_12m | 1,597 | -24.9 | -35.3 | 45.6% | 45.6% | -2.08 |

## 2. Day two after a big close-to-close move

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | Continuation | t |
|---|---|---|---|---|---|---|---|
| yesterday +10% or more | full | 7,562 | -10.6 | -16.0 | 48.0% | 48.0% | -1.9 |
| yesterday +5% to +10% | full | 37,838 | +0.1 | -1.9 | 49.5% | 49.5% | 0.05 |
| yesterday -5% to -10% | full | 35,877 | +20.2 | +16.7 | 52.2% | 47.4% | 10.6 |
| yesterday -10% or worse | full | 6,112 | +71.4 | +43.8 | 54.1% | 45.6% | 9.17 |
| yesterday +10% or more | last_24m | 1,748 | -49.1 | -58.0 | 43.1% | 43.1% | -4.94 |
| yesterday +5% to +10% | last_24m | 8,943 | +8.9 | +3.0 | 50.3% | 50.3% | 2.63 |
| yesterday -5% to -10% | last_24m | 8,496 | +33.4 | +24.8 | 53.9% | 46.0% | 8.28 |
| yesterday -10% or worse | last_24m | 1,513 | -11.5 | -5.7 | 48.9% | 50.9% | -0.97 |
| yesterday +10% or more | last_12m | 833 | +26.5 | +17.2 | 51.6% | 51.6% | 1.75 |
| yesterday +5% to +10% | last_12m | 5,405 | +20.5 | +18.3 | 52.6% | 52.6% | 4.61 |
| yesterday -5% to -10% | last_12m | 4,683 | +0.7 | +6.0 | 51.0% | 48.8% | 0.14 |
| yesterday -10% or worse | last_12m | 726 | -46.1 | -38.3 | 46.0% | 54.0% | -2.59 |

## 3. Three-day moves

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| 3-day return <= -15% | full | 8,371 | +34.7 | +12.2 | 50.9% | 5.1 |
| 3-day return -15% to -10% | full | 19,947 | +19.7 | +10.7 | 51.2% | 6.93 |
| 3-day return >= +15% | full | 11,243 | -0.3 | -4.9 | 49.2% | -0.06 |
| 3-day return <= -15% | last_24m | 2,121 | +11.5 | -7.4 | 48.9% | 1.01 |
| 3-day return -15% to -10% | last_24m | 4,940 | +24.9 | +2.0 | 50.2% | 4.07 |
| 3-day return >= +15% | last_24m | 2,632 | +6.1 | +1.4 | 50.1% | 0.79 |
| 3-day return <= -15% | last_12m | 947 | +31.0 | +11.7 | 50.9% | 2.16 |
| 3-day return -15% to -10% | last_12m | 2,566 | -1.6 | -9.6 | 48.7% | -0.22 |
| 3-day return >= +15% | last_12m | 1,496 | +18.2 | +12.3 | 51.9% | 1.71 |

## 4. 20-day momentum deciles

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| momentum top decile (20d) | full | 229,826 | +2.1 | +2.7 | 50.4% | 4.46 |
| momentum bottom decile (20d) | full | 230,115 | +2.9 | +1.9 | 50.2% | 5.58 |
| momentum top decile (20d) | last_24m | 45,000 | +2.4 | +2.0 | 50.3% | 2.01 |
| momentum bottom decile (20d) | last_24m | 45,000 | +0.4 | +0.0 | 49.7% | 0.29 |
| momentum top decile (20d) | last_12m | 22,590 | +5.4 | +0.6 | 50.0% | 2.94 |
| momentum bottom decile (20d) | last_12m | 22,590 | -2.8 | -1.9 | 49.4% | -1.58 |

## 5. Base rate: share of tradable stock-days that closed above the open

| Year | n | Share up | Mean OC (bps) |
|---|---|---|---|
| 2016 | 176,985 | 52.8% | +10.4 |
| 2017 | 197,803 | 51.4% | +2.6 |
| 2018 | 201,593 | 49.4% | -6.4 |
| 2019 | 205,746 | 52.6% | +6.7 |
| 2020 | 210,785 | 49.7% | +0.6 |
| 2021 | 216,940 | 50.2% | +0.7 |
| 2022 | 218,669 | 50.0% | +1.2 |
| 2023 | 219,751 | 51.5% | +6.0 |
| 2024 | 224,553 | 50.3% | -0.9 |
| 2025 | 223,992 | 51.0% | +4.2 |
| 2026 | 193,248 | 49.7% | +0.6 |

## 6. SPY conditionals

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| SPY all sessions | full | 2,729 | +2.1 | +5.3 | 53.9% | 1.32 |
| SPY gap >= +0.5% | full | 430 | +9.2 | +22.3 | 60.0% | 1.85 |
| SPY gap <= -0.5% | full | 346 | +5.9 | +6.7 | 53.5% | 0.86 |
| SPY after 3 up days | full | 439 | +1.4 | +4.5 | 52.8% | 0.55 |
| SPY after a -1% day | full | 297 | +8.8 | +1.1 | 52.2% | 1.12 |
| SPY all sessions | last_24m | 500 | +1.6 | +3.2 | 52.0% | 0.39 |
| SPY gap >= +0.5% | last_24m | 78 | -7.6 | -6.4 | 46.2% | -0.74 |
| SPY gap <= -0.5% | last_24m | 65 | +19.7 | +0.5 | 50.8% | 0.93 |
| SPY after 3 up days | last_24m | 84 | +1.4 | -0.4 | 50.0% | 0.23 |
| SPY after a -1% day | last_24m | 56 | +43.7 | +23.2 | 62.5% | 1.84 |
| SPY all sessions | last_12m | 251 | -0.1 | +2.6 | 51.4% | -0.03 |
| SPY gap >= +0.5% | last_12m | 43 | -1.1 | -7.2 | 44.2% | -0.09 |
| SPY gap <= -0.5% | last_12m | 30 | +3.1 | -2.8 | 46.7% | 0.23 |
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
| 2026 | 215 | 51.2% | +0.2 |

_Current index membership (survivorship bias favours longs slightly). Research output, not investment advice._
