# Playbook priors, backtested on the full panel

900 tickers, 2016-01-04 to 2026-11-10, 2,339,887 stock-days (2,290,964 pass the ledger's price and liquidity filter). Every row measures the **open-to-close return of the session after the condition is known**, before costs; the ledger pays about 4 bps per round trip. Continuation = share of sessions where the open-to-close move had the same sign as the gap or the prior move.

## Verdicts on the playbook's priors

| Prior | Verdict |
|---|---|
| long a stock that gapped up 2-5% (continuation) | no reliable edge (mean +2.2 bps, t = 1.77, n = 62,832) |
| long a stock that gapped up 5%+ (continuation) | supported: +24.2 bps/session for that side, clears 4 bps costs (t = 5.46, n = 12,646) |
| short a stock that gapped down 2-5% (continuation) | goes the other way: -20.1 bps/session for that side (t = -14.85, n = 59,421) |
| short a stock that gapped down 5%+ (continuation) | supported: +46.5 bps/session for that side, clears 4 bps costs (t = 8.84, n = 11,995) |
| fade a +5% gap (short) | goes the other way: -24.2 bps/session for that side (t = -5.46, n = 12,646) |
| fade a -5% gap (long) | goes the other way: -46.5 bps/session for that side (t = -8.84, n = 11,995) |
| day-two fade after a +10% day (short) | no reliable edge (mean -10.6 bps, t = -1.9, n = 7,589) |
| day-two bounce after a -10% day (long) | supported: +71.1 bps/session for that side, clears 4 bps costs (t = 9.13, n = 6,113) |
| oversold bounce after a -15% three-day drop (long) | supported: +34.7 bps/session for that side, clears 4 bps costs (t = 5.1, n = 8,377) |
| 20-day momentum top decile (long) | positive but inside costs (+2.1 bps vs 4 bps, t = 4.46, n = 229,916) |
| 20-day momentum bottom decile (short) | goes the other way: -2.9 bps/session for that side (t = -5.62, n = 230,205) |

## 1. Overnight gap -> open-to-close

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | Continuation | t |
|---|---|---|---|---|---|---|---|
| gap <= -5% | full | 11,995 | -46.5 | -40.4 | 46.2% | 53.5% | -8.84 |
| -5% < gap <= -2% | full | 59,421 | +20.1 | +18.6 | 52.5% | 47.1% | 14.85 |
| -2% < gap <= -1% | full | 147,458 | +9.9 | +13.2 | 52.8% | 46.8% | 16.35 |
| -1% < gap <= -0.3% | full | 421,601 | +2.9 | +7.9 | 52.1% | 47.3% | 10.84 |
| flat (|gap| < 0.3%) | full | 869,073 | +0.0 | +2.2 | 50.5% | 48.5% | 0.24 |
| +0.3% <= gap < +1% | full | 534,579 | +0.5 | +0.0 | 49.7% | 49.7% | 2.4 |
| +1% <= gap < +2% | full | 171,359 | +6.5 | +4.3 | 50.8% | 50.8% | 11.91 |
| +2% <= gap < +5% | full | 62,832 | +2.2 | -5.2 | 49.0% | 49.0% | 1.77 |
| gap >= +5% | full | 12,646 | +24.2 | +0.0 | 49.9% | 49.9% | 5.46 |
| gap <= -5% | last_24m | 2,743 | -30.8 | -39.3 | 47.3% | 52.6% | -2.94 |
| -5% < gap <= -2% | last_24m | 14,444 | +25.5 | +35.8 | 55.1% | 44.7% | 8.93 |
| -2% < gap <= -1% | last_24m | 34,108 | +24.1 | +22.7 | 54.9% | 44.7% | 17.94 |
| -1% < gap <= -0.3% | last_24m | 86,964 | +6.5 | +7.8 | 52.2% | 47.4% | 10.26 |
| flat (|gap| < 0.3%) | last_24m | 153,524 | -1.0 | +0.0 | 49.7% | 48.3% | -2.33 |
| +0.3% <= gap < +1% | last_24m | 100,188 | -2.9 | -5.0 | 48.3% | 48.3% | -5.14 |
| +1% <= gap < +2% | last_24m | 38,881 | -1.5 | -5.5 | 48.7% | 48.7% | -1.33 |
| +2% <= gap < +5% | last_24m | 15,642 | -27.5 | -30.6 | 45.2% | 45.2% | -10.83 |
| gap >= +5% | last_24m | 2,969 | -47.6 | -53.2 | 43.5% | 43.5% | -5.45 |
| gap <= -5% | last_12m | 1,324 | +8.7 | +4.4 | 50.4% | 49.5% | 0.6 |
| -5% < gap <= -2% | last_12m | 7,578 | +21.5 | +31.5 | 54.6% | 45.0% | 5.69 |
| -2% < gap <= -1% | last_12m | 18,631 | +8.2 | +15.1 | 53.2% | 46.5% | 4.81 |
| -1% < gap <= -0.3% | last_12m | 43,809 | +2.2 | +4.9 | 51.2% | 48.4% | 2.47 |
| flat (|gap| < 0.3%) | last_12m | 71,386 | -0.8 | -1.3 | 49.3% | 48.3% | -1.23 |
| +0.3% <= gap < +1% | last_12m | 49,246 | -1.3 | -5.5 | 48.2% | 48.2% | -1.5 |
| +1% <= gap < +2% | last_12m | 22,960 | -3.1 | -11.3 | 47.5% | 47.5% | -1.99 |
| +2% <= gap < +5% | last_12m | 9,036 | -2.1 | -11.1 | 48.2% | 48.2% | -0.64 |
| gap >= +5% | last_12m | 1,595 | -24.9 | -35.3 | 45.6% | 45.6% | -2.08 |

## 2. Day two after a big close-to-close move

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | Continuation | t |
|---|---|---|---|---|---|---|---|
| yesterday +10% or more | full | 7,589 | -10.6 | -15.1 | 48.0% | 48.0% | -1.9 |
| yesterday +5% to +10% | full | 37,968 | +0.2 | -1.5 | 49.5% | 49.5% | 0.15 |
| yesterday -5% to -10% | full | 35,876 | +20.2 | +16.7 | 52.2% | 47.4% | 10.6 |
| yesterday -10% or worse | full | 6,113 | +71.1 | +43.5 | 54.1% | 45.6% | 9.13 |
| yesterday +10% or more | last_24m | 1,773 | -48.5 | -54.8 | 43.3% | 43.3% | -4.94 |
| yesterday +5% to +10% | last_24m | 9,076 | +9.3 | +3.9 | 50.5% | 50.5% | 2.81 |
| yesterday -5% to -10% | last_24m | 8,497 | +33.4 | +24.8 | 53.9% | 46.0% | 8.28 |
| yesterday -10% or worse | last_24m | 1,515 | -12.4 | -5.7 | 48.9% | 50.9% | -1.04 |
| yesterday +10% or more | last_12m | 852 | +23.1 | +12.4 | 51.4% | 51.4% | 1.56 |
| yesterday +5% to +10% | last_12m | 5,523 | +21.2 | +20.1 | 52.9% | 52.9% | 4.84 |
| yesterday -5% to -10% | last_12m | 4,677 | +0.9 | +6.0 | 51.0% | 48.8% | 0.18 |
| yesterday -10% or worse | last_12m | 727 | -47.5 | -37.5 | 46.1% | 53.9% | -2.65 |

## 3. Three-day moves

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| 3-day return <= -15% | full | 8,377 | +34.7 | +12.2 | 51.0% | 5.1 |
| 3-day return -15% to -10% | full | 19,963 | +19.6 | +10.7 | 51.2% | 6.92 |
| 3-day return >= +15% | full | 11,245 | -0.3 | -5.0 | 49.2% | -0.08 |
| 3-day return <= -15% | last_24m | 2,128 | +11.5 | -7.1 | 49.0% | 1.01 |
| 3-day return -15% to -10% | last_24m | 4,953 | +24.6 | +2.1 | 50.2% | 4.03 |
| 3-day return >= +15% | last_24m | 2,636 | +6.1 | +1.1 | 50.1% | 0.79 |
| 3-day return <= -15% | last_12m | 944 | +32.5 | +19.4 | 51.4% | 2.27 |
| 3-day return -15% to -10% | last_12m | 2,569 | -0.9 | -7.1 | 48.9% | -0.12 |
| 3-day return >= +15% | last_12m | 1,483 | +16.3 | +9.6 | 51.5% | 1.52 |

## 4. 20-day momentum deciles

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| momentum top decile (20d) | full | 229,916 | +2.1 | +2.7 | 50.4% | 4.46 |
| momentum bottom decile (20d) | full | 230,205 | +2.9 | +1.9 | 50.2% | 5.62 |
| momentum top decile (20d) | last_24m | 45,090 | +2.4 | +2.0 | 50.3% | 2.01 |
| momentum bottom decile (20d) | last_24m | 45,090 | +0.5 | +0.0 | 49.7% | 0.37 |
| momentum top decile (20d) | last_12m | 22,590 | +5.2 | +0.5 | 50.0% | 2.84 |
| momentum bottom decile (20d) | last_12m | 22,590 | -2.3 | -1.3 | 49.5% | -1.31 |

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
| 2024 | 224,553 | 50.3% | -0.9 |
| 2025 | 223,992 | 51.0% | +4.2 |
| 2026 | 194,148 | 49.7% | +0.8 |

## 6. SPY conditionals

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| SPY all sessions | full | 2,730 | +2.1 | +5.4 | 54.0% | 1.32 |
| SPY gap >= +0.5% | full | 430 | +9.2 | +22.3 | 60.0% | 1.85 |
| SPY gap <= -0.5% | full | 347 | +6.0 | +6.8 | 53.6% | 0.87 |
| SPY after 3 up days | full | 439 | +1.4 | +4.5 | 52.8% | 0.55 |
| SPY after a -1% day | full | 297 | +8.8 | +1.1 | 52.2% | 1.12 |
| SPY all sessions | last_24m | 501 | +1.7 | +3.2 | 52.1% | 0.41 |
| SPY gap >= +0.5% | last_24m | 78 | -7.6 | -6.4 | 46.2% | -0.74 |
| SPY gap <= -0.5% | last_24m | 66 | +19.8 | +0.7 | 51.5% | 0.95 |
| SPY after 3 up days | last_24m | 84 | +1.4 | -0.4 | 50.0% | 0.23 |
| SPY after a -1% day | last_24m | 56 | +43.7 | +23.2 | 62.5% | 1.84 |
| SPY all sessions | last_12m | 251 | -0.3 | +2.6 | 51.4% | -0.07 |
| SPY gap >= +0.5% | last_12m | 42 | -2.6 | -8.5 | 42.9% | -0.21 |
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
| 2026 | 216 | 51.4% | +0.3 |

_Current index membership (survivorship bias favours longs slightly). Research output, not investment advice._
