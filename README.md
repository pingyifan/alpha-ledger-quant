# alpha-ledger-quant

The quantitative arm of the **Alpha Ledger**, a paper-only, self-scoring US stock
prediction journal. Every weekday evening a GitHub Actions job:

1. rebuilds the universe (current S&P 500 + S&P 400 members, plus SPY/QQQ/IWM),
2. downloads daily bars from Yahoo Finance and converts them into a
   [Microsoft Qlib](https://github.com/microsoft/qlib) binary store,
3. trains a LightGBM cross-sectional model on Qlib's **Alpha158** features with the
   label set to the **next session's open-to-close return** (the ledger's scoring rule),
4. scores every name for the next session and writes `output/scores_latest.csv`,
5. evaluates the model out of sample on the last year and backtests the ledger's
   playbook priors on the whole panel,
6. commits `output/` so the ledger's scheduled run can read it with one request.

Nothing here trades. The outputs are research inputs for a simulated fund and are
not investment advice.

## What the ledger reads

| File | Contents |
|---|---|
| `output/scores_latest.csv` | one row per name: `asof_date, ticker, name, sector, index, score, rank, rank_pct, decile, close, adv20_usd, tradable`. `score` is the model's prediction for the *next* session's open-to-close return; `rank` 1 = best among tradable names; `decile` 10 = best. |
| `output/model_card.json` | training dates, early-stopped rounds, validation IC / Rank IC, feature importance. |
| `output/oos_report.md` / `.json` | out-of-sample report on the validation year: IC, name-day hit rates (top-5 longs, bottom-5 shorts, base rate), open-to-close simulations net of 4 bps, Qlib's TopkDropout reference backtest. |
| `output/priors_report.md` / `.json` | the playbook's priors (gap continuation vs fade, day-two moves, drawdown bounces, momentum, base rates, SPY conditionals) measured on every stock-day in the panel, with verdicts. |
| `output/scores_history_top.csv` | top/bottom 25 per day for the last 300 sessions. |
| `output/status.json` | what the last run did, how long each step took, errors if any, `data_end_date`. |
| `output/universe.csv` | the ticker list used. |

Raw URL pattern (public repo):
`https://raw.githubusercontent.com/<owner>/alpha-ledger-quant/main/output/scores_latest.csv`

A consumer should check `status.json` → `ok` and that `scores_latest.csv` → `asof_date`
is the last completed session before trusting the scores.

## Method

* **Features**: Qlib `Alpha158` (9 candlestick-shape features, 4 normalised prices,
  29 rolling operators × windows 5/10/20/30/60) computed by Qlib's expression engine.
* **Label**: `Ref($close, -1)/Ref($open, -1) - 1`, cross-sectionally z-scored per day
  for training (Qlib's default `CSZScoreNorm`). The model learns *relative* next-day
  open-to-close strength, not the level of the market.
* **Split**: train from `START_DATE` (2016) to one year before the end, validate on the
  last 252 complete sessions (early stopping and all out-of-sample numbers), then refit
  on everything with the stopped round count for tonight's scores. Retrained every run.
* **Tradable filter**: last close ≥ $5, 20-day average dollar volume ≥ $5M, ≥ 250 bars.
* **Costs** in every simulation: 2 bps at the open + 2 bps at the close, the same as the
  ledger's simulated fund.

## Caveats

* The universe is *current* index membership, so the panel has survivorship bias
  (names that were removed after collapsing are missing; this flatters long-side
  statistics a little). Point-in-time membership is a planned upgrade via Qlib's
  `us_index` collector.
* Yahoo Finance data is free and occasionally wrong; the pipeline drops obviously bad
  bars and records the last-date distribution in `data/download_meta.json`.
* Daily open-to-close returns on single names are mostly noise. Expect IC in the low
  hundredths; the point is a measured prior and an evidence gate, not a money machine.

## Running locally

```bash
python3.11 -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
python -m pipeline.run_all                       # full run (needs internet for Wikipedia + Yahoo)
python -m pipeline.run_all --synthetic 60        # no network: synthetic panel end to end
python -m pipeline.run_all --steps train,score,evaluate,priors   # reuse downloaded data
```

Data lands in `data/` (ignored by git); set `ALQ_DATA_DIR` to put it elsewhere.

## Layout

```
pipeline/
  config.py          universe, dates, label, model params, costs
  universe.py        Wikipedia constituents -> output/universe.csv
  download.py        yfinance -> data/csv/*.csv (Qlib dump_bin format, adjusted prices)
  make_qlib_data.py  data/csv -> data/qlib_us (Qlib binary store) via vendored dump_bin
  qlib_env.py        qlib.init, Alpha158 handler with the open-to-close label, helpers
  train.py           walk-forward LightGBM training, model card
  score.py           tonight's scores -> output/scores_latest.csv
  evaluate.py        out-of-sample report (IC, hit rates, simulations, Qlib backtest)
  priors.py          playbook priors backtest -> output/priors_report.md
  run_all.py         orchestration + output/status.json
  vendor/dump_bin.py Qlib's CSV-to-bin converter (MIT, microsoft/qlib)
tests/synthetic.py   synthetic panel generator
.github/workflows/nightly.yml
```

Qlib is MIT-licensed; `pipeline/vendor/QLIB_LICENSE` is its license file.
