#!/usr/bin/env python3
"""Fetch Google Scholar citations-by-year and update _data/scholar_citations.yml."""

from __future__ import annotations

import re
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "_data" / "scholar_citations.yml"
USER_ID = "-Es6xrgAAAAJ"
URL = f"https://scholar.google.com/citations?user={USER_ID}&hl=en"


def fetch_html() -> str:
    req = urllib.request.Request(
        URL,
        headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"},
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", errors="ignore")


def parse(html: str) -> dict:
    years = re.findall(r'class="gsc_g_t"[^>]*>(\d{4})</span>', html)
    vals = re.findall(r'class="gsc_g_al"[^>]*>(\d+)</span>', html)
    if len(years) != len(vals):
        raise ValueError(f"Year/value mismatch: {len(years)} vs {len(vals)}")

    citedby = re.search(r"Cited by\s*([\d,]+)", html)
    total = int(citedby.group(1).replace(",", "")) if citedby else sum(int(v) for v in vals)

    hindex = re.search(r'h-index</a></td><td class="gsc_rsb_std">(\d+)</td>', html)
    i10 = re.search(r'i10-index</a></td><td class="gsc_rsb_std">(\d+)</td>', html)

    by_year = {int(y): int(v) for y, v in zip(years, vals)}
    ordered_years = sorted(by_year)
    return {
        "total": total,
        "h_index": int(hindex.group(1)) if hindex else None,
        "i10_index": int(i10.group(1)) if i10 else None,
        "years": ordered_years,
        "counts": [by_year[y] for y in ordered_years],
    }


def write_yaml(data: dict) -> None:
    from datetime import date

    years = ", ".join(str(y) for y in data["years"])
    counts = ", ".join(str(c) for c in data["counts"])
    lines = [
        "# Google Scholar citation metrics (user=-Es6xrgAAAAJ)",
        "# Regenerate: python3 scripts/update_scholar_citations.py",
        f'updated: "{date.today().isoformat()}"',
        f"total: {data['total']}",
        f"h_index: {data['h_index']}",
        f"i10_index: {data['i10_index']}",
        f'profile_url: "{URL}"',
        f"years: [{years}]",
        f"counts: [{counts}]",
    ]
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Updated {OUT}")


def main() -> None:
    data = parse(fetch_html())
    write_yaml(data)


if __name__ == "__main__":
    main()
