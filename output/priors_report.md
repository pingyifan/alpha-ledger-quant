# Playbook priors, backtested on the full panel

902 tickers, 2016-01-04 to 2026-11-12, 2,347,151 stock-days (2,295,904 pass the ledger's price and liquidity filter). Every row measures the **open-to-close return of the session after the condition is known**, before costs; the ledger pays about 4 bps per round trip. Continuation = share of sessions where the open-to-close move had the same sign as the gap or the prior move.

## Verdicts on the playbook's priors

| Prior | Verdict |
|---|---|
| long a stock that gapped up 2-5% (continuation) | no reliable edge (mean +2.1 bps, t = 1.7, n = 63,042) |
| long a stock that gapped up 5%+ (continuation) | supported: +24.3 bps/session for that side, clears 4 bps costs (t = 5.5, n = 12,726) |
| short a stock that gapped down 2-5% (continuation) | goes the other way: -20.3 bps/session for that side (t = -15.08, n = 59,609) |
| short a stock that gapped down 5%+ (continuation) | supported: +45.4 bps/session for that side, clears 4 bps costs (t = 8.67, n = 12,052) |
| fade a +5% gap (short) | goes the other way: -24.3 bps/session for that side (t = -5.5, n = 12,726) |
| fade a -5% gap (long) | goes the other way: -45.4 bps/session for that side (t = -8.67, n = 12,052) |
| day-two fade after a +10% day (short) | no reliable edge (mean -10.2 bps, t = -1.83, n = 7,614) |
| day-two bounce after a -10% day (long) | supported: +71.3 bps/session for that side, clears 4 bps costs (t = 9.17, n = 6,131) |
| oversold bounce after a -15% three-day drop (long) | supported: +34.9 bps/session for that side, clears 4 bps costs (t = 5.14, n = 8,403) |
| 20-day momentum top decile (long) | positive but inside costs (+2.0 bps vs 4 bps, t = 4.24, n = 230,468) |
| 20-day momentum bottom decile (short) | goes the other way: -3.0 bps/session for that side (t = -5.91, n = 230,720) |

## 1. Overnight gap -> open-to-close

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | Continuation | t |
|---|---|---|---|---|---|---|---|
| gap <= -5% | full | 12,052 | -45.4 | -39.3 | 46.3% | 53.4% | -8.67 |
| -5% < gap <= -2% | full | 59,609 | +20.3 | +18.8 | 52.5% | 47.1% | 15.08 |
| -2% < gap <= -1% | full | 147,977 | +10.0 | +13.4 | 52.8% | 46.7% | 16.51 |
| -1% < gap <= -0.3% | full | 422,579 | +2.9 | +7.9 | 52.2% | 47.3% | 10.94 |
| flat (|gap| < 0.3%) | full | 870,330 | +0.0 | +2.2 | 50.5% | 48.5% | 0.08 |
| +0.3% <= gap < +1% | full | 535,720 | +0.5 | +0.0 | 49.6% | 49.6% | 2.08 |
| +1% <= gap < +2% | full | 171,869 | +6.4 | +4.2 | 50.8% | 50.8% | 11.77 |
| +2% <= gap < +5% | full | 63,042 | +2.1 | -5.4 | 49.0% | 49.0% | 1.7 |
| gap >= +5% | full | 12,726 | +24.3 | +0.0 | 50.0% | 50.0% | 5.5 |
| gap <= -5% | last_24m | 2,767 | -28.1 | -35.1 | 47.5% | 52.4% | -2.69 |
| -5% < gap <= -2% | last_24m | 14,539 | +26.5 | +36.7 | 55.2% | 44.6% | 9.31 |
| -2% < gap <= -1% | last_24m | 34,340 | +24.4 | +23.3 | 55.1% | 44.6% | 18.3 |
| -1% < gap <= -0.3% | last_24m | 87,147 | +6.8 | +8.3 | 52.3% | 47.3% | 10.81 |
| flat (|gap| < 0.3%) | last_24m | 153,552 | -1.0 | +0.0 | 49.7% | 48.3% | -2.35 |
| +0.3% <= gap < +1% | last_24m | 100,346 | -3.2 | -5.3 | 48.2% | 48.2% | -5.72 |
| +1% <= gap < +2% | last_24m | 38,965 | -2.0 | -6.2 | 48.5% | 48.5% | -1.7 |
| +2% <= gap < +5% | last_24m | 15,710 | -27.7 | -31.1 | 45.1% | 45.1% | -10.95 |
| gap >= +5% | last_24m | 3,021 | -47.4 | -53.0 | 43.6% | 43.6% | -5.52 |
| gap <= -5% | last_12m | 1,350 | +15.1 | +10.2 | 51.0% | 48.7% | 1.05 |
| -5% < gap <= -2% | last_12m | 7,668 | +23.1 | +33.0 | 54.8% | 44.8% | 6.16 |
| -2% < gap <= -1% | last_12m | 18,826 | +9.1 | +16.8 | 53.5% | 46.2% | 5.39 |
| -1% < gap <= -0.3% | last_12m | 44,066 | +2.6 | +5.4 | 51.4% | 48.3% | 2.91 |
| flat (|gap| < 0.3%) | last_12m | 71,100 | -1.4 | -1.9 | 49.1% | 48.2% | -2.15 |
| +0.3% <= gap < +1% | last_12m | 49,210 | -2.6 | -7.2 | 47.8% | 47.8% | -3.07 |
| +1% <= gap < +2% | last_12m | 23,088 | -3.7 | -11.8 | 47.3% | 47.3% | -2.38 |
| +2% <= gap < +5% | last_12m | 9,115 | -2.1 | -11.2 | 48.2% | 48.2% | -0.66 |
| gap >= +5% | last_12m | 1,652 | -23.9 | -33.7 | 45.8% | 45.8% | -2.06 |

## 2. Day two after a big close-to-close move

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | Continuation | t |
|---|---|---|---|---|---|---|---|
| yesterday +10% or more | full | 7,614 | -10.2 | -14.4 | 48.1% | 48.1% | -1.83 |
| yesterday +5% to +10% | full | 38,091 | +0.5 | -1.1 | 49.5% | 49.5% | 0.33 |
| yesterday -5% to -10% | full | 35,951 | +20.3 | +16.8 | 52.2% | 47.4% | 10.64 |
| yesterday -10% or worse | full | 6,131 | +71.3 | +44.7 | 54.1% | 45.6% | 9.17 |
| yesterday +10% or more | last_24m | 1,773 | -47.6 | -53.5 | 43.4% | 43.4% | -4.84 |
| yesterday +5% to +10% | last_24m | 9,098 | +10.3 | +4.4 | 50.6% | 50.6% | 3.09 |
| yesterday -5% to -10% | last_24m | 8,514 | +33.8 | +25.2 | 53.9% | 45.9% | 8.39 |
| yesterday -10% or worse | last_24m | 1,514 | -11.3 | -4.2 | 49.1% | 50.7% | -0.95 |
| yesterday +10% or more | last_12m | 864 | +28.1 | +19.8 | 52.1% | 52.1% | 1.9 |
| yesterday +5% to +10% | last_12m | 5,544 | +23.2 | +23.1 | 53.1% | 53.1% | 5.3 |
| yesterday -5% to -10% | last_12m | 4,684 | +1.2 | +5.8 | 51.0% | 48.8% | 0.24 |
| yesterday -10% or worse | last_12m | 730 | -46.6 | -36.8 | 46.2% | 53.8% | -2.61 |

## 3. Three-day moves

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| 3-day return <= -15% | full | 8,403 | +34.9 | +12.5 | 51.0% | 5.14 |
| 3-day return -15% to -10% | full | 19,993 | +19.9 | +10.8 | 51.3% | 7.0 |
| 3-day return >= +15% | full | 11,331 | +0.6 | -4.0 | 49.3% | 0.16 |
| 3-day return <= -15% | last_24m | 2,133 | +12.4 | -7.0 | 49.1% | 1.09 |
| 3-day return -15% to -10% | last_24m | 4,950 | +25.2 | +2.4 | 50.2% | 4.12 |
| 3-day return >= +15% | last_24m | 2,651 | +8.8 | +4.2 | 50.6% | 1.14 |
| 3-day return <= -15% | last_12m | 941 | +34.0 | +23.2 | 51.6% | 2.36 |
| 3-day return -15% to -10% | last_12m | 2,567 | -1.2 | -7.3 | 48.9% | -0.16 |
| 3-day return >= +15% | last_12m | 1,529 | +23.2 | +18.8 | 52.7% | 2.21 |

## 4. 20-day momentum deciles

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| momentum top decile (20d) | full | 230,468 | +2.0 | +2.6 | 50.4% | 4.24 |
| momentum bottom decile (20d) | full | 230,720 | +3.0 | +2.0 | 50.3% | 5.91 |
| momentum top decile (20d) | last_24m | 45,174 | +1.9 | +1.5 | 50.2% | 1.54 |
| momentum bottom decile (20d) | last_24m | 45,188 | +1.3 | +0.0 | 49.9% | 1.08 |
| momentum top decile (20d) | last_12m | 22,674 | +4.6 | +0.0 | 50.0% | 2.56 |
| momentum bottom decile (20d) | last_12m | 22,688 | -1.3 | +0.0 | 49.7% | -0.71 |

## 5. Base rate: share of tradable stock-days that closed above the open

| Year | n | Share up | Mean OC (bps) |
|---|---|---|---|
| 2016 | 177,217 | 52.8% | +10.4 |
| 2017 | 198,052 | 51.4% | +2.6 |
| 2018 | 201,844 | 49.4% | -6.4 |
| 2019 | 205,998 | 52.6% | +6.7 |
| 2020 | 211,038 | 49.7% | +0.6 |
| 2021 | 217,192 | 50.2% | +0.7 |
| 2022 | 218,920 | 50.0% | +1.2 |
| 2023 | 220,001 | 51.5% | +6.0 |
| 2024 | 224,821 | 50.3% | -0.9 |
| 2025 | 224,437 | 51.0% | +4.2 |
| 2026 | 196,384 | 49.7% | +0.6 |

## 6. SPY conditionals

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| SPY all sessions | full | 2,732 | +2.2 | +5.5 | 54.0% | 1.34 |
| SPY gap >= +0.5% | full | 431 | +9.3 | +22.3 | 60.1% | 1.87 |
| SPY gap <= -0.5% | full | 348 | +6.1 | +7.4 | 53.7% | 0.89 |
| SPY after 3 up days | full | 439 | +1.4 | +4.5 | 52.8% | 0.55 |
| SPY after a -1% day | full | 297 | +8.8 | +1.1 | 52.2% | 1.12 |
| SPY all sessions | last_24m | 501 | +1.9 | +4.5 | 52.5% | 0.47 |
| SPY gap >= +0.5% | last_24m | 79 | -7.0 | -5.6 | 46.8% | -0.69 |
| SPY gap <= -0.5% | last_24m | 67 | +20.1 | +0.9 | 52.2% | 0.98 |
| SPY after 3 up days | last_24m | 82 | +2.0 | +1.7 | 51.2% | 0.33 |
| SPY after a -1% day | last_24m | 56 | +43.7 | +23.2 | 62.5% | 1.84 |
| SPY all sessions | last_12m | 251 | -0.1 | +3.2 | 51.8% | -0.01 |
| SPY gap >= +0.5% | last_12m | 43 | -1.7 | -7.2 | 44.2% | -0.14 |
| SPY gap <= -0.5% | last_12m | 32 | +5.1 | -1.0 | 50.0% | 0.4 |
| SPY after 3 up days | last_12m | 36 | +0.6 | +7.6 | 55.6% | 0.07 |
| SPY after a -1% day | last_12m | 26 | +9.8 | +0.9 | 53.8% | 0.61 |

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
| 2026 | 218 | 51.8% | +0.7 |

_Current index membership (survivorship bias favours longs slightly). Research output, not investment advice._
