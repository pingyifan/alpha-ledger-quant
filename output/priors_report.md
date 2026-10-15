# Playbook priors, backtested on the full panel

902 tickers, 2016-01-04 to 2026-10-14, 2,325,923 stock-days (2,277,024 pass the ledger's price and liquidity filter). Every row measures the **open-to-close return of the session after the condition is known**, before costs; the ledger pays about 4 bps per round trip. Continuation = share of sessions where the open-to-close move had the same sign as the gap or the prior move.

## Verdicts on the playbook's priors

| Prior | Verdict |
|---|---|
| long a stock that gapped up 2-5% (continuation) | no reliable edge (mean +1.0 bps, t = 0.76, n = 61,919) |
| long a stock that gapped up 5%+ (continuation) | supported: +25.0 bps/session for that side, clears 4 bps costs (t = 5.58, n = 12,495) |
| short a stock that gapped down 2-5% (continuation) | goes the other way: -21.1 bps/session for that side (t = -15.53, n = 58,659) |
| short a stock that gapped down 5%+ (continuation) | supported: +43.7 bps/session for that side, clears 4 bps costs (t = 8.24, n = 11,769) |
| fade a +5% gap (short) | goes the other way: -25.0 bps/session for that side (t = -5.58, n = 12,495) |
| fade a -5% gap (long) | goes the other way: -43.7 bps/session for that side (t = -8.24, n = 11,769) |
| day-two fade after a +10% day (short) | no reliable edge (mean -10.7 bps, t = -1.9, n = 7,531) |
| day-two bounce after a -10% day (long) | supported: +80.1 bps/session for that side, clears 4 bps costs (t = 10.09, n = 5,955) |
| oversold bounce after a -15% three-day drop (long) | supported: +36.1 bps/session for that side, clears 4 bps costs (t = 5.2, n = 8,161) |
| 20-day momentum top decile (long) | positive but inside costs (+2.1 bps vs 4 bps, t = 4.34, n = 228,546) |
| 20-day momentum bottom decile (short) | goes the other way: -3.2 bps/session for that side (t = -6.21, n = 228,775) |

## 1. Overnight gap -> open-to-close

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | Continuation | t |
|---|---|---|---|---|---|---|---|
| gap <= -5% | full | 11,769 | -43.7 | -38.6 | 46.3% | 53.4% | -8.24 |
| -5% < gap <= -2% | full | 58,659 | +21.1 | +18.7 | 52.5% | 47.1% | 15.53 |
| -2% < gap <= -1% | full | 146,142 | +9.7 | +13.0 | 52.7% | 46.8% | 16.05 |
| -1% < gap <= -0.3% | full | 419,410 | +2.9 | +7.9 | 52.1% | 47.3% | 10.73 |
| flat (|gap| < 0.3%) | full | 866,182 | +0.0 | +2.2 | 50.5% | 48.5% | 0.1 |
| +0.3% <= gap < +1% | full | 531,532 | +0.4 | +0.0 | 49.6% | 49.6% | 1.75 |
| +1% <= gap < +2% | full | 168,916 | +6.3 | +4.0 | 50.7% | 50.7% | 11.56 |
| +2% <= gap < +5% | full | 61,919 | +1.0 | -6.8 | 48.8% | 48.8% | 0.76 |
| gap >= +5% | full | 12,495 | +25.0 | +0.0 | 50.0% | 50.0% | 5.58 |
| gap <= -5% | last_24m | 2,622 | -16.6 | -22.2 | 48.4% | 51.5% | -1.57 |
| -5% < gap <= -2% | last_24m | 13,832 | +28.9 | +36.5 | 55.1% | 44.6% | 10.04 |
| -2% < gap <= -1% | last_24m | 33,204 | +23.4 | +21.1 | 54.6% | 45.1% | 17.28 |
| -1% < gap <= -0.3% | last_24m | 87,650 | +6.0 | +7.5 | 52.1% | 47.5% | 9.64 |
| flat (|gap| < 0.3%) | last_24m | 156,696 | -1.0 | +0.0 | 49.6% | 48.4% | -2.5 |
| +0.3% <= gap < +1% | last_24m | 100,869 | -4.0 | -6.0 | 48.0% | 48.0% | -7.19 |
| +1% <= gap < +2% | last_24m | 37,189 | -3.1 | -7.9 | 48.1% | 48.1% | -2.68 |
| +2% <= gap < +5% | last_24m | 15,201 | -32.8 | -35.0 | 44.4% | 44.4% | -12.78 |
| gap >= +5% | last_24m | 3,094 | -33.3 | -41.2 | 45.2% | 45.2% | -3.9 |
| gap <= -5% | last_12m | 1,208 | +47.1 | +20.0 | 52.6% | 47.2% | 3.22 |
| -5% < gap <= -2% | last_12m | 7,049 | +29.5 | +33.4 | 54.8% | 44.9% | 7.71 |
| -2% < gap <= -1% | last_12m | 18,032 | +6.4 | +12.2 | 52.6% | 47.1% | 3.73 |
| -1% < gap <= -0.3% | last_12m | 44,673 | +1.6 | +4.8 | 51.2% | 48.4% | 1.86 |
| flat (|gap| < 0.3%) | last_12m | 74,018 | -0.9 | -0.9 | 49.4% | 48.2% | -1.4 |
| +0.3% <= gap < +1% | last_12m | 49,497 | -3.4 | -7.9 | 47.5% | 47.5% | -4.14 |
| +1% <= gap < +2% | last_12m | 21,477 | -6.7 | -16.5 | 46.3% | 46.3% | -4.27 |
| +2% <= gap < +5% | last_12m | 8,492 | -14.0 | -22.8 | 46.4% | 46.4% | -4.13 |
| gap >= +5% | last_12m | 1,543 | -17.2 | -26.3 | 46.6% | 46.6% | -1.37 |

## 2. Day two after a big close-to-close move

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | Continuation | t |
|---|---|---|---|---|---|---|---|
| yesterday +10% or more | full | 7,531 | -10.7 | -15.5 | 48.0% | 48.0% | -1.9 |
| yesterday +5% to +10% | full | 37,335 | +0.9 | +0.0 | 49.6% | 49.6% | 0.53 |
| yesterday -5% to -10% | full | 35,398 | +22.2 | +17.5 | 52.3% | 47.3% | 11.58 |
| yesterday -10% or worse | full | 5,955 | +80.1 | +50.9 | 54.7% | 45.0% | 10.09 |
| yesterday +10% or more | last_24m | 1,821 | -56.9 | -67.6 | 42.0% | 42.0% | -5.99 |
| yesterday +5% to +10% | last_24m | 8,692 | +11.9 | +4.4 | 50.6% | 50.6% | 3.57 |
| yesterday -5% to -10% | last_24m | 8,086 | +42.2 | +28.5 | 54.4% | 45.4% | 10.39 |
| yesterday -10% or worse | last_24m | 1,386 | +10.4 | +5.4 | 50.5% | 49.3% | 0.84 |
| yesterday +10% or more | last_12m | 836 | +22.5 | +21.9 | 52.4% | 52.4% | 1.51 |
| yesterday +5% to +10% | last_12m | 5,033 | +28.1 | +26.9 | 54.1% | 54.1% | 6.24 |
| yesterday -5% to -10% | last_12m | 4,369 | +18.0 | +15.3 | 52.4% | 47.4% | 3.51 |
| yesterday -10% or worse | last_12m | 616 | -3.8 | -3.5 | 49.2% | 50.6% | -0.2 |

## 3. Three-day moves

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| 3-day return <= -15% | full | 8,161 | +36.1 | +12.5 | 51.0% | 5.2 |
| 3-day return -15% to -10% | full | 19,604 | +20.7 | +10.9 | 51.3% | 7.24 |
| 3-day return >= +15% | full | 11,207 | -0.8 | -5.1 | 49.1% | -0.19 |
| 3-day return <= -15% | last_24m | 1,934 | +11.1 | -8.3 | 48.9% | 0.92 |
| 3-day return -15% to -10% | last_24m | 4,640 | +27.9 | +2.4 | 50.2% | 4.42 |
| 3-day return >= +15% | last_24m | 2,652 | +6.7 | +1.0 | 50.1% | 0.87 |
| 3-day return <= -15% | last_12m | 788 | +39.9 | +19.1 | 50.9% | 2.66 |
| 3-day return -15% to -10% | last_12m | 2,323 | +0.3 | -11.8 | 48.3% | 0.04 |
| 3-day return >= +15% | last_12m | 1,500 | +15.5 | +10.7 | 51.8% | 1.44 |

## 4. 20-day momentum deciles

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| momentum top decile (20d) | full | 228,546 | +2.1 | +2.5 | 50.4% | 4.34 |
| momentum bottom decile (20d) | full | 228,775 | +3.2 | +1.9 | 50.2% | 6.21 |
| momentum top decile (20d) | last_24m | 45,152 | +2.0 | +1.2 | 50.1% | 1.67 |
| momentum bottom decile (20d) | last_24m | 45,167 | +1.6 | -0.4 | 49.6% | 1.34 |
| momentum top decile (20d) | last_12m | 22,652 | +4.3 | +0.0 | 49.8% | 2.34 |
| momentum bottom decile (20d) | last_12m | 22,667 | -1.1 | -2.6 | 49.2% | -0.67 |

## 5. Base rate: share of tradable stock-days that closed above the open

| Year | n | Share up | Mean OC (bps) |
|---|---|---|---|
| 2016 | 177,050 | 52.8% | +10.4 |
| 2017 | 197,846 | 51.4% | +2.7 |
| 2018 | 201,844 | 49.3% | -6.5 |
| 2019 | 205,998 | 52.7% | +6.7 |
| 2020 | 211,038 | 49.6% | +0.6 |
| 2021 | 217,192 | 50.2% | +0.7 |
| 2022 | 218,920 | 50.0% | +1.2 |
| 2023 | 220,147 | 51.5% | +6.0 |
| 2024 | 225,057 | 50.3% | -0.9 |
| 2025 | 224,491 | 51.0% | +4.2 |
| 2026 | 177,441 | 49.4% | -0.1 |

## 6. SPY conditionals

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| SPY all sessions | full | 2,711 | +2.3 | +5.1 | 53.8% | 1.4 |
| SPY gap >= +0.5% | full | 427 | +8.8 | +22.3 | 60.0% | 1.76 |
| SPY gap <= -0.5% | full | 343 | +6.3 | +8.0 | 53.6% | 0.91 |
| SPY after 3 up days | full | 437 | +1.5 | +4.5 | 52.9% | 0.57 |
| SPY after a -1% day | full | 292 | +9.1 | +2.2 | 52.0% | 1.13 |
| SPY all sessions | last_24m | 501 | +2.0 | +2.0 | 51.1% | 0.5 |
| SPY gap >= +0.5% | last_24m | 78 | -10.8 | -9.7 | 44.9% | -1.07 |
| SPY gap <= -0.5% | last_24m | 63 | +20.1 | +0.5 | 50.8% | 0.91 |
| SPY after 3 up days | last_24m | 84 | +2.0 | -0.4 | 50.0% | 0.34 |
| SPY after a -1% day | last_24m | 52 | +47.5 | +34.5 | 61.5% | 1.87 |
| SPY all sessions | last_12m | 251 | +0.6 | -0.8 | 49.8% | 0.16 |
| SPY gap >= +0.5% | last_12m | 45 | -6.4 | -12.2 | 42.2% | -0.56 |
| SPY gap <= -0.5% | last_12m | 29 | +4.4 | -3.0 | 44.8% | 0.32 |
| SPY after 3 up days | last_12m | 38 | -1.4 | +1.7 | 52.6% | -0.16 |
| SPY after a -1% day | last_12m | 24 | +13.4 | +3.3 | 54.2% | 0.8 |

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
| 2026 | 197 | 49.8% | +1.8 |

_Current index membership (survivorship bias favours longs slightly). Research output, not investment advice._
