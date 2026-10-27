# Playbook priors, backtested on the full panel

902 tickers, 2016-01-04 to 2026-10-26, 2,333,139 stock-days (2,284,242 pass the ledger's price and liquidity filter). Every row measures the **open-to-close return of the session after the condition is known**, before costs; the ledger pays about 4 bps per round trip. Continuation = share of sessions where the open-to-close move had the same sign as the gap or the prior move.

## Verdicts on the playbook's priors

| Prior | Verdict |
|---|---|
| long a stock that gapped up 2-5% (continuation) | no reliable edge (mean +0.9 bps, t = 0.67, n = 62,186) |
| long a stock that gapped up 5%+ (continuation) | supported: +24.5 bps/session for that side, clears 4 bps costs (t = 5.47, n = 12,525) |
| short a stock that gapped down 2-5% (continuation) | goes the other way: -20.9 bps/session for that side (t = -15.46, n = 58,962) |
| short a stock that gapped down 5%+ (continuation) | supported: +43.8 bps/session for that side, clears 4 bps costs (t = 8.29, n = 11,838) |
| fade a +5% gap (short) | goes the other way: -24.5 bps/session for that side (t = -5.47, n = 12,525) |
| fade a -5% gap (long) | goes the other way: -43.8 bps/session for that side (t = -8.29, n = 11,838) |
| day-two fade after a +10% day (short) | no reliable edge (mean -10.7 bps, t = -1.91, n = 7,540) |
| day-two bounce after a -10% day (long) | supported: +80.2 bps/session for that side, clears 4 bps costs (t = 10.16, n = 5,996) |
| oversold bounce after a -15% three-day drop (long) | supported: +35.5 bps/session for that side, clears 4 bps costs (t = 5.13, n = 8,212) |
| 20-day momentum top decile (long) | positive but inside costs (+2.1 bps vs 4 bps, t = 4.41, n = 229,275) |
| 20-day momentum bottom decile (short) | goes the other way: -3.2 bps/session for that side (t = -6.18, n = 229,504) |

## 1. Overnight gap -> open-to-close

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | Continuation | t |
|---|---|---|---|---|---|---|---|
| gap <= -5% | full | 11,838 | -43.8 | -38.7 | 46.4% | 53.4% | -8.29 |
| -5% < gap <= -2% | full | 58,962 | +20.9 | +18.8 | 52.5% | 47.1% | 15.46 |
| -2% < gap <= -1% | full | 146,764 | +9.9 | +13.1 | 52.7% | 46.8% | 16.3 |
| -1% < gap <= -0.3% | full | 420,701 | +2.9 | +7.9 | 52.1% | 47.3% | 10.97 |
| flat (|gap| < 0.3%) | full | 868,021 | +0.0 | +2.2 | 50.5% | 48.5% | 0.3 |
| +0.3% <= gap < +1% | full | 533,414 | +0.5 | +0.0 | 49.6% | 49.6% | 2.4 |
| +1% <= gap < +2% | full | 169,831 | +6.4 | +4.1 | 50.7% | 50.7% | 11.83 |
| +2% <= gap < +5% | full | 62,186 | +0.9 | -6.9 | 48.8% | 48.8% | 0.67 |
| gap >= +5% | full | 12,525 | +24.5 | +0.0 | 49.9% | 49.9% | 5.47 |
| gap <= -5% | last_24m | 2,658 | -17.7 | -22.2 | 48.4% | 51.5% | -1.68 |
| -5% < gap <= -2% | last_24m | 14,016 | +28.9 | +37.7 | 55.2% | 44.5% | 10.08 |
| -2% < gap <= -1% | last_24m | 33,587 | +24.1 | +22.0 | 54.8% | 44.9% | 17.86 |
| -1% < gap <= -0.3% | last_24m | 87,389 | +6.9 | +8.0 | 52.2% | 47.4% | 10.99 |
| flat (|gap| < 0.3%) | last_24m | 155,283 | -0.4 | +0.0 | 49.8% | 48.3% | -0.98 |
| +0.3% <= gap < +1% | last_24m | 100,577 | -2.6 | -4.8 | 48.4% | 48.4% | -4.65 |
| +1% <= gap < +2% | last_24m | 37,613 | -1.9 | -6.9 | 48.4% | 48.4% | -1.59 |
| +2% <= gap < +5% | last_24m | 15,300 | -32.6 | -34.7 | 44.5% | 44.5% | -12.74 |
| gap >= +5% | last_24m | 3,086 | -34.9 | -42.5 | 45.0% | 45.0% | -4.07 |
| gap <= -5% | last_12m | 1,252 | +41.1 | +18.8 | 52.4% | 47.4% | 2.84 |
| -5% < gap <= -2% | last_12m | 7,252 | +28.9 | +34.1 | 54.9% | 44.8% | 7.63 |
| -2% < gap <= -1% | last_12m | 18,424 | +8.1 | +13.5 | 52.9% | 46.8% | 4.73 |
| -1% < gap <= -0.3% | last_12m | 45,101 | +2.2 | +4.8 | 51.2% | 48.4% | 2.51 |
| flat (|gap| < 0.3%) | last_12m | 73,151 | -0.3 | -0.5 | 49.5% | 48.3% | -0.49 |
| +0.3% <= gap < +1% | last_12m | 49,131 | -1.0 | -5.8 | 48.1% | 48.1% | -1.16 |
| +1% <= gap < +2% | last_12m | 21,694 | -4.6 | -14.7 | 46.7% | 46.7% | -2.94 |
| +2% <= gap < +5% | last_12m | 8,482 | -15.1 | -23.2 | 46.2% | 46.2% | -4.49 |
| gap >= +5% | last_12m | 1,534 | -24.0 | -33.5 | 45.9% | 45.9% | -1.91 |

## 2. Day two after a big close-to-close move

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | Continuation | t |
|---|---|---|---|---|---|---|---|
| yesterday +10% or more | full | 7,540 | -10.7 | -15.7 | 48.0% | 48.0% | -1.91 |
| yesterday +5% to +10% | full | 37,534 | +0.6 | -1.0 | 49.6% | 49.6% | 0.38 |
| yesterday -5% to -10% | full | 35,608 | +22.3 | +17.8 | 52.4% | 47.2% | 11.7 |
| yesterday -10% or worse | full | 5,996 | +80.2 | +51.6 | 54.8% | 44.9% | 10.16 |
| yesterday +10% or more | last_24m | 1,813 | -56.5 | -67.6 | 41.9% | 41.9% | -5.93 |
| yesterday +5% to +10% | last_24m | 8,820 | +11.4 | +4.2 | 50.6% | 50.6% | 3.45 |
| yesterday -5% to -10% | last_24m | 8,223 | +42.8 | +29.2 | 54.6% | 45.2% | 10.63 |
| yesterday -10% or worse | last_24m | 1,417 | +13.9 | +9.3 | 50.9% | 48.8% | 1.14 |
| yesterday +10% or more | last_12m | 819 | +23.0 | +21.0 | 52.3% | 52.3% | 1.54 |
| yesterday +5% to +10% | last_12m | 5,128 | +25.9 | +25.3 | 53.7% | 53.7% | 5.8 |
| yesterday -5% to -10% | last_12m | 4,479 | +18.6 | +17.8 | 52.7% | 47.1% | 3.68 |
| yesterday -10% or worse | last_12m | 642 | -1.9 | -2.2 | 49.5% | 50.3% | -0.1 |

## 3. Three-day moves

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| 3-day return <= -15% | full | 8,212 | +35.5 | +11.8 | 50.9% | 5.13 |
| 3-day return -15% to -10% | full | 19,748 | +20.6 | +11.0 | 51.3% | 7.24 |
| 3-day return >= +15% | full | 11,212 | -0.9 | -5.4 | 49.1% | -0.22 |
| 3-day return <= -15% | last_24m | 1,978 | +9.0 | -12.1 | 48.5% | 0.76 |
| 3-day return -15% to -10% | last_24m | 4,750 | +27.8 | +3.8 | 50.4% | 4.48 |
| 3-day return >= +15% | last_24m | 2,646 | +6.7 | +0.8 | 50.0% | 0.87 |
| 3-day return <= -15% | last_12m | 829 | +31.1 | +0.0 | 49.9% | 2.12 |
| 3-day return -15% to -10% | last_12m | 2,436 | -0.3 | -11.1 | 48.5% | -0.05 |
| 3-day return >= +15% | last_12m | 1,472 | +17.4 | +11.0 | 51.9% | 1.61 |

## 4. 20-day momentum deciles

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| momentum top decile (20d) | full | 229,275 | +2.1 | +2.5 | 50.4% | 4.41 |
| momentum bottom decile (20d) | full | 229,504 | +3.2 | +1.9 | 50.2% | 6.18 |
| momentum top decile (20d) | last_24m | 45,070 | +2.8 | +1.8 | 50.2% | 2.31 |
| momentum bottom decile (20d) | last_24m | 45,085 | +2.0 | +0.0 | 49.8% | 1.62 |
| momentum top decile (20d) | last_12m | 22,660 | +5.0 | +0.0 | 49.8% | 2.76 |
| momentum bottom decile (20d) | last_12m | 22,675 | -0.9 | -2.2 | 49.3% | -0.55 |

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
| 2026 | 184,657 | 49.6% | +0.8 |

## 6. SPY conditionals

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| SPY all sessions | full | 2,719 | +2.3 | +5.1 | 53.9% | 1.4 |
| SPY gap >= +0.5% | full | 428 | +8.8 | +21.9 | 59.8% | 1.76 |
| SPY gap <= -0.5% | full | 345 | +6.2 | +6.8 | 53.6% | 0.89 |
| SPY after 3 up days | full | 438 | +1.4 | +4.4 | 52.7% | 0.55 |
| SPY after a -1% day | full | 295 | +9.2 | +1.1 | 52.2% | 1.16 |
| SPY all sessions | last_24m | 500 | +2.3 | +2.7 | 51.6% | 0.59 |
| SPY gap >= +0.5% | last_24m | 78 | -10.1 | -8.5 | 44.9% | -1.01 |
| SPY gap <= -0.5% | last_24m | 65 | +19.0 | +0.5 | 50.8% | 0.89 |
| SPY after 3 up days | last_24m | 84 | +1.7 | -0.4 | 50.0% | 0.28 |
| SPY after a -1% day | last_24m | 55 | +46.1 | +32.9 | 61.8% | 1.91 |
| SPY all sessions | last_12m | 251 | +0.6 | +0.1 | 50.2% | 0.15 |
| SPY gap >= +0.5% | last_12m | 44 | -6.5 | -11.0 | 40.9% | -0.56 |
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
| 2026 | 205 | 50.2% | +1.8 |

_Current index membership (survivorship bias favours longs slightly). Research output, not investment advice._
