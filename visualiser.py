"""This module allows for GUI representation of the parsed data"""
from PySide6.QtCore import QMetaObject

from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QSizePolicy,
    QToolBox,
    QVBoxLayout,
    QPlainTextEdit,
    QWidget,
    QTableWidget,
    QTableWidgetItem,
    QScrollArea,
    QFrame,
    QAbstractScrollArea,
)
import sys, multiprocessing
import load, longdata

policy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)


class CommentWindow(QWidget):
    """Small window that shows informations about comments in the given entry."""

    def __init__(self, comment):
        super().__init__()
        self.setWindowTitle("Comment view")
        layout = QVBoxLayout()
        for i in comment:
            label = QLabel("Comment:")
            layout.addWidget(label)
            frame = QFrame()
            frame.setFrameShape(QFrame.Box)
            lay = QVBoxLayout(frame)
            button = QPushButton("Show full text", frame)
            button.clicked.connect(lambda: self.view_text(i.text))
            lay.addWidget(button)
            labeli = QLabel(frame)
            labeli.setText("Basic information:")
            lay.addWidget(labeli)
            table = QTableWidget(frame)
            intable(table, getdata(i))
            lay.addWidget(table)
            labe = QLabel(frame)
            labe.setText("Entries:")
            lay.addWidget(labe)
            table2 = QTableWidget(frame)
            intable(table2, list(i.entries.items()))
            lay.addWidget(table2)
            layout.addWidget(frame)
        self.setLayout(layout)

    def view_text(self, text):
        """Show a window with full text."""
        self.b = TextWindow(text)
        self.b.show()


class TextWindow(QWidget):
    """Small window that show parsed text."""

    def __init__(self, text):
        super().__init__()
        self.setWindowTitle("Full text view")
        layout = QVBoxLayout()
        textpol = QPlainTextEdit(text)
        textpol.setFrameShape(QFrame.NoFrame)
        textpol.setReadOnly(True)
        layout.addWidget(textpol)
        self.setLayout(layout)


class Ui_MainWindow(object):
    """This class holds functions that build up geometry and objects in the main window."""

    def setupUi(self, MainWindow, struct):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
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

        # self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def inter(self, struct):
        """Recursively create entries for each C-object in the parsed file."""
        page = QFrame()
        page.setFrameShape(QFrame.Box)
        page.setSizePolicy(policy)
        verlay = QVBoxLayout(page)
        methods = struct.__dir__()
        if "structures" in methods:
            toolbox = QToolBox(page)
            for i in struct.structures:
                subwid = self.inter(i)
                toolbox.addItem(subwid, i.text.replace("\n", "\\n")[:50] + "...")
            verlay.addWidget(toolbox)
        else:
            buttont = QPushButton("Show full text", page)
            buttont.clicked.connect(lambda: self.view_text(struct.text))
            verlay.addWidget(buttont)
        if "type" in methods:
            labeli = QLabel(page)
            labeli.setText("Extracted information:")
            verlay.addWidget(labeli)
            data = getdata(struct)
            table = QTableWidget(page)
            intable(table, data)
            verlay.addWidget(table)
        if "comment" in methods and len(struct.comment) > 0:
            button = QPushButton("View comments", page)
            # I cannot believe this works
            button.clicked.connect(lambda: self.view_comments(struct.comment))
            verlay.addWidget(button)
        if "entries" in methods:
            label2 = QLabel(page)
            label2.setText("Entries:")
            verlay.addWidget(label2)
            table2 = QTableWidget(page)
            intable(table2, list(struct.entries.items()))
            verlay.addWidget(table2)
        if "elements" in methods:
            label = QLabel(page)
            label.setText("Objects inside:")
            verlay.addWidget(label)
            toolbox = QToolBox(page)
            for i in struct.elements:
                subwid = self.inter(i)
                toolbox.addItem(subwid, i.text.replace("\n", "\\n"))
            verlay.addWidget(toolbox)
        return page

    def view_comments(self, comment):
        """Show a window with comments."""
        self.a = CommentWindow(comment)
        self.a.show()

    def view_text(self, text):
        """Show a window with full text."""
        self.b = TextWindow(text)
        self.b.show()


def getdata(struct):
    """Extract all posible showable (str, int) data about an object"""
    data = []
    dic = struct.__dict__
    for i in dic:
        if (type(dic[i]) is str or type(dic[i]) is int) and i != "text":
            try:
                data.append([longdata.translation[i], dic[i]])
            except KeyError:
                data.append([i + ":", dic[i]])
    return data


def intable(table, data):
    """Add the given data to the given table."""
    table.setColumnCount(2)
    table.setRowCount(len(data))
    for i in range(len(data)):
        e1 = QTableWidgetItem(data[i][0])
        e2 = QTableWidgetItem(str(data[i][1]))
        table.setItem(i, 0, e1)
        table.setItem(i, 1, e2)
        table.resizeColumnToContents(0)
        table.resizeColumnToContents(1)
    table.horizontalHeader().setVisible(False)
    table.verticalHeader().setVisible(False)
    table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)


class MainWindow(QMainWindow):
    """The class of the main window."""

    def __init__(self, struct):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self, struct)
        self.setWindowTitle("Structure viewer - " + str(struct.path))


def runt(struct):
    """Run the app in one process."""
    app = QApplication(sys.argv)
    window = MainWindow(struct)
    window.show()
    sys.exit(app.exec())


def main(struct=[load.head1]):
    """For each file create a process and run the visualiser in it."""
    for i in struct:
        t = multiprocessing.Process(target=runt, args=[i])
        t.start()
