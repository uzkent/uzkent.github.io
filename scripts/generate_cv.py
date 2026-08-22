#!/usr/bin/env python3
"""Regenerate Burak Uzkent academic CV PDF (pages 1-2) and merge with prior pages 3-6."""

from __future__ import annotations

import fitz
import re
import unicodedata
from fpdf import FPDF
from matplotlib import get_data_path
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FILES = ROOT / "files"
SOURCE = FILES / "CV.BurakUzkent.pdf"
ARCHIVE = FILES / "CV.BurakUzkent.pdf.bak"
OUTPUTS = [FILES / "CV.BurakUzkent.pdf", FILES / "Burak_Uzkent_Academic_CV.pdf"]
TEMP = FILES / "_cv_pages_1_2.pdf"
PUBLICATIONS_TEMP = FILES / "_cv_publications.pdf"
CM_FONT_DIR = Path(get_data_path()) / "fonts" / "ttf"


class CVPDF(FPDF):
    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 9)
        self.set_text_color(100, 100, 100)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")


class PublicationPDF(CVPDF):
    def header(self):
        self.set_y(18)
        self.set_font("Helvetica", "B", 9)
        self.set_text_color(120, 120, 120)
        self.cell(0, 5, "Burak Uzkent - CV", new_x="LMARGIN", new_y="NEXT")
        self.ln(2)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 9)
        self.set_text_color(100, 100, 100)
        self.cell(0, 10, f"Page {self.page_no() + 3}", align="C")


def add_heading(pdf: CVPDF, title: str):
    pdf.ln(2)
    pdf.set_font("Helvetica", "B", 11)
    pdf.set_text_color(0, 80, 160)
    pdf.cell(pdf.epw, 7, title, new_x="LMARGIN", new_y="NEXT")
    pdf.set_draw_color(0, 80, 160)
    pdf.line(pdf.l_margin, pdf.get_y(), pdf.w - pdf.r_margin, pdf.get_y())
    pdf.ln(3)


def register_publication_fonts(pdf: FPDF) -> None:
    pdf.add_font("CM", "", CM_FONT_DIR / "cmr10.ttf")
    pdf.add_font("CM", "B", CM_FONT_DIR / "cmb10.ttf")


def add_publication_heading(pdf: FPDF, title: str) -> None:
    pdf.ln(2)
    x = pdf.l_margin
    y = pdf.get_y() + 1
    pdf.set_draw_color(0, 82, 155)
    pdf.set_line_width(0.45)
    pdf.rect(x, y, 4.5, 5.8)
    pdf.line(x + 2.8, y, x + 4.5, y + 1.7)
    pdf.line(x + 2.8, y, x + 2.8, y + 1.7)
    pdf.line(x + 2.8, y + 1.7, x + 4.5, y + 1.7)
    pdf.line(x + 0.9, y + 2.8, x + 3.6, y + 2.8)
    pdf.line(x + 0.9, y + 3.8, x + 3.6, y + 3.8)
    pdf.line(x + 0.9, y + 4.8, x + 3.6, y + 4.8)
    pdf.set_font("CM", "B", 14.3)
    pdf.set_text_color(0, 82, 155)
    pdf.set_x(x + 7)
    pdf.cell(pdf.epw, 8, title, new_x="LMARGIN", new_y="NEXT")
    pdf.set_draw_color(0, 82, 155)
    pdf.set_line_width(0.65)
    pdf.line(pdf.l_margin, pdf.get_y(), pdf.w - pdf.r_margin, pdf.get_y())
    pdf.ln(4)


def write_wrapped(pdf: FPDF, text: str, line_h: float = 5, style: str = "") -> None:
    pdf.set_x(pdf.l_margin)
    if style == "bold":
        pdf.set_font("Helvetica", "B", 10.5)
    elif style == "italic":
        pdf.set_font("Helvetica", "I", 9.5)
    else:
        pdf.set_font("Helvetica", "", 9.5)
    pdf.multi_cell(pdf.epw, line_h, text)


def normalize_pdf_text(text: str) -> str:
    replacements = str.maketrans(
        {
            "\u2013": "-",
            "\u2014": "-",
            "\u2018": "'",
            "\u2019": "'",
            "\u201c": '"',
            "\u201d": '"',
            "\u00bd": "",
            "\u00cd": "",
            "\x08": "",
        }
    )
    normalized = unicodedata.normalize("NFKD", text.translate(replacements))
    latin_text = normalized.encode("latin-1", "ignore").decode("latin-1")
    return re.sub(r"\s+", " ", latin_text).strip()


def numbered_entries(text: str) -> list[str]:
    chunks = re.split(r"(?m)(?=^\[\d+\]\s)", text)
    return [
        normalize_pdf_text(chunk)
        for chunk in chunks
        if re.match(r"^\[\d+\]", chunk)
    ]


def emphasize_name(text: str) -> str:
    return text.replace("B. Uzkent", "**B. Uzkent**")


def write_publication_entry(pdf: FPDF, number: int, text: str) -> None:
    if pdf.h - pdf.b_margin - pdf.get_y() < 18:
        pdf.add_page()

    text = re.sub(r"\s+o$", "", text)
    x = pdf.l_margin
    y = pdf.get_y()
    indent = 8

    pdf.set_font("CM", "", 10)
    pdf.set_text_color(0, 82, 155)
    pdf.text(x, y + 3.8, f"[{number}]")

    pdf.set_text_color(0, 0, 0)
    pdf.set_xy(x + indent, y)
    pdf.multi_cell(
        pdf.epw - indent,
        4.8,
        emphasize_name(text),
        markdown=True,
        new_x="LMARGIN",
        new_y="NEXT",
    )
    pdf.ln(1.2)


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


def build_publication_pages(source_path: Path) -> Path:
    source = fitz.open(source_path)
    page4_text = source[3].get_text()
    page5_text = source[4].get_text()
    source.close()

    conference_heading = "REFEREED CONFERENCE PUBLICATIONS"
    journal_text, first_conference_text = page4_text.split(conference_heading, 1)
    journal_entries = numbered_entries(journal_text)
    prior_conference_entries = numbered_entries(first_conference_text) + numbered_entries(page5_text)

    accepted_entries = [
        'T. Poppi, B. Uzkent, A. Garg, L. Porto, G. Kessler, Y. Yang, M. Cornia, L. Baraldi, '
        'R. Cucchiara, F. Schiffers, "CounterVid: Counterfactual Video Generation for Mitigating Action '
        'and Temporal Hallucinations in Video-Language Models", EMNLP-26, 2026.',
        'G. Sun, A. Singhal, B. Uzkent, M. Shah, C. Chen, G. Kessler, "From Frames to Clips: '
        'Efficient Key Clip Selection for Long-form Video Understanding", ECCV Workshop-26, 2026.',
        'R. Jain, K. Doshi, B. Uzkent, G. Kessler, "Narrative Aligned Long Form Video Question Answering", '
        'CVPR Workshop-26 (Best Paper Candidate), 2026.',
    ]

    pdf = PublicationPDF()
    pdf.set_margins(18, 18, 18)
    pdf.set_auto_page_break(auto=True, margin=20)
    register_publication_fonts(pdf)
    pdf.add_page()

    add_publication_heading(pdf, "REFEREED JOURNAL PUBLICATIONS (CONTINUED)")
    for entry in journal_entries:
        match = re.match(r"^\[(\d+)\]\s*(.*)", entry)
        if match:
            write_publication_entry(pdf, int(match.group(1)), match.group(2))

    add_publication_heading(pdf, conference_heading)
    conference_entries = accepted_entries + [
        re.sub(r"^\[\d+\]\s*", "", entry) for entry in prior_conference_entries
    ]
    for index, entry in enumerate(conference_entries, start=1):
        write_publication_entry(pdf, index, entry)

    pdf.output(PUBLICATIONS_TEMP)
    return PUBLICATIONS_TEMP


def build_page_6() -> Path:
    pdf = FPDF()
    pdf.set_margins(18, 18, 18)
    pdf.set_auto_page_break(auto=True, margin=20)
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 9)
    pdf.set_text_color(120, 120, 120)
    pdf.cell(0, 5, "Burak Uzkent - CV", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(2)

    add_heading(pdf, "RECENT PAPERS")
    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(30, 30, 30)
    recent_papers = [
        '[1] A. Blume, B. Uzkent, S. Chaudhuri, G. Kessler, '
        '"Learning to Rank Caption Chains for Video-Text Alignment", ECCV-26.',
    ]
    for paper in recent_papers:
        pdf.set_x(pdf.l_margin)
        pdf.multi_cell(pdf.epw, 5, emphasize_name(paper), markdown=True)
        pdf.ln(1)

    add_heading(pdf, "PROFESSIONAL SERVICE")
    pdf.set_font("Helvetica", "", 9.5)
    pdf.set_x(pdf.l_margin)
    pdf.multi_cell(
        pdf.epw,
        5,
        "Peer Reviewer: IEEE TGRS, IEEE TIFS, NeurIPS, WACV, ICCV, BMVC, IEEE TIP, ICML, ICLR, CVPR, "
        "IEEE Sensors Journal, Nature Machine Intelligence, IEEE Access",
    )

    add_heading(pdf, "HONORS & AWARDS")
    awards = [
        "Amazon Invention Award (June 2024)",
        "RIT Graduate Scholarship Award (September 2011 - May 2016)",
        "University of Bridgeport Dean's Scholarship Award (August 2009 - May 2011)",
        "University of Bridgeport Outstanding Student Award (May 2011)",
        "Fulbright Opportunity Grant (August 2009)",
        "Erasmus Exchange Student (September 2007 - January 2008)",
    ]
    pdf.set_font("Helvetica", "", 9.5)
    for award in awards:
        pdf.cell(0, 5, f"  * {award}", new_x="LMARGIN", new_y="NEXT")

    add_heading(pdf, "LANGUAGES")
    pdf.cell(0, 5, "  English - Advanced/Fluent", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 5, "  Turkish - Native", new_x="LMARGIN", new_y="NEXT")

    path = FILES / "_cv_page_6.pdf"
    pdf.output(path)
    return path


def merge_and_write() -> None:
    tail_source = ARCHIVE if ARCHIVE.exists() else SOURCE
    if not tail_source.exists():
        raise SystemExit(f"Missing source CV: {SOURCE}")

    build_pages_1_2()
    new_part = fitz.open(TEMP)
    old = fitz.open(tail_source)
    publications = fitz.open(build_publication_pages(tail_source))
    out = fitz.open()

    out.insert_pdf(new_part, from_page=0, to_page=1)
    if old.page_count > 2:
        out.insert_pdf(old, from_page=2, to_page=2)
    out.insert_pdf(publications)

    final_page = fitz.open(build_page_6())
    out.insert_pdf(final_page)
    final_page.close()

    for path in OUTPUTS:
        out.save(path, garbage=4, deflate=True)

    new_part.close()
    old.close()
    publications.close()
    out.close()
    TEMP.unlink(missing_ok=True)
    PUBLICATIONS_TEMP.unlink(missing_ok=True)
    (FILES / "_cv_page_6.pdf").unlink(missing_ok=True)
    print(f"Wrote: {', '.join(str(p) for p in OUTPUTS)}")


if __name__ == "__main__":
    merge_and_write()
