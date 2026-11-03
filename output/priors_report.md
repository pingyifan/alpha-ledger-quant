# Playbook priors, backtested on the full panel

902 tickers, 2016-01-04 to 2026-11-02, 2,337,650 stock-days (2,288,753 pass the ledger's price and liquidity filter). Every row measures the **open-to-close return of the session after the condition is known**, before costs; the ledger pays about 4 bps per round trip. Continuation = share of sessions where the open-to-close move had the same sign as the gap or the prior move.

## Verdicts on the playbook's priors

| Prior | Verdict |
|---|---|
| long a stock that gapped up 2-5% (continuation) | no reliable edge (mean +0.9 bps, t = 0.71, n = 62,443) |
| long a stock that gapped up 5%+ (continuation) | supported: +25.0 bps/session for that side, clears 4 bps costs (t = 5.6, n = 12,573) |
| short a stock that gapped down 2-5% (continuation) | goes the other way: -20.8 bps/session for that side (t = -15.41, n = 59,164) |
| short a stock that gapped down 5%+ (continuation) | supported: +43.4 bps/session for that side, clears 4 bps costs (t = 8.26, n = 11,940) |
| fade a +5% gap (short) | goes the other way: -25.0 bps/session for that side (t = -5.6, n = 12,573) |
| fade a -5% gap (long) | goes the other way: -43.4 bps/session for that side (t = -8.26, n = 11,940) |
| day-two fade after a +10% day (short) | no reliable edge (mean -10.2 bps, t = -1.82, n = 7,565) |
| day-two bounce after a -10% day (long) | supported: +78.3 bps/session for that side, clears 4 bps costs (t = 9.96, n = 6,029) |
| oversold bounce after a -15% three-day drop (long) | supported: +35.0 bps/session for that side, clears 4 bps costs (t = 5.08, n = 8,247) |
| 20-day momentum top decile (long) | positive but inside costs (+2.1 bps vs 4 bps, t = 4.47, n = 229,730) |
| 20-day momentum bottom decile (short) | goes the other way: -3.1 bps/session for that side (t = -6.08, n = 229,959) |

## 1. Overnight gap -> open-to-close

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | Continuation | t |
|---|---|---|---|---|---|---|---|
| gap <= -5% | full | 11,940 | -43.4 | -38.5 | 46.3% | 53.4% | -8.26 |
| -5% < gap <= -2% | full | 59,164 | +20.8 | +18.6 | 52.5% | 47.1% | 15.41 |
| -2% < gap <= -1% | full | 147,083 | +9.9 | +13.2 | 52.8% | 46.8% | 16.34 |
| -1% < gap <= -0.3% | full | 421,375 | +3.0 | +7.9 | 52.1% | 47.3% | 11.03 |
| flat (|gap| < 0.3%) | full | 868,990 | +0.0 | +2.2 | 50.5% | 48.5% | 0.31 |
| +0.3% <= gap < +1% | full | 534,429 | +0.6 | +0.0 | 49.7% | 49.7% | 2.61 |
| +1% <= gap < +2% | full | 170,756 | +6.6 | +4.3 | 50.8% | 50.8% | 12.06 |
| +2% <= gap < +5% | full | 62,443 | +0.9 | -6.8 | 48.8% | 48.8% | 0.71 |
| gap >= +5% | full | 12,573 | +25.0 | +0.0 | 49.9% | 49.9% | 5.6 |
| gap <= -5% | last_24m | 2,708 | -15.6 | -21.1 | 48.4% | 51.5% | -1.5 |
| -5% < gap <= -2% | last_24m | 14,098 | +28.9 | +36.9 | 55.1% | 44.6% | 10.07 |
| -2% < gap <= -1% | last_24m | 33,675 | +24.3 | +22.3 | 54.8% | 44.9% | 18.04 |
| -1% < gap <= -0.3% | last_24m | 87,074 | +7.1 | +8.2 | 52.3% | 47.3% | 11.24 |
| flat (|gap| < 0.3%) | last_24m | 154,737 | -0.2 | +0.0 | 49.9% | 48.3% | -0.5 |
| +0.3% <= gap < +1% | last_24m | 100,437 | -2.2 | -4.5 | 48.5% | 48.5% | -3.94 |
| +1% <= gap < +2% | last_24m | 38,257 | -1.1 | -5.5 | 48.6% | 48.6% | -0.96 |
| +2% <= gap < +5% | last_24m | 15,478 | -31.9 | -33.7 | 44.6% | 44.6% | -12.6 |
| gap >= +5% | last_24m | 3,073 | -34.1 | -42.5 | 44.9% | 44.9% | -3.99 |
| gap <= -5% | last_12m | 1,286 | +37.4 | +13.1 | 51.6% | 48.2% | 2.62 |
| -5% < gap <= -2% | last_12m | 7,358 | +29.0 | +33.9 | 54.8% | 44.8% | 7.68 |
| -2% < gap <= -1% | last_12m | 18,455 | +9.2 | +15.0 | 53.1% | 46.5% | 5.36 |
| -1% < gap <= -0.3% | last_12m | 44,403 | +3.1 | +5.4 | 51.4% | 48.3% | 3.5 |
| flat (|gap| < 0.3%) | last_12m | 72,650 | +0.2 | +0.0 | 49.6% | 48.2% | 0.38 |
| +0.3% <= gap < +1% | last_12m | 49,467 | -0.1 | -5.0 | 48.4% | 48.4% | -0.1 |
| +1% <= gap < +2% | last_12m | 22,293 | -2.9 | -11.9 | 47.3% | 47.3% | -1.91 |
| +2% <= gap < +5% | last_12m | 8,599 | -13.5 | -21.1 | 46.6% | 46.6% | -4.05 |
| gap >= +5% | last_12m | 1,531 | -21.5 | -33.1 | 45.8% | 45.8% | -1.74 |

## 2. Day two after a big close-to-close move

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | Continuation | t |
|---|---|---|---|---|---|---|---|
| yesterday +10% or more | full | 7,565 | -10.2 | -14.8 | 48.0% | 48.0% | -1.82 |
| yesterday +5% to +10% | full | 37,664 | +0.8 | -0.7 | 49.6% | 49.6% | 0.45 |
| yesterday -5% to -10% | full | 35,719 | +21.6 | +17.5 | 52.3% | 47.3% | 11.31 |
| yesterday -10% or worse | full | 6,029 | +78.3 | +49.6 | 54.6% | 45.1% | 9.96 |
| yesterday +10% or more | last_24m | 1,813 | -54.4 | -67.0 | 42.0% | 42.0% | -5.71 |
| yesterday +5% to +10% | last_24m | 8,898 | +12.2 | +4.8 | 50.7% | 50.7% | 3.69 |
| yesterday -5% to -10% | last_24m | 8,277 | +39.9 | +28.1 | 54.4% | 45.4% | 9.86 |
| yesterday -10% or worse | last_24m | 1,424 | +9.6 | +6.7 | 50.6% | 49.2% | 0.78 |
| yesterday +10% or more | last_12m | 819 | +29.4 | +23.2 | 52.8% | 52.8% | 1.98 |
| yesterday +5% to +10% | last_12m | 5,196 | +26.7 | +25.6 | 53.7% | 53.7% | 6.04 |
| yesterday -5% to -10% | last_12m | 4,504 | +13.7 | +14.8 | 52.2% | 47.6% | 2.67 |
| yesterday -10% or worse | last_12m | 645 | -11.3 | -10.6 | 48.7% | 51.3% | -0.59 |

## 3. Three-day moves

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| 3-day return <= -15% | full | 8,247 | +35.0 | +11.5 | 50.9% | 5.08 |
| 3-day return -15% to -10% | full | 19,798 | +20.4 | +10.9 | 51.3% | 7.16 |
| 3-day return >= +15% | full | 11,262 | -0.5 | -5.0 | 49.2% | -0.12 |
| 3-day return <= -15% | last_24m | 1,992 | +8.0 | -12.4 | 48.4% | 0.68 |
| 3-day return -15% to -10% | last_24m | 4,763 | +27.1 | +3.1 | 50.3% | 4.37 |
| 3-day return >= +15% | last_24m | 2,673 | +8.5 | +1.7 | 50.2% | 1.11 |
| 3-day return <= -15% | last_12m | 842 | +27.1 | -4.2 | 49.5% | 1.85 |
| 3-day return -15% to -10% | last_12m | 2,420 | -0.6 | -11.1 | 48.5% | -0.08 |
| 3-day return >= +15% | last_12m | 1,482 | +21.4 | +13.1 | 52.2% | 2.0 |

## 4. 20-day momentum deciles

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| momentum top decile (20d) | full | 229,730 | +2.1 | +2.6 | 50.4% | 4.47 |
| momentum bottom decile (20d) | full | 229,959 | +3.1 | +1.9 | 50.2% | 6.08 |
| momentum top decile (20d) | last_24m | 45,075 | +3.2 | +2.4 | 50.4% | 2.62 |
| momentum bottom decile (20d) | last_24m | 45,090 | +1.8 | +0.0 | 49.8% | 1.52 |
| momentum top decile (20d) | last_12m | 22,665 | +6.2 | +1.1 | 50.1% | 3.4 |
| momentum bottom decile (20d) | last_12m | 22,680 | -0.7 | -1.6 | 49.4% | -0.41 |

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
| 2025 | 224,492 | 51.0% | +4.2 |
| 2026 | 189,167 | 49.7% | +1.2 |

## 6. SPY conditionals

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| SPY all sessions | full | 2,724 | +2.2 | +5.2 | 53.9% | 1.37 |
| SPY gap >= +0.5% | full | 428 | +8.8 | +21.9 | 59.8% | 1.76 |
| SPY gap <= -0.5% | full | 346 | +5.9 | +6.7 | 53.5% | 0.86 |
| SPY after 3 up days | full | 439 | +1.4 | +4.5 | 52.8% | 0.55 |
| SPY after a -1% day | full | 296 | +8.8 | +1.0 | 52.0% | 1.12 |
| SPY all sessions | last_24m | 500 | +2.4 | +3.2 | 52.0% | 0.6 |
| SPY gap >= +0.5% | last_24m | 77 | -9.9 | -7.2 | 45.5% | -0.97 |
| SPY gap <= -0.5% | last_24m | 65 | +19.7 | +0.5 | 50.8% | 0.93 |
| SPY after 3 up days | last_24m | 85 | +1.7 | +0.1 | 50.6% | 0.3 |
| SPY after a -1% day | last_24m | 55 | +44.4 | +32.9 | 61.8% | 1.83 |
| SPY all sessions | last_12m | 251 | +0.4 | +0.9 | 50.6% | 0.11 |
| SPY gap >= +0.5% | last_12m | 42 | -6.6 | -11.0 | 40.5% | -0.55 |
| SPY gap <= -0.5% | last_12m | 31 | +2.6 | -3.0 | 45.2% | 0.2 |
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
| 2026 | 210 | 50.5% | +1.2 |

_Current index membership (survivorship bias favours longs slightly). Research output, not investment advice._
