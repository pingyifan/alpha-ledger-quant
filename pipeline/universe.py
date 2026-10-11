"""Build the ticker universe: current S&P 500 + S&P 400 members from Wikipedia.

Writes output/universe.csv (committed, so a failed fetch can fall back to the
last good list). Tickers are normalised to Yahoo's convention (BRK.B -> BRK-B).
Membership is *current*, not point-in-time: see README for the survivorship caveat.
"""
from __future__ import annotations

import io
import logging
from pathlib import Path

import pandas as pd
import requests

from . import config

log = logging.getLogger(__name__)
HEADERS = {"User-Agent": "alpha-ledger-quant/1.0 (research pipeline; contact via GitHub)"}


def _read_wiki_table(url: str) -> pd.DataFrame:
    resp = requests.get(url, headers=HEADERS, timeout=60)
    resp.raise_for_status()
    tables = pd.read_html(io.StringIO(resp.text))
    for t in tables:
        cols = {str(c).strip().lower() for c in t.columns}
        if ("symbol" in cols or "ticker symbol" in cols or "ticker" in cols) and len(t) > 100:
            return t
    raise ValueError(f"no constituents table found at {url}")


def _normalise(t: pd.DataFrame, index_name: str) -> pd.DataFrame:
    t = t.copy()
    t.columns = [str(c).strip() for c in t.columns]
    lower = {c.lower(): c for c in t.columns}
    sym_col = lower.get("symbol") or lower.get("ticker symbol") or lower.get("ticker")
    name_col = lower.get("security") or lower.get("company") or lower.get("name")
    sector_col = lower.get("gics sector") or lower.get("sector")
    out = pd.DataFrame(
        {
            "ticker": t[sym_col].astype(str).str.strip().str.upper().str.replace(".", "-", regex=False),
            "name": t[name_col].astype(str).str.strip() if name_col else "",
            "sector": t[sector_col].astype(str).str.strip() if sector_col else "",
            "index": index_name,
        }
    )
    out = out[out["ticker"].str.match(r"^[A-Z][A-Z0-9\-]{0,6}$")]
    return out


def build_universe(output_path: Path | None = None) -> pd.DataFrame:
    output_path = output_path or (config.OUTPUT_DIR / "universe.csv")
    frames = []
    errors = []
    for name, url in config.INDEX_PAGES.items():
        try:
            frames.append(_normalise(_read_wiki_table(url), name))
            log.info("%s: %d constituents", name, len(frames[-1]))
        except Exception as exc:  # noqa: BLE001 - we fall back to the committed list
            errors.append(f"{name}: {exc}")
            log.warning("could not fetch %s: %s", name, exc)
    if frames:
        uni = pd.concat(frames, ignore_index=True).drop_duplicates("ticker").sort_values("ticker")
        if len(uni) < 600:
            errors.append(f"only {len(uni)} tickers fetched; keeping previous list")
            uni = None
    else:
        uni = None
    if uni is None:
        if output_path.exists():
            uni = pd.read_csv(output_path)
            log.warning("using previous universe (%d tickers): %s", len(uni), "; ".join(errors))
        else:
            raise RuntimeError("no universe available: " + "; ".join(errors))
    etfs = pd.DataFrame({"ticker": config.ETF_TICKERS, "name": config.ETF_TICKERS, "sector": "ETF", "index": "ETF"})
    uni = pd.concat([uni[~uni["ticker"].isin(config.ETF_TICKERS)], etfs], ignore_index=True)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    uni.to_csv(output_path, index=False)
    return uni


def load_universe() -> pd.DataFrame:
    return pd.read_csv(config.OUTPUT_DIR / "universe.csv")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    df = build_universe()
    print(df["index"].value_counts())
