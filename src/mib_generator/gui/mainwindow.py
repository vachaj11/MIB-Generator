# This Python file uses the following encoding: utf-8
import sys, os

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtCore import Slot

file_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(file_path)

import mib_generator.construction.calib as calib
import mib_generator.construction.TC_packet as tc_packet
import mib_generator.construction.TC_packet_methods as tc_packet_methods
import mib_generator.construction.TM_packet as tm_packet
import mib_generator.construction.TM_packet_methods as tm_packet_methods
import mib_generator.data.warn as warn
import mib_generator.generation.gener as gener
import mib_generator.generation.gener_doc as generd
import mib_generator.parsing.load as load
import mib_generator.temp.temp as temp
import mib_generator.utilities.visualiser as visualiser
import mib_generator.data.warn as warn

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("MIB Generator")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("MIB Generator")

        warn.disp_update(self.ui.console)
        self.tms = None
        self.TmHead = None
        self.tcs = None
        self.TcHead = None
        self.cal = None #{"mcfs": [], "txfs": [], "cafs": [], "lgfs": []}
        self.dec = None
        self.ver = None
        self.tables = {}
        self.docum = None

        self.ui.parsebutton.clicked.connect(self.parse)
        self.ui.TmHview.clicked.connect(self.TmHshow)
        self.ui.TcHview.clicked.connect(self.TcHshow)
        self.ui.TmCview.clicked.connect(self.TmCshow)
        self.ui.TcTmHview.clicked.connect(self.TcTmHshow)
        self.ui.Tmbuild.clicked.connect(self.Tminter)
        self.ui.Tcbuild.clicked.connect(self.Tcinter)
        self.ui.mibgen.clicked.connect(self.MIBgen)
        self.ui.docgen.clicked.connect(self.DOCgen)
        self.ui.mibsave.clicked.connect(self.MIBsave)
        self.ui.docsave.clicked.connect(self.DOCsave)
        self.ui.compute_all.clicked.connect(self.compute)
        self.ui.TmHbutton.clicked.connect(lambda: self.Cfile(self.ui.TmHfield))
        self.ui.TcHbutton.clicked.connect(lambda: self.Cfile(self.ui.TcHfield))
        self.ui.TmCbutton.clicked.connect(lambda: self.Cfile(self.ui.TmCfield))
        self.ui.TcTmHbutton.clicked.connect(lambda: self.Cfile(self.ui.TcTmHfield))
        self.ui.outdirbutton.clicked.connect(lambda: self.direc(self.ui.outdirfield))
        self.ui.outdocbutton.clicked.connect(self.Dfile)
        self.ui.configbutton.clicked.connect(lambda:self.direc(self.ui.configfield))
        self.ui.pathsbutton.clicked.connect(self.use_paths)

    @Slot()
    def compute(self):
        self.ui.parsebutton.click()
        self.ui.Tmbuild.click()
        self.ui.Tcbuild.click()
        self.ui.mibgen.click()
        self.ui.docgen.click()
        self.ui.mibsave.click()
        self.ui.docsave.click()

    @Slot()
    def parse(self):
            load.load_all()
            if load.TmH:
                self.ui.TmHview.setEnabled(True)
                self.ui.TmHview.setText("View")
            else:
                self.ui.TmHview.setEnabled(False)
                self.ui.TmHview.setText("Error")
            if load.TcH:
                self.ui.TcHview.setEnabled(True)
                self.ui.TcHview.setText("View")
                self.ui.Tcbuild.setEnabled(True)
            else:
                self.ui.TcHview.setEnabled(False)
                self.ui.TcHview.setText("Error")
                self.ui.Tcbuild.setEnabled(False)
            if load.TmC:
                self.ui.TmCview.setEnabled(True)
                self.ui.TmCview.setText("View")
            else:
                self.ui.TmCview.setEnabled(False)
                self.ui.TmCview.setText("Error")
            if load.TcTmH:
                self.ui.TcTmHview.setEnabled(True)
                self.ui.TcTmHview.setText("View")
            else:
                self.ui.TcTmHview.setEnabled(False)
                self.ui.TcTmHview.setText("Error")
            if load.TmH and load.TmC:
                self.ui.Tmbuild.setEnabled(True)
            else:
                self.ui.Tmbuild.setEnabled(False)

    @Slot()
    def TmHshow(self):
        self.prewTmH = visualiser.MainWindow(load.TmH)
        self.prewTmH.show()

    @Slot()
    def TcHshow(self):
        self.prewTcH = visualiser.MainWindow(load.TcH)
        self.prewTcH.show()

    @Slot()
    def TmCshow(self):
        self.prewTmC = visualiser.MainWindow(load.TmC)
        self.prewTmC.show()

    @Slot()
    def TcTmHshow(self):
        self.prewTcTmH = visualiser.MainWindow(load.TcTmH)
        self.prewTcTmH.show()

    @Slot()
    def Tminter(self):
        cal1 = calib.calib_extract(load.TmH.comments)
        cal2 = calib.calib_extract(load.TcTmH.comments)
        self.cal = {i: cal1[i] + cal2[i] for i in cal1}
        self.TmHead = tm_packet.TM_header(load.TmH)
        self.tms = []
        for i in load.TmC.structures[1].elements:
            matched = tm_packet_methods.header_search(i.entries[".type"])
            for k in matched:
                pack = tm_packet.TM_packet(i, k, self.TmHead)
                calib.cur_update(pack, self.cal)
                self.tms.append(pack)
        self.ui.mibgen.setEnabled(True)
        self.ui.docgen.setEnabled(True)

    @Slot()
    def Tcinter(self):
        dec1 = calib.decal_extract(load.TcH.comments)
        dec2 = calib.decal_extract(load.TcTmH.comments)
        self.dec = dec1 + dec2
        ver1 = calib.verif_extract(load.TcH.comments)
        ver2 = calib.verif_extract(load.TcTmH.comments)
        self.ver = ver1 + ver2
        self.TcHead = tc_packet.TC_header(tc_packet_methods.find_header(load.TcH))
        packets = tc_packet_methods.packet_search(load.TcH)
        self.tcs = []
        for i in packets:
            comm = tc_packet.TC_packet(i, self.TcHead)
            calib.cpc_update(comm, self.dec)
            calib.cvs_update(comm, self.ver)
            self.tcs.append(comm)
        self.ui.mibgen.setEnabled(True)
        self.ui.docgen.setEnabled(True)

    @Slot()
    def MIBgen(self):
        self.tables = gener.generation_hub(self.tms, self.tcs, self.cal, self.dec, self.ver, self.TcHead)
        self.ui.mibsave.setEnabled(True)

    @Slot()
    def DOCgen(self):
        self.docum = generd.gen_doc(self.tms, self.tcs)
        self.ui.docsave.setEnabled(True)

    @Slot()
    def MIBsave(self):
        gener.save_tables(self.tables)

    @Slot()
    def DOCsave(self):
        self.docum.save(load.out_doc)

    @Slot()
    def Cfile(self, field):
        ftype = "C files (*.c *.h)"
        base = os.path.dirname(field.text())
        file = QFileDialog.getOpenFileName(self, "Choose file", base, ftype)
        if file[0] != '':
            field.setText(file[0])

    @Slot()
    def direc(self, field):
        base = os.path.dirname(field.text())
        capt = "Choose a directory"
        file = QFileDialog.getExistingDirectory(self, capt, base)
        if file != '':
            field.setText(file)

    @Slot()
    def Dfile(self):
        ftype = "Microsoft Word files (*.docx)"
        base = os.path.dirname(self.ui.outdocfield.text())
        file = QFileDialog.getSaveFileName(self, "Choose file", base, ftype)
        if file[0] != '':
            self.ui.outdocfield.setText(file[0])

    @Slot()
    def use_paths(self):
        dic = {
            "TmHeader": self.ui.TmHfield.text(),
            "TcTmHeader": self.ui.TcTmHfield.text(),
            "TmFile": self.ui.TmCfield.text(),
            "TcHeader": self.ui.TcHfield.text(),
            "OutDir": self.ui.outdirfield.text(),
            "OutDoc": self.ui.outdocfield.text(),
        }
        dictn = temp.update_paths(dic)
        load.get_paths()
        self.dist_paths(dictn)


    def dist_paths(self, dic):
        try:
            self.ui.TmHfield.setText(dic["TmHeader"])
            self.ui.TcTmHfield.setText(dic["TcTmHeader"])
            self.ui.TmCfield.setText(dic["TmFile"])
            self.ui.TcHfiled.setText(dic["TcHeader"])
            self.ui.outdirfield.setText(dic["OutDir"])
            self.ui.outdocfield.setText(dic["OutDoc"])
        except:
            self.ui.console.append("WARN.:\tThe list of files to be distributed into all the fields isn't complete.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
