# Playbook priors, backtested on the full panel

901 tickers, 2016-01-04 to 2026-11-03, 2,337,674 stock-days (2,288,797 pass the ledger's price and liquidity filter). Every row measures the **open-to-close return of the session after the condition is known**, before costs; the ledger pays about 4 bps per round trip. Continuation = share of sessions where the open-to-close move had the same sign as the gap or the prior move.

## Verdicts on the playbook's priors

| Prior | Verdict |
|---|---|
| long a stock that gapped up 2-5% (continuation) | no reliable edge (mean +1.0 bps, t = 0.76, n = 62,505) |
| long a stock that gapped up 5%+ (continuation) | supported: +25.2 bps/session for that side, clears 4 bps costs (t = 5.66, n = 12,577) |
| short a stock that gapped down 2-5% (continuation) | goes the other way: -20.9 bps/session for that side (t = -15.44, n = 59,183) |
| short a stock that gapped down 5%+ (continuation) | supported: +43.2 bps/session for that side, clears 4 bps costs (t = 8.22, n = 11,947) |
| fade a +5% gap (short) | goes the other way: -25.2 bps/session for that side (t = -5.66, n = 12,577) |
| fade a -5% gap (long) | goes the other way: -43.2 bps/session for that side (t = -8.22, n = 11,947) |
| day-two fade after a +10% day (short) | no reliable edge (mean -10.1 bps, t = -1.81, n = 7,565) |
| day-two bounce after a -10% day (long) | supported: +78.2 bps/session for that side, clears 4 bps costs (t = 9.96, n = 6,035) |
| oversold bounce after a -15% three-day drop (long) | supported: +35.5 bps/session for that side, clears 4 bps costs (t = 5.17, n = 8,276) |
| 20-day momentum top decile (long) | positive but inside costs (+2.1 bps vs 4 bps, t = 4.45, n = 229,717) |
| 20-day momentum bottom decile (short) | goes the other way: -3.2 bps/session for that side (t = -6.19, n = 230,027) |

## 1. Overnight gap -> open-to-close

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | Continuation | t |
|---|---|---|---|---|---|---|---|
| gap <= -5% | full | 11,947 | -43.2 | -38.5 | 46.4% | 53.4% | -8.22 |
| -5% < gap <= -2% | full | 59,183 | +20.9 | +18.6 | 52.5% | 47.1% | 15.44 |
| -2% < gap <= -1% | full | 147,168 | +9.9 | +13.2 | 52.7% | 46.8% | 16.31 |
| -1% < gap <= -0.3% | full | 421,433 | +2.9 | +7.9 | 52.1% | 47.3% | 10.94 |
| flat (|gap| < 0.3%) | full | 868,870 | +0.0 | +2.2 | 50.5% | 48.5% | 0.26 |
| +0.3% <= gap < +1% | full | 534,325 | +0.6 | +0.0 | 49.7% | 49.7% | 2.63 |
| +1% <= gap < +2% | full | 170,789 | +6.6 | +4.3 | 50.8% | 50.8% | 12.12 |
| +2% <= gap < +5% | full | 62,505 | +1.0 | -6.7 | 48.8% | 48.8% | 0.76 |
| gap >= +5% | full | 12,577 | +25.2 | +0.0 | 50.0% | 50.0% | 5.66 |
| gap <= -5% | last_24m | 2,718 | -14.5 | -19.9 | 48.5% | 51.4% | -1.4 |
| -5% < gap <= -2% | last_24m | 14,121 | +29.0 | +37.1 | 55.1% | 44.6% | 10.12 |
| -2% < gap <= -1% | last_24m | 33,775 | +24.2 | +22.2 | 54.8% | 44.9% | 17.97 |
| -1% < gap <= -0.3% | last_24m | 87,216 | +7.0 | +8.0 | 52.2% | 47.4% | 11.08 |
| flat (|gap| < 0.3%) | last_24m | 154,760 | -0.3 | +0.0 | 49.9% | 48.3% | -0.64 |
| +0.3% <= gap < +1% | last_24m | 100,418 | -2.2 | -4.5 | 48.5% | 48.5% | -3.97 |
| +1% <= gap < +2% | last_24m | 38,311 | -1.0 | -5.4 | 48.7% | 48.7% | -0.84 |
| +2% <= gap < +5% | last_24m | 15,541 | -31.5 | -33.4 | 44.7% | 44.7% | -12.44 |
| gap >= +5% | last_24m | 3,079 | -33.1 | -41.4 | 45.1% | 45.1% | -3.87 |
| gap <= -5% | last_12m | 1,294 | +39.8 | +14.9 | 51.9% | 47.9% | 2.8 |
| -5% < gap <= -2% | last_12m | 7,371 | +29.2 | +33.9 | 54.9% | 44.8% | 7.76 |
| -2% < gap <= -1% | last_12m | 18,499 | +9.0 | +14.9 | 53.1% | 46.5% | 5.27 |
| -1% < gap <= -0.3% | last_12m | 44,237 | +3.0 | +5.1 | 51.3% | 48.4% | 3.34 |
| flat (|gap| < 0.3%) | last_12m | 72,488 | +0.0 | +0.0 | 49.5% | 48.2% | 0.07 |
| +0.3% <= gap < +1% | last_12m | 49,414 | -0.2 | -5.0 | 48.3% | 48.3% | -0.21 |
| +1% <= gap < +2% | last_12m | 22,310 | -2.6 | -11.5 | 47.4% | 47.4% | -1.67 |
| +2% <= gap < +5% | last_12m | 8,647 | -12.6 | -20.1 | 46.7% | 46.7% | -3.81 |
| gap >= +5% | last_12m | 1,536 | -21.1 | -29.7 | 46.0% | 46.0% | -1.72 |

## 2. Day two after a big close-to-close move

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | Continuation | t |
|---|---|---|---|---|---|---|---|
| yesterday +10% or more | full | 7,565 | -10.1 | -14.5 | 48.1% | 48.1% | -1.81 |
| yesterday +5% to +10% | full | 37,711 | +0.7 | -1.1 | 49.6% | 49.6% | 0.4 |
| yesterday -5% to -10% | full | 35,748 | +21.6 | +17.6 | 52.3% | 47.3% | 11.35 |
| yesterday -10% or worse | full | 6,035 | +78.2 | +49.4 | 54.6% | 45.1% | 9.96 |
| yesterday +10% or more | last_24m | 1,815 | -54.3 | -66.7 | 42.1% | 42.1% | -5.7 |
| yesterday +5% to +10% | last_24m | 8,949 | +11.8 | +4.2 | 50.6% | 50.6% | 3.61 |
| yesterday -5% to -10% | last_24m | 8,308 | +40.1 | +28.6 | 54.4% | 45.4% | 9.95 |
| yesterday -10% or worse | last_24m | 1,430 | +9.6 | +6.7 | 50.6% | 49.2% | 0.78 |
| yesterday +10% or more | last_12m | 816 | +30.5 | +25.3 | 53.1% | 53.1% | 2.05 |
| yesterday +5% to +10% | last_12m | 5,227 | +26.1 | +24.7 | 53.6% | 53.6% | 5.93 |
| yesterday -5% to -10% | last_12m | 4,529 | +14.2 | +15.3 | 52.3% | 47.5% | 2.79 |
| yesterday -10% or worse | last_12m | 650 | -10.4 | -10.1 | 48.8% | 51.2% | -0.55 |

## 3. Three-day moves

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| 3-day return <= -15% | full | 8,276 | +35.5 | +12.4 | 51.0% | 5.17 |
| 3-day return -15% to -10% | full | 19,833 | +20.6 | +10.9 | 51.3% | 7.24 |
| 3-day return >= +15% | full | 11,274 | -0.5 | -5.0 | 49.2% | -0.13 |
| 3-day return <= -15% | last_24m | 2,020 | +10.4 | -8.9 | 48.8% | 0.89 |
| 3-day return -15% to -10% | last_24m | 4,797 | +27.8 | +3.8 | 50.4% | 4.5 |
| 3-day return >= +15% | last_24m | 2,687 | +8.5 | +1.6 | 50.2% | 1.11 |
| 3-day return <= -15% | last_12m | 859 | +30.0 | +4.8 | 50.4% | 2.08 |
| 3-day return -15% to -10% | last_12m | 2,436 | +1.7 | -9.7 | 48.8% | 0.24 |
| 3-day return >= +15% | last_12m | 1,482 | +20.5 | +12.7 | 52.1% | 1.93 |

## 4. 20-day momentum deciles

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| momentum top decile (20d) | full | 229,717 | +2.1 | +2.6 | 50.4% | 4.45 |
| momentum bottom decile (20d) | full | 230,027 | +3.2 | +1.9 | 50.2% | 6.19 |
| momentum top decile (20d) | last_24m | 45,090 | +3.1 | +2.4 | 50.4% | 2.56 |
| momentum bottom decile (20d) | last_24m | 45,167 | +2.1 | +0.0 | 49.9% | 1.75 |
| momentum top decile (20d) | last_12m | 22,590 | +6.2 | +1.1 | 50.1% | 3.38 |
| momentum bottom decile (20d) | last_12m | 22,667 | -0.1 | -1.0 | 49.6% | -0.08 |

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
| 2023 | 220,001 | 51.5% | +6.0 |
| 2024 | 224,805 | 50.3% | -0.9 |
| 2025 | 224,242 | 51.0% | +4.2 |
| 2026 | 189,859 | 49.6% | +1.2 |

## 6. SPY conditionals

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| SPY all sessions | full | 2,725 | +2.2 | +5.2 | 53.9% | 1.37 |
| SPY gap >= +0.5% | full | 428 | +8.8 | +21.9 | 59.8% | 1.76 |
| SPY gap <= -0.5% | full | 346 | +5.9 | +6.7 | 53.5% | 0.86 |
| SPY after 3 up days | full | 439 | +1.4 | +4.5 | 52.8% | 0.55 |
| SPY after a -1% day | full | 296 | +8.8 | +1.0 | 52.0% | 1.12 |
| SPY all sessions | last_24m | 501 | +2.4 | +3.2 | 52.1% | 0.61 |
| SPY gap >= +0.5% | last_24m | 77 | -9.9 | -7.2 | 45.5% | -0.97 |
| SPY gap <= -0.5% | last_24m | 65 | +19.7 | +0.5 | 50.8% | 0.93 |
| SPY after 3 up days | last_24m | 85 | +1.7 | +0.1 | 50.6% | 0.3 |
| SPY after a -1% day | last_24m | 55 | +44.4 | +32.9 | 61.8% | 1.83 |
| SPY all sessions | last_12m | 251 | +0.7 | +0.9 | 51.0% | 0.17 |
| SPY gap >= +0.5% | last_12m | 41 | -6.0 | -9.8 | 41.5% | -0.48 |
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
| 2026 | 211 | 50.7% | +1.3 |

_Current index membership (survivorship bias favours longs slightly). Research output, not investment advice._
