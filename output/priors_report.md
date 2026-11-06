# Playbook priors, backtested on the full panel

901 tickers, 2016-01-04 to 2026-11-05, 2,339,476 stock-days (2,290,534 pass the ledger's price and liquidity filter). Every row measures the **open-to-close return of the session after the condition is known**, before costs; the ledger pays about 4 bps per round trip. Continuation = share of sessions where the open-to-close move had the same sign as the gap or the prior move.

## Verdicts on the playbook's priors

| Prior | Verdict |
|---|---|
| long a stock that gapped up 2-5% (continuation) | no reliable edge (mean +1.5 bps, t = 1.18, n = 62,915) |
| long a stock that gapped up 5%+ (continuation) | supported: +25.6 bps/session for that side, clears 4 bps costs (t = 5.74, n = 12,628) |
| short a stock that gapped down 2-5% (continuation) | goes the other way: -19.9 bps/session for that side (t = -14.68, n = 59,368) |
| short a stock that gapped down 5%+ (continuation) | supported: +46.3 bps/session for that side, clears 4 bps costs (t = 8.83, n = 12,029) |
| fade a +5% gap (short) | goes the other way: -25.6 bps/session for that side (t = -5.74, n = 12,628) |
| fade a -5% gap (long) | goes the other way: -46.3 bps/session for that side (t = -8.83, n = 12,029) |
| day-two fade after a +10% day (short) | supported: +11.2 bps/session for that side, clears 4 bps costs (t = 2.0, n = 7,608) |
| day-two bounce after a -10% day (long) | supported: +75.1 bps/session for that side, clears 4 bps costs (t = 9.59, n = 6,080) |
| oversold bounce after a -15% three-day drop (long) | supported: +33.7 bps/session for that side, clears 4 bps costs (t = 4.92, n = 8,326) |
| 20-day momentum top decile (long) | positive but inside costs (+2.0 bps vs 4 bps, t = 4.26, n = 229,892) |
| 20-day momentum bottom decile (short) | goes the other way: -2.8 bps/session for that side (t = -5.49, n = 230,206) |

## 1. Overnight gap -> open-to-close

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | Continuation | t |
|---|---|---|---|---|---|---|---|
| gap <= -5% | full | 12,029 | -46.3 | -40.4 | 46.2% | 53.5% | -8.83 |
| -5% < gap <= -2% | full | 59,368 | +19.9 | +18.1 | 52.4% | 47.2% | 14.68 |
| -2% < gap <= -1% | full | 147,427 | +9.7 | +13.1 | 52.7% | 46.8% | 15.98 |
| -1% < gap <= -0.3% | full | 421,543 | +2.9 | +7.8 | 52.1% | 47.3% | 10.63 |
| flat (|gap| < 0.3%) | full | 868,538 | +0.0 | +2.2 | 50.5% | 48.5% | 0.07 |
| +0.3% <= gap < +1% | full | 534,623 | +0.5 | +0.0 | 49.6% | 49.6% | 2.15 |
| +1% <= gap < +2% | full | 171,463 | +6.2 | +4.1 | 50.7% | 50.7% | 11.39 |
| +2% <= gap < +5% | full | 62,915 | +1.5 | -6.0 | 48.9% | 48.9% | 1.18 |
| gap >= +5% | full | 12,628 | +25.6 | +0.8 | 50.0% | 50.0% | 5.74 |
| gap <= -5% | last_24m | 2,772 | -30.0 | -34.5 | 47.6% | 52.3% | -2.89 |
| -5% < gap <= -2% | last_24m | 14,243 | +24.6 | +34.2 | 54.7% | 45.0% | 8.5 |
| -2% < gap <= -1% | last_24m | 33,837 | +23.1 | +21.6 | 54.7% | 45.0% | 17.13 |
| -1% < gap <= -0.3% | last_24m | 86,878 | +6.1 | +7.4 | 52.0% | 47.6% | 9.64 |
| flat (|gap| < 0.3%) | last_24m | 153,964 | -1.0 | +0.0 | 49.7% | 48.3% | -2.36 |
| +0.3% <= gap < +1% | last_24m | 100,444 | -3.0 | -5.0 | 48.3% | 48.3% | -5.36 |
| +1% <= gap < +2% | last_24m | 38,814 | -2.8 | -6.7 | 48.4% | 48.4% | -2.4 |
| +2% <= gap < +5% | last_24m | 15,892 | -28.5 | -30.9 | 45.1% | 45.1% | -11.38 |
| gap >= +5% | last_24m | 3,105 | -31.0 | -39.5 | 45.4% | 45.4% | -3.63 |
| gap <= -5% | last_12m | 1,332 | +9.5 | +3.8 | 50.3% | 49.5% | 0.65 |
| -5% < gap <= -2% | last_12m | 7,361 | +21.5 | +30.9 | 54.3% | 45.3% | 5.53 |
| -2% < gap <= -1% | last_12m | 18,382 | +7.6 | +13.9 | 53.0% | 46.7% | 4.38 |
| -1% < gap <= -0.3% | last_12m | 43,960 | +2.0 | +4.7 | 51.1% | 48.5% | 2.2 |
| flat (|gap| < 0.3%) | last_12m | 72,032 | -1.0 | -1.3 | 49.3% | 48.2% | -1.5 |
| +0.3% <= gap < +1% | last_12m | 49,429 | -1.7 | -5.8 | 48.1% | 48.1% | -2.08 |
| +1% <= gap < +2% | last_12m | 22,798 | -5.8 | -13.4 | 47.0% | 47.0% | -3.75 |
| +2% <= gap < +5% | last_12m | 8,952 | -8.2 | -16.4 | 47.3% | 47.3% | -2.53 |
| gap >= +5% | last_12m | 1,558 | -18.8 | -27.5 | 46.3% | 46.3% | -1.54 |

## 2. Day two after a big close-to-close move

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | Continuation | t |
|---|---|---|---|---|---|---|---|
| yesterday +10% or more | full | 7,608 | -11.2 | -16.2 | 47.9% | 47.9% | -2.0 |
| yesterday +5% to +10% | full | 37,988 | -0.8 | -2.7 | 49.4% | 49.4% | -0.49 |
| yesterday -5% to -10% | full | 35,901 | +20.4 | +17.0 | 52.3% | 47.4% | 10.67 |
| yesterday -10% or worse | full | 6,080 | +75.1 | +47.4 | 54.4% | 45.3% | 9.59 |
| yesterday +10% or more | last_24m | 1,843 | -58.2 | -70.2 | 41.6% | 41.6% | -6.16 |
| yesterday +5% to +10% | last_24m | 9,131 | +5.1 | -0.9 | 49.7% | 49.7% | 1.56 |
| yesterday -5% to -10% | last_24m | 8,395 | +34.3 | +25.8 | 54.0% | 45.8% | 8.43 |
| yesterday -10% or worse | last_24m | 1,454 | -1.2 | +0.0 | 49.9% | 49.9% | -0.1 |
| yesterday +10% or more | last_12m | 841 | +16.9 | +14.3 | 51.4% | 51.4% | 1.15 |
| yesterday +5% to +10% | last_12m | 5,405 | +14.9 | +14.4 | 52.1% | 52.1% | 3.39 |
| yesterday -5% to -10% | last_12m | 4,573 | +2.2 | +7.5 | 51.3% | 48.5% | 0.43 |
| yesterday -10% or worse | last_12m | 670 | -30.9 | -19.6 | 47.6% | 52.4% | -1.62 |

## 3. Three-day moves

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| 3-day return <= -15% | full | 8,326 | +33.7 | +11.0 | 50.8% | 4.92 |
| 3-day return -15% to -10% | full | 19,939 | +19.3 | +10.6 | 51.2% | 6.78 |
| 3-day return >= +15% | full | 11,330 | -0.8 | -5.6 | 49.1% | -0.21 |
| 3-day return <= -15% | last_24m | 2,029 | +3.4 | -12.6 | 48.3% | 0.29 |
| 3-day return -15% to -10% | last_24m | 4,833 | +22.5 | +0.0 | 49.9% | 3.64 |
| 3-day return >= +15% | last_24m | 2,708 | +5.7 | -0.6 | 49.8% | 0.75 |
| 3-day return <= -15% | last_12m | 872 | +16.7 | -1.3 | 49.8% | 1.14 |
| 3-day return -15% to -10% | last_12m | 2,467 | -7.9 | -12.9 | 48.0% | -1.08 |
| 3-day return >= +15% | last_12m | 1,502 | +16.4 | +10.7 | 51.7% | 1.55 |

## 4. 20-day momentum deciles

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| momentum top decile (20d) | full | 229,892 | +2.0 | +2.5 | 50.4% | 4.26 |
| momentum bottom decile (20d) | full | 230,206 | +2.8 | +1.8 | 50.2% | 5.49 |
| momentum top decile (20d) | last_24m | 45,090 | +2.2 | +1.6 | 50.2% | 1.83 |
| momentum bottom decile (20d) | last_24m | 45,169 | -0.2 | -0.5 | 49.6% | -0.18 |
| momentum top decile (20d) | last_12m | 22,590 | +4.5 | +0.0 | 49.9% | 2.46 |
| momentum bottom decile (20d) | last_12m | 22,669 | -4.1 | -2.3 | 49.3% | -2.32 |

## 5. Base rate: share of tradable stock-days that closed above the open

| Year | n | Share up | Mean OC (bps) |
|---|---|---|---|
| 2016 | 176,985 | 52.8% | +10.4 |
| 2017 | 197,848 | 51.4% | +2.6 |
| 2018 | 201,844 | 49.4% | -6.4 |
| 2019 | 205,998 | 52.6% | +6.7 |
| 2020 | 211,038 | 49.7% | +0.6 |
| 2021 | 217,192 | 50.2% | +0.7 |
| 2022 | 218,920 | 50.0% | +1.2 |
| 2023 | 220,001 | 51.5% | +6.0 |
| 2024 | 224,805 | 50.3% | -0.9 |
| 2025 | 224,242 | 51.0% | +4.2 |
| 2026 | 191,661 | 49.5% | -0.3 |

## 6. SPY conditionals

| Condition | Period | n | Mean OC (bps) | Median (bps) | Share up | t |
|---|---|---|---|---|---|---|
| SPY all sessions | full | 2,727 | +2.1 | +5.2 | 53.9% | 1.28 |
| SPY gap >= +0.5% | full | 429 | +8.9 | +22.3 | 59.9% | 1.78 |
| SPY gap <= -0.5% | full | 346 | +5.9 | +6.7 | 53.5% | 0.86 |
| SPY after 3 up days | full | 439 | +1.4 | +4.5 | 52.8% | 0.55 |
| SPY after a -1% day | full | 296 | +8.8 | +1.0 | 52.0% | 1.12 |
| SPY all sessions | last_24m | 501 | +1.5 | +3.2 | 52.1% | 0.37 |
| SPY gap >= +0.5% | last_24m | 78 | -9.1 | -6.4 | 46.2% | -0.9 |
| SPY gap <= -0.5% | last_24m | 65 | +19.7 | +0.5 | 50.8% | 0.93 |
| SPY after 3 up days | last_24m | 85 | +1.7 | +0.1 | 50.6% | 0.3 |
| SPY after a -1% day | last_24m | 55 | +44.4 | +32.9 | 61.8% | 1.83 |
| SPY all sessions | last_12m | 251 | -0.9 | +0.9 | 51.0% | -0.22 |
| SPY gap >= +0.5% | last_12m | 42 | -4.6 | -8.5 | 42.9% | -0.38 |
| SPY gap <= -0.5% | last_12m | 30 | +3.1 | -2.8 | 46.7% | 0.23 |
| SPY after 3 up days | last_12m | 37 | +0.0 | +7.4 | 54.0% | 0.01 |
| SPY after a -1% day | last_12m | 26 | +11.3 | +0.9 | 53.8% | 0.7 |

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
| 2026 | 213 | 50.7% | -0.5 |

_Current index membership (survivorship bias favours longs slightly). Research output, not investment advice._
