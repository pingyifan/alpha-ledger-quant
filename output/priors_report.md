# Playbook priors, backtested on the full panel

902 tickers, 2016-01-04 to 2026-10-15, 2,326,826 stock-days (2,277,928 pass the ledger's price and liquidity filter). Every row measures the **open-to-close return of the session after the condition is known**, before costs; the ledger pays about 4 bps per round trip. Continuation = share of sessions where the open-to-close move had the same sign as the gap or the prior move.

## Verdicts on the playbook's priors

| Prior | Verdict |
|---|---|
| long a stock that gapped up 2-5% (continuation) | no reliable edge (mean +1.1 bps, t = 0.84, n = 61,996) |
| long a stock that gapped up 5%+ (continuation) | supported: +25.0 bps/session for that side, clears 4 bps costs (t = 5.57, n = 12,497) |
| short a stock that gapped down 2-5% (continuation) | goes the other way: -21.3 bps/session for that side (t = -15.71, n = 58,739) |
| short a stock that gapped down 5%+ (continuation) | supported: +43.3 bps/session for that side, clears 4 bps costs (t = 8.17, n = 11,787) |
| fade a +5% gap (short) | goes the other way: -25.0 bps/session for that side (t = -5.57, n = 12,497) |
| fade a -5% gap (long) | goes the other way: -43.3 bps/session for that side (t = -8.17, n = 11,787) |
| day-two fade after a +10% day (short) | no reliable edge (mean -10.7 bps, t = -1.89, n = 7,532) |
| day-two bounce after a -10% day (long) | supported: +80.4 bps/session for that side, clears 4 bps costs (t = 10.13, n = 5,960) |
| oversold bounce after a -15% three-day drop (long) | supported: +36.4 bps/session for that side, clears 4 bps costs (t = 5.25, n = 8,171) |
| 20-day momentum top decile (long) | positive but inside costs (+2.1 bps vs 4 bps, t = 4.43, n = 228,638) |
| 20-day momentum bottom decile (short) | goes the other way: -3.2 bps/session for that side (t = -6.36, n = 228,867) |

## 1. Overnight gap -> open-to-close

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | Continuation | t |
|---|---|---|---|---|---|---|---|
| gap <= -5% | full | 11,787 | -43.3 | -38.1 | 46.4% | 53.3% | -8.17 |
| -5% < gap <= -2% | full | 58,739 | +21.3 | +19.1 | 52.6% | 47.0% | 15.71 |
| -2% < gap <= -1% | full | 146,181 | +9.8 | +13.1 | 52.7% | 46.8% | 16.16 |
| -1% < gap <= -0.3% | full | 419,466 | +2.9 | +7.9 | 52.1% | 47.3% | 10.8 |
| flat (|gap| < 0.3%) | full | 866,286 | +0.0 | +2.2 | 50.5% | 48.5% | 0.17 |
| +0.3% <= gap < +1% | full | 531,724 | +0.4 | +0.0 | 49.6% | 49.6% | 1.93 |
| +1% <= gap < +2% | full | 169,252 | +6.4 | +4.1 | 50.7% | 50.7% | 11.78 |
| +2% <= gap < +5% | full | 61,996 | +1.1 | -6.7 | 48.8% | 48.8% | 0.84 |
| gap >= +5% | full | 12,497 | +25.0 | +0.0 | 50.0% | 50.0% | 5.57 |
| gap <= -5% | last_24m | 2,638 | -15.1 | -19.3 | 48.6% | 51.3% | -1.44 |
| -5% < gap <= -2% | last_24m | 13,876 | +30.2 | +38.7 | 55.4% | 44.4% | 10.51 |
| -2% < gap <= -1% | last_24m | 33,222 | +23.8 | +21.5 | 54.7% | 45.0% | 17.54 |
| -1% < gap <= -0.3% | last_24m | 87,569 | +6.2 | +7.6 | 52.1% | 47.5% | 9.95 |
| flat (|gap| < 0.3%) | last_24m | 156,424 | -0.9 | +0.0 | 49.7% | 48.4% | -2.19 |
| +0.3% <= gap < +1% | last_24m | 100,776 | -3.8 | -5.9 | 48.0% | 48.0% | -6.74 |
| +1% <= gap < +2% | last_24m | 37,494 | -2.5 | -7.4 | 48.2% | 48.2% | -2.16 |
| +2% <= gap < +5% | last_24m | 15,270 | -32.2 | -34.4 | 44.5% | 44.5% | -12.58 |
| gap >= +5% | last_24m | 3,095 | -33.4 | -40.9 | 45.2% | 45.2% | -3.92 |
| gap <= -5% | last_12m | 1,225 | +49.8 | +30.4 | 53.1% | 46.8% | 3.43 |
| -5% < gap <= -2% | last_12m | 7,123 | +31.4 | +35.7 | 55.1% | 44.5% | 8.23 |
| -2% < gap <= -1% | last_12m | 18,064 | +7.1 | +12.7 | 52.7% | 47.0% | 4.1 |
| -1% < gap <= -0.3% | last_12m | 44,628 | +1.9 | +5.0 | 51.2% | 48.4% | 2.13 |
| flat (|gap| < 0.3%) | last_12m | 73,827 | -0.6 | -0.7 | 49.5% | 48.2% | -1.0 |
| +0.3% <= gap < +1% | last_12m | 49,406 | -2.6 | -7.3 | 47.7% | 47.7% | -3.19 |
| +1% <= gap < +2% | last_12m | 21,684 | -5.5 | -15.4 | 46.6% | 46.6% | -3.5 |
| +2% <= gap < +5% | last_12m | 8,498 | -13.4 | -21.9 | 46.5% | 46.5% | -3.96 |
| gap >= +5% | last_12m | 1,539 | -17.3 | -25.8 | 46.7% | 46.7% | -1.38 |

## 2. Day two after a big close-to-close move

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | Continuation | t |
|---|---|---|---|---|---|---|---|
| yesterday +10% or more | full | 7,532 | -10.7 | -15.7 | 48.0% | 48.0% | -1.89 |
| yesterday +5% to +10% | full | 37,336 | +0.9 | +0.0 | 49.6% | 49.6% | 0.56 |
| yesterday -5% to -10% | full | 35,450 | +22.5 | +17.8 | 52.4% | 47.2% | 11.75 |
| yesterday -10% or worse | full | 5,960 | +80.4 | +51.6 | 54.8% | 44.9% | 10.13 |
| yesterday +10% or more | last_24m | 1,820 | -57.0 | -67.6 | 42.0% | 42.0% | -5.99 |
| yesterday +5% to +10% | last_24m | 8,689 | +12.0 | +4.5 | 50.6% | 50.6% | 3.6 |
| yesterday -5% to -10% | last_24m | 8,141 | +43.2 | +29.7 | 54.6% | 45.2% | 10.69 |
| yesterday -10% or worse | last_24m | 1,391 | +11.7 | +7.3 | 50.7% | 49.1% | 0.95 |
| yesterday +10% or more | last_12m | 834 | +23.3 | +22.9 | 52.5% | 52.5% | 1.56 |
| yesterday +5% to +10% | last_12m | 5,028 | +28.4 | +27.4 | 54.2% | 54.2% | 6.3 |
| yesterday -5% to -10% | last_12m | 4,422 | +20.1 | +18.7 | 52.8% | 47.0% | 3.94 |
| yesterday -10% or worse | last_12m | 621 | -0.6 | -1.3 | 49.6% | 50.2% | -0.03 |

## 3. Three-day moves

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| 3-day return <= -15% | full | 8,171 | +36.4 | +13.1 | 51.0% | 5.25 |
| 3-day return -15% to -10% | full | 19,636 | +21.1 | +11.3 | 51.4% | 7.37 |
| 3-day return >= +15% | full | 11,207 | -0.8 | -5.1 | 49.1% | -0.19 |
| 3-day return <= -15% | last_24m | 1,943 | +12.4 | -7.0 | 49.0% | 1.03 |
| 3-day return -15% to -10% | last_24m | 4,670 | +29.4 | +4.2 | 50.5% | 4.67 |
| 3-day return >= +15% | last_24m | 2,650 | +6.7 | +1.0 | 50.1% | 0.87 |
| 3-day return <= -15% | last_12m | 796 | +41.9 | +23.5 | 51.3% | 2.81 |
| 3-day return -15% to -10% | last_12m | 2,348 | +3.8 | -9.3 | 48.9% | 0.52 |
| 3-day return >= +15% | last_12m | 1,498 | +16.2 | +11.0 | 51.9% | 1.51 |

## 4. 20-day momentum deciles

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| momentum top decile (20d) | full | 228,638 | +2.1 | +2.6 | 50.4% | 4.43 |
| momentum bottom decile (20d) | full | 228,867 | +3.2 | +1.9 | 50.2% | 6.36 |
| momentum top decile (20d) | last_24m | 45,154 | +2.5 | +1.6 | 50.2% | 2.06 |
| momentum bottom decile (20d) | last_24m | 45,168 | +1.9 | +0.0 | 49.7% | 1.6 |
| momentum top decile (20d) | last_12m | 22,654 | +4.6 | +0.0 | 49.8% | 2.52 |
| momentum bottom decile (20d) | last_12m | 22,668 | -0.1 | -1.6 | 49.4% | -0.07 |

## 5. Base rate: share of tradable stock-days that closed above the open

| Year | n | Share up | Mean OC (bps) |
|---|---|---|---|
| 2016 | 177,050 | 52.8% | +10.4 |
| 2017 | 197,848 | 51.4% | +2.7 |
| 2018 | 201,844 | 49.3% | -6.5 |
| 2019 | 205,998 | 52.7% | +6.7 |
| 2020 | 211,038 | 49.6% | +0.6 |
| 2021 | 217,191 | 50.2% | +0.7 |
| 2022 | 218,920 | 50.0% | +1.2 |
| 2023 | 220,147 | 51.5% | +6.0 |
| 2024 | 225,057 | 50.3% | -0.9 |
| 2025 | 224,491 | 51.0% | +4.2 |
| 2026 | 178,344 | 49.5% | +0.4 |

## 6. SPY conditionals

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| SPY all sessions | full | 2,712 | +2.3 | +5.2 | 53.9% | 1.41 |
| SPY gap >= +0.5% | full | 427 | +8.8 | +22.3 | 60.0% | 1.76 |
| SPY gap <= -0.5% | full | 343 | +6.3 | +8.0 | 53.6% | 0.91 |
| SPY after 3 up days | full | 437 | +1.5 | +4.5 | 52.9% | 0.57 |
| SPY after a -1% day | full | 293 | +9.3 | +3.3 | 52.2% | 1.16 |
| SPY all sessions | last_24m | 501 | +2.3 | +2.6 | 51.3% | 0.58 |
| SPY gap >= +0.5% | last_24m | 78 | -10.8 | -9.7 | 44.9% | -1.07 |
| SPY gap <= -0.5% | last_24m | 63 | +20.1 | +0.5 | 50.8% | 0.91 |
| SPY after 3 up days | last_24m | 84 | +2.0 | -0.4 | 50.0% | 0.34 |
| SPY after a -1% day | last_24m | 53 | +48.0 | +36.2 | 62.3% | 1.92 |
| SPY all sessions | last_12m | 251 | +1.0 | +0.1 | 50.2% | 0.25 |
| SPY gap >= +0.5% | last_12m | 44 | -6.0 | -9.7 | 43.2% | -0.52 |
| SPY gap <= -0.5% | last_12m | 29 | +4.4 | -3.0 | 44.8% | 0.32 |
| SPY after 3 up days | last_12m | 38 | -1.4 | +1.7 | 52.6% | -0.16 |
| SPY after a -1% day | last_12m | 25 | +15.8 | +5.7 | 56.0% | 0.97 |

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
| 2026 | 198 | 50.0% | +2.2 |

_Current index membership (survivorship bias favours longs slightly). Research output, not investment advice._
