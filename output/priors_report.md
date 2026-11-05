# Playbook priors, backtested on the full panel

902 tickers, 2016-01-04 to 2026-11-04, 2,341,301 stock-days (2,292,338 pass the ledger's price and liquidity filter). Every row measures the **open-to-close return of the session after the condition is known**, before costs; the ledger pays about 4 bps per round trip. Continuation = share of sessions where the open-to-close move had the same sign as the gap or the prior move.

## Verdicts on the playbook's priors

| Prior | Verdict |
|---|---|
| long a stock that gapped up 2-5% (continuation) | no reliable edge (mean +1.6 bps, t = 1.28, n = 62,895) |
| long a stock that gapped up 5%+ (continuation) | supported: +25.8 bps/session for that side, clears 4 bps costs (t = 5.79, n = 12,624) |
| short a stock that gapped down 2-5% (continuation) | goes the other way: -20.7 bps/session for that side (t = -15.3, n = 59,319) |
| short a stock that gapped down 5%+ (continuation) | supported: +43.8 bps/session for that side, clears 4 bps costs (t = 8.35, n = 11,994) |
| fade a +5% gap (short) | goes the other way: -25.8 bps/session for that side (t = -5.79, n = 12,624) |
| fade a -5% gap (long) | goes the other way: -43.8 bps/session for that side (t = -8.35, n = 11,994) |
| day-two fade after a +10% day (short) | no reliable edge (mean -10.3 bps, t = -1.85, n = 7,590) |
| day-two bounce after a -10% day (long) | supported: +77.7 bps/session for that side, clears 4 bps costs (t = 9.92, n = 6,057) |
| oversold bounce after a -15% three-day drop (long) | supported: +35.0 bps/session for that side, clears 4 bps costs (t = 5.11, n = 8,312) |
| 20-day momentum top decile (long) | positive but inside costs (+2.2 bps vs 4 bps, t = 4.53, n = 230,114) |
| 20-day momentum bottom decile (short) | goes the other way: -3.1 bps/session for that side (t = -6.02, n = 230,327) |

## 1. Overnight gap -> open-to-close

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | Continuation | t |
|---|---|---|---|---|---|---|---|
| gap <= -5% | full | 11,994 | -43.8 | -39.0 | 46.3% | 53.4% | -8.35 |
| -5% < gap <= -2% | full | 59,319 | +20.7 | +18.6 | 52.5% | 47.1% | 15.3 |
| -2% < gap <= -1% | full | 147,440 | +9.8 | +13.1 | 52.7% | 46.8% | 16.22 |
| -1% < gap <= -0.3% | full | 421,980 | +2.9 | +7.9 | 52.1% | 47.3% | 10.8 |
| flat (|gap| < 0.3%) | full | 869,798 | +0.1 | +2.2 | 50.5% | 48.5% | 0.36 |
| +0.3% <= gap < +1% | full | 535,021 | +0.6 | +0.0 | 49.7% | 49.7% | 2.67 |
| +1% <= gap < +2% | full | 171,267 | +6.7 | +4.4 | 50.8% | 50.8% | 12.35 |
| +2% <= gap < +5% | full | 62,895 | +1.6 | -5.9 | 48.9% | 48.9% | 1.28 |
| gap >= +5% | full | 12,624 | +25.8 | +1.2 | 50.1% | 50.1% | 5.79 |
| gap <= -5% | last_24m | 2,738 | -17.4 | -24.7 | 48.2% | 51.7% | -1.68 |
| -5% < gap <= -2% | last_24m | 14,186 | +27.8 | +35.9 | 55.0% | 44.7% | 9.69 |
| -2% < gap <= -1% | last_24m | 33,843 | +24.0 | +22.2 | 54.8% | 44.9% | 17.81 |
| -1% < gap <= -0.3% | last_24m | 87,179 | +6.8 | +7.9 | 52.2% | 47.4% | 10.78 |
| flat (|gap| < 0.3%) | last_24m | 154,497 | -0.3 | +0.0 | 49.8% | 48.3% | -0.81 |
| +0.3% <= gap < +1% | last_24m | 100,457 | -2.3 | -4.5 | 48.4% | 48.4% | -4.06 |
| +1% <= gap < +2% | last_24m | 38,571 | -0.4 | -4.8 | 48.8% | 48.8% | -0.38 |
| +2% <= gap < +5% | last_24m | 15,868 | -27.9 | -30.4 | 45.2% | 45.2% | -11.13 |
| gap >= +5% | last_24m | 3,106 | -30.0 | -38.0 | 45.5% | 45.5% | -3.52 |
| gap <= -5% | last_12m | 1,300 | +35.2 | +12.6 | 51.5% | 48.4% | 2.46 |
| -5% < gap <= -2% | last_12m | 7,308 | +28.1 | +34.3 | 54.9% | 44.8% | 7.32 |
| -2% < gap <= -1% | last_12m | 18,381 | +8.8 | +15.0 | 53.1% | 46.5% | 5.12 |
| -1% < gap <= -0.3% | last_12m | 44,124 | +2.6 | +4.9 | 51.2% | 48.4% | 2.89 |
| flat (|gap| < 0.3%) | last_12m | 72,417 | -0.1 | -0.4 | 49.5% | 48.2% | -0.08 |
| +0.3% <= gap < +1% | last_12m | 49,463 | -0.2 | -5.0 | 48.3% | 48.3% | -0.2 |
| +1% <= gap < +2% | last_12m | 22,551 | -1.8 | -10.7 | 47.6% | 47.6% | -1.16 |
| +2% <= gap < +5% | last_12m | 8,948 | -6.9 | -15.2 | 47.5% | 47.5% | -2.11 |
| gap >= +5% | last_12m | 1,559 | -15.8 | -25.0 | 46.6% | 46.6% | -1.29 |

## 2. Day two after a big close-to-close move

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | Continuation | t |
|---|---|---|---|---|---|---|---|
| yesterday +10% or more | full | 7,590 | -10.3 | -14.8 | 48.0% | 48.0% | -1.85 |
| yesterday +5% to +10% | full | 37,836 | +0.5 | -1.1 | 49.5% | 49.5% | 0.31 |
| yesterday -5% to -10% | full | 35,840 | +21.8 | +17.7 | 52.4% | 47.3% | 11.43 |
| yesterday -10% or worse | full | 6,057 | +77.7 | +49.2 | 54.6% | 45.1% | 9.92 |
| yesterday +10% or more | last_24m | 1,821 | -54.8 | -67.6 | 42.0% | 42.0% | -5.77 |
| yesterday +5% to +10% | last_24m | 8,984 | +10.8 | +4.0 | 50.5% | 50.5% | 3.28 |
| yesterday -5% to -10% | last_24m | 8,330 | +40.5 | +29.1 | 54.5% | 45.3% | 10.07 |
| yesterday -10% or worse | last_24m | 1,433 | +9.2 | +7.3 | 50.7% | 49.1% | 0.76 |
| yesterday +10% or more | last_12m | 824 | +28.4 | +23.3 | 52.8% | 52.8% | 1.91 |
| yesterday +5% to +10% | last_12m | 5,258 | +24.6 | +24.3 | 53.5% | 53.5% | 5.55 |
| yesterday -5% to -10% | last_12m | 4,542 | +15.1 | +16.4 | 52.4% | 47.4% | 2.95 |
| yesterday -10% or worse | last_12m | 651 | -9.9 | -7.0 | 49.0% | 51.0% | -0.53 |

## 3. Three-day moves

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| 3-day return <= -15% | full | 8,312 | +35.0 | +12.0 | 50.9% | 5.11 |
| 3-day return -15% to -10% | full | 19,910 | +20.3 | +10.9 | 51.3% | 7.16 |
| 3-day return >= +15% | full | 11,315 | -0.4 | -5.0 | 49.2% | -0.09 |
| 3-day return <= -15% | last_24m | 2,022 | +8.8 | -11.5 | 48.6% | 0.76 |
| 3-day return -15% to -10% | last_24m | 4,815 | +27.2 | +3.3 | 50.4% | 4.41 |
| 3-day return >= +15% | last_24m | 2,696 | +7.9 | +1.0 | 50.1% | 1.04 |
| 3-day return <= -15% | last_12m | 860 | +28.7 | +3.9 | 50.3% | 1.99 |
| 3-day return -15% to -10% | last_12m | 2,447 | +0.4 | -10.3 | 48.7% | 0.05 |
| 3-day return >= +15% | last_12m | 1,489 | +20.2 | +12.7 | 52.1% | 1.9 |

## 4. 20-day momentum deciles

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| momentum top decile (20d) | full | 230,114 | +2.2 | +2.6 | 50.4% | 4.53 |
| momentum bottom decile (20d) | full | 230,327 | +3.1 | +1.9 | 50.2% | 6.02 |
| momentum top decile (20d) | last_24m | 45,168 | +3.3 | +2.5 | 50.4% | 2.73 |
| momentum bottom decile (20d) | last_24m | 45,182 | +1.5 | +0.0 | 49.8% | 1.24 |
| momentum top decile (20d) | last_12m | 22,668 | +6.6 | +1.6 | 50.2% | 3.64 |
| momentum bottom decile (20d) | last_12m | 22,682 | -1.1 | -1.3 | 49.5% | -0.65 |

## 5. Base rate: share of tradable stock-days that closed above the open

| Year | n | Share up | Mean OC (bps) |
|---|---|---|---|
| 2016 | 177,217 | 52.8% | +10.4 |
| 2017 | 198,099 | 51.4% | +2.6 |
| 2018 | 202,095 | 49.4% | -6.4 |
| 2019 | 206,250 | 52.7% | +6.7 |
| 2020 | 211,290 | 49.7% | +0.6 |
| 2021 | 217,444 | 50.2% | +0.7 |
| 2022 | 219,171 | 50.0% | +1.2 |
| 2023 | 220,251 | 51.5% | +6.0 |
| 2024 | 225,057 | 50.3% | -0.9 |
| 2025 | 224,492 | 51.0% | +4.2 |
| 2026 | 190,972 | 49.7% | +1.3 |

## 6. SPY conditionals

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| SPY all sessions | full | 2,726 | +2.2 | +5.3 | 53.9% | 1.39 |
| SPY gap >= +0.5% | full | 429 | +8.9 | +22.3 | 59.9% | 1.78 |
| SPY gap <= -0.5% | full | 346 | +5.9 | +6.7 | 53.5% | 0.86 |
| SPY after 3 up days | full | 439 | +1.4 | +4.5 | 52.8% | 0.55 |
| SPY after a -1% day | full | 296 | +8.8 | +1.0 | 52.0% | 1.12 |
| SPY all sessions | last_24m | 501 | +2.6 | +4.5 | 52.3% | 0.65 |
| SPY gap >= +0.5% | last_24m | 78 | -9.1 | -6.4 | 46.2% | -0.9 |
| SPY gap <= -0.5% | last_24m | 65 | +19.7 | +0.5 | 50.8% | 0.93 |
| SPY after 3 up days | last_24m | 85 | +1.7 | +0.1 | 50.6% | 0.3 |
| SPY after a -1% day | last_24m | 55 | +44.4 | +32.9 | 61.8% | 1.83 |
| SPY all sessions | last_12m | 251 | +0.9 | +2.6 | 51.4% | 0.23 |
| SPY gap >= +0.5% | last_12m | 42 | -4.6 | -8.5 | 42.9% | -0.38 |
| SPY gap <= -0.5% | last_12m | 30 | +3.1 | -2.8 | 46.7% | 0.23 |
| SPY after 3 up days | last_12m | 37 | +0.0 | +7.4 | 54.0% | 0.01 |
| SPY after a -1% day | last_12m | 27 | +12.3 | +0.9 | 55.6% | 0.79 |

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
| 2026 | 212 | 50.9% | +1.5 |

_Current index membership (survivorship bias favours longs slightly). Research output, not investment advice._
