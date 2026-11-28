# Playbook priors, backtested on the full panel

901 tickers, 2016-01-04 to 2026-11-27, 2,351,050 stock-days (2,299,781 pass the ledger's price and liquidity filter). Every row measures the **open-to-close return of the session after the condition is known**, before costs; the ledger pays about 4 bps per round trip. Continuation = share of sessions where the open-to-close move had the same sign as the gap or the prior move.

## Verdicts on the playbook's priors

| Prior | Verdict |
|---|---|
| long a stock that gapped up 2-5% (continuation) | no reliable edge (mean +1.4 bps, t = 1.14, n = 63,492) |
| long a stock that gapped up 5%+ (continuation) | supported: +21.7 bps/session for that side, clears 4 bps costs (t = 4.99, n = 12,928) |
| short a stock that gapped down 2-5% (continuation) | goes the other way: -20.0 bps/session for that side (t = -14.85, n = 59,993) |
| short a stock that gapped down 5%+ (continuation) | supported: +43.2 bps/session for that side, clears 4 bps costs (t = 8.27, n = 12,113) |
| fade a +5% gap (short) | goes the other way: -21.7 bps/session for that side (t = -4.99, n = 12,928) |
| fade a -5% gap (long) | goes the other way: -43.2 bps/session for that side (t = -8.27, n = 12,113) |
| day-two fade after a +10% day (short) | supported: +12.7 bps/session for that side, clears 4 bps costs (t = 2.28, n = 7,666) |
| day-two bounce after a -10% day (long) | supported: +70.6 bps/session for that side, clears 4 bps costs (t = 9.13, n = 6,183) |
| oversold bounce after a -15% three-day drop (long) | supported: +34.1 bps/session for that side, clears 4 bps costs (t = 5.04, n = 8,423) |
| 20-day momentum top decile (long) | positive but inside costs (+2.1 bps vs 4 bps, t = 4.36, n = 230,781) |
| 20-day momentum bottom decile (short) | goes the other way: -2.6 bps/session for that side (t = -5.13, n = 231,084) |

## 1. Overnight gap -> open-to-close

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | Continuation | t |
|---|---|---|---|---|---|---|---|
| gap <= -5% | full | 12,113 | -43.2 | -37.4 | 46.4% | 53.3% | -8.27 |
| -5% < gap <= -2% | full | 59,993 | +20.0 | +18.7 | 52.5% | 47.1% | 14.85 |
| -2% < gap <= -1% | full | 148,669 | +9.8 | +13.3 | 52.8% | 46.8% | 16.23 |
| -1% < gap <= -0.3% | full | 423,597 | +2.9 | +7.9 | 52.1% | 47.3% | 10.71 |
| flat (|gap| < 0.3%) | full | 870,197 | -0.0 | +2.1 | 50.5% | 48.5% | -0.23 |
| +0.3% <= gap < +1% | full | 536,315 | +0.4 | +0.0 | 49.6% | 49.6% | 1.62 |
| +1% <= gap < +2% | full | 172,477 | +6.1 | +3.9 | 50.7% | 50.7% | 11.2 |
| +2% <= gap < +5% | full | 63,492 | +1.4 | -5.7 | 48.9% | 48.9% | 1.14 |
| gap >= +5% | full | 12,928 | +21.7 | -2.5 | 49.6% | 49.6% | 4.99 |
| gap <= -5% | last_24m | 2,834 | -18.7 | -26.2 | 48.0% | 51.9% | -1.82 |
| -5% < gap <= -2% | last_24m | 14,923 | +25.0 | +35.8 | 55.0% | 44.8% | 8.8 |
| -2% < gap <= -1% | last_24m | 34,656 | +23.0 | +22.2 | 54.8% | 44.9% | 17.22 |
| -1% < gap <= -0.3% | last_24m | 87,190 | +6.3 | +7.9 | 52.1% | 47.5% | 9.99 |
| flat (|gap| < 0.3%) | last_24m | 151,412 | -1.4 | +0.0 | 49.5% | 48.3% | -3.29 |
| +0.3% <= gap < +1% | last_24m | 99,261 | -4.0 | -6.1 | 48.0% | 48.0% | -7.0 |
| +1% <= gap < +2% | last_24m | 39,251 | -3.7 | -7.9 | 48.1% | 48.1% | -3.24 |
| +2% <= gap < +5% | last_24m | 16,125 | -29.8 | -30.7 | 45.0% | 45.0% | -12.02 |
| gap >= +5% | last_24m | 3,203 | -52.3 | -58.3 | 42.8% | 42.8% | -6.43 |
| gap <= -5% | last_12m | 1,422 | +27.3 | +16.0 | 52.0% | 47.9% | 1.95 |
| -5% < gap <= -2% | last_12m | 7,924 | +17.3 | +28.4 | 53.9% | 45.7% | 4.57 |
| -2% < gap <= -1% | last_12m | 19,246 | +8.2 | +15.4 | 53.2% | 46.4% | 4.8 |
| -1% < gap <= -0.3% | last_12m | 44,160 | +2.9 | +5.4 | 51.3% | 48.3% | 3.19 |
| flat (|gap| < 0.3%) | last_12m | 69,431 | -2.4 | -2.5 | 48.9% | 48.1% | -3.59 |
| +0.3% <= gap < +1% | last_12m | 48,853 | -6.0 | -10.0 | 47.0% | 47.0% | -7.13 |
| +1% <= gap < +2% | last_12m | 23,464 | -5.1 | -12.9 | 47.0% | 47.0% | -3.37 |
| +2% <= gap < +5% | last_12m | 9,507 | -0.8 | -10.4 | 48.3% | 48.3% | -0.26 |
| gap >= +5% | last_12m | 1,841 | -29.8 | -38.1 | 44.5% | 44.5% | -2.84 |

## 2. Day two after a big close-to-close move

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | Continuation | t |
|---|---|---|---|---|---|---|---|
| yesterday +10% or more | full | 7,666 | -12.7 | -16.9 | 47.8% | 47.8% | -2.28 |
| yesterday +5% to +10% | full | 38,262 | +0.4 | -1.5 | 49.5% | 49.5% | 0.26 |
| yesterday -5% to -10% | full | 36,247 | +19.8 | +15.8 | 52.1% | 47.5% | 10.42 |
| yesterday -10% or worse | full | 6,183 | +70.6 | +42.2 | 53.9% | 45.8% | 9.13 |
| yesterday +10% or more | last_24m | 1,816 | -59.9 | -62.8 | 42.5% | 42.5% | -6.18 |
| yesterday +5% to +10% | last_24m | 9,218 | +9.9 | +4.0 | 50.5% | 50.5% | 2.99 |
| yesterday -5% to -10% | last_24m | 8,753 | +31.8 | +22.7 | 53.4% | 46.4% | 8.0 |
| yesterday -10% or worse | last_24m | 1,565 | -7.0 | -4.4 | 48.9% | 50.9% | -0.59 |
| yesterday +10% or more | last_12m | 918 | +0.1 | -1.4 | 49.6% | 49.6% | 0.01 |
| yesterday +5% to +10% | last_12m | 5,589 | +20.0 | +15.9 | 52.2% | 52.2% | 4.6 |
| yesterday -5% to -10% | last_12m | 4,883 | -6.0 | -3.7 | 49.4% | 50.4% | -1.19 |
| yesterday -10% or worse | last_12m | 782 | -46.9 | -46.2 | 45.5% | 54.5% | -2.72 |

## 3. Three-day moves

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| 3-day return <= -15% | full | 8,423 | +34.1 | +11.2 | 50.9% | 5.04 |
| 3-day return -15% to -10% | full | 20,208 | +17.9 | +8.9 | 51.0% | 6.36 |
| 3-day return >= +15% | full | 11,335 | +0.7 | -3.9 | 49.3% | 0.19 |
| 3-day return <= -15% | last_24m | 2,134 | +11.7 | -7.1 | 49.0% | 1.03 |
| 3-day return -15% to -10% | last_24m | 5,124 | +18.4 | -3.2 | 49.4% | 3.07 |
| 3-day return >= +15% | last_24m | 2,621 | +9.7 | +5.2 | 50.7% | 1.25 |
| 3-day return <= -15% | last_12m | 967 | +24.7 | +7.5 | 50.6% | 1.77 |
| 3-day return -15% to -10% | last_12m | 2,722 | -16.4 | -19.9 | 46.6% | -2.36 |
| 3-day return >= +15% | last_12m | 1,537 | +22.5 | +17.9 | 52.6% | 2.18 |

## 4. 20-day momentum deciles

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| momentum top decile (20d) | full | 230,781 | +2.1 | +2.7 | 50.4% | 4.36 |
| momentum bottom decile (20d) | full | 231,084 | +2.6 | +1.7 | 50.2% | 5.13 |
| momentum top decile (20d) | last_24m | 45,000 | +2.1 | +2.2 | 50.3% | 1.75 |
| momentum bottom decile (20d) | last_24m | 45,089 | -1.0 | -1.5 | 49.4% | -0.8 |
| momentum top decile (20d) | last_12m | 22,590 | +4.8 | +0.0 | 49.9% | 2.65 |
| momentum bottom decile (20d) | last_12m | 22,679 | -5.2 | -3.3 | 49.0% | -2.88 |

## 5. Base rate: share of tradable stock-days that closed above the open

| Year | n | Share up | Mean OC (bps) |
|---|---|---|---|
| 2016 | 176,753 | 52.8% | +10.4 |
| 2017 | 197,549 | 51.4% | +2.6 |
| 2018 | 201,342 | 49.4% | -6.4 |
| 2019 | 205,494 | 52.7% | +6.7 |
| 2020 | 210,532 | 49.7% | +0.6 |
| 2021 | 216,688 | 50.2% | +0.7 |
| 2022 | 218,418 | 50.0% | +1.2 |
| 2023 | 219,501 | 51.5% | +6.0 |
| 2024 | 224,315 | 50.3% | -0.9 |
| 2025 | 224,018 | 51.0% | +4.2 |
| 2026 | 205,171 | 49.5% | -0.6 |

## 6. SPY conditionals

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| SPY all sessions | full | 2,742 | +1.9 | +5.3 | 53.9% | 1.17 |
| SPY gap >= +0.5% | full | 434 | +8.5 | +22.3 | 59.9% | 1.71 |
| SPY gap <= -0.5% | full | 351 | +6.4 | +8.0 | 53.8% | 0.93 |
| SPY after 3 up days | full | 439 | +1.4 | +4.5 | 52.8% | 0.55 |
| SPY after a -1% day | full | 301 | +7.1 | +1.0 | 51.5% | 0.9 |
| SPY all sessions | last_24m | 500 | +0.5 | +3.9 | 52.0% | 0.12 |
| SPY gap >= +0.5% | last_24m | 81 | -10.0 | -5.6 | 46.9% | -0.95 |
| SPY gap <= -0.5% | last_24m | 68 | +21.1 | +3.3 | 52.9% | 1.03 |
| SPY after 3 up days | last_24m | 77 | +2.0 | +0.1 | 50.6% | 0.32 |
| SPY after a -1% day | last_24m | 59 | +32.7 | +6.4 | 57.6% | 1.39 |
| SPY all sessions | last_12m | 251 | -2.4 | +0.9 | 50.6% | -0.53 |
| SPY gap >= +0.5% | last_12m | 44 | -3.3 | -8.5 | 43.2% | -0.28 |
| SPY gap <= -0.5% | last_12m | 33 | +6.3 | +0.5 | 51.5% | 0.45 |
| SPY after 3 up days | last_12m | 34 | +3.4 | +7.6 | 55.9% | 0.4 |
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
| 2026 | 228 | 50.9% | -2.4 |

_Current index membership (survivorship bias favours longs slightly). Research output, not investment advice._
