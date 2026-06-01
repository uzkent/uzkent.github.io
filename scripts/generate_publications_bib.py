#!/usr/bin/env python3
"""Generate files/publications.bib from _pages/publications.md."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUB_MD = ROOT / "_pages" / "publications.md"
OUT = ROOT / "files" / "publications.bib"

PAPER_OPEN = '<div class="paper">'
TITLE_RE = re.compile(r'<div class="paper-title">(.*?)</div>', re.DOTALL)
VENUE_RE = re.compile(r'<div class="paper-venue">(.*?)</div>', re.DOTALL)
AUTHORS_RE = re.compile(r'<div class="paper-authors">(.*?)</div>', re.DOTALL)
TAG_RE = re.compile(r"<[^>]+>")


def iter_paper_blocks(md: str):
    i = 0
    while True:
        start = md.find(PAPER_OPEN, i)
        if start == -1:
            return
        inner_start = start + len(PAPER_OPEN)
        depth = 1
        pos = inner_start
        while depth > 0 and pos < len(md):
            next_open = md.find("<div", pos)
            next_close = md.find("</div>", pos)
            if next_close == -1:
                return
            if next_open != -1 and next_open < next_close:
                depth += 1
                pos = next_open + 4
            else:
                depth -= 1
                if depth == 0:
                    yield md[inner_start:next_close]
                    i = next_close + len("</div>")
                    break
                pos = next_close + len("</div>")
        else:
            return


def strip_html(s: str) -> str:
    return re.sub(r"\s+", " ", TAG_RE.sub("", s)).strip()


def bib_key(title: str, year: str) -> str:
    words = re.findall(r"[a-z0-9]+", title.lower())[:3]
    author = "uzkent"
    y = year if year.isdigit() else "unknown"
    return f"{author}{''.join(words)}{y}"[:48]


def authors_to_bib(authors: str) -> str:
    authors = authors.replace("&amp;", "&")
    parts = [p.strip() for p in authors.split(",") if p.strip()]
    bib_authors = []
    for p in parts:
        p = strip_html(p)
        if not p:
            continue
        if p.startswith("B. Uzkent") or p == "B. Uzkent":
            bib_authors.append("Uzkent, Burak")
            continue
        m = re.match(r"([A-Z])\.\s*(.+)", p)
        if m:
            initial, last = m.group(1), m.group(2)
            bib_authors.append(f"{last}, {initial}.")
        else:
            bib_authors.append(p)
    return " and ".join(bib_authors) if bib_authors else "Uzkent, Burak"


def venue_type(venue: str) -> tuple[str, str]:
    v = venue.lower()
    if any(x in v for x in ("arxiv", "preprint", "under review")):
        return "misc", "eprint"
    if "journal" in v or "transactions" in v or "remote sensing" in v:
        return "article", "journal"
    return "inproceedings", "booktitle"


def main() -> None:
    md = PUB_MD.read_text(encoding="utf-8")
    year = ""
    entries = []
    for block in iter_paper_blocks(md):
        # walk backwards in md for year - approximate from block position
        pass

    # assign years by scanning md with markers
    parts = re.split(r'<div class="year-marker"><span>(\d{4})</span></div>', md)
    for i in range(1, len(parts), 2):
        year = parts[i]
        section = parts[i + 1]
        for block in iter_paper_blocks(section):
            tm = TITLE_RE.search(block)
            vm = VENUE_RE.search(block)
            am = AUTHORS_RE.search(block)
            if not tm:
                continue
            title = strip_html(tm.group(1))
            venue = strip_html(vm.group(1)) if vm else ""
            venue = re.sub(r"·.*", "", venue).strip()
            authors = authors_to_bib(am.group(1) if am else "")
            key = bib_key(title, year)
            entry_type, field = venue_type(venue)
            lines = [f"@{entry_type}{{{key},"]
            lines.append(f"  title = {{{{{title}}}}},")
            lines.append(f"  author = {{{{{authors}}}}},")
            lines.append(f"  year = {{{{{year}}}}},")
            if entry_type == "article":
                lines.append(f"  journal = {{{{{venue}}}}},")
            else:
                lines.append(f"  {field} = {{{{{venue}}}}},")
            lines.append("}")
            entries.append("\n".join(lines))

    OUT.parent.mkdir(parents=True, exist_ok=True)
    header = "% Auto-generated from publications.md — run: python3 scripts/generate_publications_bib.py\n\n"
    OUT.write_text(header + "\n\n".join(entries) + "\n", encoding="utf-8")
    print(f"Wrote {len(entries)} entries to {OUT}")


if __name__ == "__main__":
    main()
