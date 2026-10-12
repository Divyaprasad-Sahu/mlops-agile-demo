"""Build the final lab report using bundled python-docx, with actual evidence."""
import json
import ast
from pathlib import Path
import subprocess

from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT

ROOT = Path(__file__).resolve().parents[1]
metrics = json.loads((ROOT / "models/metrics.json").read_text())
evidence_file = ROOT / "docs/evidence/github_evidence.json"
evidence = json.loads(evidence_file.read_text()) if evidence_file.exists() else {}
doc = Document()
section = doc.sections[0]
section.page_width, section.page_height = Inches(8.27), Inches(11.69)
section.top_margin = section.bottom_margin = Inches(1)
section.left_margin = section.right_margin = Inches(1)
for name in ("Normal", "Title", "Subtitle", "Heading 1", "Heading 2", "Heading 3", "List Bullet"):
    style = doc.styles[name]
    style.font.name = "Times New Roman"
    style.font.color.rgb = RGBColor(0, 0, 0)
    fonts = style.element.get_or_add_rPr().get_or_add_rFonts()
    for attr in list(fonts.attrib):
        if "Theme" in attr:
            del fonts.attrib[attr]
    for attr in ("ascii", "hAnsi", "eastAsia", "cs"):
        fonts.set(qn("w:" + attr), "Times New Roman")
    style.paragraph_format.space_after = Pt(6)
doc.styles["Normal"].font.size = Pt(10.5)
doc.styles["Normal"].paragraph_format.line_spacing = 1.08
doc.styles["Title"].font.size = Pt(14)
doc.styles["Title"].font.bold = True
doc.styles["Heading 1"].font.size = Pt(14)
doc.styles["Heading 1"].font.bold = True
doc.styles["Heading 2"].font.size = Pt(12)
doc.styles["Heading 2"].font.bold = False
doc.styles["Heading 2"].paragraph_format.space_before = Pt(8)
doc.styles["List Bullet"].font.size = Pt(10.5)
doc.styles["List Bullet"].paragraph_format.space_after = Pt(0)
doc.styles["List Bullet"].paragraph_format.line_spacing = 1.0
doc.styles["List Bullet"].paragraph_format.left_indent = Inches(0.2)
doc.styles["List Bullet"].paragraph_format.first_line_indent = Inches(-0.12)
for style in doc.styles:
    for border in style.element.xpath(".//w:pBdr"):
        border.getparent().remove(border)
doc.core_properties.title = "Agile and Scrum MLOps Experiment"
doc.core_properties.author = "Divyaprasad Sahu"


def p(text, style=None):
    return doc.add_paragraph(text, style)


def h(text):
    doc.add_heading(text, 2)


def rule():
    para = p("")
    para.paragraph_format.space_before = Pt(5)
    para.paragraph_format.space_after = Pt(7)
    para.paragraph_format.line_spacing = Pt(1)
    borders = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    for key, value in (("val", "single"), ("sz", "6"), ("color", "888888"), ("space", "1")):
        bottom.set(qn("w:" + key), value)
    borders.append(bottom)
    para._p.get_or_add_pPr().append(borders)


def page(title):
    doc.add_page_break()
    doc.add_heading(title, 1)


def table(headers, rows, widths=None):
    t = doc.add_table(rows=1, cols=len(headers))
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = False
    for i, text in enumerate(headers):
        t.rows[0].cells[i].text = str(text)
    for row in rows:
        cells = t.add_row().cells
        for i, text in enumerate(row):
            cells[i].text = str(text)
    repeat = OxmlElement("w:tblHeader")
    t.rows[0]._tr.get_or_add_trPr().append(repeat)
    for ri, row in enumerate(t.rows):
        keep = OxmlElement("w:cantSplit")
        row._tr.get_or_add_trPr().append(keep)
        for ci, cell in enumerate(row.cells):
            if widths:
                cell.width = Inches(widths[ci] * 6.27 / sum(widths))
            cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
            props = cell._tc.get_or_add_tcPr()
            borders = OxmlElement("w:tcBorders")
            for edge in ("top", "left", "bottom", "right"):
                border = OxmlElement("w:" + edge)
                for key, value in (("val", "single"), ("sz", "4"), ("color", "D9D9D9")):
                    border.set(qn("w:" + key), value)
                borders.append(border)
            props.append(borders)
            margins = OxmlElement("w:tcMar")
            for side in ("top", "left", "bottom", "right"):
                item = OxmlElement("w:" + side)
                item.set(qn("w:w"), "90")
                item.set(qn("w:type"), "dxa")
                margins.append(item)
            props.append(margins)
            shading = OxmlElement("w:shd")
            shading.set(qn("w:fill"), "EEEEEE" if ri == 0 else "FFFFFF")
            props.append(shading)
            for para in cell.paragraphs:
                para.paragraph_format.space_after = Pt(2)
                para.paragraph_format.line_spacing = 1.0
                for run in para.runs:
                    run.font.size = Pt(9.5)
                    if ri == 0:
                        run.font.bold = True
                        run.font.color.rgb = RGBColor(0, 0, 0)
    p("")
    return t


def code(text):
    para = p(text)
    para.paragraph_format.line_spacing = 1
    for run in para.runs:
        run.font.name = "Consolas"
        run.font.size = Pt(9)


def source_excerpt(relative_path, start, end):
    """Copy actual source lines with editor-style line numbers into Word."""
    lines = (ROOT / relative_path).read_text(encoding="utf-8").splitlines()
    p(f"{relative_path}   |   Lines {start} to {end}")
    for number in range(start, end + 1):
        para = p("")
        para.paragraph_format.space_after = Pt(0)
        para.paragraph_format.line_spacing = 1.05
        number_run = para.add_run(f"{number:>3}  ")
        number_run.font.name = "Consolas"
        number_run.font.size = Pt(8)
        number_run.font.color.rgb = RGBColor.from_string("666666")
        run = para.add_run(lines[number - 1])
        run.font.name = "Consolas"
        run.font.size = Pt(8)
        if lines[number - 1].lstrip().startswith("#"):
            run.font.color.rgb = RGBColor.from_string("38761D")
        elif lines[number - 1].lstrip().startswith(("def ", "if ", "return ", "with ")):
            run.font.color.rgb = RGBColor.from_string("17365D")
    p("")


def function_excerpt(relative_path, function_name):
    source = (ROOT / relative_path).read_text(encoding="utf-8")
    node = next(node for node in ast.parse(source).body
                if isinstance(node, ast.FunctionDef) and node.name == function_name)
    source_excerpt(relative_path, node.lineno, node.end_lineno)


def link(label, url):
    para = p("")
    rel = para.part.relate_to(url, "http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink", is_external=True)
    element = OxmlElement("w:hyperlink")
    element.set(qn("r:id"), rel)
    run = OxmlElement("w:r")
    text = OxmlElement("w:t")
    text.text = label + "  " + url
    run.append(text)
    element.append(run)
    para._p.append(element)


from report_content import build_content
build_content(p, h, page, table, code, source_excerpt, function_excerpt, link, metrics, evidence, rule)

footer = section.footer.paragraphs[0]
footer.alignment = 2
footer.add_run("Experiment 1   |   ")
field = OxmlElement("w:fldSimple")
field.set(qn("w:instr"), "PAGE")
footer._p.append(field)
for run in footer.runs:
    run.font.size = Pt(9)
target = ROOT / "docs/Experiment_1_Agile_and_Scrum_Report_Template.docx"
doc.save(target)
print(target)
