# Playbook priors, backtested on the full panel

902 tickers, 2016-01-04 to 2026-10-22, 2,331,336 stock-days (2,282,438 pass the ledger's price and liquidity filter). Every row measures the **open-to-close return of the session after the condition is known**, before costs; the ledger pays about 4 bps per round trip. Continuation = share of sessions where the open-to-close move had the same sign as the gap or the prior move.

## Verdicts on the playbook's priors

| Prior | Verdict |
|---|---|
| long a stock that gapped up 2-5% (continuation) | no reliable edge (mean +0.8 bps, t = 0.66, n = 62,172) |
| long a stock that gapped up 5%+ (continuation) | supported: +24.6 bps/session for that side, clears 4 bps costs (t = 5.49, n = 12,521) |
| short a stock that gapped down 2-5% (continuation) | goes the other way: -20.9 bps/session for that side (t = -15.45, n = 58,918) |
| short a stock that gapped down 5%+ (continuation) | supported: +43.8 bps/session for that side, clears 4 bps costs (t = 8.28, n = 11,828) |
| fade a +5% gap (short) | goes the other way: -24.6 bps/session for that side (t = -5.49, n = 12,521) |
| fade a -5% gap (long) | goes the other way: -43.8 bps/session for that side (t = -8.28, n = 11,828) |
| day-two fade after a +10% day (short) | no reliable edge (mean -10.6 bps, t = -1.89, n = 7,538) |
| day-two bounce after a -10% day (long) | supported: +80.1 bps/session for that side, clears 4 bps costs (t = 10.11, n = 5,967) |
| oversold bounce after a -15% three-day drop (long) | supported: +35.1 bps/session for that side, clears 4 bps costs (t = 5.07, n = 8,202) |
| 20-day momentum top decile (long) | positive but inside costs (+2.1 bps vs 4 bps, t = 4.43, n = 229,093) |
| 20-day momentum bottom decile (short) | goes the other way: -3.1 bps/session for that side (t = -6.03, n = 229,322) |

## 1. Overnight gap -> open-to-close

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | Continuation | t |
|---|---|---|---|---|---|---|---|
| gap <= -5% | full | 11,828 | -43.8 | -38.6 | 46.4% | 53.4% | -8.28 |
| -5% < gap <= -2% | full | 58,918 | +20.9 | +18.8 | 52.5% | 47.1% | 15.45 |
| -2% < gap <= -1% | full | 146,520 | +9.9 | +13.2 | 52.8% | 46.8% | 16.36 |
| -1% < gap <= -0.3% | full | 420,247 | +3.0 | +7.9 | 52.2% | 47.3% | 11.01 |
| flat (|gap| < 0.3%) | full | 867,451 | +0.0 | +2.2 | 50.5% | 48.5% | 0.3 |
| +0.3% <= gap < +1% | full | 533,031 | +0.5 | +0.0 | 49.6% | 49.6% | 2.26 |
| +1% <= gap < +2% | full | 169,750 | +6.4 | +4.1 | 50.7% | 50.7% | 11.77 |
| +2% <= gap < +5% | full | 62,172 | +0.8 | -6.9 | 48.8% | 48.8% | 0.66 |
| gap >= +5% | full | 12,521 | +24.6 | +0.0 | 50.0% | 50.0% | 5.49 |
| gap <= -5% | last_24m | 2,668 | -18.5 | -24.7 | 48.3% | 51.6% | -1.76 |
| -5% < gap <= -2% | last_24m | 14,013 | +28.8 | +37.7 | 55.2% | 44.5% | 10.01 |
| -2% < gap <= -1% | last_24m | 33,417 | +24.4 | +22.2 | 54.8% | 44.9% | 17.98 |
| -1% < gap <= -0.3% | last_24m | 87,421 | +6.8 | +7.9 | 52.2% | 47.4% | 10.82 |
| flat (|gap| < 0.3%) | last_24m | 155,683 | -0.6 | +0.0 | 49.8% | 48.3% | -1.42 |
| +0.3% <= gap < +1% | last_24m | 101,029 | -3.2 | -5.4 | 48.2% | 48.2% | -5.75 |
| +1% <= gap < +2% | last_24m | 37,715 | -2.4 | -7.3 | 48.3% | 48.3% | -2.03 |
| +2% <= gap < +5% | last_24m | 15,339 | -32.7 | -34.6 | 44.5% | 44.5% | -12.8 |
| gap >= +5% | last_24m | 3,109 | -34.4 | -42.1 | 45.1% | 45.1% | -4.04 |
| gap <= -5% | last_12m | 1,253 | +43.4 | +20.9 | 52.6% | 47.2% | 2.99 |
| -5% < gap <= -2% | last_12m | 7,227 | +29.1 | +34.5 | 54.9% | 44.8% | 7.65 |
| -2% < gap <= -1% | last_12m | 18,225 | +8.6 | +13.9 | 53.0% | 46.7% | 5.0 |
| -1% < gap <= -0.3% | last_12m | 44,754 | +2.5 | +5.1 | 51.3% | 48.4% | 2.83 |
| flat (|gap| < 0.3%) | last_12m | 73,120 | -0.1 | -0.5 | 49.5% | 48.2% | -0.22 |
| +0.3% <= gap < +1% | last_12m | 49,439 | -1.5 | -6.8 | 47.8% | 47.8% | -1.82 |
| +1% <= gap < +2% | last_12m | 21,882 | -5.5 | -15.5 | 46.5% | 46.5% | -3.56 |
| +2% <= gap < +5% | last_12m | 8,572 | -14.1 | -23.1 | 46.3% | 46.3% | -4.21 |
| gap >= +5% | last_12m | 1,542 | -20.9 | -28.5 | 46.2% | 46.2% | -1.67 |

## 2. Day two after a big close-to-close move

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | Continuation | t |
|---|---|---|---|---|---|---|---|
| yesterday +10% or more | full | 7,538 | -10.6 | -15.3 | 48.0% | 48.0% | -1.89 |
| yesterday +5% to +10% | full | 37,440 | +0.6 | -0.8 | 49.6% | 49.6% | 0.35 |
| yesterday -5% to -10% | full | 35,518 | +22.3 | +17.7 | 52.4% | 47.3% | 11.66 |
| yesterday -10% or worse | full | 5,967 | +80.1 | +51.2 | 54.7% | 45.0% | 10.11 |
| yesterday +10% or more | last_24m | 1,822 | -56.9 | -67.6 | 41.9% | 41.9% | -5.99 |
| yesterday +5% to +10% | last_24m | 8,749 | +11.1 | +4.1 | 50.5% | 50.5% | 3.34 |
| yesterday -5% to -10% | last_24m | 8,172 | +42.7 | +29.0 | 54.5% | 45.3% | 10.59 |
| yesterday -10% or worse | last_24m | 1,391 | +12.1 | +7.3 | 50.7% | 49.1% | 0.98 |
| yesterday +10% or more | last_12m | 832 | +25.1 | +21.9 | 52.4% | 52.4% | 1.69 |
| yesterday +5% to +10% | last_12m | 5,075 | +26.3 | +25.6 | 53.8% | 53.8% | 5.84 |
| yesterday -5% to -10% | last_12m | 4,426 | +19.4 | +16.3 | 52.4% | 47.4% | 3.79 |
| yesterday -10% or worse | last_12m | 615 | -6.6 | -7.0 | 48.9% | 50.9% | -0.34 |

## 3. Three-day moves

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| 3-day return <= -15% | full | 8,202 | +35.1 | +11.2 | 50.8% | 5.07 |
| 3-day return -15% to -10% | full | 19,703 | +20.4 | +10.9 | 51.3% | 7.14 |
| 3-day return >= +15% | full | 11,210 | -0.8 | -5.2 | 49.1% | -0.2 |
| 3-day return <= -15% | last_24m | 1,972 | +7.7 | -13.5 | 48.3% | 0.64 |
| 3-day return -15% to -10% | last_24m | 4,721 | +26.9 | +2.4 | 50.2% | 4.31 |
| 3-day return >= +15% | last_24m | 2,646 | +6.5 | +0.8 | 50.0% | 0.84 |
| 3-day return <= -15% | last_12m | 823 | +28.7 | -2.9 | 49.6% | 1.96 |
| 3-day return -15% to -10% | last_12m | 2,395 | -2.4 | -12.9 | 48.1% | -0.33 |
| 3-day return >= +15% | last_12m | 1,484 | +17.9 | +11.6 | 51.9% | 1.66 |

## 4. 20-day momentum deciles

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| momentum top decile (20d) | full | 229,093 | +2.1 | +2.6 | 50.4% | 4.43 |
| momentum bottom decile (20d) | full | 229,322 | +3.1 | +1.8 | 50.2% | 6.03 |
| momentum top decile (20d) | last_24m | 45,159 | +2.6 | +1.8 | 50.2% | 2.14 |
| momentum bottom decile (20d) | last_24m | 45,173 | +1.3 | +0.0 | 49.6% | 1.09 |
| momentum top decile (20d) | last_12m | 22,659 | +5.9 | +0.2 | 50.0% | 3.21 |
| momentum bottom decile (20d) | last_12m | 22,673 | -1.8 | -3.0 | 49.1% | -1.05 |

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
| 2026 | 182,854 | 49.6% | +0.8 |

## 6. SPY conditionals

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| SPY all sessions | full | 2,717 | +2.2 | +5.1 | 53.8% | 1.39 |
| SPY gap >= +0.5% | full | 428 | +8.8 | +21.9 | 59.8% | 1.76 |
| SPY gap <= -0.5% | full | 344 | +6.2 | +7.4 | 53.5% | 0.89 |
| SPY after 3 up days | full | 438 | +1.4 | +4.4 | 52.7% | 0.55 |
| SPY after a -1% day | full | 294 | +9.2 | +2.2 | 52.0% | 1.16 |
| SPY all sessions | last_24m | 501 | +2.0 | +2.0 | 51.1% | 0.51 |
| SPY gap >= +0.5% | last_24m | 78 | -10.1 | -8.5 | 44.9% | -1.01 |
| SPY gap <= -0.5% | last_24m | 64 | +19.3 | -1.0 | 50.0% | 0.89 |
| SPY after 3 up days | last_24m | 84 | +1.7 | -0.4 | 50.0% | 0.28 |
| SPY after a -1% day | last_24m | 54 | +46.9 | +34.5 | 61.1% | 1.91 |
| SPY all sessions | last_12m | 251 | +0.7 | +0.1 | 50.2% | 0.17 |
| SPY gap >= +0.5% | last_12m | 45 | -6.1 | -9.8 | 42.2% | -0.54 |
| SPY gap <= -0.5% | last_12m | 30 | +3.2 | -3.1 | 43.3% | 0.24 |
| SPY after 3 up days | last_12m | 39 | -2.2 | +0.1 | 51.3% | -0.26 |
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
| 2026 | 203 | 49.8% | +1.6 |

_Current index membership (survivorship bias favours longs slightly). Research output, not investment advice._
