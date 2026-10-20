# Playbook priors, backtested on the full panel

902 tickers, 2016-01-04 to 2026-10-19, 2,328,629 stock-days (2,279,731 pass the ledger's price and liquidity filter). Every row measures the **open-to-close return of the session after the condition is known**, before costs; the ledger pays about 4 bps per round trip. Continuation = share of sessions where the open-to-close move had the same sign as the gap or the prior move.

## Verdicts on the playbook's priors

| Prior | Verdict |
|---|---|
| long a stock that gapped up 2-5% (continuation) | no reliable edge (mean +0.8 bps, t = 0.64, n = 62,072) |
| long a stock that gapped up 5%+ (continuation) | supported: +24.8 bps/session for that side, clears 4 bps costs (t = 5.53, n = 12,513) |
| short a stock that gapped down 2-5% (continuation) | goes the other way: -21.2 bps/session for that side (t = -15.64, n = 58,765) |
| short a stock that gapped down 5%+ (continuation) | supported: +43.3 bps/session for that side, clears 4 bps costs (t = 8.17, n = 11,788) |
| fade a +5% gap (short) | goes the other way: -24.8 bps/session for that side (t = -5.53, n = 12,513) |
| fade a -5% gap (long) | goes the other way: -43.3 bps/session for that side (t = -8.17, n = 11,788) |
| day-two fade after a +10% day (short) | no reliable edge (mean -10.7 bps, t = -1.9, n = 7,534) |
| day-two bounce after a -10% day (long) | supported: +80.0 bps/session for that side, clears 4 bps costs (t = 10.09, n = 5,966) |
| oversold bounce after a -15% three-day drop (long) | supported: +35.0 bps/session for that side, clears 4 bps costs (t = 5.06, n = 8,201) |
| 20-day momentum top decile (long) | positive but inside costs (+2.1 bps vs 4 bps, t = 4.29, n = 228,819) |
| 20-day momentum bottom decile (short) | goes the other way: -3.1 bps/session for that side (t = -6.05, n = 229,049) |

## 1. Overnight gap -> open-to-close

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | Continuation | t |
|---|---|---|---|---|---|---|---|
| gap <= -5% | full | 11,788 | -43.3 | -38.1 | 46.4% | 53.3% | -8.17 |
| -5% < gap <= -2% | full | 58,765 | +21.2 | +19.0 | 52.6% | 47.0% | 15.64 |
| -2% < gap <= -1% | full | 146,304 | +9.7 | +13.1 | 52.7% | 46.8% | 16.06 |
| -1% < gap <= -0.3% | full | 419,800 | +2.9 | +7.9 | 52.1% | 47.3% | 10.7 |
| flat (|gap| < 0.3%) | full | 866,773 | -0.0 | +2.2 | 50.5% | 48.5% | -0.06 |
| +0.3% <= gap < +1% | full | 532,287 | +0.4 | +0.0 | 49.6% | 49.6% | 1.7 |
| +1% <= gap < +2% | full | 169,429 | +6.3 | +4.0 | 50.7% | 50.7% | 11.58 |
| +2% <= gap < +5% | full | 62,072 | +0.8 | -7.0 | 48.8% | 48.8% | 0.64 |
| gap >= +5% | full | 12,513 | +24.8 | +0.0 | 50.0% | 50.0% | 5.53 |
| gap <= -5% | last_24m | 2,632 | -15.6 | -20.4 | 48.6% | 51.3% | -1.48 |
| -5% < gap <= -2% | last_24m | 13,876 | +29.9 | +38.5 | 55.3% | 44.4% | 10.37 |
| -2% < gap <= -1% | last_24m | 33,299 | +23.5 | +21.3 | 54.7% | 45.0% | 17.35 |
| -1% < gap <= -0.3% | last_24m | 87,640 | +6.0 | +7.4 | 52.0% | 47.5% | 9.71 |
| flat (|gap| < 0.3%) | last_24m | 155,823 | -1.2 | +0.0 | 49.6% | 48.3% | -2.86 |
| +0.3% <= gap < +1% | last_24m | 100,409 | -4.0 | -6.1 | 48.0% | 48.0% | -7.17 |
| +1% <= gap < +2% | last_24m | 37,438 | -2.9 | -7.7 | 48.1% | 48.1% | -2.51 |
| +2% <= gap < +5% | last_24m | 15,259 | -32.9 | -34.9 | 44.4% | 44.4% | -12.86 |
| gap >= +5% | last_24m | 3,103 | -33.6 | -41.4 | 45.1% | 45.1% | -3.95 |
| gap <= -5% | last_12m | 1,221 | +50.8 | +31.0 | 53.1% | 46.7% | 3.5 |
| -5% < gap <= -2% | last_12m | 7,111 | +31.4 | +35.9 | 55.1% | 44.5% | 8.23 |
| -2% < gap <= -1% | last_12m | 18,084 | +7.0 | +12.8 | 52.7% | 47.0% | 4.05 |
| -1% < gap <= -0.3% | last_12m | 44,686 | +1.8 | +4.7 | 51.1% | 48.5% | 2.0 |
| flat (|gap| < 0.3%) | last_12m | 73,561 | -0.8 | -1.1 | 49.4% | 48.2% | -1.29 |
| +0.3% <= gap < +1% | last_12m | 49,475 | -2.6 | -7.4 | 47.6% | 47.6% | -3.16 |
| +1% <= gap < +2% | last_12m | 21,770 | -6.2 | -15.9 | 46.5% | 46.5% | -3.97 |
| +2% <= gap < +5% | last_12m | 8,546 | -14.8 | -23.3 | 46.2% | 46.2% | -4.4 |
| gap >= +5% | last_12m | 1,547 | -18.4 | -27.8 | 46.4% | 46.4% | -1.48 |

## 2. Day two after a big close-to-close move

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | Continuation | t |
|---|---|---|---|---|---|---|---|
| yesterday +10% or more | full | 7,534 | -10.7 | -16.1 | 48.0% | 48.0% | -1.9 |
| yesterday +5% to +10% | full | 37,399 | +0.6 | -0.7 | 49.6% | 49.6% | 0.36 |
| yesterday -5% to -10% | full | 35,498 | +22.2 | +17.7 | 52.4% | 47.3% | 11.61 |
| yesterday -10% or worse | full | 5,966 | +80.0 | +51.1 | 54.7% | 45.0% | 10.09 |
| yesterday +10% or more | last_24m | 1,820 | -57.1 | -67.6 | 41.9% | 41.9% | -6.01 |
| yesterday +5% to +10% | last_24m | 8,719 | +11.1 | +4.1 | 50.5% | 50.5% | 3.33 |
| yesterday -5% to -10% | last_24m | 8,163 | +42.3 | +28.6 | 54.5% | 45.3% | 10.47 |
| yesterday -10% or worse | last_24m | 1,390 | +11.4 | +6.7 | 50.6% | 49.1% | 0.92 |
| yesterday +10% or more | last_12m | 832 | +24.0 | +22.9 | 52.5% | 52.5% | 1.6 |
| yesterday +5% to +10% | last_12m | 5,056 | +26.4 | +25.6 | 53.9% | 53.9% | 5.89 |
| yesterday -5% to -10% | last_12m | 4,425 | +18.7 | +15.3 | 52.4% | 47.5% | 3.66 |
| yesterday -10% or worse | last_12m | 620 | -6.2 | -5.6 | 48.9% | 51.0% | -0.32 |

## 3. Three-day moves

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| 3-day return <= -15% | full | 8,201 | +35.0 | +11.2 | 50.8% | 5.06 |
| 3-day return -15% to -10% | full | 19,696 | +20.3 | +10.8 | 51.3% | 7.13 |
| 3-day return >= +15% | full | 11,210 | -0.7 | -5.0 | 49.1% | -0.18 |
| 3-day return <= -15% | last_24m | 1,972 | +7.3 | -13.5 | 48.3% | 0.62 |
| 3-day return -15% to -10% | last_24m | 4,718 | +26.6 | +2.0 | 50.2% | 4.26 |
| 3-day return >= +15% | last_24m | 2,645 | +6.7 | +1.0 | 50.1% | 0.86 |
| 3-day return <= -15% | last_12m | 827 | +28.5 | -5.5 | 49.5% | 1.95 |
| 3-day return -15% to -10% | last_12m | 2,401 | -2.4 | -12.9 | 48.1% | -0.33 |
| 3-day return >= +15% | last_12m | 1,488 | +17.2 | +11.6 | 51.9% | 1.6 |

## 4. 20-day momentum deciles

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| momentum top decile (20d) | full | 228,819 | +2.1 | +2.5 | 50.4% | 4.29 |
| momentum bottom decile (20d) | full | 229,049 | +3.1 | +1.8 | 50.2% | 6.05 |
| momentum top decile (20d) | last_24m | 45,065 | +2.2 | +1.4 | 50.2% | 1.79 |
| momentum bottom decile (20d) | last_24m | 45,080 | +1.2 | -0.9 | 49.6% | 0.96 |
| momentum top decile (20d) | last_12m | 22,655 | +4.6 | +0.0 | 49.8% | 2.51 |
| momentum bottom decile (20d) | last_12m | 22,670 | -1.2 | -2.6 | 49.2% | -0.72 |

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
| 2026 | 180,147 | 49.4% | -0.2 |

## 6. SPY conditionals

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| SPY all sessions | full | 2,714 | +2.2 | +5.1 | 53.8% | 1.38 |
| SPY gap >= +0.5% | full | 428 | +8.8 | +21.9 | 59.8% | 1.76 |
| SPY gap <= -0.5% | full | 343 | +6.3 | +8.0 | 53.6% | 0.91 |
| SPY after 3 up days | full | 437 | +1.5 | +4.5 | 52.9% | 0.57 |
| SPY after a -1% day | full | 294 | +9.2 | +2.2 | 52.0% | 1.16 |
| SPY all sessions | last_24m | 500 | +2.0 | +1.9 | 51.0% | 0.51 |
| SPY gap >= +0.5% | last_24m | 78 | -10.1 | -8.5 | 44.9% | -1.01 |
| SPY gap <= -0.5% | last_24m | 63 | +20.1 | +0.5 | 50.8% | 0.91 |
| SPY after 3 up days | last_24m | 84 | +2.0 | -0.4 | 50.0% | 0.34 |
| SPY after a -1% day | last_24m | 54 | +46.9 | +34.5 | 61.1% | 1.91 |
| SPY all sessions | last_12m | 251 | +0.5 | -0.8 | 49.8% | 0.13 |
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
| 2026 | 200 | 49.5% | +1.4 |

_Current index membership (survivorship bias favours longs slightly). Research output, not investment advice._
