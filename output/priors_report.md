# Playbook priors, backtested on the full panel

902 tickers, 2016-01-04 to 2026-10-28, 2,334,944 stock-days (2,286,046 pass the ledger's price and liquidity filter). Every row measures the **open-to-close return of the session after the condition is known**, before costs; the ledger pays about 4 bps per round trip. Continuation = share of sessions where the open-to-close move had the same sign as the gap or the prior move.

## Verdicts on the playbook's priors

| Prior | Verdict |
|---|---|
| long a stock that gapped up 2-5% (continuation) | no reliable edge (mean +0.9 bps, t = 0.74, n = 62,268) |
| long a stock that gapped up 5%+ (continuation) | supported: +24.5 bps/session for that side, clears 4 bps costs (t = 5.49, n = 12,551) |
| short a stock that gapped down 2-5% (continuation) | goes the other way: -21.0 bps/session for that side (t = -15.48, n = 59,011) |
| short a stock that gapped down 5%+ (continuation) | supported: +43.7 bps/session for that side, clears 4 bps costs (t = 8.26, n = 11,853) |
| fade a +5% gap (short) | goes the other way: -24.5 bps/session for that side (t = -5.49, n = 12,551) |
| fade a -5% gap (long) | goes the other way: -43.7 bps/session for that side (t = -8.26, n = 11,853) |
| day-two fade after a +10% day (short) | no reliable edge (mean -10.4 bps, t = -1.85, n = 7,545) |
| day-two bounce after a -10% day (long) | supported: +80.1 bps/session for that side, clears 4 bps costs (t = 10.15, n = 6,000) |
| oversold bounce after a -15% three-day drop (long) | supported: +35.7 bps/session for that side, clears 4 bps costs (t = 5.16, n = 8,223) |
| 20-day momentum top decile (long) | positive but inside costs (+2.1 bps vs 4 bps, t = 4.33, n = 229,457) |
| 20-day momentum bottom decile (short) | goes the other way: -3.2 bps/session for that side (t = -6.32, n = 229,685) |

## 1. Overnight gap -> open-to-close

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | Continuation | t |
|---|---|---|---|---|---|---|---|
| gap <= -5% | full | 11,853 | -43.7 | -38.5 | 46.4% | 53.3% | -8.26 |
| -5% < gap <= -2% | full | 59,011 | +21.0 | +18.8 | 52.5% | 47.1% | 15.48 |
| -2% < gap <= -1% | full | 146,920 | +9.9 | +13.2 | 52.8% | 46.8% | 16.37 |
| -1% < gap <= -0.3% | full | 421,153 | +2.9 | +7.9 | 52.1% | 47.3% | 10.95 |
| flat (|gap| < 0.3%) | full | 868,566 | +0.0 | +2.2 | 50.5% | 48.5% | 0.22 |
| +0.3% <= gap < +1% | full | 533,725 | +0.5 | +0.0 | 49.6% | 49.6% | 2.37 |
| +1% <= gap < +2% | full | 169,999 | +6.5 | +4.1 | 50.7% | 50.7% | 11.97 |
| +2% <= gap < +5% | full | 62,268 | +0.9 | -6.8 | 48.8% | 48.8% | 0.74 |
| gap >= +5% | full | 12,551 | +24.5 | +0.0 | 49.9% | 49.9% | 5.49 |
| gap <= -5% | last_24m | 2,674 | -17.5 | -21.3 | 48.5% | 51.4% | -1.66 |
| -5% < gap <= -2% | last_24m | 14,031 | +28.8 | +37.1 | 55.1% | 44.6% | 10.03 |
| -2% < gap <= -1% | last_24m | 33,735 | +24.2 | +22.2 | 54.8% | 44.9% | 17.98 |
| -1% < gap <= -0.3% | last_24m | 87,826 | +6.8 | +7.9 | 52.2% | 47.4% | 10.94 |
| flat (|gap| < 0.3%) | last_24m | 155,676 | -0.5 | +0.0 | 49.8% | 48.3% | -1.16 |
| +0.3% <= gap < +1% | last_24m | 100,372 | -2.7 | -5.0 | 48.3% | 48.3% | -4.86 |
| +1% <= gap < +2% | last_24m | 37,630 | -1.6 | -6.7 | 48.4% | 48.4% | -1.41 |
| +2% <= gap < +5% | last_24m | 15,365 | -32.1 | -34.2 | 44.6% | 44.6% | -12.6 |
| gap >= +5% | last_24m | 3,109 | -34.2 | -42.5 | 45.0% | 45.0% | -4.01 |
| gap <= -5% | last_12m | 1,258 | +42.6 | +20.0 | 52.5% | 47.3% | 2.93 |
| -5% < gap <= -2% | last_12m | 7,270 | +28.9 | +34.0 | 54.9% | 44.8% | 7.65 |
| -2% < gap <= -1% | last_12m | 18,545 | +8.5 | +14.3 | 53.0% | 46.6% | 4.99 |
| -1% < gap <= -0.3% | last_12m | 45,207 | +2.6 | +5.1 | 51.3% | 48.3% | 2.92 |
| flat (|gap| < 0.3%) | last_12m | 73,005 | -0.0 | +0.0 | 49.6% | 48.2% | -0.04 |
| +0.3% <= gap < +1% | last_12m | 49,043 | -0.7 | -5.5 | 48.2% | 48.2% | -0.89 |
| +1% <= gap < +2% | last_12m | 21,664 | -3.5 | -13.7 | 47.0% | 47.0% | -2.23 |
| +2% <= gap < +5% | last_12m | 8,490 | -13.7 | -22.1 | 46.5% | 46.5% | -4.06 |
| gap >= +5% | last_12m | 1,548 | -21.7 | -32.5 | 45.9% | 45.9% | -1.75 |

## 2. Day two after a big close-to-close move

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | Continuation | t |
|---|---|---|---|---|---|---|---|
| yesterday +10% or more | full | 7,545 | -10.4 | -14.9 | 48.1% | 48.1% | -1.85 |
| yesterday +5% to +10% | full | 37,592 | +0.7 | -0.7 | 49.6% | 49.6% | 0.4 |
| yesterday -5% to -10% | full | 35,625 | +22.4 | +17.9 | 52.4% | 47.2% | 11.74 |
| yesterday -10% or worse | full | 6,000 | +80.1 | +51.4 | 54.8% | 44.9% | 10.15 |
| yesterday +10% or more | last_24m | 1,812 | -55.8 | -67.3 | 42.0% | 42.0% | -5.85 |
| yesterday +5% to +10% | last_24m | 8,872 | +11.5 | +4.4 | 50.6% | 50.6% | 3.49 |
| yesterday -5% to -10% | last_24m | 8,232 | +42.9 | +29.7 | 54.7% | 45.1% | 10.68 |
| yesterday -10% or worse | last_24m | 1,419 | +13.3 | +8.4 | 50.8% | 49.0% | 1.09 |
| yesterday +10% or more | last_12m | 817 | +27.4 | +23.2 | 52.8% | 52.8% | 1.83 |
| yesterday +5% to +10% | last_12m | 5,158 | +26.2 | +25.6 | 53.8% | 53.8% | 5.89 |
| yesterday -5% to -10% | last_12m | 4,486 | +18.8 | +18.0 | 52.8% | 47.1% | 3.72 |
| yesterday -10% or worse | last_12m | 643 | -3.1 | -4.1 | 49.3% | 50.7% | -0.17 |

## 3. Three-day moves

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| 3-day return <= -15% | full | 8,223 | +35.7 | +11.9 | 50.9% | 5.16 |
| 3-day return -15% to -10% | full | 19,770 | +20.5 | +11.0 | 51.3% | 7.2 |
| 3-day return >= +15% | full | 11,226 | -0.8 | -5.5 | 49.1% | -0.19 |
| 3-day return <= -15% | last_24m | 1,986 | +9.7 | -12.4 | 48.4% | 0.82 |
| 3-day return -15% to -10% | last_24m | 4,762 | +27.8 | +3.9 | 50.4% | 4.48 |
| 3-day return >= +15% | last_24m | 2,657 | +6.9 | +0.0 | 50.0% | 0.9 |
| 3-day return <= -15% | last_12m | 836 | +32.7 | +0.6 | 50.0% | 2.24 |
| 3-day return -15% to -10% | last_12m | 2,448 | -0.2 | -10.8 | 48.6% | -0.03 |
| 3-day return >= +15% | last_12m | 1,464 | +19.3 | +12.2 | 51.9% | 1.78 |

## 4. 20-day momentum deciles

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| momentum top decile (20d) | full | 229,457 | +2.1 | +2.5 | 50.4% | 4.33 |
| momentum bottom decile (20d) | full | 229,685 | +3.2 | +1.9 | 50.2% | 6.32 |
| momentum top decile (20d) | last_24m | 45,162 | +2.6 | +1.6 | 50.2% | 2.11 |
| momentum bottom decile (20d) | last_24m | 45,177 | +2.2 | +0.0 | 49.8% | 1.86 |
| momentum top decile (20d) | last_12m | 22,662 | +5.3 | +0.0 | 49.9% | 2.92 |
| momentum bottom decile (20d) | last_12m | 22,677 | +0.3 | -0.9 | 49.6% | 0.16 |

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
| 2025 | 224,492 | 51.0% | +4.2 |
| 2026 | 186,461 | 49.6% | +0.9 |

## 6. SPY conditionals

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| SPY all sessions | full | 2,721 | +2.3 | +5.2 | 53.9% | 1.41 |
| SPY gap >= +0.5% | full | 428 | +8.8 | +21.9 | 59.8% | 1.76 |
| SPY gap <= -0.5% | full | 345 | +6.2 | +6.8 | 53.6% | 0.89 |
| SPY after 3 up days | full | 438 | +1.4 | +4.4 | 52.7% | 0.55 |
| SPY after a -1% day | full | 295 | +9.2 | +1.1 | 52.2% | 1.16 |
| SPY all sessions | last_24m | 501 | +2.5 | +3.2 | 51.9% | 0.62 |
| SPY gap >= +0.5% | last_24m | 77 | -9.9 | -7.2 | 45.5% | -0.97 |
| SPY gap <= -0.5% | last_24m | 65 | +19.0 | +0.5 | 50.8% | 0.89 |
| SPY after 3 up days | last_24m | 84 | +1.7 | -0.4 | 50.0% | 0.28 |
| SPY after a -1% day | last_24m | 55 | +46.1 | +32.9 | 61.8% | 1.91 |
| SPY all sessions | last_12m | 251 | +0.6 | +0.5 | 50.2% | 0.15 |
| SPY gap >= +0.5% | last_12m | 43 | -7.5 | -12.2 | 39.5% | -0.63 |
| SPY gap <= -0.5% | last_12m | 31 | +3.1 | -3.0 | 45.2% | 0.24 |
| SPY after 3 up days | last_12m | 38 | -2.2 | +1.2 | 50.0% | -0.26 |
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
| 2026 | 207 | 50.7% | +2.0 |

_Current index membership (survivorship bias favours longs slightly). Research output, not investment advice._
