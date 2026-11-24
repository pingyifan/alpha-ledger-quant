# Playbook priors, backtested on the full panel

900 tickers, 2016-01-04 to 2026-11-23, 2,345,947 stock-days (2,294,815 pass the ledger's price and liquidity filter). Every row measures the **open-to-close return of the session after the condition is known**, before costs; the ledger pays about 4 bps per round trip. Continuation = share of sessions where the open-to-close move had the same sign as the gap or the prior move.

## Verdicts on the playbook's priors

| Prior | Verdict |
|---|---|
| long a stock that gapped up 2-5% (continuation) | no reliable edge (mean +1.4 bps, t = 1.12, n = 63,317) |
| long a stock that gapped up 5%+ (continuation) | supported: +21.6 bps/session for that side, clears 4 bps costs (t = 4.95, n = 12,897) |
| short a stock that gapped down 2-5% (continuation) | goes the other way: -19.3 bps/session for that side (t = -14.27, n = 59,679) |
| short a stock that gapped down 5%+ (continuation) | supported: +45.4 bps/session for that side, clears 4 bps costs (t = 8.67, n = 12,057) |
| fade a +5% gap (short) | goes the other way: -21.6 bps/session for that side (t = -4.95, n = 12,897) |
| fade a -5% gap (long) | goes the other way: -45.4 bps/session for that side (t = -8.67, n = 12,057) |
| day-two fade after a +10% day (short) | no reliable edge (mean -9.8 bps, t = -1.76, n = 7,605) |
| day-two bounce after a -10% day (long) | supported: +68.6 bps/session for that side, clears 4 bps costs (t = 8.87, n = 6,161) |
| oversold bounce after a -15% three-day drop (long) | supported: +33.6 bps/session for that side, clears 4 bps costs (t = 4.96, n = 8,415) |
| 20-day momentum top decile (long) | positive but inside costs (+1.9 bps vs 4 bps, t = 4.06, n = 230,340) |
| 20-day momentum bottom decile (short) | goes the other way: -2.5 bps/session for that side (t = -4.87, n = 230,561) |

## 1. Overnight gap -> open-to-close

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | Continuation | t |
|---|---|---|---|---|---|---|---|
| gap <= -5% | full | 12,057 | -45.4 | -39.4 | 46.2% | 53.5% | -8.67 |
| -5% < gap <= -2% | full | 59,679 | +19.3 | +18.1 | 52.4% | 47.2% | 14.27 |
| -2% < gap <= -1% | full | 148,224 | +9.4 | +12.9 | 52.7% | 46.8% | 15.57 |
| -1% < gap <= -0.3% | full | 422,626 | +2.7 | +7.8 | 52.1% | 47.3% | 10.07 |
| flat (|gap| < 0.3%) | full | 868,675 | -0.1 | +2.1 | 50.5% | 48.5% | -0.68 |
| +0.3% <= gap < +1% | full | 535,274 | +0.3 | +0.0 | 49.6% | 49.6% | 1.31 |
| +1% <= gap < +2% | full | 172,066 | +6.1 | +3.9 | 50.7% | 50.7% | 11.23 |
| +2% <= gap < +5% | full | 63,317 | +1.4 | -5.7 | 48.9% | 48.9% | 1.12 |
| gap >= +5% | full | 12,897 | +21.6 | -2.5 | 49.6% | 49.6% | 4.95 |
| gap <= -5% | last_24m | 2,784 | -27.3 | -35.1 | 47.3% | 52.5% | -2.64 |
| -5% < gap <= -2% | last_24m | 14,675 | +22.0 | +33.1 | 54.7% | 45.1% | 7.73 |
| -2% < gap <= -1% | last_24m | 34,383 | +21.4 | +20.6 | 54.5% | 45.2% | 15.94 |
| -1% < gap <= -0.3% | last_24m | 86,898 | +5.3 | +6.9 | 51.9% | 47.7% | 8.47 |
| flat (|gap| < 0.3%) | last_24m | 151,399 | -1.9 | -1.0 | 49.4% | 48.3% | -4.58 |
| +0.3% <= gap < +1% | last_24m | 99,623 | -4.4 | -6.4 | 47.9% | 47.9% | -7.64 |
| +1% <= gap < +2% | last_24m | 39,335 | -3.6 | -7.7 | 48.1% | 48.1% | -3.11 |
| +2% <= gap < +5% | last_24m | 16,053 | -30.1 | -31.3 | 45.0% | 45.0% | -12.07 |
| gap >= +5% | last_24m | 3,187 | -53.4 | -59.2 | 42.7% | 42.7% | -6.51 |
| gap <= -5% | last_12m | 1,369 | +10.4 | +7.1 | 50.6% | 49.2% | 0.74 |
| -5% < gap <= -2% | last_12m | 7,676 | +11.9 | +24.5 | 53.4% | 46.2% | 3.13 |
| -2% < gap <= -1% | last_12m | 18,971 | +5.5 | +13.2 | 52.7% | 46.9% | 3.24 |
| -1% < gap <= -0.3% | last_12m | 44,034 | +1.8 | +4.6 | 51.1% | 48.6% | 1.98 |
| flat (|gap| < 0.3%) | last_12m | 69,839 | -2.3 | -2.5 | 49.0% | 48.2% | -3.54 |
| +0.3% <= gap < +1% | last_12m | 49,062 | -5.0 | -9.2 | 47.3% | 47.3% | -6.0 |
| +1% <= gap < +2% | last_12m | 23,407 | -3.8 | -12.3 | 47.2% | 47.2% | -2.49 |
| +2% <= gap < +5% | last_12m | 9,410 | +0.0 | -10.3 | 48.4% | 48.4% | 0.01 |
| gap >= +5% | last_12m | 1,826 | -30.1 | -39.0 | 44.4% | 44.4% | -2.85 |

## 2. Day two after a big close-to-close move

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | Continuation | t |
|---|---|---|---|---|---|---|---|
| yesterday +10% or more | full | 7,605 | -9.8 | -14.3 | 48.1% | 48.1% | -1.76 |
| yesterday +5% to +10% | full | 38,029 | +0.4 | -1.3 | 49.5% | 49.5% | 0.24 |
| yesterday -5% to -10% | full | 36,156 | +19.1 | +15.4 | 52.0% | 47.6% | 10.07 |
| yesterday -10% or worse | full | 6,161 | +68.6 | +41.1 | 53.8% | 45.9% | 8.87 |
| yesterday +10% or more | last_24m | 1,769 | -48.0 | -53.4 | 43.5% | 43.5% | -4.88 |
| yesterday +5% to +10% | last_24m | 9,083 | +9.2 | +3.7 | 50.4% | 50.4% | 2.76 |
| yesterday -5% to -10% | last_24m | 8,711 | +28.5 | +20.6 | 53.1% | 46.7% | 7.19 |
| yesterday -10% or worse | last_24m | 1,546 | -16.1 | -10.8 | 48.3% | 51.5% | -1.37 |
| yesterday +10% or more | last_12m | 871 | +26.8 | +20.3 | 52.1% | 52.1% | 1.83 |
| yesterday +5% to +10% | last_12m | 5,558 | +23.8 | +22.8 | 53.1% | 53.1% | 5.46 |
| yesterday -5% to -10% | last_12m | 4,836 | -11.5 | -6.5 | 48.8% | 50.9% | -2.3 |
| yesterday -10% or worse | last_12m | 763 | -65.7 | -52.6 | 44.3% | 55.7% | -3.86 |

## 3. Three-day moves

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| 3-day return <= -15% | full | 8,415 | +33.6 | +10.6 | 50.8% | 4.96 |
| 3-day return -15% to -10% | full | 20,160 | +17.8 | +9.0 | 51.0% | 6.33 |
| 3-day return >= +15% | full | 11,315 | +0.5 | -4.1 | 49.3% | 0.12 |
| 3-day return <= -15% | last_24m | 2,130 | +10.1 | -7.6 | 48.9% | 0.9 |
| 3-day return -15% to -10% | last_24m | 5,103 | +17.0 | -3.7 | 49.3% | 2.84 |
| 3-day return >= +15% | last_24m | 2,635 | +9.0 | +4.7 | 50.6% | 1.17 |
| 3-day return <= -15% | last_12m | 966 | +23.2 | +5.8 | 50.4% | 1.66 |
| 3-day return -15% to -10% | last_12m | 2,714 | -18.8 | -19.9 | 46.6% | -2.71 |
| 3-day return >= +15% | last_12m | 1,537 | +23.1 | +17.9 | 52.6% | 2.22 |

## 4. 20-day momentum deciles

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| momentum top decile (20d) | full | 230,340 | +1.9 | +2.5 | 50.4% | 4.06 |
| momentum bottom decile (20d) | full | 230,561 | +2.5 | +1.6 | 50.2% | 4.87 |
| momentum top decile (20d) | last_24m | 45,000 | +1.1 | +0.9 | 50.1% | 0.89 |
| momentum bottom decile (20d) | last_24m | 45,000 | -2.0 | -2.0 | 49.4% | -1.64 |
| momentum top decile (20d) | last_12m | 22,590 | +4.7 | +0.0 | 49.9% | 2.58 |
| momentum bottom decile (20d) | last_12m | 22,590 | -5.6 | -2.7 | 49.1% | -3.11 |

## 5. Base rate: share of tradable stock-days that closed above the open

| Year | n | Share up | Mean OC (bps) |
|---|---|---|---|
| 2016 | 176,753 | 52.8% | +10.4 |
| 2017 | 197,427 | 51.4% | +2.6 |
| 2018 | 201,091 | 49.4% | -6.4 |
| 2019 | 205,254 | 52.7% | +6.7 |
| 2020 | 210,359 | 49.7% | +0.6 |
| 2021 | 216,436 | 50.2% | +0.7 |
| 2022 | 218,167 | 50.0% | +1.2 |
| 2023 | 219,251 | 51.5% | +6.0 |
| 2024 | 224,063 | 50.3% | -0.9 |
| 2025 | 223,768 | 51.0% | +4.2 |
| 2026 | 202,246 | 49.1% | -2.2 |

## 6. SPY conditionals

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| SPY all sessions | full | 2,739 | +1.8 | +5.1 | 53.8% | 1.11 |
| SPY gap >= +0.5% | full | 433 | +8.5 | +22.3 | 59.8% | 1.7 |
| SPY gap <= -0.5% | full | 349 | +5.7 | +6.8 | 53.6% | 0.83 |
| SPY after 3 up days | full | 439 | +1.4 | +4.5 | 52.8% | 0.55 |
| SPY after a -1% day | full | 301 | +7.1 | +1.0 | 51.5% | 0.9 |
| SPY all sessions | last_24m | 500 | -0.1 | +3.0 | 51.6% | -0.03 |
| SPY gap >= +0.5% | last_24m | 81 | -10.8 | -7.2 | 45.7% | -1.03 |
| SPY gap <= -0.5% | last_24m | 66 | +18.1 | +0.7 | 51.5% | 0.86 |
| SPY after 3 up days | last_24m | 80 | +1.6 | -0.4 | 50.0% | 0.25 |
| SPY after a -1% day | last_24m | 59 | +32.7 | +6.4 | 57.6% | 1.39 |
| SPY all sessions | last_12m | 251 | -2.7 | +0.9 | 50.6% | -0.59 |
| SPY gap >= +0.5% | last_12m | 44 | -2.0 | -8.5 | 43.2% | -0.17 |
| SPY gap <= -0.5% | last_12m | 31 | -1.1 | -2.6 | 48.4% | -0.08 |
| SPY after 3 up days | last_12m | 35 | +4.2 | +7.7 | 57.1% | 0.51 |
| SPY after a -1% day | last_12m | 28 | -13.9 | -14.8 | 42.9% | -0.73 |

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
| 2026 | 225 | 50.2% | -3.7 |

_Current index membership (survivorship bias favours longs slightly). Research output, not investment advice._
