# Playbook priors, backtested on the full panel

902 tickers, 2016-01-04 to 2026-10-30, 2,336,748 stock-days (2,287,849 pass the ledger's price and liquidity filter). Every row measures the **open-to-close return of the session after the condition is known**, before costs; the ledger pays about 4 bps per round trip. Continuation = share of sessions where the open-to-close move had the same sign as the gap or the prior move.

## Verdicts on the playbook's priors

| Prior | Verdict |
|---|---|
| long a stock that gapped up 2-5% (continuation) | no reliable edge (mean +0.9 bps, t = 0.74, n = 62,385) |
| long a stock that gapped up 5%+ (continuation) | supported: +24.9 bps/session for that side, clears 4 bps costs (t = 5.57, n = 12,571) |
| short a stock that gapped down 2-5% (continuation) | goes the other way: -21.0 bps/session for that side (t = -15.53, n = 59,151) |
| short a stock that gapped down 5%+ (continuation) | supported: +43.4 bps/session for that side, clears 4 bps costs (t = 8.26, n = 11,935) |
| fade a +5% gap (short) | goes the other way: -24.9 bps/session for that side (t = -5.57, n = 12,571) |
| fade a -5% gap (long) | goes the other way: -43.4 bps/session for that side (t = -8.26, n = 11,935) |
| day-two fade after a +10% day (short) | no reliable edge (mean -10.3 bps, t = -1.83, n = 7,562) |
| day-two bounce after a -10% day (long) | supported: +79.9 bps/session for that side, clears 4 bps costs (t = 10.15, n = 6,013) |
| oversold bounce after a -15% three-day drop (long) | supported: +35.6 bps/session for that side, clears 4 bps costs (t = 5.16, n = 8,232) |
| 20-day momentum top decile (long) | positive but inside costs (+2.1 bps vs 4 bps, t = 4.37, n = 229,638) |
| 20-day momentum bottom decile (short) | goes the other way: -3.2 bps/session for that side (t = -6.34, n = 229,867) |

## 1. Overnight gap -> open-to-close

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | Continuation | t |
|---|---|---|---|---|---|---|---|
| gap <= -5% | full | 11,935 | -43.4 | -38.6 | 46.3% | 53.4% | -8.26 |
| -5% < gap <= -2% | full | 59,151 | +21.0 | +18.7 | 52.5% | 47.1% | 15.53 |
| -2% < gap <= -1% | full | 147,051 | +9.9 | +13.2 | 52.8% | 46.8% | 16.36 |
| -1% < gap <= -0.3% | full | 421,290 | +3.0 | +7.9 | 52.1% | 47.3% | 11.0 |
| flat (|gap| < 0.3%) | full | 868,811 | +0.0 | +2.2 | 50.5% | 48.5% | 0.22 |
| +0.3% <= gap < +1% | full | 534,174 | +0.6 | +0.0 | 49.6% | 49.6% | 2.46 |
| +1% <= gap < +2% | full | 170,481 | +6.6 | +4.2 | 50.8% | 50.8% | 12.06 |
| +2% <= gap < +5% | full | 62,385 | +0.9 | -6.8 | 48.8% | 48.8% | 0.74 |
| gap >= +5% | full | 12,571 | +24.9 | +0.0 | 49.9% | 49.9% | 5.57 |
| gap <= -5% | last_24m | 2,731 | -18.2 | -24.0 | 48.2% | 51.7% | -1.76 |
| -5% < gap <= -2% | last_24m | 14,123 | +28.9 | +36.5 | 55.1% | 44.6% | 10.1 |
| -2% < gap <= -1% | last_24m | 33,720 | +24.2 | +22.0 | 54.8% | 44.9% | 17.93 |
| -1% < gap <= -0.3% | last_24m | 87,360 | +6.7 | +7.8 | 52.2% | 47.4% | 10.73 |
| flat (|gap| < 0.3%) | last_24m | 155,192 | -0.5 | +0.0 | 49.8% | 48.3% | -1.26 |
| +0.3% <= gap < +1% | last_24m | 100,647 | -2.6 | -4.9 | 48.4% | 48.4% | -4.62 |
| +1% <= gap < +2% | last_24m | 38,095 | -1.4 | -6.2 | 48.5% | 48.5% | -1.21 |
| +2% <= gap < +5% | last_24m | 15,459 | -32.1 | -34.1 | 44.6% | 44.6% | -12.65 |
| gap >= +5% | last_24m | 3,102 | -34.3 | -42.4 | 45.0% | 45.0% | -4.04 |
| gap <= -5% | last_12m | 1,293 | +39.7 | +14.1 | 51.8% | 48.0% | 2.79 |
| -5% < gap <= -2% | last_12m | 7,350 | +30.1 | +34.2 | 54.9% | 44.8% | 7.99 |
| -2% < gap <= -1% | last_12m | 18,471 | +9.6 | +15.3 | 53.2% | 46.4% | 5.6 |
| -1% < gap <= -0.3% | last_12m | 44,710 | +3.6 | +6.1 | 51.5% | 48.1% | 4.02 |
| flat (|gap| < 0.3%) | last_12m | 72,701 | +0.2 | +0.0 | 49.6% | 48.2% | 0.29 |
| +0.3% <= gap < +1% | last_12m | 49,323 | -0.5 | -5.3 | 48.2% | 48.2% | -0.61 |
| +1% <= gap < +2% | last_12m | 22,086 | -3.1 | -12.5 | 47.2% | 47.2% | -2.0 |
| +2% <= gap < +5% | last_12m | 8,562 | -13.3 | -21.3 | 46.5% | 46.5% | -3.99 |
| gap >= +5% | last_12m | 1,542 | -21.3 | -32.5 | 45.9% | 45.9% | -1.73 |

## 2. Day two after a big close-to-close move

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | Continuation | t |
|---|---|---|---|---|---|---|---|
| yesterday +10% or more | full | 7,562 | -10.3 | -14.7 | 48.1% | 48.1% | -1.83 |
| yesterday +5% to +10% | full | 37,650 | +0.6 | -1.1 | 49.6% | 49.6% | 0.38 |
| yesterday -5% to -10% | full | 35,647 | +22.4 | +17.9 | 52.4% | 47.2% | 11.74 |
| yesterday -10% or worse | full | 6,013 | +79.9 | +50.4 | 54.7% | 45.0% | 10.15 |
| yesterday +10% or more | last_24m | 1,819 | -55.1 | -67.0 | 42.1% | 42.1% | -5.8 |
| yesterday +5% to +10% | last_24m | 8,915 | +11.3 | +4.1 | 50.5% | 50.5% | 3.45 |
| yesterday -5% to -10% | last_24m | 8,248 | +43.1 | +29.9 | 54.7% | 45.1% | 10.73 |
| yesterday -10% or worse | last_24m | 1,429 | +13.4 | +8.4 | 50.8% | 49.0% | 1.11 |
| yesterday +10% or more | last_12m | 821 | +27.6 | +21.2 | 52.5% | 52.5% | 1.86 |
| yesterday +5% to +10% | last_12m | 5,195 | +26.1 | +24.8 | 53.6% | 53.6% | 5.9 |
| yesterday -5% to -10% | last_12m | 4,462 | +19.9 | +19.5 | 52.9% | 46.9% | 3.92 |
| yesterday -10% or worse | last_12m | 643 | -0.2 | -3.1 | 49.6% | 50.4% | -0.01 |

## 3. Three-day moves

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| 3-day return <= -15% | full | 8,232 | +35.6 | +12.1 | 50.9% | 5.16 |
| 3-day return -15% to -10% | full | 19,783 | +20.7 | +11.0 | 51.3% | 7.26 |
| 3-day return >= +15% | full | 11,251 | -0.8 | -5.5 | 49.1% | -0.2 |
| 3-day return <= -15% | last_24m | 1,994 | +10.1 | -11.7 | 48.6% | 0.86 |
| 3-day return -15% to -10% | last_24m | 4,765 | +28.0 | +3.8 | 50.4% | 4.52 |
| 3-day return >= +15% | last_24m | 2,675 | +6.7 | +0.6 | 50.0% | 0.88 |
| 3-day return <= -15% | last_12m | 841 | +34.4 | +6.7 | 50.4% | 2.38 |
| 3-day return -15% to -10% | last_12m | 2,434 | +1.5 | -9.7 | 48.9% | 0.21 |
| 3-day return >= +15% | last_12m | 1,482 | +18.5 | +12.2 | 51.9% | 1.73 |

## 4. 20-day momentum deciles

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| momentum top decile (20d) | full | 229,638 | +2.1 | +2.5 | 50.4% | 4.37 |
| momentum bottom decile (20d) | full | 229,867 | +3.2 | +1.9 | 50.2% | 6.34 |
| momentum top decile (20d) | last_24m | 45,164 | +2.6 | +1.8 | 50.2% | 2.11 |
| momentum bottom decile (20d) | last_24m | 45,179 | +2.2 | +0.0 | 49.8% | 1.8 |
| momentum top decile (20d) | last_12m | 22,664 | +5.5 | +0.3 | 50.0% | 3.05 |
| momentum bottom decile (20d) | last_12m | 22,679 | +0.9 | +0.0 | 49.7% | 0.54 |

## 5. Base rate: share of tradable stock-days that closed above the open

| Year | n | Share up | Mean OC (bps) |
|---|---|---|---|
| 2016 | 177,050 | 52.8% | +10.4 |
| 2017 | 197,848 | 51.4% | +2.7 |
| 2018 | 201,844 | 49.3% | -6.5 |
| 2019 | 205,998 | 52.7% | +6.7 |
| 2020 | 211,037 | 49.6% | +0.6 |
| 2021 | 217,191 | 50.2% | +0.7 |
| 2022 | 218,920 | 50.0% | +1.2 |
| 2023 | 220,147 | 51.5% | +6.0 |
| 2024 | 225,057 | 50.3% | -0.9 |
| 2025 | 224,492 | 51.0% | +4.2 |
| 2026 | 188,265 | 49.6% | +1.1 |

## 6. SPY conditionals

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| SPY all sessions | full | 2,723 | +2.2 | +5.2 | 53.9% | 1.39 |
| SPY gap >= +0.5% | full | 428 | +8.8 | +21.9 | 59.8% | 1.76 |
| SPY gap <= -0.5% | full | 346 | +5.9 | +6.7 | 53.5% | 0.86 |
| SPY after 3 up days | full | 439 | +1.4 | +4.5 | 52.8% | 0.55 |
| SPY after a -1% day | full | 295 | +9.2 | +1.1 | 52.2% | 1.16 |
| SPY all sessions | last_24m | 501 | +2.3 | +3.2 | 51.9% | 0.58 |
| SPY gap >= +0.5% | last_24m | 77 | -9.9 | -7.2 | 45.5% | -0.97 |
| SPY gap <= -0.5% | last_24m | 66 | +17.6 | -1.0 | 50.0% | 0.84 |
| SPY after 3 up days | last_24m | 85 | +1.7 | +0.1 | 50.6% | 0.3 |
| SPY after a -1% day | last_24m | 55 | +46.1 | +32.9 | 61.8% | 1.91 |
| SPY all sessions | last_12m | 251 | +0.7 | +0.9 | 50.6% | 0.17 |
| SPY gap >= +0.5% | last_12m | 43 | -7.5 | -12.2 | 39.5% | -0.63 |
| SPY gap <= -0.5% | last_12m | 31 | +2.6 | -3.0 | 45.2% | 0.2 |
| SPY after 3 up days | last_12m | 37 | +0.0 | +7.4 | 54.0% | 0.01 |
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
| 2026 | 209 | 50.7% | +1.6 |

_Current index membership (survivorship bias favours longs slightly). Research output, not investment advice._
