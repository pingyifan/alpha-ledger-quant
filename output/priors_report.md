# Playbook priors, backtested on the full panel

902 tickers, 2016-01-04 to 2026-10-21, 2,330,434 stock-days (2,281,537 pass the ledger's price and liquidity filter). Every row measures the **open-to-close return of the session after the condition is known**, before costs; the ledger pays about 4 bps per round trip. Continuation = share of sessions where the open-to-close move had the same sign as the gap or the prior move.

## Verdicts on the playbook's priors

| Prior | Verdict |
|---|---|
| long a stock that gapped up 2-5% (continuation) | no reliable edge (mean +0.8 bps, t = 0.61, n = 62,158) |
| long a stock that gapped up 5%+ (continuation) | supported: +24.5 bps/session for that side, clears 4 bps costs (t = 5.48, n = 12,520) |
| short a stock that gapped down 2-5% (continuation) | goes the other way: -21.3 bps/session for that side (t = -15.72, n = 58,816) |
| short a stock that gapped down 5%+ (continuation) | supported: +43.1 bps/session for that side, clears 4 bps costs (t = 8.14, n = 11,794) |
| fade a +5% gap (short) | goes the other way: -24.5 bps/session for that side (t = -5.48, n = 12,520) |
| fade a -5% gap (long) | goes the other way: -43.1 bps/session for that side (t = -8.14, n = 11,794) |
| day-two fade after a +10% day (short) | no reliable edge (mean -10.7 bps, t = -1.89, n = 7,538) |
| day-two bounce after a -10% day (long) | supported: +80.0 bps/session for that side, clears 4 bps costs (t = 10.09, n = 5,965) |
| oversold bounce after a -15% three-day drop (long) | supported: +35.1 bps/session for that side, clears 4 bps costs (t = 5.07, n = 8,202) |
| 20-day momentum top decile (long) | positive but inside costs (+2.1 bps vs 4 bps, t = 4.35, n = 229,003) |
| 20-day momentum bottom decile (short) | goes the other way: -3.1 bps/session for that side (t = -6.12, n = 229,231) |

## 1. Overnight gap -> open-to-close

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | Continuation | t |
|---|---|---|---|---|---|---|---|
| gap <= -5% | full | 11,794 | -43.1 | -37.9 | 46.4% | 53.3% | -8.14 |
| -5% < gap <= -2% | full | 58,816 | +21.3 | +19.1 | 52.6% | 47.0% | 15.72 |
| -2% < gap <= -1% | full | 146,421 | +9.8 | +13.1 | 52.7% | 46.8% | 16.23 |
| -1% < gap <= -0.3% | full | 420,065 | +2.9 | +7.9 | 52.1% | 47.3% | 10.84 |
| flat (|gap| < 0.3%) | full | 867,264 | +0.0 | +2.2 | 50.5% | 48.5% | 0.08 |
| +0.3% <= gap < +1% | full | 532,829 | +0.4 | +0.0 | 49.6% | 49.6% | 1.91 |
| +1% <= gap < +2% | full | 169,670 | +6.3 | +4.0 | 50.7% | 50.7% | 11.61 |
| +2% <= gap < +5% | full | 62,158 | +0.8 | -7.0 | 48.8% | 48.8% | 0.61 |
| gap >= +5% | full | 12,520 | +24.5 | +0.0 | 49.9% | 49.9% | 5.48 |
| gap <= -5% | last_24m | 2,638 | -14.7 | -17.6 | 48.7% | 51.2% | -1.39 |
| -5% < gap <= -2% | last_24m | 13,925 | +30.2 | +38.9 | 55.4% | 44.3% | 10.51 |
| -2% < gap <= -1% | last_24m | 33,393 | +24.0 | +21.9 | 54.8% | 44.9% | 17.73 |
| -1% < gap <= -0.3% | last_24m | 87,628 | +6.5 | +7.8 | 52.2% | 47.4% | 10.39 |
| flat (|gap| < 0.3%) | last_24m | 155,833 | -0.8 | +0.0 | 49.7% | 48.3% | -1.91 |
| +0.3% <= gap < +1% | last_24m | 100,877 | -3.7 | -5.6 | 48.1% | 48.1% | -6.54 |
| +1% <= gap < +2% | last_24m | 37,646 | -2.8 | -7.5 | 48.2% | 48.2% | -2.4 |
| +2% <= gap < +5% | last_24m | 15,339 | -32.8 | -34.7 | 44.5% | 44.5% | -12.87 |
| gap >= +5% | last_24m | 3,109 | -34.4 | -42.1 | 45.1% | 45.1% | -4.04 |
| gap <= -5% | last_12m | 1,223 | +53.2 | +34.7 | 53.5% | 46.4% | 3.66 |
| -5% < gap <= -2% | last_12m | 7,148 | +32.0 | +36.5 | 55.3% | 44.4% | 8.44 |
| -2% < gap <= -1% | last_12m | 18,166 | +7.6 | +13.3 | 52.8% | 46.8% | 4.42 |
| -1% < gap <= -0.3% | last_12m | 44,730 | +1.7 | +4.7 | 51.1% | 48.5% | 1.95 |
| flat (|gap| < 0.3%) | last_12m | 73,346 | -0.9 | -1.4 | 49.3% | 48.3% | -1.49 |
| +0.3% <= gap < +1% | last_12m | 49,437 | -2.7 | -7.5 | 47.6% | 47.6% | -3.24 |
| +1% <= gap < +2% | last_12m | 21,838 | -6.4 | -16.2 | 46.4% | 46.4% | -4.09 |
| +2% <= gap < +5% | last_12m | 8,578 | -14.7 | -23.3 | 46.2% | 46.2% | -4.4 |
| gap >= +5% | last_12m | 1,544 | -21.0 | -29.7 | 46.2% | 46.2% | -1.68 |

## 2. Day two after a big close-to-close move

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | Continuation | t |
|---|---|---|---|---|---|---|---|
| yesterday +10% or more | full | 7,538 | -10.7 | -16.0 | 48.0% | 48.0% | -1.89 |
| yesterday +5% to +10% | full | 37,422 | +0.7 | -0.6 | 49.6% | 49.6% | 0.4 |
| yesterday -5% to -10% | full | 35,505 | +22.2 | +17.7 | 52.4% | 47.3% | 11.63 |
| yesterday -10% or worse | full | 5,965 | +80.0 | +51.2 | 54.7% | 45.0% | 10.09 |
| yesterday +10% or more | last_24m | 1,821 | -56.9 | -67.6 | 41.9% | 41.9% | -5.99 |
| yesterday +5% to +10% | last_24m | 8,738 | +11.6 | +4.4 | 50.6% | 50.6% | 3.48 |
| yesterday -5% to -10% | last_24m | 8,164 | +42.5 | +28.8 | 54.5% | 45.3% | 10.52 |
| yesterday -10% or worse | last_24m | 1,390 | +11.4 | +6.7 | 50.6% | 49.1% | 0.92 |
| yesterday +10% or more | last_12m | 834 | +25.9 | +22.9 | 52.5% | 52.5% | 1.75 |
| yesterday +5% to +10% | last_12m | 5,072 | +26.8 | +25.7 | 53.9% | 53.9% | 5.96 |
| yesterday -5% to -10% | last_12m | 4,419 | +18.9 | +16.0 | 52.4% | 47.4% | 3.71 |
| yesterday -10% or worse | last_12m | 618 | -6.7 | -8.4 | 48.9% | 51.0% | -0.35 |

## 3. Three-day moves

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| 3-day return <= -15% | full | 8,202 | +35.1 | +11.2 | 50.8% | 5.07 |
| 3-day return -15% to -10% | full | 19,702 | +20.4 | +10.9 | 51.3% | 7.14 |
| 3-day return >= +15% | full | 11,207 | -0.8 | -5.3 | 49.1% | -0.21 |
| 3-day return <= -15% | last_24m | 1,973 | +7.7 | -13.4 | 48.4% | 0.65 |
| 3-day return -15% to -10% | last_24m | 4,725 | +27.1 | +2.7 | 50.3% | 4.34 |
| 3-day return >= +15% | last_24m | 2,644 | +6.6 | +0.8 | 50.0% | 0.86 |
| 3-day return <= -15% | last_12m | 826 | +29.8 | -2.7 | 49.6% | 2.03 |
| 3-day return -15% to -10% | last_12m | 2,400 | -2.3 | -13.0 | 48.1% | -0.32 |
| 3-day return >= +15% | last_12m | 1,484 | +18.2 | +12.2 | 52.0% | 1.69 |

## 4. 20-day momentum deciles

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| momentum top decile (20d) | full | 229,003 | +2.1 | +2.5 | 50.4% | 4.35 |
| momentum bottom decile (20d) | full | 229,231 | +3.1 | +1.8 | 50.2% | 6.12 |
| momentum top decile (20d) | last_24m | 45,158 | +2.4 | +1.6 | 50.2% | 1.94 |
| momentum bottom decile (20d) | last_24m | 45,172 | +1.5 | +0.0 | 49.7% | 1.28 |
| momentum top decile (20d) | last_12m | 22,658 | +4.9 | +0.0 | 49.9% | 2.71 |
| momentum bottom decile (20d) | last_12m | 22,672 | -1.6 | -3.1 | 49.1% | -0.92 |

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
| 2026 | 181,952 | 49.5% | +0.2 |

## 6. SPY conditionals

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| SPY all sessions | full | 2,716 | +2.3 | +5.2 | 53.9% | 1.4 |
| SPY gap >= +0.5% | full | 428 | +8.8 | +21.9 | 59.8% | 1.76 |
| SPY gap <= -0.5% | full | 343 | +6.3 | +8.0 | 53.6% | 0.91 |
| SPY after 3 up days | full | 437 | +1.5 | +4.5 | 52.9% | 0.57 |
| SPY after a -1% day | full | 294 | +9.2 | +2.2 | 52.0% | 1.16 |
| SPY all sessions | last_24m | 501 | +2.2 | +2.6 | 51.3% | 0.55 |
| SPY gap >= +0.5% | last_24m | 78 | -10.1 | -8.5 | 44.9% | -1.01 |
| SPY gap <= -0.5% | last_24m | 63 | +20.1 | +0.5 | 50.8% | 0.91 |
| SPY after 3 up days | last_24m | 83 | +2.1 | +0.1 | 50.6% | 0.35 |
| SPY after a -1% day | last_24m | 54 | +46.9 | +34.5 | 61.1% | 1.91 |
| SPY all sessions | last_12m | 251 | +0.6 | +0.1 | 50.2% | 0.14 |
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
| 2026 | 202 | 50.0% | +1.8 |

_Current index membership (survivorship bias favours longs slightly). Research output, not investment advice._
