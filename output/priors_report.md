# Playbook priors, backtested on the full panel

902 tickers, 2016-01-04 to 2026-10-12, 2,324,119 stock-days (2,275,221 pass the ledger's price and liquidity filter). Every row measures the **open-to-close return of the session after the condition is known**, before costs; the ledger pays about 4 bps per round trip. Continuation = share of sessions where the open-to-close move had the same sign as the gap or the prior move.

## Verdicts on the playbook's priors

| Prior | Verdict |
|---|---|
| long a stock that gapped up 2-5% (continuation) | no reliable edge (mean +1.0 bps, t = 0.76, n = 61,911) |
| long a stock that gapped up 5%+ (continuation) | supported: +25.1 bps/session for that side, clears 4 bps costs (t = 5.6, n = 12,494) |
| short a stock that gapped down 2-5% (continuation) | goes the other way: -21.3 bps/session for that side (t = -15.68, n = 58,542) |
| short a stock that gapped down 5%+ (continuation) | supported: +44.0 bps/session for that side, clears 4 bps costs (t = 8.29, n = 11,759) |
| fade a +5% gap (short) | goes the other way: -25.1 bps/session for that side (t = -5.6, n = 12,494) |
| fade a -5% gap (long) | goes the other way: -44.0 bps/session for that side (t = -8.29, n = 11,759) |
| day-two fade after a +10% day (short) | no reliable edge (mean -10.6 bps, t = -1.88, n = 7,531) |
| day-two bounce after a -10% day (long) | supported: +80.1 bps/session for that side, clears 4 bps costs (t = 10.09, n = 5,954) |
| oversold bounce after a -15% three-day drop (long) | supported: +36.1 bps/session for that side, clears 4 bps costs (t = 5.2, n = 8,161) |
| 20-day momentum top decile (long) | positive but inside costs (+2.1 bps vs 4 bps, t = 4.44, n = 228,365) |
| 20-day momentum bottom decile (short) | goes the other way: -3.2 bps/session for that side (t = -6.24, n = 228,593) |

## 1. Overnight gap -> open-to-close

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | Continuation | t |
|---|---|---|---|---|---|---|---|
| gap <= -5% | full | 11,759 | -44.0 | -38.9 | 46.3% | 53.4% | -8.29 |
| -5% < gap <= -2% | full | 58,542 | +21.3 | +18.9 | 52.6% | 47.0% | 15.68 |
| -2% < gap <= -1% | full | 145,897 | +9.8 | +13.0 | 52.7% | 46.8% | 16.13 |
| -1% < gap <= -0.3% | full | 419,124 | +2.9 | +7.9 | 52.1% | 47.3% | 10.74 |
| flat (|gap| < 0.3%) | full | 865,762 | +0.0 | +2.2 | 50.5% | 48.5% | 0.05 |
| +0.3% <= gap < +1% | full | 530,968 | +0.4 | +0.0 | 49.6% | 49.6% | 1.8 |
| +1% <= gap < +2% | full | 168,764 | +6.4 | +4.1 | 50.7% | 50.7% | 11.7 |
| +2% <= gap < +5% | full | 61,911 | +1.0 | -6.8 | 48.8% | 48.8% | 0.76 |
| gap >= +5% | full | 12,494 | +25.1 | +0.1 | 50.0% | 50.0% | 5.6 |
| gap <= -5% | last_24m | 2,611 | -18.0 | -25.2 | 48.3% | 51.6% | -1.69 |
| -5% < gap <= -2% | last_24m | 13,719 | +30.0 | +37.6 | 55.2% | 44.5% | 10.38 |
| -2% < gap <= -1% | last_24m | 32,996 | +23.8 | +21.2 | 54.7% | 45.0% | 17.51 |
| -1% < gap <= -0.3% | last_24m | 87,480 | +6.1 | +7.5 | 52.1% | 47.5% | 9.73 |
| flat (|gap| < 0.3%) | last_24m | 156,771 | -0.9 | +0.0 | 49.7% | 48.4% | -2.12 |
| +0.3% <= gap < +1% | last_24m | 100,520 | -3.9 | -5.8 | 48.1% | 48.1% | -6.89 |
| +1% <= gap < +2% | last_24m | 37,058 | -2.8 | -7.4 | 48.2% | 48.2% | -2.39 |
| +2% <= gap < +5% | last_24m | 15,200 | -32.7 | -34.9 | 44.4% | 44.4% | -12.73 |
| gap >= +5% | last_24m | 3,094 | -32.9 | -40.6 | 45.3% | 45.3% | -3.85 |
| gap <= -5% | last_12m | 1,198 | +45.0 | +18.7 | 52.4% | 47.4% | 3.06 |
| -5% < gap <= -2% | last_12m | 7,047 | +34.7 | +38.5 | 55.6% | 44.0% | 9.1 |
| -2% < gap <= -1% | last_12m | 18,071 | +10.1 | +15.0 | 53.2% | 46.5% | 5.83 |
| -1% < gap <= -0.3% | last_12m | 44,759 | +3.0 | +5.6 | 51.4% | 48.2% | 3.33 |
| flat (|gap| < 0.3%) | last_12m | 73,963 | -0.6 | -0.2 | 49.5% | 48.2% | -0.9 |
| +0.3% <= gap < +1% | last_12m | 49,192 | -3.0 | -7.2 | 47.7% | 47.7% | -3.67 |
| +1% <= gap < +2% | last_12m | 21,575 | -5.6 | -14.9 | 46.7% | 46.7% | -3.58 |
| +2% <= gap < +5% | last_12m | 8,607 | -12.2 | -20.5 | 46.7% | 46.7% | -3.65 |
| gap >= +5% | last_12m | 1,569 | -13.8 | -23.0 | 47.2% | 47.2% | -1.12 |

## 2. Day two after a big close-to-close move

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | Continuation | t |
|---|---|---|---|---|---|---|---|
| yesterday +10% or more | full | 7,531 | -10.6 | -15.5 | 48.0% | 48.0% | -1.88 |
| yesterday +5% to +10% | full | 37,327 | +0.9 | +0.0 | 49.6% | 49.6% | 0.56 |
| yesterday -5% to -10% | full | 35,366 | +22.1 | +17.4 | 52.3% | 47.3% | 11.54 |
| yesterday -10% or worse | full | 5,954 | +80.1 | +51.1 | 54.7% | 45.0% | 10.09 |
| yesterday +10% or more | last_24m | 1,821 | -56.8 | -67.6 | 42.0% | 42.0% | -5.98 |
| yesterday +5% to +10% | last_24m | 8,702 | +12.3 | +4.7 | 50.7% | 50.7% | 3.68 |
| yesterday -5% to -10% | last_24m | 8,065 | +42.0 | +28.0 | 54.4% | 45.4% | 10.33 |
| yesterday -10% or worse | last_24m | 1,385 | +10.1 | +5.3 | 50.5% | 49.3% | 0.82 |
| yesterday +10% or more | last_12m | 838 | +23.9 | +23.3 | 52.6% | 52.6% | 1.6 |
| yesterday +5% to +10% | last_12m | 5,097 | +31.4 | +29.7 | 54.6% | 54.6% | 7.03 |
| yesterday -5% to -10% | last_12m | 4,480 | +20.1 | +20.4 | 53.0% | 46.8% | 4.01 |
| yesterday -10% or worse | last_12m | 622 | -3.1 | -3.5 | 49.2% | 50.6% | -0.16 |

## 3. Three-day moves

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| 3-day return <= -15% | full | 8,161 | +36.1 | +12.5 | 51.0% | 5.2 |
| 3-day return -15% to -10% | full | 19,591 | +20.5 | +10.9 | 51.3% | 7.17 |
| 3-day return >= +15% | full | 11,204 | -0.7 | -5.0 | 49.1% | -0.18 |
| 3-day return <= -15% | last_24m | 1,934 | +11.1 | -8.3 | 48.9% | 0.92 |
| 3-day return -15% to -10% | last_24m | 4,628 | +27.5 | +2.0 | 50.2% | 4.36 |
| 3-day return >= +15% | last_24m | 2,650 | +6.9 | +1.1 | 50.1% | 0.89 |
| 3-day return <= -15% | last_12m | 790 | +39.4 | +19.1 | 50.9% | 2.63 |
| 3-day return -15% to -10% | last_12m | 2,330 | +0.9 | -11.3 | 48.4% | 0.12 |
| 3-day return >= +15% | last_12m | 1,500 | +16.1 | +11.0 | 51.9% | 1.5 |

## 4. 20-day momentum deciles

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| momentum top decile (20d) | full | 228,365 | +2.1 | +2.6 | 50.4% | 4.44 |
| momentum bottom decile (20d) | full | 228,593 | +3.2 | +1.9 | 50.2% | 6.24 |
| momentum top decile (20d) | last_24m | 45,060 | +2.3 | +1.6 | 50.2% | 1.92 |
| momentum bottom decile (20d) | last_24m | 45,075 | +1.8 | +0.0 | 49.7% | 1.54 |
| momentum top decile (20d) | last_12m | 22,650 | +5.5 | +1.0 | 50.1% | 3.03 |
| momentum bottom decile (20d) | last_12m | 22,665 | +0.3 | -1.4 | 49.5% | 0.19 |

## 5. Base rate: share of tradable stock-days that closed above the open

| Year | n | Share up | Mean OC (bps) |
|---|---|---|---|
| 2016 | 177,050 | 52.8% | +10.4 |
| 2017 | 197,848 | 51.4% | +2.7 |
| 2018 | 201,844 | 49.3% | -6.5 |
| 2019 | 205,998 | 52.7% | +6.7 |
| 2020 | 211,037 | 49.6% | +0.6 |
| 2021 | 217,192 | 50.2% | +0.7 |
| 2022 | 218,920 | 50.0% | +1.2 |
| 2023 | 220,147 | 51.5% | +6.0 |
| 2024 | 225,057 | 50.3% | -0.9 |
| 2025 | 224,491 | 51.0% | +4.2 |
| 2026 | 175,637 | 49.4% | +0.0 |

## 6. SPY conditionals

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| SPY all sessions | full | 2,709 | +2.3 | +5.1 | 53.9% | 1.41 |
| SPY gap >= +0.5% | full | 427 | +8.8 | +22.3 | 60.0% | 1.76 |
| SPY gap <= -0.5% | full | 343 | +6.3 | +8.0 | 53.6% | 0.91 |
| SPY after 3 up days | full | 437 | +1.5 | +4.5 | 52.9% | 0.57 |
| SPY after a -1% day | full | 292 | +9.1 | +2.2 | 52.0% | 1.13 |
| SPY all sessions | last_24m | 500 | +2.2 | +2.3 | 51.2% | 0.56 |
| SPY gap >= +0.5% | last_24m | 78 | -10.8 | -9.7 | 44.9% | -1.07 |
| SPY gap <= -0.5% | last_24m | 63 | +20.1 | +0.5 | 50.8% | 0.91 |
| SPY after 3 up days | last_24m | 84 | +2.0 | -0.4 | 50.0% | 0.34 |
| SPY after a -1% day | last_24m | 52 | +47.5 | +34.5 | 61.5% | 1.87 |
| SPY all sessions | last_12m | 251 | +1.3 | +0.1 | 50.2% | 0.33 |
| SPY gap >= +0.5% | last_12m | 46 | -5.5 | -9.7 | 43.5% | -0.49 |
| SPY gap <= -0.5% | last_12m | 30 | +6.8 | -2.8 | 46.7% | 0.5 |
| SPY after 3 up days | last_12m | 38 | -1.4 | +1.7 | 52.6% | -0.16 |
| SPY after a -1% day | last_12m | 25 | +14.3 | +5.7 | 56.0% | 0.89 |

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
| 2026 | 195 | 49.7% | +2.1 |

_Current index membership (survivorship bias favours longs slightly). Research output, not investment advice._
