# Playbook priors, backtested on the full panel

900 tickers, 2016-01-04 to 2026-11-19, 2,343,630 stock-days (2,292,386 pass the ledger's price and liquidity filter). Every row measures the **open-to-close return of the session after the condition is known**, before costs; the ledger pays about 4 bps per round trip. Continuation = share of sessions where the open-to-close move had the same sign as the gap or the prior move.

## Verdicts on the playbook's priors

| Prior | Verdict |
|---|---|
| long a stock that gapped up 2-5% (continuation) | no reliable edge (mean +1.5 bps, t = 1.21, n = 63,024) |
| long a stock that gapped up 5%+ (continuation) | supported: +23.6 bps/session for that side, clears 4 bps costs (t = 5.34, n = 12,719) |
| short a stock that gapped down 2-5% (continuation) | goes the other way: -20.0 bps/session for that side (t = -14.85, n = 59,588) |
| short a stock that gapped down 5%+ (continuation) | supported: +45.2 bps/session for that side, clears 4 bps costs (t = 8.64, n = 12,052) |
| fade a +5% gap (short) | goes the other way: -23.6 bps/session for that side (t = -5.34, n = 12,719) |
| fade a -5% gap (long) | goes the other way: -45.2 bps/session for that side (t = -8.64, n = 12,052) |
| day-two fade after a +10% day (short) | no reliable edge (mean -9.6 bps, t = -1.72, n = 7,604) |
| day-two bounce after a -10% day (long) | supported: +70.8 bps/session for that side, clears 4 bps costs (t = 9.1, n = 6,120) |
| oversold bounce after a -15% three-day drop (long) | supported: +34.3 bps/session for that side, clears 4 bps costs (t = 5.06, n = 8,394) |
| 20-day momentum top decile (long) | positive but inside costs (+2.0 bps vs 4 bps, t = 4.25, n = 230,087) |
| 20-day momentum bottom decile (short) | goes the other way: -2.7 bps/session for that side (t = -5.19, n = 230,316) |

## 1. Overnight gap -> open-to-close

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | Continuation | t |
|---|---|---|---|---|---|---|---|
| gap <= -5% | full | 12,052 | -45.2 | -39.2 | 46.3% | 53.4% | -8.64 |
| -5% < gap <= -2% | full | 59,588 | +20.0 | +18.4 | 52.5% | 47.1% | 14.85 |
| -2% < gap <= -1% | full | 148,057 | +9.7 | +13.0 | 52.7% | 46.8% | 16.01 |
| -1% < gap <= -0.3% | full | 422,305 | +2.8 | +7.8 | 52.1% | 47.3% | 10.35 |
| flat (|gap| < 0.3%) | full | 867,930 | -0.1 | +2.1 | 50.5% | 48.5% | -0.44 |
| +0.3% <= gap < +1% | full | 534,899 | +0.4 | +0.0 | 49.6% | 49.6% | 1.63 |
| +1% <= gap < +2% | full | 171,812 | +6.1 | +3.9 | 50.7% | 50.7% | 11.26 |
| +2% <= gap < +5% | full | 63,024 | +1.5 | -5.7 | 48.9% | 48.9% | 1.21 |
| gap >= +5% | full | 12,719 | +23.6 | +0.0 | 49.9% | 49.9% | 5.34 |
| gap <= -5% | last_24m | 2,787 | -27.1 | -34.8 | 47.4% | 52.5% | -2.62 |
| -5% < gap <= -2% | last_24m | 14,600 | +25.3 | +34.8 | 54.9% | 44.8% | 8.94 |
| -2% < gap <= -1% | last_24m | 34,278 | +22.6 | +21.2 | 54.6% | 45.0% | 16.92 |
| -1% < gap <= -0.3% | last_24m | 86,985 | +6.1 | +7.5 | 52.0% | 47.5% | 9.67 |
| flat (|gap| < 0.3%) | last_24m | 152,211 | -1.1 | +0.0 | 49.6% | 48.3% | -2.53 |
| +0.3% <= gap < +1% | last_24m | 100,180 | -3.4 | -5.4 | 48.2% | 48.2% | -5.97 |
| +1% <= gap < +2% | last_24m | 39,168 | -2.8 | -7.1 | 48.3% | 48.3% | -2.47 |
| +2% <= gap < +5% | last_24m | 15,804 | -29.9 | -32.3 | 44.9% | 44.9% | -11.82 |
| gap >= +5% | last_24m | 3,022 | -48.5 | -54.4 | 43.5% | 43.5% | -5.65 |
| gap <= -5% | last_12m | 1,366 | +10.3 | +6.5 | 50.6% | 49.2% | 0.73 |
| -5% < gap <= -2% | last_12m | 7,595 | +17.9 | +27.3 | 53.8% | 45.8% | 4.78 |
| -2% < gap <= -1% | last_12m | 18,816 | +7.6 | +13.9 | 53.0% | 46.6% | 4.48 |
| -1% < gap <= -0.3% | last_12m | 43,843 | +2.8 | +5.1 | 51.2% | 48.4% | 3.12 |
| flat (|gap| < 0.3%) | last_12m | 69,990 | -1.1 | -1.7 | 49.2% | 48.2% | -1.69 |
| +0.3% <= gap < +1% | last_12m | 49,496 | -3.5 | -8.2 | 47.5% | 47.5% | -4.19 |
| +1% <= gap < +2% | last_12m | 23,405 | -5.3 | -13.4 | 47.0% | 47.0% | -3.46 |
| +2% <= gap < +5% | last_12m | 9,232 | -6.6 | -14.1 | 47.8% | 47.8% | -2.02 |
| gap >= +5% | last_12m | 1,664 | -27.1 | -35.5 | 45.5% | 45.5% | -2.33 |

## 2. Day two after a big close-to-close move

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | Continuation | t |
|---|---|---|---|---|---|---|---|
| yesterday +10% or more | full | 7,604 | -9.6 | -14.3 | 48.1% | 48.1% | -1.72 |
| yesterday +5% to +10% | full | 38,051 | +0.4 | -1.4 | 49.5% | 49.5% | 0.22 |
| yesterday -5% to -10% | full | 36,034 | +19.6 | +16.0 | 52.1% | 47.5% | 10.31 |
| yesterday -10% or worse | full | 6,120 | +70.8 | +43.1 | 54.0% | 45.7% | 9.1 |
| yesterday +10% or more | last_24m | 1,775 | -47.3 | -53.4 | 43.5% | 43.5% | -4.82 |
| yesterday +5% to +10% | last_24m | 9,108 | +9.4 | +3.9 | 50.5% | 50.5% | 2.82 |
| yesterday -5% to -10% | last_24m | 8,582 | +31.5 | +23.2 | 53.6% | 46.2% | 7.84 |
| yesterday -10% or worse | last_24m | 1,507 | -8.8 | -4.1 | 49.2% | 50.6% | -0.74 |
| yesterday +10% or more | last_12m | 867 | +27.3 | +20.3 | 52.1% | 52.1% | 1.86 |
| yesterday +5% to +10% | last_12m | 5,557 | +22.8 | +22.6 | 53.0% | 53.0% | 5.19 |
| yesterday -5% to -10% | last_12m | 4,744 | -7.1 | -1.1 | 49.7% | 50.1% | -1.4 |
| yesterday -10% or worse | last_12m | 732 | -55.1 | -45.7 | 45.6% | 54.4% | -3.15 |

## 3. Three-day moves

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| 3-day return <= -15% | full | 8,394 | +34.3 | +12.0 | 50.9% | 5.06 |
| 3-day return -15% to -10% | full | 20,074 | +18.6 | +9.5 | 51.1% | 6.59 |
| 3-day return >= +15% | full | 11,319 | +0.6 | -4.1 | 49.3% | 0.15 |
| 3-day return <= -15% | last_24m | 2,111 | +12.6 | -6.7 | 49.3% | 1.1 |
| 3-day return -15% to -10% | last_24m | 5,005 | +21.4 | +0.0 | 49.8% | 3.53 |
| 3-day return >= +15% | last_24m | 2,646 | +9.7 | +4.7 | 50.6% | 1.26 |
| 3-day return <= -15% | last_12m | 949 | +27.0 | +12.8 | 51.1% | 1.91 |
| 3-day return -15% to -10% | last_12m | 2,619 | -12.8 | -16.1 | 47.2% | -1.81 |
| 3-day return >= +15% | last_12m | 1,537 | +22.5 | +17.9 | 52.6% | 2.15 |

## 4. 20-day momentum deciles

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| momentum top decile (20d) | full | 230,087 | +2.0 | +2.5 | 50.4% | 4.25 |
| momentum bottom decile (20d) | full | 230,316 | +2.7 | +1.7 | 50.2% | 5.19 |
| momentum top decile (20d) | last_24m | 45,072 | +2.0 | +1.8 | 50.2% | 1.67 |
| momentum bottom decile (20d) | last_24m | 45,072 | -0.2 | -0.4 | 49.6% | -0.19 |
| momentum top decile (20d) | last_12m | 22,572 | +4.7 | +0.0 | 49.9% | 2.58 |
| momentum bottom decile (20d) | last_12m | 22,572 | -3.6 | -1.9 | 49.4% | -2.0 |

## 5. Base rate: share of tradable stock-days that closed above the open

| Year | n | Share up | Mean OC (bps) |
|---|---|---|---|
| 2016 | 176,521 | 52.8% | +10.4 |
| 2017 | 197,301 | 51.4% | +2.6 |
| 2018 | 201,091 | 49.4% | -6.4 |
| 2019 | 205,242 | 52.6% | +6.7 |
| 2020 | 210,279 | 49.6% | +0.6 |
| 2021 | 216,436 | 50.2% | +0.7 |
| 2022 | 218,167 | 50.0% | +1.2 |
| 2023 | 219,251 | 51.5% | +6.0 |
| 2024 | 224,065 | 50.3% | -0.9 |
| 2025 | 223,768 | 51.0% | +4.2 |
| 2026 | 200,265 | 49.3% | -1.0 |

## 6. SPY conditionals

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| SPY all sessions | full | 2,737 | +1.9 | +5.2 | 53.9% | 1.2 |
| SPY gap >= +0.5% | full | 432 | +8.6 | +22.3 | 60.0% | 1.71 |
| SPY gap <= -0.5% | full | 349 | +5.7 | +6.8 | 53.6% | 0.83 |
| SPY after 3 up days | full | 439 | +1.4 | +4.5 | 52.8% | 0.55 |
| SPY after a -1% day | full | 299 | +8.3 | +1.0 | 51.8% | 1.07 |
| SPY all sessions | last_24m | 501 | +0.7 | +3.2 | 52.1% | 0.17 |
| SPY gap >= +0.5% | last_24m | 80 | -10.6 | -6.4 | 46.2% | -1.0 |
| SPY gap <= -0.5% | last_24m | 66 | +18.1 | +0.7 | 51.5% | 0.86 |
| SPY after 3 up days | last_24m | 82 | +2.0 | +1.7 | 51.2% | 0.33 |
| SPY after a -1% day | last_24m | 57 | +40.2 | +7.4 | 59.7% | 1.71 |
| SPY all sessions | last_12m | 251 | -2.2 | +0.9 | 51.0% | -0.49 |
| SPY gap >= +0.5% | last_12m | 44 | -8.3 | -8.5 | 43.2% | -0.6 |
| SPY gap <= -0.5% | last_12m | 31 | -1.1 | -2.6 | 48.4% | -0.08 |
| SPY after 3 up days | last_12m | 35 | +4.2 | +7.7 | 57.1% | 0.51 |
| SPY after a -1% day | last_12m | 27 | +1.2 | -9.8 | 48.1% | 0.08 |

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
| 2026 | 223 | 50.7% | -2.1 |

_Current index membership (survivorship bias favours longs slightly). Research output, not investment advice._
