"""This module enables...
Todo:
    Add correct dependencies for package and documentation.

"""

from docx import Document
from docx.shared import Inches
from docx.oxml.ns import nsdecls
from docx.oxml import parse_xml
from docx.enum.table import WD_ALIGN_VERTICAL

import mib_generator.parsing.load as load


def gen_doc(Tm_packets, Tc_packets):
    document = Document()
    document.add_heading("TM packets", 0)
    for i in Tm_packets:
        h = document.add_paragraph("")
        try:
            name = i.h_structure.comment[-1].entries["pack_type"]
        except:
            name = i.h_structure.name
        h.add_run(name + ": " + i.pid["PID_DESCR"]).italic = True
        table = document.add_table(rows=1, cols=4)
        table.style = "Table Grid"
        table.rows[0].cells[0].paragraphs[0].add_run("Byte").bold = True
        table.rows[0].cells[1].paragraphs[0].add_run("ID").bold = True
        table.rows[0].cells[2].paragraphs[0].add_run("Size in bites").bold = True
        table.rows[0].cells[3].paragraphs[0].add_run("Description").bold = True
        for l in range(4):
            table.rows[0].cells[l]._tc.get_or_add_tcPr().append(
                parse_xml(r'<w:shd {} w:fill="C7D9F1"/>'.format(nsdecls("w")))
            )
            table.rows[0].cells[l].vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        for l in range(len(i.plf)):
            row = table.add_row().cells
            row[0].text = to_bytes(i.positions[l])
            row[1].text = i.pcf[l]["PCF_NAME"]
            row[2].text = str(i.positions[l + 1] - i.positions[l])
            row[3].text = i.pcf[l]["PCF_DESCR"]
            for k in range(4):
                row[k].vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        document.add_paragraph()
    document.add_heading("TC packets", 0)
    for i in Tc_packets:
        h = document.add_paragraph("")
        h.add_run(i.ccf["CCF_DESCR2"]).italic = True
        table = document.add_table(rows=1, cols=5)
        table.style = "Table Grid"
        table.rows[0].cells[0].paragraphs[0].add_run("Byte").bold = True
        table.rows[0].cells[1].paragraphs[0].add_run("ID").bold = True
        table.rows[0].cells[2].paragraphs[0].add_run("Size in bites").bold = True
        table.rows[0].cells[3].paragraphs[0].add_run("Type").bold = True
        table.rows[0].cells[4].paragraphs[0].add_run("Description").bold = True
        for l in range(5):
            table.rows[0].cells[l]._tc.get_or_add_tcPr().append(
                parse_xml(r'<w:shd {} w:fill="C7D9F1"/>'.format(nsdecls("w")))
            )
            table.rows[0].cells[l].vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        for l in range(len(i.cdf)):
            row = table.add_row().cells
            row[0].text = to_bytes(i.positions[l])
            row[1].text = i.cdf[l]["CDF_PNAME"]
            if not row[1].text:
                row[1].text = i.entries[l].name
            row[2].text = str(i.positions[l + 1] - i.positions[l])
            row[3].text = str(i.entries[l].type)
            row[4].text = i.cdf[l]["CDF_DESCR"]
            for k in range(4):
                row[k].vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        document.add_paragraph()
    document.save(load.out_doc)


def to_bytes(bits):
    byt = int(bits / 8)
    bit = bits - byt * 8
    if bit == 0:
        return str(byt)
    elif bit == 1:
        return str(byt) + " (+ " + str(bit) + " bit)"
    else:
        return str(byt) + " (+ " + str(bit) + " bits)"
