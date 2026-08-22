#!/usr/bin/env python3
"""Regenerate Burak Uzkent academic CV PDF (pages 1-2) and merge with prior pages 3-6."""

from __future__ import annotations

import fitz
import re
from fpdf import FPDF
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FILES = ROOT / "files"
SOURCE = FILES / "CV.BurakUzkent.pdf"
ARCHIVE = FILES / "CV.BurakUzkent.pdf.bak"
OUTPUTS = [FILES / "CV.BurakUzkent.pdf", FILES / "Burak_Uzkent_Academic_CV.pdf"]
TEMP = FILES / "_cv_pages_1_2.pdf"


class CVPDF(FPDF):
    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 9)
        self.set_text_color(100, 100, 100)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")


def add_heading(pdf: CVPDF, title: str):
    pdf.ln(2)
    pdf.set_font("Helvetica", "B", 11)
    pdf.set_text_color(0, 80, 160)
    pdf.cell(pdf.epw, 7, title, new_x="LMARGIN", new_y="NEXT")
    pdf.set_draw_color(0, 80, 160)
    pdf.line(pdf.l_margin, pdf.get_y(), pdf.w - pdf.r_margin, pdf.get_y())
    pdf.ln(3)


def write_wrapped(pdf: FPDF, text: str, line_h: float = 5, style: str = "") -> None:
    pdf.set_x(pdf.l_margin)
    if style == "bold":
        pdf.set_font("Helvetica", "B", 10.5)
    elif style == "italic":
        pdf.set_font("Helvetica", "I", 9.5)
    else:
        pdf.set_font("Helvetica", "", 9.5)
    pdf.multi_cell(pdf.epw, line_h, text)


def add_role(
    pdf: CVPDF,
    role: str,
    dates: str,
    org: str,
    location: str,
    bullets: list[str],
):
    pdf.set_text_color(20, 20, 20)
    write_wrapped(pdf, role, line_h=5.5, style="bold")
    pdf.set_text_color(80, 80, 80)
    write_wrapped(pdf, dates, line_h=4.8, style="italic")
    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(0, 80, 160)
    write_wrapped(pdf, f"{org}  |  {location}", line_h=5)
    pdf.set_text_color(30, 30, 30)
    pdf.set_font("Helvetica", "", 9.5)
    for bullet in bullets:
        pdf.set_x(pdf.l_margin)
        pdf.multi_cell(pdf.epw, 4.8, f"- {bullet}")
    pdf.ln(1.5)


def build_pages_1_2() -> None:
    pdf = CVPDF()
    pdf.set_margins(18, 18, 18)
    pdf.set_auto_page_break(auto=True, margin=20)
    pdf.add_page()

    pdf.set_font("Helvetica", "B", 16)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(pdf.epw, 9, "BURAK UZKENT, Ph.D.", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "", 9.5)
    pdf.set_text_color(50, 50, 50)
    pdf.set_x(pdf.l_margin)
    pdf.multi_cell(
        pdf.epw,
        4.8,
        "Santa Clara, CA  |  +1-650-861-8068  |  uzkent.burak@gmail.com  |  uzkent.github.io",
    )
    pdf.ln(2)

    add_heading(pdf, "PROFESSIONAL SUMMARY")
    pdf.set_font("Helvetica", "", 9.8)
    pdf.set_text_color(30, 30, 30)
    pdf.set_x(pdf.l_margin)
    pdf.multi_cell(
        pdf.epw,
        5,
        (
            "Principal Member of Technical Staff with 10+ years of experience developing and deploying "
            "large-scale machine learning systems. Specialized in generative AI, computer vision, "
            "multimodal and video-language modeling, and efficient transformer architectures. "
            "Published 40+ papers in top-tier venues (CVPR, ICCV, ICLR, NeurIPS, AAAI, EMNLP) "
            "with extensive experience in both academic research and industrial applications. "
            "Proven track record of leading research initiatives at AMD, Amazon, Samsung, and Stanford University."
        ),
    )

    add_heading(pdf, "PROFESSIONAL EXPERIENCE")
    add_role(
        pdf,
        "Principal Member of Technical Staff",
        "April 2026 - Present",
        "AMD",
        "Santa Clara, CA",
        [
            "Work on applications of Generative AI on AMD hardware",
            "Develop and evaluate ML systems optimized for AMD accelerators and platforms",
            "Hiring for full-time positions at all levels",
        ],
    )
    add_role(
        pdf,
        "Machine Learning Scientist",
        "April 2022 - March 2026",
        "Amazon Prime Video",
        "Sunnyvale, CA",
        [
            "Led development of Video LLMs for advanced video understanding and content moderation in long-form videos",
            "Designed and implemented multimodal foundation models for video summarization pipeline",
            "Developed transformer-based NLP models for subtitle analysis enabling automated content moderation at scale",
            "Published papers at CVPR, WACV, and EMNLP; ECCV workshop paper accepted; filed multiple patents",
        ],
    )
    add_role(
        pdf,
        "Senior Research Scientist",
        "November 2020 - April 2022",
        "Samsung Research America",
        "Mountain View, CA",
        [
            "Optimized vision transformer architectures achieving significant model compression while maintaining accuracy",
            "Developed efficient multi-modal transformers for on-device applications with reduced inference latency",
            "Led team of 3 researchers in developing novel computer vision and multimodal ML models",
            "Published 4 papers in top-tier conferences (CVPR, ICLR, AAAI) and filed 6 patents",
        ],
    )
    add_role(
        pdf,
        "Postdoctoral Fellow",
        "July 2018 - October 2020",
        "Stanford University, Department of Computer Science",
        "Stanford, CA",
        [
            "Published 15+ papers in top-tier conferences (ICCV, CVPR, ICLR, AAAI, IJCAI, KDD)",
            "Developed novel self-supervised and weakly supervised learning approaches for remote sensing",
            "Created efficient deep learning models using reinforcement learning for adaptive computation",
            "Built ML models for sustainability applications including poverty mapping and farmland delineation",
        ],
    )

    pdf.add_page()
    pdf.set_font("Helvetica", "B", 9)
    pdf.set_text_color(120, 120, 120)
    pdf.cell(0, 5, "Burak Uzkent - CV", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(1)

    add_role(
        pdf,
        "Computer Vision Engineer",
        "June 2017 - July 2018",
        "Planet Labs",
        "San Francisco, CA",
        [
            "Built large-scale object detection dataset with 100K+ annotated satellite images",
            "Improved small object detection accuracy in low-resolution aerial imagery using convolutional detectors",
            "Conducted research to tackle unique challenges of satellite image object detection",
        ],
    )
    add_role(
        pdf,
        "Computer Vision Engineer",
        "August 2016 - June 2017",
        "Autel Robotics",
        "San Ramon, CA",
        [
            "Designed long-term target following system for next-generation drones",
            "Implemented online learning method for real-time single object tracking on embedded platforms",
            "Deployed and optimized tracking algorithms on low-end embedded systems",
        ],
    )
    add_role(
        pdf,
        "Computer Vision Algorithm Engineer Intern",
        "November 2015 - May 2016",
        "Futurewei Technologies (Huawei R&D)",
        "Bridgewater, NJ",
        [
            "Designed subspace learning method for stranger detection in family photo albums using deep CNNs",
            "Developed probabilistic graph-based approach for semantic role assignment in family photos",
        ],
    )

    add_heading(pdf, "EDUCATION")
    entries = [
        (
            "Rochester Institute of Technology",
            "August 2011 - May 2016",
            "Ph.D. in Imaging Science, Chester F. Carlson Center for Imaging Science",
            "Thesis: Aerial visual vehicle detection and tracking using an adaptive, multi-modal sensor",
            "Advisor: Matthew J. Hoffman, Ph.D.",
        ),
        (
            "University of Bridgeport",
            "August 2009 - May 2011",
            "M.S. in Electrical Engineering",
            "Thesis: Environmental non-speech sound classification with a new set of time-domain features",
            "Advisor: Buket D. Barkana, Ph.D.",
        ),
        (
            "Eskisehir Osmangazi University",
            "September 2004 - May 2009",
            "B.S. in Electrical and Electronics Engineering",
            "Thesis: Autonomous parallel parking of non-holonomic vehicles",
            "Advisor: Osman Parlaktuna, Ph.D.",
        ),
    ]
    for inst, years, degree, thesis, advisor in entries:
        pdf.set_text_color(20, 20, 20)
        write_wrapped(pdf, inst, line_h=5, style="bold")
        pdf.set_text_color(80, 80, 80)
        write_wrapped(pdf, years, line_h=4.5, style="italic")
        pdf.set_text_color(30, 30, 30)
        write_wrapped(pdf, degree, line_h=4.5)
        pdf.set_font("Helvetica", "I", 9)
        pdf.set_x(pdf.l_margin)
        pdf.multi_cell(pdf.epw, 4.5, thesis)
        write_wrapped(pdf, advisor, line_h=4.5)
        pdf.ln(1)

    add_heading(pdf, "RESEARCH EXPERIENCE")
    add_role(
        pdf,
        "Graduate Research Assistant",
        "April 2012 - July 2016",
        "RIT, Chester F. Carlson Center for Imaging Science",
        "Rochester, NY",
        [
            "Conducted research on aerial vehicle detection and tracking using adaptive, multi-modal sensors",
            "Developed computer vision and ML methods for vehicle detection, association, and tracking in aerial video",
            "Addressed challenges of medium-to-high altitude tracking through efficient use of hyperspectral data",
        ],
    )

    TEMP.parent.mkdir(parents=True, exist_ok=True)
    pdf.output(TEMP)


# Geometry, colours and fonts below are measured from the archived LaTeX CV so
# that regenerated publication pages reuse its typesetting instead of imitating it.
PAGE_W, PAGE_H = 612.0, 792.0
SIZE = 9.96
LEADING = 11.9533
ASCENT = 0.75 * SIZE
SPACE = 0.3333 * SIZE
TEXT_LEFT = 58.70
TEXT_RIGHT = 568.80
TEXT_WIDTH = TEXT_RIGHT - TEXT_LEFT
LABEL_RIGHT = 53.72
CLIP_LEFT = 55.0
CLIP_RIGHT = 570.0
CLIP_PAD = 3.0
BODY_TOP = 38.18
BODY_BOTTOM = 726.5
BLUE = (0.0, 0.32158, 0.60783)
GRAY = (0.50980, 0.50980, 0.50980)

JOURNAL_PAGE = 3
REVIEW_PAGE = 5
JOURNAL_CLIP = fitz.Rect(30, 33.0, CLIP_RIGHT, 208.0)
CONFERENCE_HEADING_CLIP = fitz.Rect(30, 220.0, CLIP_RIGHT, 249.0)
CONFERENCE_TOP = 261.74
REVIEW_HEADING_CLIP = fitz.Rect(30, 30.0, CLIP_RIGHT, 58.0)
REVIEW_ENTRY_TOP = 71.05
REVIEW_TAIL_CLIP = fitz.Rect(30, 172.0, CLIP_RIGHT, 540.0)
REVIEW_TAIL_ANCHOR = 164.70
HEADER_CLIP = fitz.Rect(470, 0, 580, 14)
FOOTER_CLIP = fitz.Rect(270, 770, 342, PAGE_H)

# The archived CMBX10 subset carries no capital N, so bold falls back to CMBX12.
STYLE_FONTS = {"r": ("CMR10",), "b": ("CMBX10", "CMBX12"), "i": ("CMTI10", "CMR10")}
LIGATURES = (("ffi", "\ufb03"), ("ffl", "\ufb04"), ("ff", "\ufb00"), ("fi", "\ufb01"), ("fl", "\ufb02"))
LABEL_RE = re.compile(r"^\[\d+\]$")

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


def load_cm_fonts(source: fitz.Document) -> dict[str, tuple[bytes, fitz.Font]]:
    fonts: dict[str, tuple[bytes, fitz.Font]] = {}
    for number in range(source.page_count):
        for item in source.get_page_fonts(number, full=True):
            name = item[3].split("+")[-1]
            if name not in fonts:
                buffer = source.extract_font(item[0])[3]
                fonts[name] = (buffer, fitz.Font(fontbuffer=buffer))
    return fonts


def register_fonts(page: fitz.Page, fonts: dict) -> None:
    for name in ("CMR10", "CMBX10", "CMBX12", "CMTI10"):
        page.insert_font(fontname=name, fontbuffer=fonts[name][0])


def ligate(word: str) -> str:
    for plain, ligature in LIGATURES:
        word = word.replace(plain, ligature)
    return word


def style_runs(word: str, style: str, fonts: dict) -> list[tuple[str, str]]:
    """Split a word into runs per font, since the archived subsets lack some glyphs."""
    candidates = STYLE_FONTS[style]
    runs: list[list[str]] = []
    for char in word:
        chosen = next(
            (name for name in candidates if fonts[name][1].has_glyph(ord(char))),
            candidates[0],
        )
        if runs and runs[-1][1] == chosen:
            runs[-1][0] += char
        else:
            runs.append([char, chosen])
    return [(text, name) for text, name in runs]


def tokenize(fragments: list[tuple[str, str]], fonts: dict) -> list[dict]:
    tokens: list[dict] = []
    pending_space = False
    for text, style in fragments:
        if not text:
            continue
        leading_space = text.startswith(" ")
        words = text.split()
        for index, word in enumerate(words):
            spaced = True if index else (pending_space or leading_space)
            runs = style_runs(ligate(word), style, fonts)
            width = sum(fonts[name][1].text_length(run, SIZE) for run, name in runs)
            tokens.append({"runs": runs, "width": width, "space": spaced})
        pending_space = text.endswith(" ") if words else pending_space
    return tokens


def wrap_tokens(tokens: list[dict], width: float = TEXT_WIDTH) -> list[list[dict]]:
    """Break tokens into lines, minimising stretched word spacing as TeX does."""
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
                used += SPACE
                gaps += 1
            used += token["width"]
            if used > width and end > start:
                break
            slack = width - used
            if end == count - 1:
                penalty = 0.0
            elif not gaps:
                penalty = float("inf")
            else:
                penalty = (slack / gaps) ** 3
            total = cost[end + 1] + penalty
            if total < cost[start]:
                cost[start] = total
                follow[start] = end + 1

    lines: list[list[dict]] = []
    start = 0
    while start < count:
        end = follow[start]
        lines.append(tokens[start:end])
        start = end
    return lines


def draw_label(page: fitz.Page, fonts: dict, number: int, top: float) -> None:
    label = f"[{number}]"
    width = fonts["CMR10"][1].text_length(label, SIZE)
    page.insert_text(
        (LABEL_RIGHT - width, top + ASCENT), label, fontname="CMR10", fontsize=SIZE, color=BLUE
    )


def draw_entry(page: fitz.Page, fonts: dict, number: int, lines: list[list[dict]], top: float) -> None:
    draw_label(page, fonts, number, top)
    for index, line in enumerate(lines):
        baseline = top + index * LEADING + ASCENT
        gaps = sum(1 for token in line[1:] if token["space"])
        ink = sum(token["width"] for token in line)
        space = (TEXT_WIDTH - ink) / gaps if gaps and index < len(lines) - 1 else SPACE
        x = TEXT_LEFT
        for position, token in enumerate(line):
            if position and token["space"]:
                x += space
            for run, name in token["runs"]:
                page.insert_text((x, baseline), run, fontname=name, fontsize=SIZE)
                x += fonts[name][1].text_length(run, SIZE)


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


def conference_entries(source: fitz.Document) -> list[dict]:
    entries: list[dict] = []
    collecting = False
    for number in (JOURNAL_PAGE, JOURNAL_PAGE + 1):
        for line in page_lines(source[number]):
            spans = line["spans"]
            if spans[0]["size"] > 13:
                title = "".join(span["text"] for span in spans).upper()
                collecting = "CONFERENCE" in title
                continue
            if not collecting:
                continue
            _, top, _, bottom = line["bbox"]
            is_label = LABEL_RE.match(spans[0]["text"].strip()) and spans[0]["bbox"][2] <= LABEL_RIGHT + 1
            if is_label:
                entries.append({"page": number, "top": top, "bottom": bottom, "count": 1})
            elif entries:
                entries[-1]["bottom"] = max(entries[-1]["bottom"], bottom)
                entries[-1]["count"] += 1
    if not entries:
        raise SystemExit("Could not read conference publications from the archived CV")
    return entries


def copy_block(page: fitz.Page, source: fitz.Document, number: int, clip: fitz.Rect, dy: float = 0.0) -> None:
    page.show_pdf_page(clip + (0, dy, 0, dy), source, number, clip=clip)
    for link in source[number].get_links():
        box = link["from"]
        if link.get("uri") and clip.y0 <= box.y0 and box.y1 <= clip.y1:
            page.insert_link({"kind": link["kind"], "uri": link["uri"], "from": box + (0, dy, 0, dy)})


def decorate(page: fitz.Page, source: fitz.Document, fonts: dict, number: int) -> None:
    page.show_pdf_page(HEADER_CLIP, source, JOURNAL_PAGE, clip=HEADER_CLIP)
    if number <= source.page_count:
        page.show_pdf_page(FOOTER_CLIP, source, number - 1, clip=FOOTER_CLIP)
    else:
        label = f"Page {number}"
        width = fonts["CMR10"][1].text_length(label, 8.97)
        page.insert_text(
            ((PAGE_W - width) / 2, 778.88 + 0.75 * 8.97),
            label,
            fontname="CMR10",
            fontsize=8.97,
            color=GRAY,
        )


def build_publication_pages(source: fitz.Document, fonts: dict, first_number: int) -> fitz.Document:
    items = [
        {"kind": "text", "lines": lines, "count": len(lines)}
        for lines in (wrap_tokens(tokenize(fragments, fonts)) for fragments in ACCEPTED_ENTRIES)
    ]
    items += [{"kind": "copy", "entry": entry, "count": entry["count"]} for entry in conference_entries(source)]

    placements: list[dict] = []
    index, top = 0, CONFERENCE_TOP
    for position, item in enumerate(items, start=1):
        height = (item["count"] - 1) * LEADING + SIZE
        if top + height > BODY_BOTTOM:
            index += 1
            top = BODY_TOP
        placements.append({"page": index, "top": top, "item": item, "number": position})
        top += (item["count"] + 1) * LEADING

    out = fitz.open()
    for _ in range(placements[-1]["page"] + 1):
        out.new_page(width=PAGE_W, height=PAGE_H)
    pages = [out[index] for index in range(out.page_count)]
    for offset, page in enumerate(pages):
        register_fonts(page, fonts)
        decorate(page, source, fonts, first_number + offset)

    copy_block(pages[0], source, JOURNAL_PAGE, JOURNAL_CLIP)
    copy_block(pages[0], source, JOURNAL_PAGE, CONFERENCE_HEADING_CLIP)

    # Archived entries keep their original typesetting; each is copied right
    # after its (renumbered) label so the text still reads in order.
    for placement in placements:
        page = pages[placement["page"]]
        item = placement["item"]
        if item["kind"] == "text":
            draw_entry(page, fonts, placement["number"], item["lines"], placement["top"])
            continue
        entry = item["entry"]
        draw_label(page, fonts, placement["number"], placement["top"])
        clip = fitz.Rect(CLIP_LEFT, entry["top"] - CLIP_PAD, CLIP_RIGHT, entry["bottom"] + CLIP_PAD)
        copy_block(page, source, entry["page"], clip, placement["top"] - entry["top"])

    return out


def fix_hyphen_mapping(document: fitz.Document) -> None:
    """Newly set text maps the Computer Modern hyphen to U+00AD; make it copy as "-"."""
    for xref in range(1, document.xref_length()):
        if not document.xref_is_stream(xref):
            continue
        stream = document.xref_stream(xref)
        if b"beginbfchar" in stream and b"<00ad>" in stream:
            document.update_stream(xref, stream.replace(b"<00ad>", b"<002d>"))


def build_final_page(source: fitz.Document, fonts: dict, number: int) -> fitz.Document:
    out = fitz.open()
    page = out.new_page(width=PAGE_W, height=PAGE_H)
    register_fonts(page, fonts)
    decorate(page, source, fonts, number)

    copy_block(page, source, REVIEW_PAGE, REVIEW_HEADING_CLIP)
    lines = wrap_tokens(tokenize(REVIEW_ENTRY, fonts))
    draw_entry(page, fonts, 1, lines, REVIEW_ENTRY_TOP)

    bottom = REVIEW_ENTRY_TOP + (len(lines) - 1) * LEADING + SIZE
    copy_block(page, source, REVIEW_PAGE, REVIEW_TAIL_CLIP, bottom - REVIEW_TAIL_ANCHOR)
    return out


def merge_and_write() -> None:
    tail_source = ARCHIVE if ARCHIVE.exists() else SOURCE
    if not tail_source.exists():
        raise SystemExit(f"Missing source CV: {SOURCE}")

    build_pages_1_2()
    intro = fitz.open(TEMP)
    old = fitz.open(tail_source)
    fonts = load_cm_fonts(old)
    out = fitz.open()

    out.insert_pdf(intro, from_page=0, to_page=1)
    out.insert_pdf(old, from_page=2, to_page=2)

    publications = build_publication_pages(old, fonts, out.page_count + 1)
    out.insert_pdf(publications)
    final_page = build_final_page(old, fonts, out.page_count + 1)
    out.insert_pdf(final_page)
    fix_hyphen_mapping(out)

    for path in OUTPUTS:
        out.save(path, garbage=4, deflate=True)

    for document in (intro, old, publications, final_page, out):
        document.close()
    TEMP.unlink(missing_ok=True)
    print(f"Wrote: {', '.join(str(p) for p in OUTPUTS)}")


if __name__ == "__main__":
    merge_and_write()
