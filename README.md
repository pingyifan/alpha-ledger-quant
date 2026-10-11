# alpha-ledger-quant

The quantitative arm of the **Alpha Ledger**, a paper-only, self-scoring US stock
prediction journal. Every weekday evening a GitHub Actions job:

1. rebuilds the universe (current S&P 500 + S&P 400 members, plus SPY/QQQ/IWM),
2. downloads daily bars from Yahoo Finance and converts them into a
   [Microsoft Qlib](https://github.com/microsoft/qlib) binary store,
3. trains two LightGBM cross-sectional models on Qlib's **Alpha158** features: `oc`, whose
   label is the **next session's open-to-close return** (the ledger's scoring rule), and `cc`,
   whose label is **next close to the following close** (a one-session hold that keeps the overnight),
4. scores every name for the next session (`output/scores_latest.csv` for `oc`,
   `output/scores_cc_latest.csv` for `cc`),
5. evaluates the model out of sample on the last year and backtests the ledger's
   playbook priors on the whole panel,
6. commits `output/` so the ledger's scheduled run can read it with one request.

Nothing here trades. The outputs are research inputs for a simulated fund and are
not investment advice.

## What the ledger reads

| File | Contents |
|---|---|
| `output/scores_latest.csv` | `oc` model, one row per name: `asof_date, model, horizon, ticker, name, sector, index, score, rank, rank_pct, decile, close, adv20_usd, tradable`. `score` is the prediction for the *next* session's open-to-close return; `rank` 1 = best among tradable names; `decile` 10 = best. |
| `output/scores_cc_latest.csv` | same layout for the `cc` model (next close to the following close). |
| `output/model_card.json`, `output/model_card_cc.json` | per model: training dates, early-stopped rounds, validation IC / Rank IC (the ledger gates each sleeve on `validation.rank_ic_mean >= 0.01`), feature importance. |
| `output/oos_report.md` / `.json`, `output/oos_report_cc.*` | per model, out of sample on the validation year: IC, name-day hit rates (top-5 longs, bottom-5 shorts, base rate), horizon-return simulations net of 4 bps, Qlib's TopkDropout reference backtest. |
| `output/priors_report.md` / `.json` | the playbook's priors (gap continuation vs fade, day-two moves, drawdown bounces, momentum, base rates, SPY conditionals) measured on every stock-day in the panel, with verdicts. |
| `output/scores_history_top.csv`, `output/scores_history_top_cc.csv` | top/bottom 25 per day for the last 300 sessions, per model. |
| `output/status.json` | what the last run did, how long each step took, errors if any, `data_end_date`. |
| `output/universe.csv` | the ticker list used. |

Raw URL pattern (public repo):
`https://raw.githubusercontent.com/pingyifan/alpha-ledger-quant/main/output/scores_latest.csv`

A consumer should check `status.json` → `ok` and that `scores_latest.csv` → `asof_date`
is the last completed session before trusting the scores.

## Method

* **Features**: Qlib `Alpha158` (9 candlestick-shape features, 4 normalised prices,
  29 rolling operators × windows 5/10/20/30/60) computed by Qlib's expression engine.
* **Labels**: `oc` = `Ref($close, -1)/Ref($open, -1) - 1`; `cc` = `Ref($close, -2)/Ref($close, -1) - 1`.
  Both are cross-sectionally z-scored per day for training (Qlib's default `CSZScoreNorm`),
  so each model learns *relative* strength over its horizon, not the level of the market.
* **Regularisation**: learning rate 0.02, 31 leaves, depth 6, 500 rows per leaf, L1 50 / L2 300,
  early stopping on the validation year. Daily cross-sectional targets are mostly noise; the
  first, lighter configuration stopped after 8 trees with IC ≈ 0.
* **Why two horizons** (label experiments, validation year to 2026-10-08, 252 sessions):
  open-to-close has no out-of-sample signal under any setting (IC 0.002–0.005, Rank IC ≈ 0,
  early stopping after 2–21 trees), while horizons that keep the overnight do: close-to-close
  IC 0.026 / Rank IC 0.021 (regularised), open-to-next-open IC 0.020 / Rank IC 0.013,
  overnight-only IC 0.017. The top-5 long basket of the close-to-close model averaged about
  +45 bps per session net of costs against +6 bps for the universe; the long-short decile spread
  stayed inside the noise (t < 1). `cc` is therefore the hold-sleeve model; `oc` is kept because
  it is the ledger's own scoring rule and the agreement record is the experiment.
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

## Research

`python -m research.label_experiments --labels oc,oo,cc_qlib,co --params base,reg` compares
return horizons and parameter sets out of sample; the `label experiments` workflow runs the
same thing on GitHub's runners, one job per label, from the rolling `panel` release asset
(the adjusted price panel, replaced by every nightly run, for offline research).

## Running locally

```bash
python3.11 -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
python -m pipeline.run_all                       # full run (needs internet for Wikipedia + Yahoo)
python -m pipeline.run_all --synthetic 60        # no network: synthetic panel end to end
python -m pipeline.run_all --steps train,score,evaluate,priors   # reuse downloaded data
```

Data lands in `data/` (ignored by git); set `ALQ_DATA_DIR` to put it elsewhere and
`ALQ_OUTPUT_DIR` to keep research runs from touching the committed `output/`.

## Layout

```
pipeline/
  config.py          universe, dates, label, model params, costs
  universe.py        Wikipedia constituents -> output/universe.csv
  download.py        yfinance -> data/csv/*.csv (Qlib dump_bin format, adjusted prices)
  make_qlib_data.py  data/csv -> data/qlib_us (Qlib binary store) via vendored dump_bin
  qlib_env.py        qlib.init, Alpha158 handler with the open-to-close label, helpers
  train.py           walk-forward LightGBM training per model, model cards
  score.py           tonight's scores per model -> output/scores_*latest.csv
  evaluate.py        per-model out-of-sample report (IC, hit rates, simulations, Qlib backtest)
  priors.py          playbook priors backtest -> output/priors_report.md
  run_all.py         orchestration + output/status.json
  vendor/dump_bin.py Qlib's CSV-to-bin converter (MIT, microsoft/qlib)
tests/synthetic.py   synthetic panel generator
research/label_experiments.py   horizon and parameter comparison
.github/workflows/nightly.yml, experiments.yml
```

Qlib is MIT-licensed; `pipeline/vendor/QLIB_LICENSE` is its license file.
