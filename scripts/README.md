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

## BibTeX export

```bash
python3 scripts/generate_publications_bib.py
```

Regenerates `files/publications.bib` from `_pages/publications.md`.
