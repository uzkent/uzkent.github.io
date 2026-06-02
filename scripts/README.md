# Site maintenance scripts

## Paper thumbnails

```bash
python3 scripts/extract_paper_thumbnails.py          # use cached PDFs
python3 scripts/extract_paper_thumbnails.py --force # re-download all PDFs
```

Requires: `pip install pymupdf pillow`

## Google Scholar citations chart

```bash
python3 scripts/update_scholar_citations.py
```

Updates `_data/scholar_citations.yml` (used on the publications page).

**Automatic refresh:** GitHub Actions runs this every **Monday at 09:00 UTC** (`.github/workflows/sync-scholar-citations.yml`). You can also trigger it manually under **Actions → Sync Google Scholar citations → Run workflow**.

## BibTeX export

```bash
python3 scripts/generate_publications_bib.py
```

Regenerates `files/publications.bib` from `_pages/publications.md`.
