# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPlainTextEdit, QPushButton, QSizePolicy,
    QStatusBar, QTabWidget, QTextBrowser, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(893, 890)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_27 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.horizontalLayout_4 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.tabWidget = QTabWidget(self.widget_2)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy1)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout = QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_34 = QVBoxLayout(self.groupBox)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.tabWidget1 = QTabWidget(self.groupBox)
        self.tabWidget1.setObjectName(u"tabWidget1")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tabWidget1.sizePolicy().hasHeightForWidth())
        self.tabWidget1.setSizePolicy(sizePolicy2)
        self.tabWidgetPage1 = QWidget()
        self.tabWidgetPage1.setObjectName(u"tabWidgetPage1")
        self.verticalLayout_23 = QVBoxLayout(self.tabWidgetPage1)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_30 = QLabel(self.tabWidgetPage1)
        self.label_30.setObjectName(u"label_30")
        sizePolicy2.setHeightForWidth(self.label_30.sizePolicy().hasHeightForWidth())
        self.label_30.setSizePolicy(sizePolicy2)

        self.verticalLayout_23.addWidget(self.label_30)

        self.label_4 = QLabel(self.tabWidgetPage1)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_23.addWidget(self.label_4)

        self.TmHfield = QPlainTextEdit(self.tabWidgetPage1)
        self.TmHfield.setObjectName(u"TmHfield")

        self.verticalLayout_23.addWidget(self.TmHfield)

        self.TmHbutton = QPushButton(self.tabWidgetPage1)
        self.TmHbutton.setObjectName(u"TmHbutton")

        self.verticalLayout_23.addWidget(self.TmHbutton)

        self.tabWidget1.addTab(self.tabWidgetPage1, "")
        self.tabWidgetPage2 = QWidget()
        self.tabWidgetPage2.setObjectName(u"tabWidgetPage2")
        self.verticalLayout_24 = QVBoxLayout(self.tabWidgetPage2)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_31 = QLabel(self.tabWidgetPage2)
        self.label_31.setObjectName(u"label_31")
        sizePolicy2.setHeightForWidth(self.label_31.sizePolicy().hasHeightForWidth())
        self.label_31.setSizePolicy(sizePolicy2)

        self.verticalLayout_24.addWidget(self.label_31)

        self.label_8 = QLabel(self.tabWidgetPage2)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_24.addWidget(self.label_8)

        self.TmCfield = QPlainTextEdit(self.tabWidgetPage2)
        self.TmCfield.setObjectName(u"TmCfield")

        self.verticalLayout_24.addWidget(self.TmCfield)

        self.TmCbutton = QPushButton(self.tabWidgetPage2)
        self.TmCbutton.setObjectName(u"TmCbutton")

        self.verticalLayout_24.addWidget(self.TmCbutton)

        self.tabWidget1.addTab(self.tabWidgetPage2, "")
        self.tabWidgetPage3 = QWidget()
        self.tabWidgetPage3.setObjectName(u"tabWidgetPage3")
        self.verticalLayout_25 = QVBoxLayout(self.tabWidgetPage3)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_32 = QLabel(self.tabWidgetPage3)
        self.label_32.setObjectName(u"label_32")
        sizePolicy2.setHeightForWidth(self.label_32.sizePolicy().hasHeightForWidth())
        self.label_32.setSizePolicy(sizePolicy2)

        self.verticalLayout_25.addWidget(self.label_32)

        self.label_10 = QLabel(self.tabWidgetPage3)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_25.addWidget(self.label_10)

        self.TcHfield = QPlainTextEdit(self.tabWidgetPage3)
        self.TcHfield.setObjectName(u"TcHfield")

        self.verticalLayout_25.addWidget(self.TcHfield)

        self.TcHbutton = QPushButton(self.tabWidgetPage3)
        self.TcHbutton.setObjectName(u"TcHbutton")

        self.verticalLayout_25.addWidget(self.TcHbutton)

        self.tabWidget1.addTab(self.tabWidgetPage3, "")
        self.tabWidgetPage4 = QWidget()
        self.tabWidgetPage4.setObjectName(u"tabWidgetPage4")
        self.verticalLayout_26 = QVBoxLayout(self.tabWidgetPage4)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_33 = QLabel(self.tabWidgetPage4)
        self.label_33.setObjectName(u"label_33")
        sizePolicy2.setHeightForWidth(self.label_33.sizePolicy().hasHeightForWidth())
        self.label_33.setSizePolicy(sizePolicy2)

        self.verticalLayout_26.addWidget(self.label_33)

        self.label_12 = QLabel(self.tabWidgetPage4)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_26.addWidget(self.label_12)

        self.TcTmHfield = QPlainTextEdit(self.tabWidgetPage4)
        self.TcTmHfield.setObjectName(u"TcTmHfield")

        self.verticalLayout_26.addWidget(self.TcTmHfield)

        self.TcTmHbutton = QPushButton(self.tabWidgetPage4)
        self.TcTmHbutton.setObjectName(u"TcTmHbutton")
        self.TcTmHbutton.setEnabled(True)

        self.verticalLayout_26.addWidget(self.TcTmHbutton)

        self.tabWidget1.addTab(self.tabWidgetPage4, "")

        self.verticalLayout_34.addWidget(self.tabWidget1)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_3 = QGroupBox(self.tab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_36 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.tabWidget_3 = QTabWidget(self.groupBox_3)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tabWidget_3.sizePolicy().hasHeightForWidth())
        self.tabWidget_3.setSizePolicy(sizePolicy3)
        self.tabWidget_3Page1 = QWidget()
        self.tabWidget_3Page1.setObjectName(u"tabWidget_3Page1")
        self.verticalLayout_19 = QVBoxLayout(self.tabWidget_3Page1)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_24 = QLabel(self.tabWidget_3Page1)
        self.label_24.setObjectName(u"label_24")
        sizePolicy2.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy2)

        self.verticalLayout_19.addWidget(self.label_24)

        self.outdirfield = QLineEdit(self.tabWidget_3Page1)
        self.outdirfield.setObjectName(u"outdirfield")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.outdirfield.sizePolicy().hasHeightForWidth())
        self.outdirfield.setSizePolicy(sizePolicy4)

        self.verticalLayout_19.addWidget(self.outdirfield)

        self.outdirbutton = QPushButton(self.tabWidget_3Page1)
        self.outdirbutton.setObjectName(u"outdirbutton")

        self.verticalLayout_19.addWidget(self.outdirbutton)

        self.tabWidget_3.addTab(self.tabWidget_3Page1, "")
        self.tabWidget_3Page2 = QWidget()
        self.tabWidget_3Page2.setObjectName(u"tabWidget_3Page2")
        self.verticalLayout_20 = QVBoxLayout(self.tabWidget_3Page2)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_25 = QLabel(self.tabWidget_3Page2)
        self.label_25.setObjectName(u"label_25")
        sizePolicy2.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy2)

        self.verticalLayout_20.addWidget(self.label_25)

        self.outdocfield = QLineEdit(self.tabWidget_3Page2)
        self.outdocfield.setObjectName(u"outdocfield")
        sizePolicy4.setHeightForWidth(self.outdocfield.sizePolicy().hasHeightForWidth())
        self.outdocfield.setSizePolicy(sizePolicy4)

        self.verticalLayout_20.addWidget(self.outdocfield)

        self.outdocbutton = QPushButton(self.tabWidget_3Page2)
        self.outdocbutton.setObjectName(u"outdocbutton")

        self.verticalLayout_20.addWidget(self.outdocbutton)

        self.tabWidget_3.addTab(self.tabWidget_3Page2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_3 = QVBoxLayout(self.tab_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_26 = QLabel(self.tab_3)
        self.label_26.setObjectName(u"label_26")
        sizePolicy2.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy2)

        self.verticalLayout_3.addWidget(self.label_26)

        self.outxlsfield = QLineEdit(self.tab_3)
        self.outxlsfield.setObjectName(u"outxlsfield")
        sizePolicy4.setHeightForWidth(self.outxlsfield.sizePolicy().hasHeightForWidth())
        self.outxlsfield.setSizePolicy(sizePolicy4)

        self.verticalLayout_3.addWidget(self.outxlsfield)

        self.outxlsbutton = QPushButton(self.tab_3)
        self.outxlsbutton.setObjectName(u"outxlsbutton")

        self.verticalLayout_3.addWidget(self.outxlsbutton)

        self.tabWidget_3.addTab(self.tab_3, "")

        self.verticalLayout_36.addWidget(self.tabWidget_3)


        self.verticalLayout.addWidget(self.groupBox_3)

        self.pathsbutton = QPushButton(self.tab)
        self.pathsbutton.setObjectName(u"pathsbutton")

        self.verticalLayout.addWidget(self.pathsbutton)

        self.tabWidget.addTab(self.tab, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.verticalLayout_30 = QVBoxLayout(self.tab_6)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.groupBox_4 = QGroupBox(self.tab_6)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_34 = QLabel(self.groupBox_4)
        self.label_34.setObjectName(u"label_34")

        self.verticalLayout_9.addWidget(self.label_34)

        self.configfield = QLineEdit(self.groupBox_4)
        self.configfield.setObjectName(u"configfield")

        self.verticalLayout_9.addWidget(self.configfield)

        self.widget_13 = QWidget(self.groupBox_4)
        self.widget_13.setObjectName(u"widget_13")
        self.horizontalLayout_13 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.configbutton = QPushButton(self.widget_13)
        self.configbutton.setObjectName(u"configbutton")

        self.horizontalLayout_13.addWidget(self.configbutton)

        self.configdefault = QPushButton(self.widget_13)
        self.configdefault.setObjectName(u"configdefault")

        self.horizontalLayout_13.addWidget(self.configdefault)


        self.verticalLayout_9.addWidget(self.widget_13)

        self.widget_4 = QWidget(self.groupBox_4)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.configload = QPushButton(self.widget_4)
        self.configload.setObjectName(u"configload")

        self.horizontalLayout_6.addWidget(self.configload)

        self.configsave = QPushButton(self.widget_4)
        self.configsave.setObjectName(u"configsave")

        self.horizontalLayout_6.addWidget(self.configsave)


        self.verticalLayout_9.addWidget(self.widget_4)


        self.verticalLayout_30.addWidget(self.groupBox_4)

        self.groupBox_5 = QGroupBox(self.tab_6)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_28 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.tabWidget_2 = QTabWidget(self.groupBox_5)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.Page_2 = QWidget()
        self.Page_2.setObjectName(u"Page_2")
        self.verticalLayout_31 = QVBoxLayout(self.Page_2)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.label = QLabel(self.Page_2)
        self.label.setObjectName(u"label")

        self.verticalLayout_31.addWidget(self.label)

        self.label_36 = QLabel(self.Page_2)
        self.label_36.setObjectName(u"label_36")

        self.verticalLayout_31.addWidget(self.label_36)

        self.prefield = QPlainTextEdit(self.Page_2)
        self.prefield.setObjectName(u"prefield")
        sizePolicy1.setHeightForWidth(self.prefield.sizePolicy().hasHeightForWidth())
        self.prefield.setSizePolicy(sizePolicy1)
        self.prefield.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.verticalLayout_31.addWidget(self.prefield)

        self.prebutton = QPushButton(self.Page_2)
        self.prebutton.setObjectName(u"prebutton")

        self.verticalLayout_31.addWidget(self.prebutton)

        self.tabWidget_2.addTab(self.Page_2, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_2 = QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.tab_2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.label_46 = QLabel(self.tab_2)
        self.label_46.setObjectName(u"label_46")

        self.verticalLayout_2.addWidget(self.label_46)

        self.namfield = QPlainTextEdit(self.tab_2)
        self.namfield.setObjectName(u"namfield")
        sizePolicy1.setHeightForWidth(self.namfield.sizePolicy().hasHeightForWidth())
        self.namfield.setSizePolicy(sizePolicy1)
        self.namfield.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.verticalLayout_2.addWidget(self.namfield)

        self.nambutton = QPushButton(self.tab_2)
        self.nambutton.setObjectName(u"nambutton")

        self.verticalLayout_2.addWidget(self.nambutton)

        self.tabWidget_2.addTab(self.tab_2, "")
        self.Page_1 = QWidget()
        self.Page_1.setObjectName(u"Page_1")
        self.verticalLayout_32 = QVBoxLayout(self.Page_1)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.label_3 = QLabel(self.Page_1)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_32.addWidget(self.label_3)

        self.label_37 = QLabel(self.Page_1)
        self.label_37.setObjectName(u"label_37")

        self.verticalLayout_32.addWidget(self.label_37)

        self.mibfield = QPlainTextEdit(self.Page_1)
        self.mibfield.setObjectName(u"mibfield")
        sizePolicy1.setHeightForWidth(self.mibfield.sizePolicy().hasHeightForWidth())
        self.mibfield.setSizePolicy(sizePolicy1)
        self.mibfield.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.verticalLayout_32.addWidget(self.mibfield)

        self.mibbutton = QPushButton(self.Page_1)
        self.mibbutton.setObjectName(u"mibbutton")

        self.verticalLayout_32.addWidget(self.mibbutton)

        self.tabWidget_2.addTab(self.Page_1, "")

        self.verticalLayout_28.addWidget(self.tabWidget_2)


        self.verticalLayout_30.addWidget(self.groupBox_5)

        self.tabWidget.addTab(self.tab_6, "")

        self.horizontalLayout_4.addWidget(self.tabWidget)

        self.widget_6 = QWidget(self.widget_2)
        self.widget_6.setObjectName(u"widget_6")
        self.gridLayout = QGridLayout(self.widget_6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.compute_all = QPushButton(self.widget_6)
        self.compute_all.setObjectName(u"compute_all")
        font = QFont()
        font.setBold(False)
        font.setItalic(True)
        font.setStrikeOut(False)
        self.compute_all.setFont(font)

        self.gridLayout.addWidget(self.compute_all, 2, 0, 1, 1)

        self.frame_5 = QFrame(self.widget_6)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Plain)
        self.frame_5.setLineWidth(1)
        self.verticalLayout_6 = QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setTextFormat(Qt.MarkdownText)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_6)

        self.parsebutton = QPushButton(self.frame_5)
        self.parsebutton.setObjectName(u"parsebutton")
        self.parsebutton.setAutoExclusive(False)
        self.parsebutton.setAutoDefault(False)

        self.verticalLayout_6.addWidget(self.parsebutton)

        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setTextFormat(Qt.MarkdownText)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_5)


        self.gridLayout.addWidget(self.frame_5, 0, 0, 1, 1)

        self.frame_8 = QFrame(self.widget_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.widget_7 = QWidget(self.frame_8)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_10 = QVBoxLayout(self.widget_7)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_15 = QLabel(self.widget_7)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_15)

        self.Tcbuild = QPushButton(self.widget_7)
        self.Tcbuild.setObjectName(u"Tcbuild")
        self.Tcbuild.setEnabled(False)

        self.verticalLayout_10.addWidget(self.Tcbuild)

        self.label_16 = QLabel(self.widget_7)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_16)


        self.horizontalLayout_8.addWidget(self.widget_7)

        self.widget_8 = QWidget(self.frame_8)
        self.widget_8.setObjectName(u"widget_8")
        self.verticalLayout_29 = QVBoxLayout(self.widget_8)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.label_17 = QLabel(self.widget_8)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout_29.addWidget(self.label_17)

        self.Tmbuild = QPushButton(self.widget_8)
        self.Tmbuild.setObjectName(u"Tmbuild")
        self.Tmbuild.setEnabled(False)

        self.verticalLayout_29.addWidget(self.Tmbuild)

        self.label_35 = QLabel(self.widget_8)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setAlignment(Qt.AlignCenter)

        self.verticalLayout_29.addWidget(self.label_35)


        self.horizontalLayout_8.addWidget(self.widget_8)


        self.gridLayout.addWidget(self.frame_8, 2, 1, 1, 1)

        self.frame_9 = QFrame(self.widget_6)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.verticalLayout_33 = QVBoxLayout(self.frame_9)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.widget_10 = QWidget(self.frame_9)
        self.widget_10.setObjectName(u"widget_10")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_39 = QLabel(self.widget_10)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_39)

        self.mibgen = QPushButton(self.widget_10)
        self.mibgen.setObjectName(u"mibgen")
        self.mibgen.setEnabled(False)

        self.horizontalLayout_10.addWidget(self.mibgen)

        self.label_38 = QLabel(self.widget_10)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_38)


        self.verticalLayout_33.addWidget(self.widget_10)

        self.widget_11 = QWidget(self.frame_9)
        self.widget_11.setObjectName(u"widget_11")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_40 = QLabel(self.widget_11)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_40)

        self.docgen = QPushButton(self.widget_11)
        self.docgen.setObjectName(u"docgen")
        self.docgen.setEnabled(False)

        self.horizontalLayout_9.addWidget(self.docgen)

        self.label_41 = QLabel(self.widget_11)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_41)


        self.verticalLayout_33.addWidget(self.widget_11)

        self.widget = QWidget(self.frame_9)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_7 = QHBoxLayout(self.widget)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_47 = QLabel(self.widget)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_47)

        self.xlsgen = QPushButton(self.widget)
        self.xlsgen.setObjectName(u"xlsgen")
        self.xlsgen.setEnabled(False)

        self.horizontalLayout_7.addWidget(self.xlsgen)

        self.label_48 = QLabel(self.widget)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_48)


        self.verticalLayout_33.addWidget(self.widget)


        self.gridLayout.addWidget(self.frame_9, 3, 1, 1, 1)

        self.frame_6 = QFrame(self.widget_6)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.verticalLayout_35 = QVBoxLayout(self.frame_6)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.widget_14 = QWidget(self.frame_6)
        self.widget_14.setObjectName(u"widget_14")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_42 = QLabel(self.widget_14)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_42)

        self.mibsave = QPushButton(self.widget_14)
        self.mibsave.setObjectName(u"mibsave")
        self.mibsave.setEnabled(False)

        self.horizontalLayout_11.addWidget(self.mibsave)

        self.label_43 = QLabel(self.widget_14)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_43)


        self.verticalLayout_35.addWidget(self.widget_14)

        self.widget_15 = QWidget(self.frame_6)
        self.widget_15.setObjectName(u"widget_15")
        self.horizontalLayout_12 = QHBoxLayout(self.widget_15)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_44 = QLabel(self.widget_15)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_44)

        self.docsave = QPushButton(self.widget_15)
        self.docsave.setObjectName(u"docsave")
        self.docsave.setEnabled(False)

        self.horizontalLayout_12.addWidget(self.docsave)

        self.label_45 = QLabel(self.widget_15)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_45)


        self.verticalLayout_35.addWidget(self.widget_15)

        self.widget_3 = QWidget(self.frame_6)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_14 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_49 = QLabel(self.widget_3)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.label_49)

        self.xlssave = QPushButton(self.widget_3)
        self.xlssave.setObjectName(u"xlssave")
        self.xlssave.setEnabled(False)

        self.horizontalLayout_14.addWidget(self.xlssave)

        self.label_50 = QLabel(self.widget_3)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.label_50)


        self.verticalLayout_35.addWidget(self.widget_3)


        self.gridLayout.addWidget(self.frame_6, 3, 0, 1, 1)

        self.frame_7 = QFrame(self.widget_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.verticalLayout_7 = QVBoxLayout(self.frame_7)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame = QFrame(self.frame_7)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout.addWidget(self.label_7)

        self.TmHview = QPushButton(self.frame)
        self.TmHview.setObjectName(u"TmHview")
        self.TmHview.setEnabled(False)

        self.horizontalLayout.addWidget(self.TmHview)


        self.verticalLayout_7.addWidget(self.frame)

        self.frame_2 = QFrame(self.frame_7)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_2.addWidget(self.label_9)

        self.TmCview = QPushButton(self.frame_2)
        self.TmCview.setObjectName(u"TmCview")
        self.TmCview.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.TmCview)


        self.verticalLayout_7.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame_7)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_11 = QLabel(self.frame_3)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_3.addWidget(self.label_11)

        self.TcHview = QPushButton(self.frame_3)
        self.TcHview.setObjectName(u"TcHview")
        self.TcHview.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.TcHview)


        self.verticalLayout_7.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_7)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_13 = QLabel(self.frame_4)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_5.addWidget(self.label_13)

        self.TcTmHview = QPushButton(self.frame_4)
        self.TcTmHview.setObjectName(u"TcTmHview")
        self.TcTmHview.setEnabled(False)
        self.TcTmHview.setCheckable(False)
        self.TcTmHview.setChecked(False)
        self.TcTmHview.setFlat(False)

        self.horizontalLayout_5.addWidget(self.TcTmHview)


        self.verticalLayout_7.addWidget(self.frame_4)


        self.gridLayout.addWidget(self.frame_7, 0, 1, 1, 1)


        self.horizontalLayout_4.addWidget(self.widget_6)


        self.verticalLayout_27.addWidget(self.widget_2)

        self.console = QTextBrowser(self.centralwidget)
        self.console.setObjectName(u"console")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.console.sizePolicy().hasHeightForWidth())
        self.console.setSizePolicy(sizePolicy5)

        self.verticalLayout_27.addWidget(self.console)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget1.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.parsebutton.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Input", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"File paths:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"(entries separated by \";\", whitespace characters ignored)", None))
        self.TmHfield.setPlaceholderText(QCoreApplication.translate("MainWindow", u"path to files", None))
        self.TmHbutton.setText(QCoreApplication.translate("MainWindow", u"Browse files", None))
        self.tabWidget1.setTabText(self.tabWidget1.indexOf(self.tabWidgetPage1), QCoreApplication.translate("MainWindow", u"Tm .h", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"File path:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"(entries separated by \";\", whitespace characters ignored)", None))
        self.TmCfield.setPlaceholderText(QCoreApplication.translate("MainWindow", u"path to files", None))
        self.TmCbutton.setText(QCoreApplication.translate("MainWindow", u"Browse files", None))
        self.tabWidget1.setTabText(self.tabWidget1.indexOf(self.tabWidgetPage2), QCoreApplication.translate("MainWindow", u"Tm .c", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"File path:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"(entries separated by \";\", whitespace characters ignored)", None))
        self.TcHfield.setPlaceholderText(QCoreApplication.translate("MainWindow", u"path to files", None))
        self.TcHbutton.setText(QCoreApplication.translate("MainWindow", u"Browse files", None))
        self.tabWidget1.setTabText(self.tabWidget1.indexOf(self.tabWidgetPage3), QCoreApplication.translate("MainWindow", u"Tc .h", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"File path:", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"(entries separated by \";\", whitespace characters ignored)", None))
        self.TcTmHfield.setPlainText("")
        self.TcTmHfield.setPlaceholderText(QCoreApplication.translate("MainWindow", u"path to files", None))
        self.TcTmHbutton.setText(QCoreApplication.translate("MainWindow", u"Browse files", None))
        self.tabWidget1.setTabText(self.tabWidget1.indexOf(self.tabWidgetPage4), QCoreApplication.translate("MainWindow", u"TcTm .h", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Output", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Directory path:", None))
        self.outdirfield.setText("")
        self.outdirfield.setPlaceholderText(QCoreApplication.translate("MainWindow", u"path to directory", None))
        self.outdirbutton.setText(QCoreApplication.translate("MainWindow", u"Browse files", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tabWidget_3Page1), QCoreApplication.translate("MainWindow", u"MIB", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"File path:", None))
        self.outdocfield.setPlaceholderText(QCoreApplication.translate("MainWindow", u"path to file", None))
        self.outdocbutton.setText(QCoreApplication.translate("MainWindow", u"Browse files", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tabWidget_3Page2), QCoreApplication.translate("MainWindow", u".docx", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"File path:", None))
        self.outxlsfield.setPlaceholderText(QCoreApplication.translate("MainWindow", u"path to file", None))
        self.outxlsbutton.setText(QCoreApplication.translate("MainWindow", u"Browse files", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u".xls", None))
#if QT_CONFIG(tooltip)
        self.pathsbutton.setToolTip(QCoreApplication.translate("MainWindow", u"write the information above\n"
"to the runtime config files", None))
#endif // QT_CONFIG(tooltip)
        self.pathsbutton.setText(QCoreApplication.translate("MainWindow", u"Use", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Paths", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Config and paths file", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Config directory path", None))
        self.configfield.setPlaceholderText(QCoreApplication.translate("MainWindow", u"path to config directory", None))
        self.configbutton.setText(QCoreApplication.translate("MainWindow", u"Browse files", None))
#if QT_CONFIG(tooltip)
        self.configdefault.setToolTip(QCoreApplication.translate("MainWindow", u"get default config directory", None))
#endif // QT_CONFIG(tooltip)
        self.configdefault.setText(QCoreApplication.translate("MainWindow", u"Default", None))
#if QT_CONFIG(tooltip)
        self.configload.setToolTip(QCoreApplication.translate("MainWindow", u"move config files from the directory\n"
"above to the runtime config directory", None))
#endif // QT_CONFIG(tooltip)
        self.configload.setText(QCoreApplication.translate("MainWindow", u"Load", None))
#if QT_CONFIG(tooltip)
        self.configsave.setToolTip(QCoreApplication.translate("MainWindow", u"write the information present to config \n"
"files in the directory above", None))
#endif // QT_CONFIG(tooltip)
        self.configsave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Config settings", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"What variables are seen as \"defined\" by preprocessor.", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"(entries separated by \";\", whitespace characters ignored)", None))
        self.prefield.setPlainText("")
        self.prefield.setPlaceholderText("")
#if QT_CONFIG(tooltip)
        self.prebutton.setToolTip(QCoreApplication.translate("MainWindow", u"write the information above\n"
"to the runtime config files", None))
#endif // QT_CONFIG(tooltip)
        self.prebutton.setText(QCoreApplication.translate("MainWindow", u"Use", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.Page_2), QCoreApplication.translate("MainWindow", u"Preprocessing", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"How should names of Tm/Tc packet parameters look.", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"(entries separated by \";\", whitespace characters ignored)", None))
        self.namfield.setPlainText("")
        self.namfield.setPlaceholderText("")
#if QT_CONFIG(tooltip)
        self.nambutton.setToolTip(QCoreApplication.translate("MainWindow", u"write the information above\n"
"to the runtime config files", None))
#endif // QT_CONFIG(tooltip)
        self.nambutton.setText(QCoreApplication.translate("MainWindow", u"Use", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Param. name", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"What MIB tables should be generated.", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"(entries separated by \";\", whitespace characters ignored)", None))
#if QT_CONFIG(tooltip)
        self.mibbutton.setToolTip(QCoreApplication.translate("MainWindow", u"write the information above\n"
"to the runtime config files", None))
#endif // QT_CONFIG(tooltip)
        self.mibbutton.setText(QCoreApplication.translate("MainWindow", u"Use", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.Page_1), QCoreApplication.translate("MainWindow", u"Generation", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"Config", None))
#if QT_CONFIG(tooltip)
        self.compute_all.setToolTip(QCoreApplication.translate("MainWindow", u"push the all buttons around in the clockwise order", None))
#endif // QT_CONFIG(tooltip)
        self.compute_all.setText(QCoreApplication.translate("MainWindow", u"Compute\n"
"all", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"->", None))
        self.parsebutton.setText(QCoreApplication.translate("MainWindow", u"Parse!", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"->", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"v", None))
        self.Tcbuild.setText(QCoreApplication.translate("MainWindow", u"Interpret\n"
"TC", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"v", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"v", None))
        self.Tmbuild.setText(QCoreApplication.translate("MainWindow", u"Interpret\n"
"TM", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"v", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"<-", None))
        self.mibgen.setText(QCoreApplication.translate("MainWindow", u"Generate MIB", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"<-", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"<-", None))
        self.docgen.setText(QCoreApplication.translate("MainWindow", u"Generate .docx.", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"<-", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"<-", None))
        self.xlsgen.setText(QCoreApplication.translate("MainWindow", u"Generate .xls", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"<-", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"<-", None))
        self.mibsave.setText(QCoreApplication.translate("MainWindow", u"Save MIB", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"<-", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"<-", None))
        self.docsave.setText(QCoreApplication.translate("MainWindow", u"Save .docx", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"<-", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"<-", None))
        self.xlssave.setText(QCoreApplication.translate("MainWindow", u"Save .xls", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"<-", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Tm .h file", None))
        self.TmHview.setText(QCoreApplication.translate("MainWindow", u"View", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Tm .c file", None))
        self.TmCview.setText(QCoreApplication.translate("MainWindow", u"View", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Tc .h file", None))
        self.TcHview.setText(QCoreApplication.translate("MainWindow", u"View", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"TcTm .h file", None))
        self.TcTmHview.setText(QCoreApplication.translate("MainWindow", u"View", None))
        self.console.setMarkdown("")
        self.console.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.console.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Warnings, errors, etc. will be displayed here...", None))
    # retranslateUi

