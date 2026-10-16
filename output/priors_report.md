# Playbook priors, backtested on the full panel

902 tickers, 2016-01-04 to 2026-10-15, 2,326,642 stock-days (2,277,745 pass the ledger's price and liquidity filter). Every row measures the **open-to-close return of the session after the condition is known**, before costs; the ledger pays about 4 bps per round trip. Continuation = share of sessions where the open-to-close move had the same sign as the gap or the prior move.

## Verdicts on the playbook's priors

| Prior | Verdict |
|---|---|
| long a stock that gapped up 2-5% (continuation) | no reliable edge (mean +1.1 bps, t = 0.83, n = 61,984) |
| long a stock that gapped up 5%+ (continuation) | supported: +25.0 bps/session for that side, clears 4 bps costs (t = 5.57, n = 12,498) |
| short a stock that gapped down 2-5% (continuation) | goes the other way: -21.2 bps/session for that side (t = -15.63, n = 58,718) |
| short a stock that gapped down 5%+ (continuation) | supported: +43.6 bps/session for that side, clears 4 bps costs (t = 8.22, n = 11,775) |
| fade a +5% gap (short) | goes the other way: -25.0 bps/session for that side (t = -5.57, n = 12,498) |
| fade a -5% gap (long) | goes the other way: -43.6 bps/session for that side (t = -8.22, n = 11,775) |
| day-two fade after a +10% day (short) | no reliable edge (mean -10.8 bps, t = -1.91, n = 7,535) |
| day-two bounce after a -10% day (long) | supported: +80.2 bps/session for that side, clears 4 bps costs (t = 10.12, n = 5,958) |
| oversold bounce after a -15% three-day drop (long) | supported: +36.3 bps/session for that side, clears 4 bps costs (t = 5.23, n = 8,168) |
| 20-day momentum top decile (long) | positive but inside costs (+2.1 bps vs 4 bps, t = 4.37, n = 228,620) |
| 20-day momentum bottom decile (short) | goes the other way: -3.2 bps/session for that side (t = -6.3, n = 228,848) |

## 1. Overnight gap -> open-to-close

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | Continuation | t |
|---|---|---|---|---|---|---|---|
| gap <= -5% | full | 11,775 | -43.6 | -38.5 | 46.4% | 53.3% | -8.22 |
| -5% < gap <= -2% | full | 58,718 | +21.2 | +19.0 | 52.6% | 47.0% | 15.63 |
| -2% < gap <= -1% | full | 146,188 | +9.8 | +13.1 | 52.7% | 46.8% | 16.13 |
| -1% < gap <= -0.3% | full | 419,443 | +2.9 | +7.9 | 52.1% | 47.3% | 10.77 |
| flat (|gap| < 0.3%) | full | 866,251 | +0.0 | +2.2 | 50.5% | 48.5% | 0.14 |
| +0.3% <= gap < +1% | full | 531,676 | +0.4 | +0.0 | 49.6% | 49.6% | 1.86 |
| +1% <= gap < +2% | full | 169,212 | +6.4 | +4.1 | 50.7% | 50.7% | 11.71 |
| +2% <= gap < +5% | full | 61,984 | +1.1 | -6.7 | 48.8% | 48.8% | 0.83 |
| gap >= +5% | full | 12,498 | +25.0 | +0.1 | 50.0% | 50.0% | 5.57 |
| gap <= -5% | last_24m | 2,628 | -16.1 | -21.3 | 48.5% | 51.4% | -1.52 |
| -5% < gap <= -2% | last_24m | 13,852 | +29.9 | +38.1 | 55.3% | 44.4% | 10.37 |
| -2% < gap <= -1% | last_24m | 33,216 | +23.7 | +21.5 | 54.7% | 45.0% | 17.5 |
| -1% < gap <= -0.3% | last_24m | 87,553 | +6.1 | +7.5 | 52.1% | 47.5% | 9.88 |
| flat (|gap| < 0.3%) | last_24m | 156,400 | -0.9 | +0.0 | 49.7% | 48.4% | -2.27 |
| +0.3% <= gap < +1% | last_24m | 100,730 | -3.8 | -6.0 | 48.0% | 48.0% | -6.89 |
| +1% <= gap < +2% | last_24m | 37,448 | -2.7 | -7.5 | 48.2% | 48.2% | -2.31 |
| +2% <= gap < +5% | last_24m | 15,258 | -32.3 | -34.5 | 44.5% | 44.5% | -12.62 |
| gap >= +5% | last_24m | 3,095 | -33.4 | -40.9 | 45.2% | 45.2% | -3.92 |
| gap <= -5% | last_12m | 1,215 | +48.2 | +24.7 | 52.8% | 47.0% | 3.31 |
| -5% < gap <= -2% | last_12m | 7,100 | +30.6 | +35.2 | 55.0% | 44.6% | 8.03 |
| -2% < gap <= -1% | last_12m | 18,058 | +7.0 | +12.6 | 52.7% | 47.0% | 4.04 |
| -1% < gap <= -0.3% | last_12m | 44,611 | +1.8 | +4.9 | 51.2% | 48.4% | 2.03 |
| flat (|gap| < 0.3%) | last_12m | 73,804 | -0.7 | -0.7 | 49.4% | 48.2% | -1.13 |
| +0.3% <= gap < +1% | last_12m | 49,359 | -2.8 | -7.4 | 47.6% | 47.6% | -3.38 |
| +1% <= gap < +2% | last_12m | 21,638 | -5.8 | -15.6 | 46.5% | 46.5% | -3.71 |
| +2% <= gap < +5% | last_12m | 8,486 | -13.5 | -22.2 | 46.5% | 46.5% | -4.0 |
| gap >= +5% | last_12m | 1,539 | -17.3 | -25.8 | 46.7% | 46.7% | -1.38 |

## 2. Day two after a big close-to-close move

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | Continuation | t |
|---|---|---|---|---|---|---|---|
| yesterday +10% or more | full | 7,535 | -10.8 | -16.0 | 48.0% | 48.0% | -1.91 |
| yesterday +5% to +10% | full | 37,335 | +0.9 | +0.0 | 49.6% | 49.6% | 0.57 |
| yesterday -5% to -10% | full | 35,433 | +22.3 | +17.7 | 52.4% | 47.2% | 11.68 |
| yesterday -10% or worse | full | 5,958 | +80.2 | +51.6 | 54.7% | 45.0% | 10.12 |
| yesterday +10% or more | last_24m | 1,820 | -57.0 | -67.6 | 42.0% | 42.0% | -5.99 |
| yesterday +5% to +10% | last_24m | 8,687 | +12.0 | +4.4 | 50.6% | 50.6% | 3.59 |
| yesterday -5% to -10% | last_24m | 8,123 | +42.7 | +29.0 | 54.6% | 45.2% | 10.55 |
| yesterday -10% or worse | last_24m | 1,389 | +11.1 | +6.1 | 50.6% | 49.2% | 0.9 |
| yesterday +10% or more | last_12m | 834 | +23.3 | +22.9 | 52.5% | 52.5% | 1.56 |
| yesterday +5% to +10% | last_12m | 5,026 | +28.3 | +27.3 | 54.2% | 54.2% | 6.28 |
| yesterday -5% to -10% | last_12m | 4,402 | +19.0 | +17.8 | 52.7% | 47.2% | 3.72 |
| yesterday -10% or worse | last_12m | 619 | -2.0 | -1.9 | 49.4% | 50.4% | -0.11 |

## 3. Three-day moves

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| 3-day return <= -15% | full | 8,168 | +36.3 | +12.9 | 51.0% | 5.23 |
| 3-day return -15% to -10% | full | 19,624 | +21.0 | +11.2 | 51.4% | 7.32 |
| 3-day return >= +15% | full | 11,206 | -0.8 | -5.2 | 49.1% | -0.2 |
| 3-day return <= -15% | last_24m | 1,940 | +11.7 | -7.3 | 49.0% | 0.98 |
| 3-day return -15% to -10% | last_24m | 4,661 | +29.0 | +4.1 | 50.5% | 4.62 |
| 3-day return >= +15% | last_24m | 2,650 | +6.7 | +1.0 | 50.1% | 0.87 |
| 3-day return <= -15% | last_12m | 793 | +40.5 | +22.1 | 51.1% | 2.71 |
| 3-day return -15% to -10% | last_12m | 2,339 | +2.7 | -10.3 | 48.8% | 0.37 |
| 3-day return >= +15% | last_12m | 1,498 | +16.2 | +11.0 | 51.9% | 1.51 |

## 4. 20-day momentum deciles

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| momentum top decile (20d) | full | 228,620 | +2.1 | +2.6 | 50.4% | 4.37 |
| momentum bottom decile (20d) | full | 228,848 | +3.2 | +1.9 | 50.2% | 6.3 |
| momentum top decile (20d) | last_24m | 45,135 | +2.4 | +1.5 | 50.2% | 1.95 |
| momentum bottom decile (20d) | last_24m | 45,149 | +1.8 | +0.0 | 49.7% | 1.47 |
| momentum top decile (20d) | last_12m | 22,635 | +4.3 | +0.0 | 49.8% | 2.38 |
| momentum bottom decile (20d) | last_12m | 22,649 | -0.4 | -1.8 | 49.4% | -0.25 |

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
| 2026 | 178,160 | 49.5% | +0.2 |

## 6. SPY conditionals

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| SPY all sessions | full | 2,712 | +2.3 | +5.2 | 53.9% | 1.41 |
| SPY gap >= +0.5% | full | 427 | +8.8 | +22.3 | 60.0% | 1.76 |
| SPY gap <= -0.5% | full | 343 | +6.3 | +8.0 | 53.6% | 0.91 |
| SPY after 3 up days | full | 437 | +1.5 | +4.5 | 52.9% | 0.57 |
| SPY after a -1% day | full | 293 | +9.3 | +3.3 | 52.2% | 1.16 |
| SPY all sessions | last_24m | 501 | +2.3 | +2.6 | 51.3% | 0.58 |
| SPY gap >= +0.5% | last_24m | 78 | -10.8 | -9.7 | 44.9% | -1.07 |
| SPY gap <= -0.5% | last_24m | 63 | +20.1 | +0.5 | 50.8% | 0.91 |
| SPY after 3 up days | last_24m | 84 | +2.0 | -0.4 | 50.0% | 0.34 |
| SPY after a -1% day | last_24m | 53 | +48.0 | +36.2 | 62.3% | 1.92 |
| SPY all sessions | last_12m | 251 | +1.0 | +0.1 | 50.2% | 0.25 |
| SPY gap >= +0.5% | last_12m | 44 | -6.0 | -9.7 | 43.2% | -0.52 |
| SPY gap <= -0.5% | last_12m | 29 | +4.4 | -3.0 | 44.8% | 0.32 |
| SPY after 3 up days | last_12m | 38 | -1.4 | +1.7 | 52.6% | -0.16 |
| SPY after a -1% day | last_12m | 25 | +15.8 | +5.7 | 56.0% | 0.97 |

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
| 2026 | 198 | 50.0% | +2.2 |

_Current index membership (survivorship bias favours longs slightly). Research output, not investment advice._
