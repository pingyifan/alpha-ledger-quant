# Playbook priors, backtested on the full panel

900 tickers, 2016-01-04 to 2026-11-18, 2,345,205 stock-days (2,294,000 pass the ledger's price and liquidity filter). Every row measures the **open-to-close return of the session after the condition is known**, before costs; the ledger pays about 4 bps per round trip. Continuation = share of sessions where the open-to-close move had the same sign as the gap or the prior move.

## Verdicts on the playbook's priors

| Prior | Verdict |
|---|---|
| long a stock that gapped up 2-5% (continuation) | no reliable edge (mean +1.9 bps, t = 1.49, n = 62,913) |
| long a stock that gapped up 5%+ (continuation) | supported: +23.7 bps/session for that side, clears 4 bps costs (t = 5.36, n = 12,685) |
| short a stock that gapped down 2-5% (continuation) | goes the other way: -20.1 bps/session for that side (t = -14.95, n = 59,573) |
| short a stock that gapped down 5%+ (continuation) | supported: +45.1 bps/session for that side, clears 4 bps costs (t = 8.62, n = 12,024) |
| fade a +5% gap (short) | goes the other way: -23.7 bps/session for that side (t = -5.36, n = 12,685) |
| fade a -5% gap (long) | goes the other way: -45.1 bps/session for that side (t = -8.62, n = 12,024) |
| day-two fade after a +10% day (short) | no reliable edge (mean -9.8 bps, t = -1.76, n = 7,570) |
| day-two bounce after a -10% day (long) | supported: +72.4 bps/session for that side, clears 4 bps costs (t = 9.3, n = 6,103) |
| oversold bounce after a -15% three-day drop (long) | supported: +34.3 bps/session for that side, clears 4 bps costs (t = 5.06, n = 8,379) |
| 20-day momentum top decile (long) | positive but inside costs (+2.0 bps vs 4 bps, t = 4.23, n = 230,244) |
| 20-day momentum bottom decile (short) | goes the other way: -2.8 bps/session for that side (t = -5.47, n = 230,456) |

## 1. Overnight gap -> open-to-close

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | Continuation | t |
|---|---|---|---|---|---|---|---|
| gap <= -5% | full | 12,024 | -45.1 | -39.4 | 46.3% | 53.4% | -8.62 |
| -5% < gap <= -2% | full | 59,573 | +20.1 | +18.5 | 52.5% | 47.1% | 14.95 |
| -2% < gap <= -1% | full | 148,079 | +9.7 | +13.2 | 52.7% | 46.8% | 16.08 |
| -1% < gap <= -0.3% | full | 422,572 | +2.8 | +7.9 | 52.1% | 47.3% | 10.54 |
| flat (|gap| < 0.3%) | full | 868,931 | -0.0 | +2.1 | 50.5% | 48.5% | -0.25 |
| +0.3% <= gap < +1% | full | 535,384 | +0.4 | +0.0 | 49.6% | 49.6% | 1.88 |
| +1% <= gap < +2% | full | 171,839 | +6.3 | +4.0 | 50.7% | 50.7% | 11.54 |
| +2% <= gap < +5% | full | 62,913 | +1.9 | -5.6 | 49.0% | 49.0% | 1.49 |
| gap >= +5% | full | 12,685 | +23.7 | +0.0 | 49.9% | 49.9% | 5.36 |
| gap <= -5% | last_24m | 2,759 | -25.6 | -33.8 | 47.5% | 52.4% | -2.47 |
| -5% < gap <= -2% | last_24m | 14,564 | +25.9 | +35.4 | 55.0% | 44.7% | 9.14 |
| -2% < gap <= -1% | last_24m | 34,543 | +23.7 | +22.6 | 54.9% | 44.7% | 17.8 |
| -1% < gap <= -0.3% | last_24m | 87,248 | +6.6 | +8.1 | 52.2% | 47.4% | 10.46 |
| flat (|gap| < 0.3%) | last_24m | 152,332 | -0.9 | +0.0 | 49.7% | 48.2% | -2.03 |
| +0.3% <= gap < +1% | last_24m | 100,137 | -3.1 | -5.2 | 48.2% | 48.2% | -5.44 |
| +1% <= gap < +2% | last_24m | 39,085 | -2.3 | -6.8 | 48.4% | 48.4% | -1.99 |
| +2% <= gap < +5% | last_24m | 15,673 | -28.6 | -31.3 | 45.0% | 45.0% | -11.39 |
| gap >= +5% | last_24m | 2,986 | -49.3 | -54.0 | 43.5% | 43.5% | -5.74 |
| gap <= -5% | last_12m | 1,344 | +12.5 | +8.8 | 50.9% | 48.9% | 0.88 |
| -5% < gap <= -2% | last_12m | 7,570 | +18.6 | +28.1 | 54.0% | 45.6% | 4.96 |
| -2% < gap <= -1% | last_12m | 18,770 | +7.8 | +14.6 | 53.1% | 46.5% | 4.6 |
| -1% < gap <= -0.3% | last_12m | 43,780 | +3.2 | +5.5 | 51.4% | 48.2% | 3.54 |
| flat (|gap| < 0.3%) | last_12m | 70,409 | -0.8 | -1.6 | 49.2% | 48.1% | -1.29 |
| +0.3% <= gap < +1% | last_12m | 49,578 | -2.8 | -7.6 | 47.6% | 47.6% | -3.38 |
| +1% <= gap < +2% | last_12m | 23,369 | -4.4 | -12.9 | 47.1% | 47.1% | -2.91 |
| +2% <= gap < +5% | last_12m | 9,130 | -3.9 | -12.3 | 48.0% | 48.0% | -1.21 |
| gap >= +5% | last_12m | 1,637 | -25.5 | -33.6 | 45.8% | 45.8% | -2.2 |

## 2. Day two after a big close-to-close move

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | Continuation | t |
|---|---|---|---|---|---|---|---|
| yesterday +10% or more | full | 7,570 | -9.8 | -14.3 | 48.1% | 48.1% | -1.76 |
| yesterday +5% to +10% | full | 37,997 | +0.3 | -1.2 | 49.5% | 49.5% | 0.18 |
| yesterday -5% to -10% | full | 35,990 | +19.5 | +16.1 | 52.1% | 47.5% | 10.29 |
| yesterday -10% or worse | full | 6,103 | +72.4 | +44.8 | 54.1% | 45.6% | 9.3 |
| yesterday +10% or more | last_24m | 1,740 | -48.3 | -53.4 | 43.5% | 43.5% | -4.88 |
| yesterday +5% to +10% | last_24m | 9,055 | +9.4 | +4.2 | 50.5% | 50.5% | 2.83 |
| yesterday -5% to -10% | last_24m | 8,531 | +31.5 | +23.7 | 53.6% | 46.2% | 7.86 |
| yesterday -10% or worse | last_24m | 1,488 | -3.9 | -2.4 | 49.5% | 50.3% | -0.33 |
| yesterday +10% or more | last_12m | 843 | +29.6 | +21.2 | 52.5% | 52.5% | 1.98 |
| yesterday +5% to +10% | last_12m | 5,505 | +22.5 | +23.1 | 53.1% | 53.1% | 5.15 |
| yesterday -5% to -10% | last_12m | 4,702 | -7.3 | +0.0 | 49.8% | 50.0% | -1.45 |
| yesterday -10% or worse | last_12m | 714 | -44.9 | -32.2 | 46.4% | 53.6% | -2.56 |

## 3. Three-day moves

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| 3-day return <= -15% | full | 8,379 | +34.3 | +12.2 | 51.0% | 5.06 |
| 3-day return -15% to -10% | full | 20,039 | +18.9 | +9.8 | 51.1% | 6.69 |
| 3-day return >= +15% | full | 11,265 | +0.3 | -4.1 | 49.3% | 0.08 |
| 3-day return <= -15% | last_24m | 2,103 | +13.3 | -5.7 | 49.4% | 1.16 |
| 3-day return -15% to -10% | last_24m | 4,978 | +22.8 | +0.0 | 49.9% | 3.75 |
| 3-day return >= +15% | last_24m | 2,591 | +9.0 | +4.2 | 50.5% | 1.17 |
| 3-day return <= -15% | last_12m | 932 | +26.7 | +17.3 | 51.3% | 1.9 |
| 3-day return -15% to -10% | last_12m | 2,587 | -10.5 | -14.8 | 47.4% | -1.48 |
| 3-day return >= +15% | last_12m | 1,500 | +22.2 | +18.4 | 52.7% | 2.12 |

## 4. 20-day momentum deciles

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| momentum top decile (20d) | full | 230,244 | +2.0 | +2.6 | 50.4% | 4.23 |
| momentum bottom decile (20d) | full | 230,456 | +2.8 | +1.8 | 50.2% | 5.47 |
| momentum top decile (20d) | last_24m | 45,090 | +2.3 | +2.4 | 50.4% | 1.91 |
| momentum bottom decile (20d) | last_24m | 45,090 | +0.6 | +0.0 | 49.7% | 0.48 |
| momentum top decile (20d) | last_12m | 22,590 | +4.9 | +0.9 | 50.1% | 2.74 |
| momentum bottom decile (20d) | last_12m | 22,590 | -2.5 | -1.5 | 49.4% | -1.39 |

## 5. Base rate: share of tradable stock-days that closed above the open

| Year | n | Share up | Mean OC (bps) |
|---|---|---|---|
| 2016 | 176,753 | 52.8% | +10.4 |
| 2017 | 197,552 | 51.4% | +2.6 |
| 2018 | 201,342 | 49.4% | -6.4 |
| 2019 | 205,494 | 52.7% | +6.7 |
| 2020 | 210,532 | 49.7% | +0.6 |
| 2021 | 216,688 | 50.2% | +0.7 |
| 2022 | 218,418 | 50.0% | +1.2 |
| 2023 | 219,501 | 51.5% | +6.0 |
| 2024 | 224,317 | 50.3% | -0.9 |
| 2025 | 223,855 | 51.0% | +4.2 |
| 2026 | 199,548 | 49.4% | -0.3 |

## 6. SPY conditionals

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| SPY all sessions | full | 2,736 | +2.0 | +5.3 | 53.9% | 1.27 |
| SPY gap >= +0.5% | full | 431 | +9.3 | +22.3 | 60.1% | 1.87 |
| SPY gap <= -0.5% | full | 349 | +5.7 | +6.8 | 53.6% | 0.83 |
| SPY after 3 up days | full | 439 | +1.4 | +4.5 | 52.8% | 0.55 |
| SPY after a -1% day | full | 299 | +8.3 | +1.0 | 51.8% | 1.07 |
| SPY all sessions | last_24m | 501 | +1.5 | +4.5 | 52.3% | 0.36 |
| SPY gap >= +0.5% | last_24m | 79 | -7.0 | -5.6 | 46.8% | -0.69 |
| SPY gap <= -0.5% | last_24m | 67 | +19.2 | +0.9 | 52.2% | 0.93 |
| SPY after 3 up days | last_24m | 82 | +2.0 | +1.7 | 51.2% | 0.33 |
| SPY after a -1% day | last_24m | 57 | +40.2 | +7.4 | 59.7% | 1.71 |
| SPY all sessions | last_12m | 251 | -0.9 | +2.6 | 51.4% | -0.21 |
| SPY gap >= +0.5% | last_12m | 43 | -1.7 | -7.2 | 44.2% | -0.14 |
| SPY gap <= -0.5% | last_12m | 31 | -1.1 | -2.6 | 48.4% | -0.08 |
| SPY after 3 up days | last_12m | 35 | +4.2 | +7.7 | 57.1% | 0.51 |
| SPY after a -1% day | last_12m | 27 | +1.2 | -9.8 | 48.1% | 0.08 |

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
| 2026 | 222 | 50.9% | -0.8 |

_Current index membership (survivorship bias favours longs slightly). Research output, not investment advice._
