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
from PIL import Image, ImageChops

ROOT = Path(__file__).resolve().parents[1]
PUB_MD = ROOT / "_pages" / "publications.md"
OUT_DIR = ROOT / "images" / "papers"
CACHE_DIR = ROOT / ".cache" / "paper-pdfs"
THUMB_WIDTH = 220
MAX_PAGES_SCAN = 6
MIN_IMAGE_AREA = 35_000
MIN_WORKFLOW_SCORE = 18.0

# Prefer architecture / pipeline / overview figures (common in ML papers).
WORKFLOW_CAPTION_RE = re.compile(
    r"\b(architecture|pipeline|overview|framework|workflow|proposed\s+method|"
    r"our\s+method|system\s+overview|model\s+architecture|end[- ]to[- ]end|"
    r"approach|methodology|schematic)\b",
    re.IGNORECASE,
)
FIGURE_ONE_RE = re.compile(r"\b(figure\s*1|fig\.?\s*1)\b", re.IGNORECASE)

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


def trim_white_borders(img: Image.Image) -> Image.Image:
    img = img.convert("RGB")
    bg = Image.new("RGB", img.size, (255, 255, 255))
    bbox = ImageChops.difference(img, bg).getbbox()
    return img.crop(bbox) if bbox else img


def trim_bottom_text_band(img: Image.Image) -> Image.Image:
    """Drop caption / paragraph rows often left below the figure in page renders."""
    gray = img.convert("L")
    w, h = gray.size
    if h < 48:
        return img

    step = max(1, w // 100)
    rows: list[float] = []
    px = gray.load()
    for y in range(h):
        dark = sum(1 for x in range(0, w, step) if px[x, y] < 215)
        rows.append(dark / max(1, (w + step - 1) // step))

    cut = h
    text_run = 0
    scan_from = max(0, int(h * 0.55))
    for y in range(h - 1, scan_from, -1):
        ink = rows[y]
        if 0.025 <= ink <= 0.38:
            text_run += 1
            if text_run >= 4:
                cut = y
        elif text_run >= 4:
            break
        else:
            text_run = 0

    if cut < h - 10:
        return img.crop((0, 0, w, max(32, cut - 4)))
    return img


def save_pixmap_jpeg(pix: fitz.Pixmap, out_path: Path, width: int) -> None:
    img = trim_bottom_text_band(trim_white_borders(pix.pil_image()))
    if img.width > width:
        h = max(1, int(img.height * width / img.width))
        img = img.resize((width, h))
    img.convert("RGB").save(str(out_path), format="JPEG", quality=82, optimize=True)


def score_workflow_image(width: int, height: int, page_no: int, area: int) -> float:
    """Higher score = more likely an architecture / workflow diagram."""
    aspect = width / max(height, 1)
    score = 0.0

    if 1.1 <= aspect <= 4.0:
        score += 42.0
    elif aspect > 4.0:
        score += 8.0
    else:
        score -= 28.0  # portrait or square (photos, portraits)

    if page_no == 0:
        score -= 40.0
    elif page_no in (1, 2):
        score += 30.0
    elif page_no == 3:
        score += 12.0

    if 90_000 <= area <= 2_800_000:
        score += min(35.0, area / 95_000.0)
    elif area > 2_800_000:
        score += 18.0
    elif area < MIN_IMAGE_AREA:
        score -= 50.0
    else:
        score += 8.0

    if width < 140 or height < 100:
        score -= 25.0

    return score


def caption_bonus(page: fitz.Page, bbox: fitz.Rect | None) -> float:
    if bbox is None:
        return 0.0
    r = fitz.Rect(bbox)
    r.y0 = max(page.rect.y0, r.y0 - 30)
    r.y1 = min(page.rect.y1, r.y1 + 90)
    r.x0 = max(page.rect.x0, r.x0 - 15)
    r.x1 = min(page.rect.x1, r.x1 + 15)
    text = page.get_textbox(r)
    bonus = 0.0
    if WORKFLOW_CAPTION_RE.search(text):
        bonus += 35.0
    if FIGURE_ONE_RE.search(text):
        bonus += 20.0
    return bonus


def figure_page_index(doc: fitz.Document) -> int:
    for pno in range(min(len(doc), MAX_PAGES_SCAN)):
        text = doc[pno].get_text()
        if FIGURE_ONE_RE.search(text) or WORKFLOW_CAPTION_RE.search(text):
            return pno
    return 1 if len(doc) > 1 else 0


def shrink_clip_above_caption(page: fitz.Page, bbox: fitz.Rect) -> fitz.Rect:
    """Do not extend crop below the figure into caption / body text."""
    clip = fitz.Rect(bbox)
    caption_y = None
    for block in page.get_text("blocks"):
        if block[6] != 0:
            continue
        block_rect = fitz.Rect(block[:4])
        if block_rect.y0 < clip.y1 - 4:
            continue
        if block_rect.y0 > clip.y1 + 140:
            continue
        if block_rect.x1 <= clip.x0 + 15 or block_rect.x0 >= clip.x1 - 15:
            continue
        caption_y = block_rect.y0 if caption_y is None else min(caption_y, block_rect.y0)
    if caption_y is not None:
        clip.y1 = min(clip.y1, caption_y - 3)
    return clip


def figure_clip_rect(page: fitz.Page, bbox: fitz.Rect) -> fitz.Rect:
    """Tight crop around the figure only (minimal padding, no room for captions)."""
    rect = page.rect
    clip = shrink_clip_above_caption(page, fitz.Rect(bbox))
    pad_x = max(3.0, clip.width * 0.012)
    pad_top = max(3.0, clip.height * 0.015)
    clip.x0 = max(rect.x0, clip.x0 - pad_x)
    clip.x1 = min(rect.x1, clip.x1 + pad_x)
    clip.y0 = max(rect.y0, clip.y0 - pad_top)
    clip.y1 = min(rect.y1, clip.y1)  # never pad below — captions sit under the figure
    if clip.width < 40 or clip.height < 40:
        return fitz.Rect(bbox)
    return clip


def largest_figure_bbox_on_page(page: fitz.Page, page_no: int) -> fitz.Rect | None:
    best: fitz.Rect | None = None
    best_score = -1e9
    try:
        infos = page.get_image_info(xrefs=True)
    except Exception:
        infos = []
    for info in infos:
        bbox = fitz.Rect(info["bbox"])
        w, h = bbox.width, bbox.height
        if w < 80 or h < 60:
            continue
        sc = score_workflow_image(int(w), int(h), page_no, int(w * h))
        if sc > best_score:
            best_score = sc
            best = bbox
    return best


def render_figure_clip(page: fitz.Page, bbox: fitz.Rect | None, page_no: int = 1) -> fitz.Pixmap:
    rect = page.rect
    if bbox is None:
        bbox = largest_figure_bbox_on_page(page, page_no)
    if bbox is not None and bbox.width > 80 and bbox.height > 60:
        clip = figure_clip_rect(page, bbox)
    else:
        y0 = rect.y0 + 60
        y1 = rect.y0 + rect.height * 0.38
        clip = fitz.Rect(rect.x0 + 36, y0, rect.x1 - 36, y1)
    mat = fitz.Matrix(2.0, 2.0)
    return page.get_pixmap(matrix=mat, clip=clip, alpha=False)


def pixmap_from_xref(doc: fitz.Document, xref: int) -> fitz.Pixmap | None:
    try:
        pix = fitz.Pixmap(doc, xref)
        if pix.n - pix.alpha > 3:
            pix = fitz.Pixmap(fitz.csRGB, pix)
        return pix
    except Exception:
        return None


def collect_image_candidates(doc: fitz.Document) -> list[dict]:
    seen_xrefs: set[int] = set()
    candidates: list[dict] = []

    for pno in range(min(len(doc), MAX_PAGES_SCAN)):
        page = doc[pno]
        bboxes_by_xref: dict[int, fitz.Rect] = {}
        try:
            for info in page.get_image_info(xrefs=True):
                xref = info.get("xref")
                if xref:
                    bboxes_by_xref.setdefault(xref, fitz.Rect(info["bbox"]))
        except Exception:
            pass

        for img in page.get_images(full=True):
            xref = img[0]
            if xref in seen_xrefs:
                continue
            seen_xrefs.add(xref)

            pix = pixmap_from_xref(doc, xref)
            if pix is None:
                continue
            w, h = pix.width, pix.height
            area = w * h
            if w < 80 or h < 80:
                continue

            bbox = bboxes_by_xref.get(xref)
            if bbox is None:
                try:
                    rects = page.get_image_rects(xref)
                    if rects:
                        bbox = fitz.Rect(rects[0])
                except Exception:
                    bbox = None

            score = score_workflow_image(w, h, pno, area) + caption_bonus(page, bbox)
            candidates.append(
                {"score": score, "pno": pno, "xref": xref, "pix": pix, "bbox": bbox, "page": page}
            )

    return candidates


def extract_thumbnail(pdf_path: Path, out_path: Path) -> bool:
    try:
        doc = fitz.open(pdf_path)
    except Exception:
        return False

    candidates = collect_image_candidates(doc)
    best_pix: fitz.Pixmap | None = None
    best_score = -1e9

    if candidates:
        cand = max(candidates, key=lambda c: c["score"])
        best_score = cand["score"]
        # Embedded image bytes are usually the figure alone (no PDF caption text).
        best_pix = cand["pix"]
        bbox = cand["bbox"]
        page = cand["page"]
        pno = cand["pno"]
        if bbox is not None:
            bbox_area = bbox.width * bbox.height
            pix_area = cand["pix"].width * cand["pix"].height
            # Re-render only when the on-page placement is much larger than the bitmap
            # (vector figure) or the embedded asset looks like a full-page raster with text.
            if pix_area > bbox_area * 1.8 or (
                cand["score"] < MIN_WORKFLOW_SCORE + 15 and pix_area > 1_200_000
            ):
                try:
                    best_pix = render_figure_clip(page, bbox, pno)
                except Exception:
                    pass
            elif pix_area < bbox_area * 0.45:
                try:
                    best_pix = render_figure_clip(page, bbox, pno)
                except Exception:
                    pass

    if best_score < MIN_WORKFLOW_SCORE or best_pix is None:
        pno = figure_page_index(doc)
        page = doc[pno]
        bbox = largest_figure_bbox_on_page(page, pno)
        if bbox is None and candidates:
            page_hits = [c for c in candidates if c["pno"] == pno]
            if page_hits:
                bbox = max(page_hits, key=lambda c: c["score"]).get("bbox")
        try:
            best_pix = render_figure_clip(page, bbox, pno)
        except Exception:
            best_pix = None

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
