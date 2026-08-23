#!/usr/bin/env python3
"""Regenerate Burak Uzkent's academic CV from the archived LaTeX-typeset PDF.

files/CV.BurakUzkent.pdf.bak is the last CV produced from the original LaTeX
source. Rather than imitating its look, this script lifts the typeset blocks out
of that PDF, reflows them across pages, and sets only the parts that changed
using the Computer Modern fonts embedded in the same document.
"""

from __future__ import annotations

import re
import struct
from pathlib import Path

import fitz
from fontTools import t1Lib
from fontTools.agl import toUnicode
from fontTools.fontBuilder import FontBuilder
from fontTools.pens.recordingPen import RecordingPen
from fontTools.pens.t2CharStringPen import T2CharStringPen

ROOT = Path(__file__).resolve().parents[1]
FILES = ROOT / "files"
ARCHIVE = FILES / "CV.BurakUzkent.pdf.bak"
OUTPUTS = [FILES / "CV.BurakUzkent.pdf", FILES / "Burak_Uzkent_Academic_CV.pdf"]

# --- geometry, all measured from the archived CV ---------------------------
PAGE_W, PAGE_H = 612.0, 792.0
SIZE = 9.96
TITLE_SIZE = 11.96
LEADING = 11.9533
SPACE_RATIO = 0.3333
ASCENT_RATIO = 0.75
LEFT, RIGHT = 43.20, 568.80
LABEL_RIGHT = 53.72
ENTRY_LEFT = 58.70
FULL_LEFT, CLIP_LEFT, CLIP_RIGHT = 30.0, 55.0, 570.0
CLIP_PAD = 3.0
BODY_BOTTOM = 741.0
GROUP_GAP = 13.0
BULLET_ICON_X, BULLET_TEXT_X, BULLET_STEP = 40.50, 51.50, 19.92
BULLET_ICON_RISE = -0.40  # the stamp is clipped 0.5pt above the glyph
ROLE_BODY_GAP = 19.94
GAP_SECTION, GAP_ROLE, GAP_ENTRY = 23.39, 18.45, 13.95
TOP_HEADING, TOP_TITLE, TOP_TEXT = 36.25, 35.20, 38.18

BLUE = (0.0, 0.32158, 0.60783)
TITLE_BLUE = (0.0, 0.2, 0.4)
GRAY = (0.50980, 0.50980, 0.50980)
DARK = (0.23529, 0.23529, 0.23529)
LINK_BLUE = (0.0, 0.47060, 0.78432)
BOX_GRAY = (0.96078, 0.96078, 0.96078)

MASTHEAD_CLIP = fitz.Rect(0, 0, PAGE_W, 70.0)
CONTACT_TOP, CONTACT_TEXT_TOP, CONTACT_ICON_TOP = 73.658, 84.47, 83.72
CONTACT_BOTTOM_PAD, CONTACT_ITEM_GAP = 10.57, 13.27
SUMMARY_GAP = 34.06
HEADER_CLIP = fitz.Rect(470, 0, 580, 14)
FOOTER_CLIP = fitz.Rect(270, 770, 342, PAGE_H)

# Small glyph stamps copied from the archive; FontAwesome's subset cannot be
# addressed by character code, so its icons are reused as clipped artwork.
ICONS = {
    "calendar": (0, fitz.Rect(466.32, 326.60, 475.60, 337.40)),
    "marker": (0, fitz.Rect(495.03, 338.60, 500.75, 349.20)),
    "bullet": (0, fitz.Rect(40.50, 369.30, 48.20, 379.30)),
    "contact_marker": (0, fitz.Rect(80.09, 83.30, 85.80, 94.40)),
    "contact_phone": (0, fitz.Rect(291.37, 83.30, 299.21, 94.40)),
    "contact_mail": (0, fitz.Rect(388.30, 83.30, 398.28, 94.40)),
    "contact_globe": (0, fitz.Rect(523.38, 83.30, 531.93, 94.40)),
}

# The archived subsets are incomplete: CMBX10 has no capital N and CMBX12 no
# lowercase b or f, so each style falls back to its closest sibling.
STYLE_FONTS = {
    "r": ("CMR10",),
    "b": ("CMBX10", "CMBX12"),
    "i": ("CMTI10", "CMR10"),
    "t": ("CMBX12", "CMBX10"),
}
LIGATURES = (("ffi", "\ufb03"), ("ffl", "\ufb04"), ("ff", "\ufb00"), ("fi", "\ufb01"), ("fl", "\ufb02"))
LABEL_RE = re.compile(r"^\[\d+\]$")

CONTACT = [
    ("contact_marker", "Santa Clara, CA", None),
    ("contact_phone", "+1-650-861-8068", None),
    ("contact_mail", "uzkent.burak@gmail.com", "mailto:uzkent.burak@gmail.com"),
    ("contact_globe", "uzkent.github.io", "https://uzkent.github.io"),
]

SUMMARY = [
    ("Principal Member of Technical Staff with", "r"),
    (" 10+ years", "b"),
    (" of experience developing and deploying large-scale machine learning systems. Specialized in", "r"),
    (" generative AI", "b"),
    (",", "r"),
    (" computer vision", "b"),
    (",", "r"),
    (" multi-modal and video-language modeling", "b"),
    (", and efficient", "r"),
    (" transformer architectures", "b"),
    (". Published", "r"),
    (" 40+ papers", "b"),
    (
        " in top-tier venues (CVPR, ICCV, ICLR, NeurIPS, EMNLP, AAAI) across academic research and "
        "industrial applications. Proven track record of leading research initiatives at AMD, Amazon, "
        "Samsung, and Stanford University.",
        "r",
    ),
]

AMD_ROLE = {
    "title": "Principal Member of Technical Staff",
    "dates": "April 2026 \u2013 Present",
    "organisation": "AMD",
    "location": "Santa Clara, CA",
    "bullets": [
        [("Work on applications of", "r"), (" generative AI", "b"), (" on AMD hardware", "r")],
        [("Develop and evaluate ML systems optimized for AMD accelerators and platforms", "r")],
        [("Hiring for full-time positions at all levels", "r")],
    ],
}

AMAZON_DATES = "April 2022 \u2013 March 2026"
AMAZON_LAST_BULLET = [
    ("Published", "r"),
    (" 6 papers", "b"),
    (" (CVPR, WACV, EMNLP, ECCV Workshop) and filed", "r"),
    (" 2 patents", "b"),
    ("; 1 additional paper under review", "r"),
]

ACCEPTED_ENTRIES = [
    [
        ("T. Poppi,", "r"),
        (" B. Uzkent", "b"),
        (
            ", A. Garg, L. Porto, G. Kessler, Y. Yang, M. Cornia, L. Baraldi, R. Cucchiara, "
            "F. Schiffers, \u201cCounterVid: Counterfactual Video Generation for Mitigating Action "
            "and Temporal Hallucinations in Video-Language Models\u201d,",
            "r",
        ),
        (" Conference on Empirical Methods in Natural Language Processing", "i"),
        (",", "r"),
        (" EMNLP-26", "b"),
        (", 2026.", "r"),
    ],
    [
        ("G. Sun, A. Singhal,", "r"),
        (" B. Uzkent", "b"),
        (
            ", M. Shah, C. Chen, G. Kessler, \u201cFrom Frames to Clips: Efficient Key Clip "
            "Selection for Long-Form Video Understanding\u201d,",
            "r",
        ),
        (" European Conference on Computer Vision Workshops", "i"),
        (",", "r"),
        (" ECCVW-26", "b"),
        (", 2026.", "r"),
    ],
    [
        ("R. Jain, K. Doshi,", "r"),
        (" B. Uzkent", "b"),
        (", G. Kessler, \u201cNarrative Aligned Long Form Video Question Answering\u201d,", "r"),
        (" IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops", "i"),
        (",", "r"),
        (" CVPRW-26", "b"),
        (", 2026. (Best Paper Candidate)", "r"),
    ],
]

REVIEW_ENTRY = [
    ("A. Blume,", "r"),
    (" B. Uzkent", "b"),
    (
        ", S. Chaudhuri, G. Kessler, \u201cLearning to Rank Caption Chains for "
        "Video-Text Alignment\u201d,",
        "r",
    ),
    (" European Conference on Computer Vision", "i"),
    (",", "r"),
    (" ECCV-26", "b"),
    (".", "r"),
]


# --- paper PDF links -------------------------------------------------------
PUBLICATIONS_MD = ROOT / "_pages" / "publications.md"
LIGATURE_TEXT = {"\ufb00": "ff", "\ufb01": "fi", "\ufb02": "fl", "\ufb03": "ffi", "\ufb04": "ffl"}
TITLE_RE = re.compile(r"\u201c(.+?)\u201d")
PDF_LABEL_PRIORITY = ("PDF", "arXiv")
PDF_MATCH_THRESHOLD = 0.6

# A few CV entries were retitled after the website listing; these map the CV
# title to the website record for the same paper (verified by author list).
PDF_TITLE_ALIASES = {
    "efficientpovertymappingfromhighresolutionremotesensingimages":
        "efficienthighresolutionimageprocessingusingdeepreinforcementlearning",
    "predictinglivelihoodindicatorsfromcommunitygeneratedstreetlevelimagery":
        "predictinggeoattributesusingdeeplearningandpubliclyavailablestreetlevelimages",
}


def _normalize_title(text: str) -> str:
    for ligature, plain in LIGATURE_TEXT.items():
        text = text.replace(ligature, plain)
    return re.sub(r"[^a-z0-9]", "", text.lower())


def _title_tokens(text: str) -> set:
    for ligature, plain in LIGATURE_TEXT.items():
        text = text.replace(ligature, plain)
    return set(re.sub(r"[^a-z0-9 ]", " ", text.lower()).split())


def load_pdf_records() -> list[dict]:
    """Read the website publication list into (title, tokens, url) records.

    The CV reuses the same links the website exposes; for each paper we take the
    PDF link, falling back to arXiv, so every entry points at a readable copy.
    """
    if not PUBLICATIONS_MD.exists():
        return []
    markup = PUBLICATIONS_MD.read_text(encoding="utf-8")
    records: list[dict] = []
    for chunk in markup.split('<div class="paper">')[1:]:
        title_match = re.search(r'<div class="paper-title">(.*?)</div>', chunk, re.S)
        if not title_match:
            continue
        title = re.sub(r"<.*?>", "", title_match.group(1)).strip()
        links_match = re.search(r'<div class="paper-links">(.*?)</div>', chunk, re.S)
        pairs = re.findall(r'<a href="([^"]+)"[^>]*>([^<]+)</a>', links_match.group(1)) if links_match else []
        labelled: dict[str, str] = {}
        for url, label in pairs:
            labelled.setdefault(label.strip(), url)
        url = next((labelled[label] for label in PDF_LABEL_PRIORITY if label in labelled), None)
        if url:
            records.append({"key": _normalize_title(title), "tokens": _title_tokens(title), "url": url})
    return records


def resolve_pdf_url(title: str, records: list[dict]) -> str | None:
    key = _normalize_title(title)
    key = PDF_TITLE_ALIASES.get(key, key)
    for record in records:
        if record["key"] == key:
            return record["url"]
    wanted = _title_tokens(title)
    best, score = None, 0.0
    for record in records:
        overlap = len(wanted & record["tokens"]) / max(1, len(wanted | record["tokens"]))
        if overlap > score:
            best, score = record, overlap
    return best["url"] if best and score >= PDF_MATCH_THRESHOLD else None


def entry_title(text: str) -> str:
    match = TITLE_RE.search(text)
    return match.group(1) if match else ""


# --- fonts and typesetting -------------------------------------------------
CID_FONTS = ("CMR10", "CMBX10", "CMBX12", "CMTI10")
LIGATURE_CODEPOINTS = {"ff": 0xFB00, "fi": 0xFB01, "fl": 0xFB02, "ffi": 0xFB03, "ffl": 0xFB04}


def _type1_to_pfb(buffer: bytes) -> bytes:
    """Wrap MuPDF's raw Type1 program (binary eexec, no trailer) as a PFB."""
    cut = buffer.find(b"eexec") + len("eexec")
    while cut < len(buffer) and buffer[cut] in b"\r\n\t ":
        cut += 1
    ascii_part, binary_part = buffer[:cut], buffer[cut:]
    trailer = b"\n" + (b"0" * 64 + b"\n") * 8 + b"cleartomark\n"

    def segment(marker: int, data: bytes) -> bytes:
        return b"\x80" + bytes([marker]) + struct.pack("<I", len(data)) + data

    return segment(1, ascii_part) + segment(2, binary_part) + segment(1, trailer) + b"\x80\x03"


def _to_opentype(buffer: bytes, family: str) -> bytes:
    """Convert an extracted Type1 subset to a CFF OpenType font.

    MuPDF embeds fonts inserted from a Type1 buffer as Identity-H CID fonts that
    only MuPDF reads back; other viewers (Preview, browsers) scramble the glyphs.
    Re-expressing the same outlines as an OpenType font with a real Unicode cmap
    makes the text render and copy correctly everywhere.
    """
    import io
    import tempfile

    with tempfile.NamedTemporaryFile(suffix=".pfb", delete=False) as handle:
        handle.write(_type1_to_pfb(buffer))
        pfb_path = handle.name
    try:
        font = t1Lib.T1Font(pfb_path)
        font.parse()
        glyphs = font.getGlyphSet()
        order = [".notdef"] + [name for name in glyphs.keys() if name != ".notdef"]

        charstrings: dict[str, object] = {}
        widths: dict[str, int] = {}
        for name in order:
            glyph = glyphs[name]
            record = RecordingPen()
            try:
                glyph.draw(record)
            except Exception:
                record.value = []
            width = int(getattr(glyph, "width", 0) or 0)
            pen = T2CharStringPen(width, glyphs)
            record.replay(pen)
            charstrings[name] = pen.getCharString()
            widths[name] = width

        cmap: dict[int, str] = {}
        for name in order:
            text = toUnicode(name)
            if len(text) == 1:
                cmap.setdefault(ord(text), name)
        for ligature, codepoint in LIGATURE_CODEPOINTS.items():
            if ligature in glyphs:
                cmap[codepoint] = ligature

        builder = FontBuilder(1000, isTTF=False)
        builder.setupGlyphOrder(order)
        builder.setupCharacterMap(cmap)
        builder.setupCFF(family, {"FullName": family, "Weight": "Regular"}, charstrings, {})
        builder.setupHorizontalMetrics({name: (widths[name], 0) for name in order})
        builder.setupHorizontalHeader(ascent=750, descent=-250)
        builder.setupNameTable({"familyName": family, "styleName": "Regular"})
        builder.setupOS2(sTypoAscender=750, sTypoDescender=-250)
        builder.setupPost()
        with io.BytesIO() as out:
            builder.font.save(out)
            return out.getvalue()
    finally:
        Path(pfb_path).unlink(missing_ok=True)


def load_cm_fonts(source: fitz.Document) -> dict[str, tuple[bytes, fitz.Font]]:
    """Extract the Computer Modern fonts, converting the ones we typeset with.

    Fonts used only as copied artwork keep their raw Type1 buffer; the four we
    feed to insert_text are converted to OpenType so every PDF viewer renders
    the freshly typeset text.
    """
    raw: dict[str, bytes] = {}
    for number in range(source.page_count):
        for item in source.get_page_fonts(number, full=True):
            name = item[3].split("+")[-1]
            if name not in raw:
                raw[name] = source.extract_font(item[0])[3]

    fonts: dict[str, tuple[bytes, fitz.Font]] = {}
    for name, buffer in raw.items():
        if name in CID_FONTS:
            buffer = _to_opentype(buffer, name)
        fonts[name] = (buffer, fitz.Font(fontbuffer=buffer))
    return fonts


def register_fonts(page: fitz.Page, fonts: dict) -> None:
    for name in CID_FONTS:
        page.insert_font(fontname=name, fontbuffer=fonts[name][0])


def ligate(word: str, fonts: dict, candidates: tuple[str, ...]) -> str:
    def available(char: str) -> bool:
        return any(fonts[name][1].has_glyph(ord(char)) for name in candidates)

    result: list[str] = []
    index = 0
    while index < len(word):
        for plain, ligature in LIGATURES:
            if word.startswith(plain, index) and available(ligature):
                result.append(ligature)
                index += len(plain)
                break
        else:
            result.append(word[index])
            index += 1
    return "".join(result)


def style_runs(word: str, style: str, fonts: dict) -> list[tuple[str, str]]:
    candidates = STYLE_FONTS[style]
    runs: list[list[str]] = []
    for char in ligate(word, fonts, candidates):
        chosen = next((n for n in candidates if fonts[n][1].has_glyph(ord(char))), candidates[0])
        if runs and runs[-1][1] == chosen:
            runs[-1][0] += char
        else:
            runs.append([char, chosen])
    return [(text, name) for text, name in runs]


def tokenize(fragments, fonts: dict, size: float = SIZE) -> list[dict]:
    tokens: list[dict] = []
    pending_space = False
    for text, style in fragments:
        if not text:
            continue
        leading_space = text.startswith(" ")
        words = text.split()
        for index, word in enumerate(words):
            spaced = True if index else (pending_space or leading_space)
            runs = style_runs(word, style, fonts)
            width = sum(fonts[name][1].text_length(run, size) for run, name in runs)
            tokens.append({"runs": runs, "width": width, "space": spaced})
        pending_space = text.endswith(" ") if words else pending_space
    return tokens


def wrap_tokens(tokens: list[dict], width: float, size: float = SIZE) -> list[list[dict]]:
    """Break tokens into lines, minimising stretched word spacing as TeX does."""
    space = SPACE_RATIO * size
    count = len(tokens)
    cost = [float("inf")] * (count + 1)
    follow = [count] * (count + 1)
    cost[count] = 0.0
    for start in range(count - 1, -1, -1):
        used = 0.0
        gaps = 0
        for end in range(start, count):
            token = tokens[end]
            if end > start and token["space"]:
                used += space
                gaps += 1
            used += token["width"]
            if used > width and end > start:
                break
            if end == count - 1:
                penalty = 0.0
            elif not gaps:
                penalty = float("inf")
            else:
                penalty = ((width - used) / gaps) ** 3
            total = cost[end + 1] + penalty
            if total < cost[start]:
                cost[start] = total
                follow[start] = end + 1
    lines: list[list[dict]] = []
    start = 0
    while start < count:
        lines.append(tokens[start:follow[start]])
        start = follow[start]
    return lines


def compose(fragments, fonts: dict, width: float, size: float = SIZE) -> list[list[dict]]:
    return wrap_tokens(tokenize(fragments, fonts, size), width, size)


def text_width(fragments, fonts: dict, size: float = SIZE) -> float:
    tokens = tokenize(fragments, fonts, size)
    space = SPACE_RATIO * size
    return sum(t["width"] for t in tokens) + space * sum(1 for t in tokens[1:] if t["space"])


def draw_lines(page, fonts, lines, left, width, top, size=SIZE, color=(0, 0, 0)) -> None:
    space = SPACE_RATIO * size
    for index, line in enumerate(lines):
        baseline = top + index * LEADING + ASCENT_RATIO * size
        gaps = sum(1 for token in line[1:] if token["space"])
        ink = sum(token["width"] for token in line)
        gap = (width - ink) / gaps if gaps and index < len(lines) - 1 else space
        x = left
        for position, token in enumerate(line):
            if position and token["space"]:
                x += gap
            for run, name in token["runs"]:
                page.insert_text((x, baseline), run, fontname=name, fontsize=size, color=color)
                x += fonts[name][1].text_length(run, size)


# --- block model -----------------------------------------------------------
def copy_element(source_page: int, clip: fitz.Rect, top: float) -> dict:
    return {"kind": "copy", "page": source_page, "clip": clip, "rel": clip.y0 - top}


def place_block(page: fitz.Page, source: fitz.Document, fonts: dict, block: dict, top: float) -> None:
    for element in block["elements"]:
        y = top + element["rel"]
        kind = element["kind"]
        if kind == "copy":
            clip = element["clip"]
            dy = y - clip.y0
            page.show_pdf_page(clip + (0, dy, 0, dy), source, element["page"], clip=clip)
            for link in source[element["page"]].get_links():
                box = link["from"]
                if link.get("uri") and clip.y0 <= box.y0 and box.y1 <= clip.y1:
                    page.insert_link({"kind": link["kind"], "uri": link["uri"], "from": box + (0, dy, 0, dy)})
        elif kind == "stamp":
            clip = ICONS[element["icon"]][1]
            page.show_pdf_page(
                fitz.Rect(element["x"], y, element["x"] + clip.width, y + clip.height),
                source,
                ICONS[element["icon"]][0],
                clip=clip,
            )
        elif kind == "lines":
            draw_lines(
                page,
                fonts,
                element["lines"],
                element["left"],
                element["width"],
                y,
                element.get("size", SIZE),
                element.get("color", (0, 0, 0)),
            )
        elif kind == "text":
            size = element.get("size", SIZE)
            width = text_width(element["fragments"], fonts, size)
            left = element["x"] - width if element.get("align") == "right" else element["x"]
            draw_lines(page, fonts, compose(element["fragments"], fonts, width + 1, size),
                       left, width, y, size, element.get("color", (0, 0, 0)))
        elif kind == "label":
            label = f"[{element['number']}]"
            width = fonts["CMR10"][1].text_length(label, SIZE)
            page.insert_text((LABEL_RIGHT - width, y + ASCENT_RATIO * SIZE), label,
                             fontname="CMR10", fontsize=SIZE, color=BLUE)
        elif kind == "rect":
            page.draw_rect(fitz.Rect(element["x0"], y, element["x1"], y + element["height"]),
                           color=None, fill=element["fill"])
        elif kind == "link":
            page.insert_link({"kind": fitz.LINK_URI, "uri": element["uri"],
                              "from": fitz.Rect(element["x0"], y, element["x1"], y + element["height"])})


def page_lines(page: fitz.Page) -> list[dict]:
    lines = [
        line
        for block in page.get_text("dict")["blocks"]
        if block.get("type") == 0
        for line in block["lines"]
        if 20 < line["bbox"][1] < 760
    ]
    lines.sort(key=lambda line: (round(line["bbox"][1], 1), line["bbox"][0]))
    return lines


def block_kind(lines: list[dict]) -> str:
    first = lines[0]["spans"][0]
    if first["size"] > 13:
        return "heading"
    if LABEL_RE.match(first["text"].strip()) and first["bbox"][2] <= LABEL_RIGHT + 1:
        return "entry"
    return "other"


def parse_blocks(source: fitz.Document) -> list[dict]:
    """Group each archived page into blocks that can be moved as a unit."""
    blocks: list[dict] = []
    for number in range(source.page_count):
        lines = [line for line in page_lines(source[number])
                 if not (number == 0 and line["bbox"][1] < 120)]
        groups: list[dict] = []
        for line in lines:
            top, bottom = line["bbox"][1], line["bbox"][3]
            if groups and top - groups[-1]["bottom"] <= GROUP_GAP:
                groups[-1]["lines"].append(line)
                groups[-1]["bottom"] = max(groups[-1]["bottom"], bottom)
            else:
                groups.append({"lines": [line], "top": top, "bottom": bottom})

        for drawing in source[number].get_drawings():
            rect = drawing["rect"]
            if number == 0 and rect.y1 < 130:
                continue
            distances = [
                (max(group["top"] - rect.y1, rect.y0 - group["bottom"], 0.0), group)
                for group in groups
            ]
            distance, group = min(distances, key=lambda item: item[0])
            if distance <= 20:
                group["top"] = min(group["top"], rect.y0)
                group["bottom"] = max(group["bottom"], rect.y1)

        for index, group in enumerate(groups):
            top, bottom = group["top"], group["bottom"]
            text = " ".join("".join(s["text"] for s in line["spans"]) for line in group["lines"])
            clip = fitz.Rect(FULL_LEFT, top - CLIP_PAD, CLIP_RIGHT, bottom + CLIP_PAD)
            block = {
                "kind": block_kind(group["lines"]),
                "text": text,
                "height": bottom - top,
                "gap": top - groups[index - 1]["bottom"] if index else None,
                "keep": any(span["size"] >= 11.9 for line in group["lines"] for span in line["spans"]),
                "top_size": max(span["size"] for span in group["lines"][0]["spans"]),
                "elements": [copy_element(number, clip, top)],
            }
            if block["kind"] == "entry":
                last = group["lines"][-1]["spans"]
                block["pdf_src"] = {
                    "page": number,
                    "src_top": top,
                    "right": max(span["bbox"][2] for span in last),
                    "baseline": max(span["origin"][1] for span in last),
                }
            blocks.append(block)
    return blocks


def find_block(blocks: list[dict], needle: str, start: int = 0) -> int:
    for index in range(start, len(blocks)):
        if needle in blocks[index]["text"]:
            return index
    raise SystemExit(f"Could not find {needle!r} in the archived CV")


# --- the parts of the CV that changed --------------------------------------
def summary_block(fonts: dict) -> dict:
    left, width = 56.99, 498.07
    inset_top, inset_bottom, border = 10.94, 11.56, 0.996
    lines = compose(SUMMARY, fonts, width)
    height = inset_top + (len(lines) - 1) * LEADING + SIZE + inset_bottom
    return {
        "kind": "other",
        "text": "professional summary",
        "height": height,
        "gap": 15.94,
        "keep": False,
        "top_size": SIZE,
        "elements": [
            {"kind": "rect", "rel": 0.0, "x0": LEFT, "x1": 568.806, "height": height, "fill": BLUE},
            {"kind": "rect", "rel": border, "x0": LEFT + border, "x1": 568.806 - border,
             "height": height - 2 * border, "fill": BOX_GRAY},
            {"kind": "lines", "rel": inset_top, "lines": lines, "left": left, "width": width},
        ],
    }


def role_header_block(fonts: dict, role: dict) -> dict:
    return {
        "kind": "other",
        "text": role["title"],
        "height": 23.48,
        "gap": GAP_ROLE,
        "keep": True,
        "top_size": TITLE_SIZE,
        "elements": [
            {"kind": "text", "rel": 0.0, "x": LEFT, "size": TITLE_SIZE, "color": TITLE_BLUE,
             "fragments": [(role["title"], "t")]},
            {"kind": "stamp", "rel": 0.32, "icon": "calendar",
             "x": RIGHT - text_width([(role["dates"], "r")], fonts) - SPACE_RATIO * SIZE
                  - ICONS["calendar"][1].width},
            {"kind": "text", "rel": 1.56, "x": RIGHT, "align": "right", "color": GRAY,
             "fragments": [(role["dates"], "r")]},
            {"kind": "text", "rel": 13.52, "x": LEFT, "color": DARK,
             "fragments": [(role["organisation"], "i")]},
            {"kind": "stamp", "rel": 12.32, "icon": "marker",
             "x": RIGHT - text_width([(role["location"], "r")], fonts) - SPACE_RATIO * SIZE
                  - ICONS["marker"][1].width},
            {"kind": "text", "rel": 13.52, "x": RIGHT, "align": "right", "color": GRAY,
             "fragments": [(role["location"], "r")]},
        ],
    }


def bullets_block(fonts: dict, bullets: list) -> dict:
    elements = []
    top = 0.0
    for fragments in bullets:
        lines = compose(fragments, fonts, RIGHT - BULLET_TEXT_X)
        elements.append({"kind": "stamp", "rel": top + BULLET_ICON_RISE, "icon": "bullet", "x": BULLET_ICON_X})
        elements.append({
            "kind": "lines", "rel": top, "left": BULLET_TEXT_X, "width": RIGHT - BULLET_TEXT_X,
            "lines": lines,
        })
        top += (len(lines) - 1) * LEADING + BULLET_STEP
    return {
        "kind": "other",
        "text": "bullets",
        "height": top - BULLET_STEP + SIZE,
        "gap": ROLE_BODY_GAP,
        "keep": False,
        "top_size": SIZE,
        "elements": elements,
    }


def entry_block(fonts: dict, fragments: list, number: int) -> dict:
    lines = compose(fragments, fonts, RIGHT - ENTRY_LEFT)
    return {
        "kind": "entry",
        "text": "".join(text for text, _ in fragments),
        "height": (len(lines) - 1) * LEADING + SIZE,
        "gap": GAP_ENTRY,
        "keep": False,
        "top_size": SIZE,
        "pdf_typeset": True,
        "elements": [
            {"kind": "label", "rel": 0.0, "number": number},
            {"kind": "lines", "rel": 0.0, "lines": lines, "left": ENTRY_LEFT,
             "width": RIGHT - ENTRY_LEFT},
        ],
    }


def patch_amazon(blocks: list[dict], fonts: dict) -> None:
    """Amazon's dates and publication tally changed; the rest is reused as set."""
    header = find_block(blocks, "Amazon Prime Video")
    top = 326.28
    blocks[header]["elements"] = [
        copy_element(0, fitz.Rect(FULL_LEFT, top - CLIP_PAD, 440.0, 352.8), top),
        copy_element(0, fitz.Rect(440.0, 338.4, CLIP_RIGHT, 352.8), top),
        {"kind": "stamp", "rel": 0.32, "icon": "calendar",
         "x": RIGHT - text_width([(AMAZON_DATES, "r")], fonts) - SPACE_RATIO * SIZE
              - ICONS["calendar"][1].width},
        {"kind": "text", "rel": 1.56, "x": RIGHT, "align": "right", "color": GRAY,
         "fragments": [(AMAZON_DATES, "r")]},
    ]

    bullets = header + 1
    bullet_top, last_top = 369.70, 429.47
    lines = compose(AMAZON_LAST_BULLET, fonts, RIGHT - BULLET_TEXT_X)
    blocks[bullets]["elements"] = [
        copy_element(0, fitz.Rect(FULL_LEFT, bullet_top - CLIP_PAD, CLIP_RIGHT, 419.51 + CLIP_PAD), bullet_top),
        {"kind": "stamp", "rel": last_top - bullet_top + BULLET_ICON_RISE, "icon": "bullet",
         "x": BULLET_ICON_X},
        {"kind": "lines", "rel": last_top - bullet_top, "left": BULLET_TEXT_X,
         "width": RIGHT - BULLET_TEXT_X, "lines": lines},
    ]
    blocks[bullets]["height"] = (last_top - bullet_top) + (len(lines) - 1) * LEADING + SIZE


def renumber_conference(blocks: list[dict], fonts: dict) -> None:
    """Accepted papers join the conference list, so every entry is renumbered."""
    start = find_block(blocks, "REFEREED CONFERENCE PUBLICATIONS") + 1
    end = start
    while end < len(blocks) and blocks[end]["kind"] == "entry":
        end += 1

    number = len(ACCEPTED_ENTRIES)
    for block in blocks[start:end]:
        number += 1
        element = block["elements"][0]
        element["clip"] = fitz.Rect(CLIP_LEFT, element["clip"].y0, CLIP_RIGHT, element["clip"].y1)
        block["elements"] = [{"kind": "label", "rel": 0.0, "number": number}] + block["elements"]

    accepted = [entry_block(fonts, fragments, index + 1)
                for index, fragments in enumerate(ACCEPTED_ENTRIES)]
    accepted[0]["gap"] = blocks[start]["gap"]
    blocks[start]["gap"] = GAP_ENTRY
    blocks[start:start] = accepted


def patch_review_entries(blocks: list[dict], fonts: dict) -> None:
    """Two of the three papers under review were accepted and moved up."""
    start = find_block(blocks, "PAPERS UNDER REVIEW") + 1
    end = start
    while end < len(blocks) and blocks[end]["kind"] == "entry":
        end += 1
    replacement = entry_block(fonts, REVIEW_ENTRY, 1)
    replacement["gap"] = blocks[start]["gap"]
    blocks[start:end] = [replacement]


def apply_updates(blocks: list[dict], fonts: dict) -> list[dict]:
    summary = find_block(blocks, "Senior Machine Learning Scientist with")
    blocks[summary] = summary_block(fonts)

    patch_amazon(blocks, fonts)
    amazon = find_block(blocks, "Amazon Prime Video")
    header = role_header_block(fonts, AMD_ROLE)
    header["gap"], blocks[amazon]["gap"] = blocks[amazon]["gap"], GAP_ROLE
    blocks[amazon:amazon] = [header, bullets_block(fonts, AMD_ROLE["bullets"])]

    renumber_conference(blocks, fonts)
    patch_review_entries(blocks, fonts)

    records = load_pdf_records()
    width = fonts["CMBX10"][1].text_length("[PDF]", SIZE)
    space = SPACE_RATIO * SIZE
    for block in blocks:
        if block["kind"] != "entry":
            continue
        block["pdf_url"] = resolve_pdf_url(entry_title(block["text"]), records)
        if block["pdf_url"]:
            block["pdf_newline"] = entry_last_right(block, fonts) + space + width > RIGHT + 1.0
            if block["pdf_newline"]:
                block["height"] += LEADING
    return blocks


# --- page assembly ---------------------------------------------------------
def place_masthead(page: fitz.Page, source: fitz.Document, fonts: dict) -> float:
    page.show_pdf_page(MASTHEAD_CLIP, source, 0, clip=MASTHEAD_CLIP)

    widths = [text_width([(label, "r")], fonts) for _, label, _ in CONTACT]
    icons = [ICONS[name][1].width for name, _, _ in CONTACT]
    space = SPACE_RATIO * SIZE
    total = sum(widths) + sum(icons) + len(CONTACT) * space + (len(CONTACT) - 1) * CONTACT_ITEM_GAP
    bottom = CONTACT_TEXT_TOP + SIZE + CONTACT_BOTTOM_PAD
    page.draw_rect(fitz.Rect(LEFT, CONTACT_TOP, 568.806, bottom), color=None, fill=BOX_GRAY)

    x = (PAGE_W - total) / 2
    for (icon, label, uri), width, icon_width in zip(CONTACT, widths, icons):
        clip = ICONS[icon][1]
        page.show_pdf_page(
            fitz.Rect(x, CONTACT_ICON_TOP - 0.42, x + icon_width, CONTACT_ICON_TOP - 0.42 + clip.height),
            source, ICONS[icon][0], clip=clip,
        )
        x += icon_width + space
        colour = LINK_BLUE if uri else DARK
        draw_lines(page, fonts, compose([(label, "r")], fonts, width + 1), x, width,
                   CONTACT_TEXT_TOP, SIZE, colour)
        if uri:
            page.insert_link({"kind": fitz.LINK_URI, "uri": uri,
                              "from": fitz.Rect(x, CONTACT_ICON_TOP, x + width, CONTACT_TEXT_TOP + SIZE)})
        x += width + CONTACT_ITEM_GAP
    return bottom


def decorate(page: fitz.Page, source: fitz.Document, fonts: dict, number: int) -> None:
    if number > 1:
        page.show_pdf_page(HEADER_CLIP, source, 1, clip=HEADER_CLIP)
    if number <= source.page_count:
        page.show_pdf_page(FOOTER_CLIP, source, number - 1, clip=FOOTER_CLIP)
    else:
        label = f"Page {number}"
        width = fonts["CMR10"][1].text_length(label, 8.97)
        page.insert_text(((PAGE_W - width) / 2, 778.88 + ASCENT_RATIO * 8.97), label,
                         fontname="CMR10", fontsize=8.97, color=GRAY)


def gap_before(previous: dict, block: dict) -> float:
    if block["gap"] is not None:
        return block["gap"]
    if block["kind"] == "heading":
        return GAP_SECTION
    if block["kind"] == "entry" and previous["kind"] == "entry":
        return GAP_ENTRY
    return GAP_ROLE


def page_top(block: dict) -> float:
    if block["kind"] == "heading":
        return TOP_HEADING
    return TOP_TITLE if block["top_size"] >= 11.0 else TOP_TEXT


def chain_height(blocks: list[dict], index: int) -> float:
    """Height of a block plus everything that must stay with it."""
    height = blocks[index]["height"]
    position = index
    while blocks[position]["keep"] and position + 1 < len(blocks):
        height += gap_before(blocks[position], blocks[position + 1]) + blocks[position + 1]["height"]
        position += 1
    return height


def entry_last_right(block: dict, fonts: dict) -> float:
    """Right edge of an entry's last typeset line, in its own coordinate frame."""
    if block.get("pdf_typeset"):
        element = next(item for item in block["elements"] if item["kind"] == "lines")
        line = element["lines"][-1]
        gaps = sum(1 for token in line[1:] if token["space"])
        ink = sum(token["width"] for token in line)
        return element["left"] + ink + SPACE_RATIO * SIZE * gaps
    return block["pdf_src"]["right"]


def draw_pdf_link(page: fitz.Page, fonts: dict, block: dict, top: float) -> None:
    """Append a blue "[PDF]" hyperlink to a paper entry.

    Styled like the archived "[Code]" links (CMBX10 at body size, link blue).
    It follows the last line where there is room, otherwise sits right-aligned on
    its own line just beneath the entry.
    """
    if block.get("pdf_typeset"):
        element = next(item for item in block["elements"] if item["kind"] == "lines")
        last_baseline = top + (len(element["lines"]) - 1) * LEADING + ASCENT_RATIO * SIZE
    else:
        source = block["pdf_src"]
        last_baseline = source["baseline"] + (top - source["src_top"])

    label = "[PDF]"
    width = fonts["CMBX10"][1].text_length(label, SIZE)
    if block.get("pdf_newline"):
        start = RIGHT - width
        baseline = last_baseline + LEADING
    else:
        start = entry_last_right(block, fonts) + SPACE_RATIO * SIZE
        baseline = last_baseline

    x = start
    for run, name in style_runs(label, "b", fonts):
        page.insert_text((x, baseline), run, fontname=name, fontsize=SIZE, color=LINK_BLUE)
        x += fonts[name][1].text_length(run, SIZE)
    page.insert_link({
        "kind": fitz.LINK_URI,
        "uri": block["pdf_url"],
        "from": fitz.Rect(start - 1.0, baseline - ASCENT_RATIO * SIZE - 0.7, x + 1.0, baseline + 2.5),
    })


def build_document() -> fitz.Document:
    source = fitz.open(ARCHIVE)
    fonts = load_cm_fonts(source)
    blocks = apply_updates(parse_blocks(source), fonts)

    out = fitz.open()
    out.new_page(width=PAGE_W, height=PAGE_H)
    layout: list[tuple[int, dict, float]] = []

    index_page = 0
    register_fonts(out[0], fonts)
    cursor = place_masthead(out[0], source, fonts) + SUMMARY_GAP
    for index, block in enumerate(blocks):
        top = cursor if not index else cursor + gap_before(blocks[index - 1], block)
        if index and top + chain_height(blocks, index) > BODY_BOTTOM:
            index_page += 1
            out.new_page(width=PAGE_W, height=PAGE_H)
            register_fonts(out[index_page], fonts)
            top = page_top(block)
        layout.append((index_page, block, top))
        cursor = top + block["height"]

    for number in range(out.page_count):
        decorate(out[number], source, fonts, number + 1)
    for index_page, block, top in layout:
        place_block(out[index_page], source, fonts, block, top)
        if block.get("pdf_url"):
            draw_pdf_link(out[index_page], fonts, block, top)

    source.close()
    return out


def fix_hyphen_mapping(document: fitz.Document) -> None:
    """Newly set text maps the Computer Modern hyphen to U+00AD; make it copy as "-"."""
    for xref in range(1, document.xref_length()):
        if not document.xref_is_stream(xref):
            continue
        stream = document.xref_stream(xref)
        if b"beginbfchar" in stream and b"<00ad>" in stream:
            document.update_stream(xref, stream.replace(b"<00ad>", b"<002d>"))


def main() -> None:
    if not ARCHIVE.exists():
        raise SystemExit(f"Missing archived CV: {ARCHIVE}")
    document = build_document()
    fix_hyphen_mapping(document)
    for path in OUTPUTS:
        document.save(path, garbage=4, deflate=True)
    document.close()
    print(f"Wrote: {', '.join(str(path) for path in OUTPUTS)}")


if __name__ == "__main__":
    main()
