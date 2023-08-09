"""This module allows for GUI representation of the parsed data"""
from PySide6.QtCore import QMetaObject

from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QToolBox, QVBoxLayout,
    QWidget, QTableWidget, QTableWidgetItem, QScrollArea, QGroupBox)
import sys
import load, longdata

policy = QSizePolicy(QSizePolicy.Preferred,QSizePolicy.MinimumExpanding)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, struct):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(710, 552)
        centralwidget = QWidget(MainWindow)
        verlay = QVBoxLayout(centralwidget)
        scrolarea = QScrollArea(centralwidget)
        scrolarea.setWidgetResizable(True)
        widget = self.inter(struct)
        widget.setSizePolicy(policy)
        scrolarea.setWidget(widget)
        verlay.addWidget(scrolarea)
        MainWindow.setCentralWidget(centralwidget)

        #self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)
        
    def inter(self, struct):
        page = QWidget()
        page.setSizePolicy(policy)
        verlay = QVBoxLayout(page)
        methods = struct.__dir__()
        if "structures" in methods:
            toolbox = QToolBox(page)
            for i in struct.structures:
                subwid = self.inter(i)
                toolbox.addItem(subwid, i.text.replace("\n","\\n"))
            verlay.addWidget(toolbox)
        if "type" in methods:
            data = getdata(struct)
            table = QTableWidget(page)
            intable(table,data)
            verlay.addWidget(table)
        if "elements" in methods:
            label = QLabel(page)
            label.setText("Objects inside:")
            verlay.addWidget(label)
            toolbox = QToolBox(page)
            for i in struct.elements:
                subwid = self.inter(i)
                toolbox.addItem(subwid, i.text.replace("\n","\\n"))
            verlay.addWidget(toolbox)
        if "entries" in methods:
            label2 = QLabel(page)
            label2.setText("Entries:")
            verlay.addWidget(label2)
            table2 = QTableWidget(page)
            intable(table2,list(struct.entries.items()))
            verlay.addWidget(table2)
        return page
            
def getdata(struct):
    data = []
    dic = struct.__dict__
    for i in dic:
        if (type(dic[i]) is str or type(dic[i]) is int) and i != "text":
            try:
                data.append([longdata.translation[i],dic[i]])
            except KeyError:
                data.append([i+":",dic[i]])
    return data


def intable(table, data):
    table.setColumnCount(2)
    table.setRowCount(len(data))
    for i in range(len(data)):
        e1 = QTableWidgetItem(data[i][0])
        e2 = QTableWidgetItem(str(data[i][1]))
        table.setItem(i,0,e1)
        table.setItem(i,1,e2)
        table.resizeColumnToContents(0)
        table.resizeColumnToContents(1)
    table.horizontalHeader().setVisible(False)
    table.verticalHeader().setVisible(False)



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self, load.head1)
        self.setWindowTitle("Structure viewer")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

#TODO: try normal C file, make file input more variable, implement comments
