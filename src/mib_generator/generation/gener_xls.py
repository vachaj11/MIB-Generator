from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, NamedStyle

import os

h1 = NamedStyle(name = "h1")
h1.font = Font(bold = True)
h1.alignment = Alignment(horizontal="center",vertical="center")
h1.fill = PatternFill(fill_type= "solid", fgColor = "99CCFF")
h2 = NamedStyle(name = "h2")
h2.font = Font(bold = True)
h2.alignment = Alignment(horizontal="center",vertical="center")
h2.fill = PatternFill(fill_type= "solid", fgColor = "CC99FF") 
h3 = NamedStyle(name = "h3")
h3.font = Font(bold = True)
h3.alignment = Alignment(horizontal="center",vertical="center")
h3.fill = PatternFill(fill_type= "solid", fgColor = "FFCC00") 

c1 = NamedStyle(name = "c1")
c1.font = Font(bold = False)
c1.alignment = Alignment(horizontal="left",vertical="center")
c1.fill = PatternFill(fill_type= "solid", fgColor = "99CCFF")
c2 = NamedStyle(name = "c2")
c2.font = Font(bold = False)
c2.alignment = Alignment(horizontal="left",vertical="center")
c2.fill = PatternFill(fill_type= "solid", fgColor = "CC99FF")
c3 = NamedStyle(name = "c3")
c3.font = Font(bold = False)
c3.alignment = Alignment(horizontal="left",vertical="center")
c3.fill = PatternFill(fill_type= "solid", fgColor = "FFCC00") 

def gen_polyc(book, calib):
    ws = book.create_sheet("TM PolyCal")
    head = ["PolyCal Definition", "Mnemonic", "Description", "Coeff. A0", "Coeff. A1", "Coeff. A2", "Coeff. A3", "Coeff. A4"]
    for i in head:
        if i:
            ws.cell(1, head.index(i)+1, i).style = h1
    for i in range(len(calib)):
        ws.cell(i+3, 1, "PolyCal").style = c1
        ws.cell(i+3,2, calib[i].mcf["MCF_IDENT"]).style = c1
        ws.cell(i+3,3, calib[i].mcf["MCF_DESCR"]).style = c1
        ws.cell(i+3,4, calib[i].mcf["MCF_POL1"]).style = c1
        ws.cell(i+3,5, calib[i].mcf["MCF_POL2"]).style = c1
        ws.cell(i+3,6, calib[i].mcf["MCF_POL3"]).style = c1
        ws.cell(i+3,7, calib[i].mcf["MCF_POL4"]).style = c1
        ws.cell(i+3,8, calib[i].mcf["MCF_POL5"]).style = c1

def gen_logc(book, calib):
    ws = book.create_sheet("TM LogCal")
    head = ["LogCal Definition", "Mnemonic", "Description", "Coeff. A0", "Coeff. A1", "Coeff. A2", "Coeff. A3", "Coeff. A4"]
    for i in head:
        if i:
            ws.cell(1, head.index(i)+1, i).style = h1
    for i in range(len(calib)):
        ws.cell(i+3, 1, "LogCal").style = c1
        ws.cell(i+3,2, calib[i].lgf["LGF_IDENT"]).style = c1
        ws.cell(i+3,3, calib[i].lgf["LGF_DESCR"]).style = c1
        ws.cell(i+3,4, calib[i].lgf["LGF_POL1"]).style = c1
        ws.cell(i+3,5, calib[i].lgf["LGF_POL2"]).style = c1
        ws.cell(i+3,6, calib[i].lgf["LGF_POL3"]).style = c1
        ws.cell(i+3,7, calib[i].lgf["LGF_POL4"]).style = c1
        ws.cell(i+3,8, calib[i].lgf["LGF_POL5"]).style = c1

def gen_txtc(book, calib):
    ws = book.create_sheet("TM TxtCal")
    head = ["TxtCal Definition", "Mnemonic", "Description", "Number of Ranges", "Raw Format"]
    head2 = ["TxtCal Ranges Definition","","Range from","Range to","Alias"]
    for i in head:
        if i:
            ws.cell(1, head.index(i)+1, i).style = h1
    for i in head2:
        if i:
            ws.cell(2, head2.index(i)+1, i).style = h2
    ind = 4
    for i in calib:
        ws.cell(ind, 1, "TxtCal").style = c1
        ws.cell(ind, 2, i.txf["TXF_NUMBR"]).style = c1
        ws.cell(ind, 3, i.txf["TXF_DESCR"]).style = c1
        ws.cell(ind, 4, i.txf["TXF_NALIAS"]).style = c1
        ws.cell(ind, 5, i.txf["TXF_RAWFMT"]).style = c1
        ind += 1
        for l in i.txp:
            ws.cell(ind, 1, "TxtCal Ranges").style = c2
            ws.cell(ind, 3, l["TXP_FROM"]).style = c2
            ws.cell(ind, 4, l["TXP_TO"]).style = c2
            ws.cell(ind, 5, l["TXP_ALTXT"]).style = c2
            ind += 1
        ind += 1
        
def gen_numc(book, calib):
    ws = book.create_sheet("TM NumCal")
    head = ["NumCal Definition", "Mnemonic", "Description", "Number of Points", "Raw Format", "Raw Radix", "Eng Format", "Eng Unit", "Interpolation"]
    head2 = ["NumCal Points Definition","","Raw Value","Eng Value"]
    for i in head:
        if i:
            ws.cell(1, head.index(i)+1, i).style = h1
    for i in head2:
        if i:
            ws.cell(2, head2.index(i)+1, i).style = h2
    ind = 4
    for i in calib:
        ws.cell(ind, 1, "NumCal").style = c1
        ws.cell(ind, 2, i.caf["CAF_NUMBR"]).style = c1
        ws.cell(ind, 3, i.caf["CAF_DESCR"]).style = c1
        ws.cell(ind, 4, i.caf["CAF_NCURVE"]).style = c1
        ws.cell(ind, 5, i.caf["CAF_RAWFMT"]).style = c1
        ws.cell(ind, 6, i.caf["CAF_RADIX"]).style = c1
        ws.cell(ind, 7, i.caf["CAF_ENGFMT"]).style = c1
        ws.cell(ind, 8, i.caf["CAF_UNIT"]).style = c1
        ws.cell(ind, 9, i.caf["CAF_INTER"]).style = c1
        ind += 1
        for l in i.cap:
            ws.cell(ind, 1, "NumCal Points").style = c2
            ws.cell(ind, 3, l["CAP_XVALS"]).style = c2
            ws.cell(ind, 4, l["CAP_YVALS"]).style = c2
            ind += 1
        ind += 1
        
def gen_tdec(book, calib):
    ws = book.create_sheet("TC TxtCal")
    head = ["TC TxtCal Definition", "Mnemonic", "Description", "Raw Format", "Number of Ranges"]
    head2 = ["TC TxtCal Alias Definition","","Raw Value", "Alias"]
    for i in head:
        if i:
            ws.cell(1, head.index(i)+1, i).style = h1
    for i in head2:
        if i:
            ws.cell(2, head2.index(i)+1, i).style = h2
    ind = 4
    for i in calib:
        ws.cell(ind, 1, "TC TxtCal").style = c1
        ws.cell(ind, 2, i.paf["PAF_NUMBR"]).style = c1
        ws.cell(ind, 3, i.paf["PAF_DESCR"]).style = c1
        ws.cell(ind, 4, i.paf["PAF_RAWFMT"]).style = c1
        ws.cell(ind, 5, i.paf["PAF_NALIAS"]).style = c1
        ind += 1
        for l in i.pas:
            ws.cell(ind, 1, "TC TxtCal Alias").style = c2
            ws.cell(ind, 3, l["PAS_ALVAL"]).style = c2
            ws.cell(ind, 4, l["PAS_ALTXT"]).style = c2
            ind += 1
        ind += 1

def gen_verif(book, verif):
    ws = book.create_sheet("TC Verif Criteria")
    head = ["TC Verif Stage Definition", "Mnemonic", "Execution Stage", "Check Type", "Start Delay", "Interval", "Closing TM Packet", "Uncertainty"]
    head2 = ["TC Verif Criteria Definition","","TM Parameter", "Value Type", "Value", "Tolerance", "Check Flag"]
    for i in head:
        if i:
            ws.cell(1, head.index(i)+1, i).style = h1
    for i in head2:
        if i:
            ws.cell(2, head2.index(i)+1, i).style = h2
    ind = 4
    for i in verif:
        ws.cell(ind, 1, "TC Verif Stage").style = c1
        ws.cell(ind, 2, i.cvs["CVS_ID"]).style = c1
        ws.cell(ind, 3, i.cvs["CVS_TYPE"]).style = c1
        ws.cell(ind, 4, i.cvs["CVS_SOURCE"]).style = c1
        ws.cell(ind, 5, i.cvs["CVS_START"]).style = c1
        ws.cell(ind, 5, i.cvs["CVS_INTERVAL"]).style = c1
        ind += 1

def gen_pidt(book, packets):
    ws = book.create_sheet("TM Packet")

def gen_xls(
    Tm_packets=None,
    Tc_packets=None,
    calibrations=None,
    decalibrations=None,
    verifications=None,
    Tc_head=None,
):
    wb = Workbook()
    gen_polyc(wb, calibrations["mcfs"])
    gen_logc(wb, calibrations["lgfs"])
    gen_txtc(wb, calibrations["txfs"])
    gen_numc(wb, calibrations["cafs"])
    gen_tdec(wb, decalibrations)
    gen_verif(wb, verifications)
    gen_pidt(wb, Tm_packets)
    wb.remove(wb["Sheet"])
    for i in wb:
        adjust_width(i)
    return wb
    
def adjust_width(ws):
    for column in ws.column_dimensions:
        column.width = 3
    for row in ws.rows:
        for cell in row:
            if cell.value:
                ws.column_dimensions[cell.column_letter].width = max((ws.column_dimensions[cell.column_letter].width, len(str(cell.value))*1.2))
    
