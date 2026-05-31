#!/usr/bin/env python3
"""Extract teaser images from publication PDFs and patch publications.md."""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

import fitz

ROOT = Path(__file__).resolve().parents[1]
PUB_MD = ROOT / "_pages" / "publications.md"
OUT_DIR = ROOT / "images" / "papers"
CACHE_DIR = ROOT / ".cache" / "paper-pdfs"
THUMB_WIDTH = 220
MAX_PAGES_SCAN = 4
MIN_IMAGE_AREA = 40_000

PAPER_OPEN = '<div class="paper">'
TITLE_RE = re.compile(r'<div class="paper-title">(.*?)</div>', re.DOTALL)
LINK_RE = re.compile(r'<a href="([^"]+)"')


def iter_paper_blocks(md: str):
    """Yield (start, end, inner_html) for each top-level .paper block."""
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
                end = next_close + len("</div>")
                if depth == 0:
                    yield start, end, md[inner_start:next_close]
                    i = end
                    break
                pos = next_close + len("</div>")
        else:
            return


def extract_div_inner(html: str, class_name: str) -> str | None:
    """Return inner HTML of the first <div class="CLASS">...</div> (balanced)."""
    marker = f'<div class="{class_name}">'
    idx = html.find(marker)
    if idx == -1:
        return None
    inner_start = idx + len(marker)
    depth = 1
    pos = inner_start
    while depth > 0 and pos < len(html):
        next_open = html.find("<div", pos)
        next_close = html.find("</div>", pos)
        if next_close == -1:
            return None
        if next_open != -1 and next_open < next_close:
            depth += 1
            pos = next_open + 4
        else:
            depth -= 1
            if depth == 0:
                return html[inner_start:next_close].strip()
            pos = next_close + len("</div>")
    return None


def paper_body_content(block: str) -> str:
    """Venue/title/authors/links only (strip existing thumbnail wrapper)."""
    body = extract_div_inner(block, "paper-body")
    if body is not None:
        return body
    return block.strip()


def slugify(title: str) -> str:
    s = re.sub(r"<[^>]+>", "", title).strip().lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    h = hashlib.md5(title.encode()).hexdigest()[:8]
    return f"{s[:48]}-{h}" if s else h


def pick_pdf_url(links: list[str]) -> str | None:
    scored: list[tuple[int, str]] = []
    for url in links:
        u = url.lower()
        score = 0
        if "arxiv.org/pdf" in u:
            score = 100
        elif u.endswith(".pdf"):
            score = 90
        elif "openreview.net/pdf" in u:
            score = 85
        elif "openreview.net/forum" in u:
            score = 85
            m = re.search(r"id=([^&]+)", url)
            if m:
                url = f"https://openreview.net/pdf?id={m.group(1)}"
        elif "openaccess.thecvf.com" in u and ".pdf" in u:
            score = 80
        elif "arxiv.org/abs" in u:
            score = 70
            url = url.replace("/abs/", "/pdf/") + (".pdf" if not url.endswith(".pdf") else "")
        elif "agupubs.onlinelibrary.wiley.com" in u and "/pdf/" in u:
            score = 75
        elif "researchgate.net" in u and ".pdf" in u:
            score = 60
        elif "ijcai.org" in u and ".pdf" in u:
            score = 80
        elif "aaai.org" in u and ".pdf" in u:
            score = 80
        elif "dl.acm.org" in u and ".pdf" in u:
            score = 75
        if score > 0 and "ieeexplore.ieee.org" not in u and "sciencedirect.com" not in u and "spiedigitallibrary.org" not in u:
            scored.append((score, url))
    if not scored:
        return None
    scored.sort(reverse=True)
    return scored[0][1]


def download_pdf(url: str, dest: Path, *, force: bool = False) -> bool:
    dest.parent.mkdir(parents=True, exist_ok=True)
    if not force and dest.exists() and dest.stat().st_size > 10_000:
        return True
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 (compatible; academic-site-bot/1.0)"},
    )
    try:
        with urllib.request.urlopen(req, timeout=90) as resp:
            data = resp.read()
        if len(data) < 5000 or data[:4] != b"%PDF":
            return False
        dest.write_bytes(data)
        return True
    except (urllib.error.URLError, TimeoutError, ValueError):
        return False


def save_pixmap_jpeg(pix: fitz.Pixmap, out_path: Path, width: int) -> None:
    img = pix.pil_image()
    if img.width > width:
        h = max(1, int(img.height * width / img.width))
        img = img.resize((width, h))
    img.convert("RGB").save(str(out_path), format="JPEG", quality=82, optimize=True)


def extract_thumbnail(pdf_path: Path, out_path: Path) -> bool:
    try:
        doc = fitz.open(pdf_path)
    except Exception:
        return False

    best_pix = None
    best_area = 0

    for pno in range(min(len(doc), MAX_PAGES_SCAN)):
        page = doc[pno]
        for img in page.get_images(full=True):
            try:
                xref = img[0]
                pix = fitz.Pixmap(doc, xref)
                if pix.n - pix.alpha > 3:
                    pix = fitz.Pixmap(fitz.csRGB, pix)
                area = pix.width * pix.height
                if area > best_area and pix.width >= 80 and pix.height >= 80:
                    best_area = area
                    best_pix = pix
            except Exception:
                continue

    if best_area < MIN_IMAGE_AREA:
        # Fallback: render a page likely containing a figure (page 2, else page 1)
        pno = 1 if len(doc) > 1 else 0
        page = doc[pno]
        rect = page.rect
        clip = fitz.Rect(rect.x0, rect.y0, rect.x1, min(rect.y1, rect.y0 + 520))
        mat = fitz.Matrix(1.2, 1.2)
        best_pix = page.get_pixmap(matrix=mat, clip=clip, alpha=False)

    if best_pix is None:
        doc.close()
        return False

    out_path.parent.mkdir(parents=True, exist_ok=True)
    save_pixmap_jpeg(best_pix, out_path, THUMB_WIDTH)
    doc.close()
    return out_path.exists() and out_path.stat().st_size > 800


def parse_papers(md: str) -> list[dict]:
    papers = []
    for _start, _end, block in iter_paper_blocks(md):
        body = paper_body_content(block)
        tm = TITLE_RE.search(body)
        if not tm:
            continue
        title = re.sub(r"\s+", " ", tm.group(1)).strip()
        links = LINK_RE.findall(body)
        pdf = pick_pdf_url(links)
        papers.append({"title": title, "pdf": pdf, "body": body, "links": links})
    return papers


def build_thumb_html(slug: str, pdf: str | None, title: str, has_image: bool) -> str:
    alt = re.sub(r"<[^>]+>", "", title)[:120]
    if has_image and pdf:
        return (
            f'    <a class="paper-thumb" href="{pdf}" target="_blank" rel="noopener">\n'
            f'      <img src="/images/papers/{slug}.jpg" alt="{alt}" width="128" loading="lazy" />\n'
            f"    </a>\n"
        )
    return '    <div class="paper-thumb paper-thumb--placeholder" aria-hidden="true"></div>\n'


def format_paper(body: str, thumb_html: str) -> str:
    return (
        '<div class="paper">\n'
        '  <div class="paper-inner">\n'
        f"{thumb_html}"
        '    <div class="paper-body">\n'
        f"{body}\n"
        "    </div>\n"
        "  </div>\n"
        "</div>"
    )


def patch_markdown(md: str, results: dict[str, dict]) -> str:
    out = []
    last = 0
    for start, end, block in iter_paper_blocks(md):
        out.append(md[last:start])
        body = paper_body_content(block)
        tm = TITLE_RE.search(body)
        if not tm:
            out.append(md[start:end])
        else:
            title = re.sub(r"\s+", " ", tm.group(1)).strip()
            slug = slugify(title)
            info = results.get(title, {})
            thumb_html = build_thumb_html(
                slug, info.get("pdf"), title, info.get("ok", False)
            )
            out.append(format_paper(body, thumb_html))
        last = end
    out.append(md[last:])
    return "".join(out)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--force",
        action="store_true",
        help="Re-download PDFs and regenerate all thumbnails",
    )
    parser.add_argument(
        "--markdown-only",
        action="store_true",
        help="Only refresh publications.md from existing images (no downloads)",
    )
    args = parser.parse_args()

    md = PUB_MD.read_text(encoding="utf-8")
    papers = parse_papers(md)
    print(f"Found {len(papers)} paper entries")

    results: dict[str, dict] = {}
    ok_count = 0
    for i, p in enumerate(papers, 1):
        title = p["title"]
        slug = slugify(title)
        pdf = p["pdf"]
        out = OUT_DIR / f"{slug}.jpg"
        info = {"pdf": pdf, "ok": out.exists() and out.stat().st_size > 800, "slug": slug}

        if args.markdown_only:
            results[title] = info
            if info["ok"]:
                ok_count += 1
            continue

        if not pdf:
            print(f"[{i}/{len(papers)}] skip (no PDF): {title[:60]}...")
            results[title] = info
            continue

        cache = CACHE_DIR / f"{slug}.pdf"
        print(f"[{i}/{len(papers)}] {title[:55]}...")
        if download_pdf(pdf, cache, force=args.force) and extract_thumbnail(cache, out):
            info["ok"] = True
            ok_count += 1
            print(f"  -> {out.name}")
        elif info["ok"] and not args.force:
            ok_count += 1
            print(f"  -> kept {out.name}")
        else:
            info["ok"] = False
            print("  -> failed")
        results[title] = info
        time.sleep(0.3)

    new_md = patch_markdown(md, results)
    PUB_MD.write_text(new_md, encoding="utf-8")
    print(f"\nDone: {ok_count}/{len(papers)} thumbnails, updated {PUB_MD}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
