# Playbook priors, backtested on the full panel

901 tickers, 2016-01-04 to 2026-11-25, 2,350,150 stock-days (2,298,881 pass the ledger's price and liquidity filter). Every row measures the **open-to-close return of the session after the condition is known**, before costs; the ledger pays about 4 bps per round trip. Continuation = share of sessions where the open-to-close move had the same sign as the gap or the prior move.

## Verdicts on the playbook's priors

| Prior | Verdict |
|---|---|
| long a stock that gapped up 2-5% (continuation) | no reliable edge (mean +1.4 bps, t = 1.09, n = 63,355) |
| long a stock that gapped up 5%+ (continuation) | supported: +21.7 bps/session for that side, clears 4 bps costs (t = 4.98, n = 12,906) |
| short a stock that gapped down 2-5% (continuation) | goes the other way: -20.0 bps/session for that side (t = -14.84, n = 59,986) |
| short a stock that gapped down 5%+ (continuation) | supported: +43.1 bps/session for that side, clears 4 bps costs (t = 8.26, n = 12,116) |
| fade a +5% gap (short) | goes the other way: -21.7 bps/session for that side (t = -4.98, n = 12,906) |
| fade a -5% gap (long) | goes the other way: -43.1 bps/session for that side (t = -8.26, n = 12,116) |
| day-two fade after a +10% day (short) | supported: +12.7 bps/session for that side, clears 4 bps costs (t = 2.28, n = 7,669) |
| day-two bounce after a -10% day (long) | supported: +70.6 bps/session for that side, clears 4 bps costs (t = 9.14, n = 6,182) |
| oversold bounce after a -15% three-day drop (long) | supported: +34.1 bps/session for that side, clears 4 bps costs (t = 5.04, n = 8,423) |
| 20-day momentum top decile (long) | positive but inside costs (+2.0 bps vs 4 bps, t = 4.29, n = 230,691) |
| 20-day momentum bottom decile (short) | goes the other way: -2.6 bps/session for that side (t = -5.1, n = 230,994) |

## 1. Overnight gap -> open-to-close

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | Continuation | t |
|---|---|---|---|---|---|---|---|
| gap <= -5% | full | 12,116 | -43.1 | -37.3 | 46.4% | 53.3% | -8.26 |
| -5% < gap <= -2% | full | 59,986 | +20.0 | +18.7 | 52.5% | 47.1% | 14.84 |
| -2% < gap <= -1% | full | 148,656 | +9.7 | +13.2 | 52.8% | 46.8% | 16.17 |
| -1% < gap <= -0.3% | full | 423,495 | +2.9 | +7.9 | 52.1% | 47.3% | 10.66 |
| flat (|gap| < 0.3%) | full | 869,944 | -0.1 | +2.1 | 50.5% | 48.5% | -0.33 |
| +0.3% <= gap < +1% | full | 536,122 | +0.4 | +0.0 | 49.6% | 49.6% | 1.57 |
| +1% <= gap < +2% | full | 172,301 | +6.1 | +3.8 | 50.7% | 50.7% | 11.19 |
| +2% <= gap < +5% | full | 63,355 | +1.4 | -5.8 | 48.9% | 48.9% | 1.09 |
| gap >= +5% | full | 12,906 | +21.7 | -2.4 | 49.6% | 49.6% | 4.98 |
| gap <= -5% | last_24m | 2,840 | -18.3 | -26.2 | 48.0% | 51.9% | -1.78 |
| -5% < gap <= -2% | last_24m | 14,941 | +24.8 | +35.7 | 54.9% | 44.8% | 8.74 |
| -2% < gap <= -1% | last_24m | 34,714 | +22.7 | +21.9 | 54.7% | 44.9% | 17.03 |
| -1% < gap <= -0.3% | last_24m | 87,410 | +6.1 | +7.6 | 52.1% | 47.5% | 9.71 |
| flat (|gap| < 0.3%) | last_24m | 151,913 | -1.5 | -0.5 | 49.5% | 48.3% | -3.63 |
| +0.3% <= gap < +1% | last_24m | 99,570 | -4.2 | -6.3 | 47.9% | 47.9% | -7.39 |
| +1% <= gap < +2% | last_24m | 39,156 | -4.0 | -8.2 | 48.0% | 48.0% | -3.44 |
| +2% <= gap < +5% | last_24m | 16,010 | -30.4 | -31.3 | 45.0% | 45.0% | -12.17 |
| gap >= +5% | last_24m | 3,189 | -52.9 | -58.7 | 42.8% | 42.8% | -6.46 |
| gap <= -5% | last_12m | 1,423 | +26.6 | +15.5 | 51.9% | 47.9% | 1.9 |
| -5% < gap <= -2% | last_12m | 7,924 | +17.2 | +28.3 | 53.9% | 45.7% | 4.54 |
| -2% < gap <= -1% | last_12m | 19,247 | +8.0 | +15.3 | 53.2% | 46.5% | 4.74 |
| -1% < gap <= -0.3% | last_12m | 44,256 | +3.0 | +5.4 | 51.3% | 48.3% | 3.3 |
| flat (|gap| < 0.3%) | last_12m | 69,639 | -2.2 | -2.3 | 49.0% | 48.1% | -3.39 |
| +0.3% <= gap < +1% | last_12m | 48,817 | -5.8 | -9.9 | 47.0% | 47.0% | -6.96 |
| +1% <= gap < +2% | last_12m | 23,333 | -4.8 | -13.0 | 47.0% | 47.0% | -3.2 |
| +2% <= gap < +5% | last_12m | 9,384 | -1.1 | -10.9 | 48.2% | 48.2% | -0.36 |
| gap >= +5% | last_12m | 1,824 | -30.5 | -38.3 | 44.4% | 44.4% | -2.89 |

## 2. Day two after a big close-to-close move

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | Continuation | t |
|---|---|---|---|---|---|---|---|
| yesterday +10% or more | full | 7,669 | -12.7 | -16.9 | 47.8% | 47.8% | -2.28 |
| yesterday +5% to +10% | full | 38,234 | +0.3 | -1.6 | 49.5% | 49.5% | 0.2 |
| yesterday -5% to -10% | full | 36,247 | +19.8 | +15.8 | 52.1% | 47.5% | 10.43 |
| yesterday -10% or worse | full | 6,182 | +70.6 | +42.2 | 53.9% | 45.8% | 9.14 |
| yesterday +10% or more | last_24m | 1,821 | -59.4 | -62.8 | 42.4% | 42.4% | -6.11 |
| yesterday +5% to +10% | last_24m | 9,237 | +8.8 | +3.0 | 50.3% | 50.3% | 2.67 |
| yesterday -5% to -10% | last_24m | 8,766 | +31.7 | +22.3 | 53.4% | 46.4% | 7.99 |
| yesterday -10% or worse | last_24m | 1,565 | -6.9 | -4.4 | 48.9% | 50.9% | -0.59 |
| yesterday +10% or more | last_12m | 921 | +0.1 | -0.9 | 49.6% | 49.6% | 0.0 |
| yesterday +5% to +10% | last_12m | 5,605 | +20.6 | +16.5 | 52.3% | 52.3% | 4.72 |
| yesterday -5% to -10% | last_12m | 4,882 | -6.0 | -3.7 | 49.4% | 50.4% | -1.18 |
| yesterday -10% or worse | last_12m | 782 | -46.1 | -45.7 | 45.6% | 54.4% | -2.67 |

## 3. Three-day moves

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| 3-day return <= -15% | full | 8,423 | +34.1 | +11.2 | 50.9% | 5.04 |
| 3-day return -15% to -10% | full | 20,205 | +17.9 | +8.9 | 51.0% | 6.36 |
| 3-day return >= +15% | full | 11,326 | +0.6 | -4.1 | 49.3% | 0.15 |
| 3-day return <= -15% | last_24m | 2,134 | +11.7 | -7.1 | 49.0% | 1.03 |
| 3-day return -15% to -10% | last_24m | 5,125 | +18.7 | -2.9 | 49.4% | 3.11 |
| 3-day return >= +15% | last_24m | 2,630 | +9.2 | +4.4 | 50.6% | 1.19 |
| 3-day return <= -15% | last_12m | 967 | +24.7 | +7.5 | 50.6% | 1.77 |
| 3-day return -15% to -10% | last_12m | 2,722 | -16.2 | -19.6 | 46.6% | -2.32 |
| 3-day return >= +15% | last_12m | 1,540 | +23.7 | +18.9 | 52.7% | 2.28 |

## 4. 20-day momentum deciles

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| momentum top decile (20d) | full | 230,691 | +2.0 | +2.6 | 50.4% | 4.29 |
| momentum bottom decile (20d) | full | 230,994 | +2.6 | +1.7 | 50.2% | 5.1 |
| momentum top decile (20d) | last_24m | 45,090 | +1.8 | +1.7 | 50.2% | 1.5 |
| momentum bottom decile (20d) | last_24m | 45,179 | -1.3 | -1.8 | 49.4% | -1.04 |
| momentum top decile (20d) | last_12m | 22,590 | +4.8 | +0.0 | 49.9% | 2.64 |
| momentum bottom decile (20d) | last_12m | 22,679 | -5.0 | -3.1 | 49.1% | -2.77 |

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
| 2026 | 204,271 | 49.4% | -0.7 |

## 6. SPY conditionals

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| SPY all sessions | full | 2,741 | +1.9 | +5.2 | 53.9% | 1.16 |
| SPY gap >= +0.5% | full | 433 | +8.5 | +22.3 | 59.8% | 1.7 |
| SPY gap <= -0.5% | full | 351 | +6.4 | +8.0 | 53.8% | 0.93 |
| SPY after 3 up days | full | 439 | +1.4 | +4.5 | 52.8% | 0.55 |
| SPY after a -1% day | full | 301 | +7.1 | +1.0 | 51.5% | 0.9 |
| SPY all sessions | last_24m | 501 | +0.4 | +3.2 | 51.9% | 0.1 |
| SPY gap >= +0.5% | last_24m | 80 | -10.5 | -6.4 | 46.2% | -0.99 |
| SPY gap <= -0.5% | last_24m | 68 | +21.1 | +3.3 | 52.9% | 1.03 |
| SPY after 3 up days | last_24m | 79 | +2.0 | +0.1 | 50.6% | 0.32 |
| SPY after a -1% day | last_24m | 59 | +32.7 | +6.4 | 57.6% | 1.39 |
| SPY all sessions | last_12m | 251 | -2.4 | +0.9 | 50.6% | -0.53 |
| SPY gap >= +0.5% | last_12m | 43 | -4.2 | -9.8 | 41.9% | -0.35 |
| SPY gap <= -0.5% | last_12m | 33 | +6.3 | +0.5 | 51.5% | 0.45 |
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
| 2026 | 227 | 50.7% | -2.6 |

_Current index membership (survivorship bias favours longs slightly). Research output, not investment advice._
