# Playbook priors, backtested on the full panel

902 tickers, 2016-01-04 to 2026-10-27, 2,334,041 stock-days (2,285,143 pass the ledger's price and liquidity filter). Every row measures the **open-to-close return of the session after the condition is known**, before costs; the ledger pays about 4 bps per round trip. Continuation = share of sessions where the open-to-close move had the same sign as the gap or the prior move.

## Verdicts on the playbook's priors

| Prior | Verdict |
|---|---|
| long a stock that gapped up 2-5% (continuation) | no reliable edge (mean +1.0 bps, t = 0.75, n = 62,228) |
| long a stock that gapped up 5%+ (continuation) | supported: +24.5 bps/session for that side, clears 4 bps costs (t = 5.48, n = 12,533) |
| short a stock that gapped down 2-5% (continuation) | goes the other way: -20.9 bps/session for that side (t = -15.45, n = 58,982) |
| short a stock that gapped down 5%+ (continuation) | supported: +43.6 bps/session for that side, clears 4 bps costs (t = 8.25, n = 11,843) |
| fade a +5% gap (short) | goes the other way: -24.5 bps/session for that side (t = -5.48, n = 12,533) |
| fade a -5% gap (long) | goes the other way: -43.6 bps/session for that side (t = -8.25, n = 11,843) |
| day-two fade after a +10% day (short) | no reliable edge (mean -10.5 bps, t = -1.87, n = 7,543) |
| day-two bounce after a -10% day (long) | supported: +80.2 bps/session for that side, clears 4 bps costs (t = 10.16, n = 5,999) |
| oversold bounce after a -15% three-day drop (long) | supported: +35.6 bps/session for that side, clears 4 bps costs (t = 5.16, n = 8,219) |
| 20-day momentum top decile (long) | positive but inside costs (+2.1 bps vs 4 bps, t = 4.32, n = 229,365) |
| 20-day momentum bottom decile (short) | goes the other way: -3.2 bps/session for that side (t = -6.3, n = 229,595) |

## 1. Overnight gap -> open-to-close

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | Continuation | t |
|---|---|---|---|---|---|---|---|
| gap <= -5% | full | 11,843 | -43.6 | -38.6 | 46.4% | 53.3% | -8.25 |
| -5% < gap <= -2% | full | 58,982 | +20.9 | +18.8 | 52.5% | 47.1% | 15.45 |
| -2% < gap <= -1% | full | 146,814 | +9.9 | +13.1 | 52.7% | 46.8% | 16.28 |
| -1% < gap <= -0.3% | full | 420,936 | +2.9 | +7.9 | 52.1% | 47.3% | 10.92 |
| flat (|gap| < 0.3%) | full | 868,281 | +0.0 | +2.2 | 50.5% | 48.5% | 0.28 |
| +0.3% <= gap < +1% | full | 533,595 | +0.5 | +0.0 | 49.6% | 49.6% | 2.38 |
| +1% <= gap < +2% | full | 169,931 | +6.5 | +4.1 | 50.7% | 50.7% | 11.97 |
| +2% <= gap < +5% | full | 62,228 | +1.0 | -6.8 | 48.8% | 48.8% | 0.75 |
| gap >= +5% | full | 12,533 | +24.5 | +0.0 | 49.9% | 49.9% | 5.48 |
| gap <= -5% | last_24m | 2,663 | -16.9 | -21.4 | 48.5% | 51.4% | -1.61 |
| -5% < gap <= -2% | last_24m | 14,034 | +28.9 | +37.7 | 55.2% | 44.5% | 10.08 |
| -2% < gap <= -1% | last_24m | 33,645 | +24.0 | +22.0 | 54.8% | 44.9% | 17.82 |
| -1% < gap <= -0.3% | last_24m | 87,616 | +6.8 | +7.9 | 52.2% | 47.4% | 10.87 |
| flat (|gap| < 0.3%) | last_24m | 155,548 | -0.4 | +0.0 | 49.8% | 48.4% | -1.01 |
| +0.3% <= gap < +1% | last_24m | 100,756 | -2.6 | -4.8 | 48.4% | 48.4% | -4.67 |
| +1% <= gap < +2% | last_24m | 37,712 | -1.5 | -6.5 | 48.4% | 48.4% | -1.27 |
| +2% <= gap < +5% | last_24m | 15,346 | -32.1 | -34.2 | 44.6% | 44.6% | -12.57 |
| gap >= +5% | last_24m | 3,091 | -34.7 | -42.5 | 45.0% | 45.0% | -4.06 |
| gap <= -5% | last_12m | 1,257 | +42.5 | +19.1 | 52.5% | 47.3% | 2.92 |
| -5% < gap <= -2% | last_12m | 7,260 | +28.9 | +34.3 | 54.9% | 44.8% | 7.64 |
| -2% < gap <= -1% | last_12m | 18,480 | +8.1 | +13.6 | 52.9% | 46.8% | 4.71 |
| -1% < gap <= -0.3% | last_12m | 45,268 | +2.1 | +4.7 | 51.1% | 48.5% | 2.35 |
| flat (|gap| < 0.3%) | last_12m | 73,142 | -0.3 | -0.6 | 49.5% | 48.3% | -0.55 |
| +0.3% <= gap < +1% | last_12m | 48,994 | -0.8 | -5.6 | 48.1% | 48.1% | -1.0 |
| +1% <= gap < +2% | last_12m | 21,619 | -3.6 | -13.7 | 47.0% | 47.0% | -2.28 |
| +2% <= gap < +5% | last_12m | 8,470 | -14.1 | -22.5 | 46.5% | 46.5% | -4.17 |
| gap >= +5% | last_12m | 1,535 | -23.2 | -33.1 | 46.0% | 46.0% | -1.85 |

## 2. Day two after a big close-to-close move

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | Continuation | t |
|---|---|---|---|---|---|---|---|
| yesterday +10% or more | full | 7,543 | -10.5 | -15.2 | 48.0% | 48.0% | -1.87 |
| yesterday +5% to +10% | full | 37,549 | +0.7 | -0.9 | 49.6% | 49.6% | 0.4 |
| yesterday -5% to -10% | full | 35,606 | +22.4 | +17.9 | 52.4% | 47.2% | 11.74 |
| yesterday -10% or worse | full | 5,999 | +80.2 | +51.5 | 54.8% | 44.9% | 10.16 |
| yesterday +10% or more | last_24m | 1,815 | -55.8 | -67.6 | 42.0% | 42.0% | -5.86 |
| yesterday +5% to +10% | last_24m | 8,836 | +11.6 | +4.4 | 50.6% | 50.6% | 3.49 |
| yesterday -5% to -10% | last_24m | 8,228 | +43.0 | +29.5 | 54.7% | 45.1% | 10.68 |
| yesterday -10% or worse | last_24m | 1,418 | +13.8 | +8.9 | 50.9% | 48.9% | 1.13 |
| yesterday +10% or more | last_12m | 817 | +26.9 | +22.6 | 52.6% | 52.6% | 1.8 |
| yesterday +5% to +10% | last_12m | 5,124 | +26.4 | +25.6 | 53.8% | 53.8% | 5.92 |
| yesterday -5% to -10% | last_12m | 4,478 | +19.1 | +17.9 | 52.8% | 47.1% | 3.77 |
| yesterday -10% or worse | last_12m | 641 | -2.6 | -3.9 | 49.5% | 50.5% | -0.14 |

## 3. Three-day moves

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| 3-day return <= -15% | full | 8,219 | +35.6 | +11.9 | 50.9% | 5.16 |
| 3-day return -15% to -10% | full | 19,768 | +20.6 | +11.0 | 51.3% | 7.24 |
| 3-day return >= +15% | full | 11,217 | -0.8 | -5.5 | 49.1% | -0.21 |
| 3-day return <= -15% | last_24m | 1,985 | +9.9 | -12.0 | 48.5% | 0.83 |
| 3-day return -15% to -10% | last_24m | 4,764 | +27.8 | +3.8 | 50.4% | 4.48 |
| 3-day return >= +15% | last_24m | 2,650 | +6.8 | +0.3 | 50.0% | 0.88 |
| 3-day return <= -15% | last_12m | 834 | +32.8 | +0.6 | 50.0% | 2.25 |
| 3-day return -15% to -10% | last_12m | 2,443 | -0.5 | -11.2 | 48.5% | -0.06 |
| 3-day return >= +15% | last_12m | 1,467 | +19.1 | +12.2 | 52.0% | 1.77 |

## 4. 20-day momentum deciles

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| momentum top decile (20d) | full | 229,365 | +2.1 | +2.5 | 50.4% | 4.32 |
| momentum bottom decile (20d) | full | 229,595 | +3.2 | +1.9 | 50.2% | 6.3 |
| momentum top decile (20d) | last_24m | 45,161 | +2.6 | +1.6 | 50.2% | 2.13 |
| momentum bottom decile (20d) | last_24m | 45,176 | +2.3 | +0.0 | 49.8% | 1.87 |
| momentum top decile (20d) | last_12m | 22,661 | +4.9 | +0.0 | 49.8% | 2.7 |
| momentum bottom decile (20d) | last_12m | 22,676 | -0.1 | -1.4 | 49.5% | -0.07 |

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
| 2026 | 185,559 | 49.6% | +0.9 |

## 6. SPY conditionals

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| SPY all sessions | full | 2,720 | +2.3 | +5.2 | 53.9% | 1.4 |
| SPY gap >= +0.5% | full | 428 | +8.8 | +21.9 | 59.8% | 1.76 |
| SPY gap <= -0.5% | full | 345 | +6.2 | +6.8 | 53.6% | 0.89 |
| SPY after 3 up days | full | 438 | +1.4 | +4.4 | 52.7% | 0.55 |
| SPY after a -1% day | full | 295 | +9.2 | +1.1 | 52.2% | 1.16 |
| SPY all sessions | last_24m | 501 | +2.4 | +2.8 | 51.7% | 0.6 |
| SPY gap >= +0.5% | last_24m | 78 | -10.1 | -8.5 | 44.9% | -1.01 |
| SPY gap <= -0.5% | last_24m | 65 | +19.0 | +0.5 | 50.8% | 0.89 |
| SPY after 3 up days | last_24m | 84 | +1.7 | -0.4 | 50.0% | 0.28 |
| SPY after a -1% day | last_24m | 55 | +46.1 | +32.9 | 61.8% | 1.91 |
| SPY all sessions | last_12m | 251 | +0.6 | +0.1 | 50.2% | 0.14 |
| SPY gap >= +0.5% | last_12m | 43 | -7.5 | -12.2 | 39.5% | -0.63 |
| SPY gap <= -0.5% | last_12m | 31 | +3.1 | -3.0 | 45.2% | 0.24 |
| SPY after 3 up days | last_12m | 39 | -2.2 | +0.1 | 51.3% | -0.26 |
| SPY after a -1% day | last_12m | 27 | +14.3 | +0.9 | 55.6% | 0.94 |

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
| 2026 | 206 | 50.5% | +1.9 |

_Current index membership (survivorship bias favours longs slightly). Research output, not investment advice._
