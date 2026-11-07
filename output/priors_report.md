# Playbook priors, backtested on the full panel

902 tickers, 2016-01-04 to 2026-11-06, 2,343,105 stock-days (2,294,140 pass the ledger's price and liquidity filter). Every row measures the **open-to-close return of the session after the condition is known**, before costs; the ledger pays about 4 bps per round trip. Continuation = share of sessions where the open-to-close move had the same sign as the gap or the prior move.

## Verdicts on the playbook's priors

| Prior | Verdict |
|---|---|
| long a stock that gapped up 2-5% (continuation) | no reliable edge (mean +1.5 bps, t = 1.18, n = 62,975) |
| long a stock that gapped up 5%+ (continuation) | supported: +24.4 bps/session for that side, clears 4 bps costs (t = 5.5, n = 12,699) |
| short a stock that gapped down 2-5% (continuation) | goes the other way: -20.2 bps/session for that side (t = -14.96, n = 59,614) |
| short a stock that gapped down 5%+ (continuation) | supported: +46.0 bps/session for that side, clears 4 bps costs (t = 8.77, n = 12,051) |
| fade a +5% gap (short) | goes the other way: -24.4 bps/session for that side (t = -5.5, n = 12,699) |
| fade a -5% gap (long) | goes the other way: -46.0 bps/session for that side (t = -8.77, n = 12,051) |
| day-two fade after a +10% day (short) | no reliable edge (mean -11.1 bps, t = -1.98, n = 7,612) |
| day-two bounce after a -10% day (long) | supported: +72.0 bps/session for that side, clears 4 bps costs (t = 9.28, n = 6,149) |
| oversold bounce after a -15% three-day drop (long) | supported: +32.6 bps/session for that side, clears 4 bps costs (t = 4.79, n = 8,381) |
| 20-day momentum top decile (long) | positive but inside costs (+2.1 bps vs 4 bps, t = 4.37, n = 230,297) |
| 20-day momentum bottom decile (short) | goes the other way: -2.7 bps/session for that side (t = -5.33, n = 230,509) |

## 1. Overnight gap -> open-to-close

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | Continuation | t |
|---|---|---|---|---|---|---|---|
| gap <= -5% | full | 12,051 | -46.0 | -40.1 | 46.2% | 53.5% | -8.77 |
| -5% < gap <= -2% | full | 59,614 | +20.2 | +18.6 | 52.5% | 47.1% | 14.96 |
| -2% < gap <= -1% | full | 147,741 | +9.8 | +13.2 | 52.8% | 46.8% | 16.18 |
| -1% < gap <= -0.3% | full | 422,172 | +2.9 | +7.9 | 52.1% | 47.3% | 10.7 |
| flat (|gap| < 0.3%) | full | 869,976 | +0.0 | +2.2 | 50.5% | 48.5% | 0.1 |
| +0.3% <= gap < +1% | full | 535,290 | +0.5 | +0.0 | 49.6% | 49.6% | 2.17 |
| +1% <= gap < +2% | full | 171,622 | +6.2 | +4.1 | 50.7% | 50.7% | 11.42 |
| +2% <= gap < +5% | full | 62,975 | +1.5 | -6.0 | 48.9% | 48.9% | 1.18 |
| gap >= +5% | full | 12,699 | +24.4 | +0.0 | 49.9% | 49.9% | 5.5 |
| gap <= -5% | last_24m | 2,758 | -30.9 | -37.7 | 47.3% | 52.6% | -2.96 |
| -5% < gap <= -2% | last_24m | 14,443 | +25.7 | +35.7 | 55.0% | 44.7% | 9.0 |
| -2% < gap <= -1% | last_24m | 34,100 | +23.6 | +22.2 | 54.8% | 44.9% | 17.57 |
| -1% < gap <= -0.3% | last_24m | 87,092 | +6.2 | +7.5 | 52.1% | 47.5% | 9.82 |
| flat (|gap| < 0.3%) | last_24m | 154,222 | -0.9 | +0.0 | 49.7% | 48.3% | -2.25 |
| +0.3% <= gap < +1% | last_24m | 100,547 | -3.0 | -5.0 | 48.3% | 48.3% | -5.25 |
| +1% <= gap < +2% | last_24m | 38,752 | -2.5 | -6.4 | 48.5% | 48.5% | -2.17 |
| +2% <= gap < +5% | last_24m | 15,547 | -30.5 | -33.3 | 44.8% | 44.8% | -12.0 |
| gap >= +5% | last_24m | 2,994 | -48.2 | -54.4 | 43.4% | 43.4% | -5.54 |
| gap <= -5% | last_12m | 1,330 | +13.3 | +6.5 | 50.6% | 49.2% | 0.92 |
| -5% < gap <= -2% | last_12m | 7,569 | +23.6 | +33.4 | 54.8% | 44.8% | 6.21 |
| -2% < gap <= -1% | last_12m | 18,603 | +8.8 | +15.6 | 53.3% | 46.4% | 5.14 |
| -1% < gap <= -0.3% | last_12m | 43,929 | +2.6 | +5.1 | 51.3% | 48.4% | 2.86 |
| flat (|gap| < 0.3%) | last_12m | 71,815 | -0.5 | -0.8 | 49.4% | 48.2% | -0.7 |
| +0.3% <= gap < +1% | last_12m | 49,402 | -1.5 | -5.6 | 48.2% | 48.2% | -1.76 |
| +1% <= gap < +2% | last_12m | 22,831 | -5.5 | -13.2 | 47.0% | 47.0% | -3.56 |
| +2% <= gap < +5% | last_12m | 8,977 | -7.8 | -15.9 | 47.4% | 47.4% | -2.39 |
| gap >= +5% | last_12m | 1,603 | -26.1 | -35.5 | 45.4% | 45.4% | -2.19 |

## 2. Day two after a big close-to-close move

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | Continuation | t |
|---|---|---|---|---|---|---|---|
| yesterday +10% or more | full | 7,612 | -11.1 | -16.2 | 47.9% | 47.9% | -1.98 |
| yesterday +5% to +10% | full | 38,007 | -0.7 | -2.7 | 49.4% | 49.4% | -0.45 |
| yesterday -5% to -10% | full | 36,066 | +20.2 | +16.8 | 52.2% | 47.4% | 10.64 |
| yesterday -10% or worse | full | 6,149 | +72.0 | +44.8 | 54.1% | 45.6% | 9.28 |
| yesterday +10% or more | last_24m | 1,839 | -58.0 | -68.5 | 41.6% | 41.6% | -6.12 |
| yesterday +5% to +10% | last_24m | 9,127 | +5.1 | -0.7 | 49.7% | 49.7% | 1.56 |
| yesterday -5% to -10% | last_24m | 8,541 | +33.3 | +24.5 | 53.8% | 46.0% | 8.29 |
| yesterday -10% or worse | last_24m | 1,519 | -10.7 | -4.4 | 49.0% | 50.8% | -0.9 |
| yesterday +10% or more | last_12m | 835 | +19.3 | +17.2 | 51.6% | 51.6% | 1.3 |
| yesterday +5% to +10% | last_12m | 5,377 | +16.6 | +16.6 | 52.4% | 52.4% | 3.77 |
| yesterday -5% to -10% | last_12m | 4,710 | +2.3 | +6.6 | 51.1% | 48.7% | 0.45 |
| yesterday -10% or worse | last_12m | 730 | -45.5 | -36.8 | 46.2% | 53.8% | -2.55 |

## 3. Three-day moves

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| 3-day return <= -15% | full | 8,381 | +32.6 | +9.4 | 50.7% | 4.79 |
| 3-day return -15% to -10% | full | 20,011 | +18.9 | +10.1 | 51.2% | 6.68 |
| 3-day return >= +15% | full | 11,339 | -0.6 | -5.3 | 49.1% | -0.15 |
| 3-day return <= -15% | last_24m | 2,083 | -0.4 | -16.4 | 47.9% | -0.04 |
| 3-day return -15% to -10% | last_24m | 4,900 | +21.1 | -0.8 | 49.8% | 3.44 |
| 3-day return >= +15% | last_24m | 2,707 | +6.3 | +0.0 | 49.8% | 0.83 |
| 3-day return <= -15% | last_12m | 915 | +9.0 | -7.9 | 49.1% | 0.63 |
| 3-day return -15% to -10% | last_12m | 2,529 | -8.2 | -13.0 | 47.9% | -1.14 |
| 3-day return >= +15% | last_12m | 1,502 | +18.1 | +12.3 | 51.9% | 1.71 |

## 4. 20-day momentum deciles

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| momentum top decile (20d) | full | 230,297 | +2.1 | +2.6 | 50.4% | 4.37 |
| momentum bottom decile (20d) | full | 230,509 | +2.7 | +1.7 | 50.2% | 5.33 |
| momentum top decile (20d) | last_24m | 45,170 | +2.2 | +1.6 | 50.2% | 1.8 |
| momentum bottom decile (20d) | last_24m | 45,184 | -0.6 | -0.8 | 49.6% | -0.46 |
| momentum top decile (20d) | last_12m | 22,670 | +5.4 | +0.7 | 50.0% | 2.95 |
| momentum bottom decile (20d) | last_12m | 22,684 | -3.9 | -2.2 | 49.3% | -2.2 |

## 5. Base rate: share of tradable stock-days that closed above the open

| Year | n | Share up | Mean OC (bps) |
|---|---|---|---|
| 2016 | 177,217 | 52.8% | +10.4 |
| 2017 | 198,096 | 51.4% | +2.6 |
| 2018 | 202,095 | 49.4% | -6.4 |
| 2019 | 206,250 | 52.7% | +6.7 |
| 2020 | 211,291 | 49.7% | +0.6 |
| 2021 | 217,444 | 50.2% | +0.7 |
| 2022 | 219,171 | 50.0% | +1.2 |
| 2023 | 220,251 | 51.5% | +6.0 |
| 2024 | 225,057 | 50.3% | -0.9 |
| 2025 | 224,492 | 51.0% | +4.2 |
| 2026 | 192,776 | 49.5% | -0.1 |

## 6. SPY conditionals

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| SPY all sessions | full | 2,728 | +2.1 | +5.3 | 53.9% | 1.28 |
| SPY gap >= +0.5% | full | 429 | +8.9 | +22.3 | 59.9% | 1.78 |
| SPY gap <= -0.5% | full | 346 | +5.9 | +6.7 | 53.5% | 0.86 |
| SPY after 3 up days | full | 439 | +1.4 | +4.5 | 52.8% | 0.55 |
| SPY after a -1% day | full | 297 | +8.8 | +1.1 | 52.2% | 1.12 |
| SPY all sessions | last_24m | 501 | +1.5 | +3.2 | 52.1% | 0.36 |
| SPY gap >= +0.5% | last_24m | 77 | -9.6 | -7.2 | 45.5% | -0.94 |
| SPY gap <= -0.5% | last_24m | 65 | +19.7 | +0.5 | 50.8% | 0.93 |
| SPY after 3 up days | last_24m | 85 | +1.7 | +0.1 | 50.6% | 0.3 |
| SPY after a -1% day | last_24m | 56 | +43.7 | +23.2 | 62.5% | 1.84 |
| SPY all sessions | last_12m | 251 | -0.5 | +2.6 | 51.4% | -0.13 |
| SPY gap >= +0.5% | last_12m | 42 | -4.6 | -8.5 | 42.9% | -0.38 |
| SPY gap <= -0.5% | last_12m | 30 | +3.1 | -2.8 | 46.7% | 0.23 |
| SPY after 3 up days | last_12m | 37 | +0.0 | +7.4 | 54.0% | 0.01 |
| SPY after a -1% day | last_12m | 27 | +11.1 | +0.9 | 55.6% | 0.72 |

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
| 2026 | 214 | 50.9% | -0.5 |

_Current index membership (survivorship bias favours longs slightly). Research output, not investment advice._
