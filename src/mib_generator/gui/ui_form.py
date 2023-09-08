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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPlainTextEdit, QPushButton, QSizePolicy, QStatusBar,
    QTabWidget, QTextBrowser, QToolBox, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(893, 780)
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
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout = QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_34 = QVBoxLayout(self.groupBox)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.toolBox = QToolBox(self.groupBox)
        self.toolBox.setObjectName(u"toolBox")
        self.page_17 = QWidget()
        self.page_17.setObjectName(u"page_17")
        self.page_17.setGeometry(QRect(0, 0, 404, 97))
        self.verticalLayout_23 = QVBoxLayout(self.page_17)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_30 = QLabel(self.page_17)
        self.label_30.setObjectName(u"label_30")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_30.sizePolicy().hasHeightForWidth())
        self.label_30.setSizePolicy(sizePolicy1)

        self.verticalLayout_23.addWidget(self.label_30)

        self.lineEdit_17 = QLineEdit(self.page_17)
        self.lineEdit_17.setObjectName(u"lineEdit_17")

        self.verticalLayout_23.addWidget(self.lineEdit_17)

        self.pushButton_24 = QPushButton(self.page_17)
        self.pushButton_24.setObjectName(u"pushButton_24")

        self.verticalLayout_23.addWidget(self.pushButton_24)

        self.toolBox.addItem(self.page_17, u"Tm .h file")
        self.page_18 = QWidget()
        self.page_18.setObjectName(u"page_18")
        self.page_18.setGeometry(QRect(0, 0, 404, 97))
        self.verticalLayout_24 = QVBoxLayout(self.page_18)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_31 = QLabel(self.page_18)
        self.label_31.setObjectName(u"label_31")
        sizePolicy1.setHeightForWidth(self.label_31.sizePolicy().hasHeightForWidth())
        self.label_31.setSizePolicy(sizePolicy1)

        self.verticalLayout_24.addWidget(self.label_31)

        self.lineEdit_18 = QLineEdit(self.page_18)
        self.lineEdit_18.setObjectName(u"lineEdit_18")

        self.verticalLayout_24.addWidget(self.lineEdit_18)

        self.pushButton_25 = QPushButton(self.page_18)
        self.pushButton_25.setObjectName(u"pushButton_25")

        self.verticalLayout_24.addWidget(self.pushButton_25)

        self.toolBox.addItem(self.page_18, u"Tm .c file")
        self.page_19 = QWidget()
        self.page_19.setObjectName(u"page_19")
        self.page_19.setGeometry(QRect(0, 0, 404, 97))
        self.verticalLayout_25 = QVBoxLayout(self.page_19)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_32 = QLabel(self.page_19)
        self.label_32.setObjectName(u"label_32")
        sizePolicy1.setHeightForWidth(self.label_32.sizePolicy().hasHeightForWidth())
        self.label_32.setSizePolicy(sizePolicy1)

        self.verticalLayout_25.addWidget(self.label_32)

        self.lineEdit_19 = QLineEdit(self.page_19)
        self.lineEdit_19.setObjectName(u"lineEdit_19")

        self.verticalLayout_25.addWidget(self.lineEdit_19)

        self.pushButton_26 = QPushButton(self.page_19)
        self.pushButton_26.setObjectName(u"pushButton_26")

        self.verticalLayout_25.addWidget(self.pushButton_26)

        self.toolBox.addItem(self.page_19, u"Tc .h file")
        self.page_20 = QWidget()
        self.page_20.setObjectName(u"page_20")
        self.page_20.setGeometry(QRect(0, 0, 404, 97))
        self.verticalLayout_26 = QVBoxLayout(self.page_20)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_33 = QLabel(self.page_20)
        self.label_33.setObjectName(u"label_33")
        sizePolicy1.setHeightForWidth(self.label_33.sizePolicy().hasHeightForWidth())
        self.label_33.setSizePolicy(sizePolicy1)

        self.verticalLayout_26.addWidget(self.label_33)

        self.lineEdit_20 = QLineEdit(self.page_20)
        self.lineEdit_20.setObjectName(u"lineEdit_20")

        self.verticalLayout_26.addWidget(self.lineEdit_20)

        self.pushButton_27 = QPushButton(self.page_20)
        self.pushButton_27.setObjectName(u"pushButton_27")

        self.verticalLayout_26.addWidget(self.pushButton_27)

        self.toolBox.addItem(self.page_20, u"TcTm .h file")

        self.verticalLayout_34.addWidget(self.toolBox)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_3 = QGroupBox(self.tab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_36 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.toolBox_3 = QToolBox(self.groupBox_3)
        self.toolBox_3.setObjectName(u"toolBox_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.toolBox_3.sizePolicy().hasHeightForWidth())
        self.toolBox_3.setSizePolicy(sizePolicy2)
        self.page_11 = QWidget()
        self.page_11.setObjectName(u"page_11")
        self.page_11.setGeometry(QRect(0, 0, 404, 98))
        self.verticalLayout_19 = QVBoxLayout(self.page_11)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_24 = QLabel(self.page_11)
        self.label_24.setObjectName(u"label_24")
        sizePolicy1.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy1)

        self.verticalLayout_19.addWidget(self.label_24)

        self.lineEdit_11 = QLineEdit(self.page_11)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lineEdit_11.sizePolicy().hasHeightForWidth())
        self.lineEdit_11.setSizePolicy(sizePolicy3)

        self.verticalLayout_19.addWidget(self.lineEdit_11)

        self.pushButton_18 = QPushButton(self.page_11)
        self.pushButton_18.setObjectName(u"pushButton_18")

        self.verticalLayout_19.addWidget(self.pushButton_18)

        self.toolBox_3.addItem(self.page_11, u"MIB")
        self.page_12 = QWidget()
        self.page_12.setObjectName(u"page_12")
        self.page_12.setGeometry(QRect(0, 0, 404, 98))
        self.verticalLayout_20 = QVBoxLayout(self.page_12)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_25 = QLabel(self.page_12)
        self.label_25.setObjectName(u"label_25")
        sizePolicy1.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy1)

        self.verticalLayout_20.addWidget(self.label_25)

        self.lineEdit_12 = QLineEdit(self.page_12)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        sizePolicy3.setHeightForWidth(self.lineEdit_12.sizePolicy().hasHeightForWidth())
        self.lineEdit_12.setSizePolicy(sizePolicy3)

        self.verticalLayout_20.addWidget(self.lineEdit_12)

        self.pushButton_19 = QPushButton(self.page_12)
        self.pushButton_19.setObjectName(u"pushButton_19")

        self.verticalLayout_20.addWidget(self.pushButton_19)

        self.toolBox_3.addItem(self.page_12, u".docx")

        self.verticalLayout_36.addWidget(self.toolBox_3)


        self.verticalLayout.addWidget(self.groupBox_3)

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

        self.lineEdit_21 = QLineEdit(self.groupBox_4)
        self.lineEdit_21.setObjectName(u"lineEdit_21")

        self.verticalLayout_9.addWidget(self.lineEdit_21)

        self.widget_13 = QWidget(self.groupBox_4)
        self.widget_13.setObjectName(u"widget_13")
        self.horizontalLayout_13 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.pushButton_28 = QPushButton(self.widget_13)
        self.pushButton_28.setObjectName(u"pushButton_28")

        self.horizontalLayout_13.addWidget(self.pushButton_28)

        self.pushButton_31 = QPushButton(self.widget_13)
        self.pushButton_31.setObjectName(u"pushButton_31")

        self.horizontalLayout_13.addWidget(self.pushButton_31)


        self.verticalLayout_9.addWidget(self.widget_13)

        self.widget_4 = QWidget(self.groupBox_4)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pushButton_29 = QPushButton(self.widget_4)
        self.pushButton_29.setObjectName(u"pushButton_29")

        self.horizontalLayout_6.addWidget(self.pushButton_29)

        self.pushButton_30 = QPushButton(self.widget_4)
        self.pushButton_30.setObjectName(u"pushButton_30")

        self.horizontalLayout_6.addWidget(self.pushButton_30)


        self.verticalLayout_9.addWidget(self.widget_4)


        self.verticalLayout_30.addWidget(self.groupBox_4)

        self.groupBox_5 = QGroupBox(self.tab_6)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_28 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.toolBox_2 = QToolBox(self.groupBox_5)
        self.toolBox_2.setObjectName(u"toolBox_2")
        self.page_21 = QWidget()
        self.page_21.setObjectName(u"page_21")
        self.page_21.setGeometry(QRect(0, 0, 404, 173))
        self.verticalLayout_31 = QVBoxLayout(self.page_21)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.label_36 = QLabel(self.page_21)
        self.label_36.setObjectName(u"label_36")

        self.verticalLayout_31.addWidget(self.label_36)

        self.plainTextEdit = QPlainTextEdit(self.page_21)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.verticalLayout_31.addWidget(self.plainTextEdit)

        self.pushButton_34 = QPushButton(self.page_21)
        self.pushButton_34.setObjectName(u"pushButton_34")

        self.verticalLayout_31.addWidget(self.pushButton_34)

        self.toolBox_2.addItem(self.page_21, u"Parsing preprocessor config")
        self.page_22 = QWidget()
        self.page_22.setObjectName(u"page_22")
        self.page_22.setGeometry(QRect(0, 0, 428, 186))
        self.verticalLayout_32 = QVBoxLayout(self.page_22)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.label_37 = QLabel(self.page_22)
        self.label_37.setObjectName(u"label_37")

        self.verticalLayout_32.addWidget(self.label_37)

        self.plainTextEdit_2 = QPlainTextEdit(self.page_22)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")

        self.verticalLayout_32.addWidget(self.plainTextEdit_2)

        self.pushButton_35 = QPushButton(self.page_22)
        self.pushButton_35.setObjectName(u"pushButton_35")

        self.verticalLayout_32.addWidget(self.pushButton_35)

        self.toolBox_2.addItem(self.page_22, u"MIB generation config")

        self.verticalLayout_28.addWidget(self.toolBox_2)


        self.verticalLayout_30.addWidget(self.groupBox_5)

        self.tabWidget.addTab(self.tab_6, "")

        self.horizontalLayout_4.addWidget(self.tabWidget)

        self.widget_6 = QWidget(self.widget_2)
        self.widget_6.setObjectName(u"widget_6")
        self.gridLayout = QGridLayout(self.widget_6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox_2 = QGroupBox(self.widget_6)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame = QFrame(self.groupBox_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout.addWidget(self.label_7)

        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setTextFormat(Qt.MarkdownText)

        self.horizontalLayout.addWidget(self.label_8)

        self.pushButton_6 = QPushButton(self.frame)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.horizontalLayout.addWidget(self.pushButton_6)


        self.verticalLayout_7.addWidget(self.frame)

        self.frame_2 = QFrame(self.groupBox_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_2.addWidget(self.label_9)

        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setTextFormat(Qt.MarkdownText)

        self.horizontalLayout_2.addWidget(self.label_10)

        self.pushButton_7 = QPushButton(self.frame_2)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.horizontalLayout_2.addWidget(self.pushButton_7)


        self.verticalLayout_7.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.groupBox_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_11 = QLabel(self.frame_3)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_3.addWidget(self.label_11)

        self.label_12 = QLabel(self.frame_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setTextFormat(Qt.MarkdownText)

        self.horizontalLayout_3.addWidget(self.label_12)

        self.pushButton_8 = QPushButton(self.frame_3)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.horizontalLayout_3.addWidget(self.pushButton_8)


        self.verticalLayout_7.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.groupBox_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_13 = QLabel(self.frame_4)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_5.addWidget(self.label_13)

        self.label_14 = QLabel(self.frame_4)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setTextFormat(Qt.MarkdownText)

        self.horizontalLayout_5.addWidget(self.label_14)

        self.pushButton_9 = QPushButton(self.frame_4)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setCheckable(False)
        self.pushButton_9.setChecked(False)
        self.pushButton_9.setFlat(False)

        self.horizontalLayout_5.addWidget(self.pushButton_9)


        self.verticalLayout_7.addWidget(self.frame_4)


        self.gridLayout.addWidget(self.groupBox_2, 0, 1, 1, 1)

        self.widget = QWidget(self.widget_6)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_6 = QVBoxLayout(self.widget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setTextFormat(Qt.MarkdownText)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_6)

        self.pushButton_5 = QPushButton(self.widget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setAutoExclusive(False)
        self.pushButton_5.setAutoDefault(False)

        self.verticalLayout_6.addWidget(self.pushButton_5)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setTextFormat(Qt.MarkdownText)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_5)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.pushButton_33 = QPushButton(self.widget_6)
        self.pushButton_33.setObjectName(u"pushButton_33")

        self.gridLayout.addWidget(self.pushButton_33, 2, 0, 1, 1)

        self.widget_3 = QWidget(self.widget_6)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.widget_7 = QWidget(self.widget_3)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_10 = QVBoxLayout(self.widget_7)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_15 = QLabel(self.widget_7)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_15)

        self.pushButton_11 = QPushButton(self.widget_7)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.verticalLayout_10.addWidget(self.pushButton_11)

        self.label_16 = QLabel(self.widget_7)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_16)


        self.horizontalLayout_8.addWidget(self.widget_7)

        self.widget_8 = QWidget(self.widget_3)
        self.widget_8.setObjectName(u"widget_8")
        self.verticalLayout_29 = QVBoxLayout(self.widget_8)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.label_17 = QLabel(self.widget_8)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout_29.addWidget(self.label_17)

        self.pushButton_10 = QPushButton(self.widget_8)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.verticalLayout_29.addWidget(self.pushButton_10)

        self.label_35 = QLabel(self.widget_8)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setAlignment(Qt.AlignCenter)

        self.verticalLayout_29.addWidget(self.label_35)


        self.horizontalLayout_8.addWidget(self.widget_8)


        self.gridLayout.addWidget(self.widget_3, 2, 1, 1, 1)

        self.widget_9 = QWidget(self.widget_6)
        self.widget_9.setObjectName(u"widget_9")
        self.verticalLayout_33 = QVBoxLayout(self.widget_9)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.widget_10 = QWidget(self.widget_9)
        self.widget_10.setObjectName(u"widget_10")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_39 = QLabel(self.widget_10)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_39)

        self.pushButton_36 = QPushButton(self.widget_10)
        self.pushButton_36.setObjectName(u"pushButton_36")

        self.horizontalLayout_10.addWidget(self.pushButton_36)

        self.label_38 = QLabel(self.widget_10)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_38)


        self.verticalLayout_33.addWidget(self.widget_10)

        self.widget_11 = QWidget(self.widget_9)
        self.widget_11.setObjectName(u"widget_11")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_40 = QLabel(self.widget_11)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_40)

        self.pushButton_37 = QPushButton(self.widget_11)
        self.pushButton_37.setObjectName(u"pushButton_37")

        self.horizontalLayout_9.addWidget(self.pushButton_37)

        self.label_41 = QLabel(self.widget_11)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_41)


        self.verticalLayout_33.addWidget(self.widget_11)


        self.gridLayout.addWidget(self.widget_9, 3, 1, 1, 1)

        self.widget_12 = QWidget(self.widget_6)
        self.widget_12.setObjectName(u"widget_12")
        self.verticalLayout_35 = QVBoxLayout(self.widget_12)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.widget_14 = QWidget(self.widget_12)
        self.widget_14.setObjectName(u"widget_14")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_42 = QLabel(self.widget_14)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_42)

        self.pushButton_38 = QPushButton(self.widget_14)
        self.pushButton_38.setObjectName(u"pushButton_38")

        self.horizontalLayout_11.addWidget(self.pushButton_38)

        self.label_43 = QLabel(self.widget_14)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_43)


        self.verticalLayout_35.addWidget(self.widget_14)

        self.widget_15 = QWidget(self.widget_12)
        self.widget_15.setObjectName(u"widget_15")
        self.horizontalLayout_12 = QHBoxLayout(self.widget_15)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_44 = QLabel(self.widget_15)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_44)

        self.pushButton_39 = QPushButton(self.widget_15)
        self.pushButton_39.setObjectName(u"pushButton_39")

        self.horizontalLayout_12.addWidget(self.pushButton_39)

        self.label_45 = QLabel(self.widget_15)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_45)


        self.verticalLayout_35.addWidget(self.widget_15)


        self.gridLayout.addWidget(self.widget_12, 3, 0, 1, 1)


        self.horizontalLayout_4.addWidget(self.widget_6)


        self.verticalLayout_27.addWidget(self.widget_2)

        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy4)

        self.verticalLayout_27.addWidget(self.textBrowser)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)
        self.toolBox.setCurrentIndex(2)
        self.toolBox_3.setCurrentIndex(0)
        self.toolBox_2.setCurrentIndex(0)
        self.pushButton_5.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Input", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"File path:", None))
        self.lineEdit_17.setText("")
        self.lineEdit_17.setPlaceholderText(QCoreApplication.translate("MainWindow", u"path to file", None))
        self.pushButton_24.setText(QCoreApplication.translate("MainWindow", u"Browse files", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_17), QCoreApplication.translate("MainWindow", u"Tm .h file", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"File path:", None))
        self.lineEdit_18.setText("")
        self.lineEdit_18.setPlaceholderText(QCoreApplication.translate("MainWindow", u"path to file", None))
        self.pushButton_25.setText(QCoreApplication.translate("MainWindow", u"Browse files", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_18), QCoreApplication.translate("MainWindow", u"Tm .c file", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"File path:", None))
        self.lineEdit_19.setText("")
        self.lineEdit_19.setPlaceholderText(QCoreApplication.translate("MainWindow", u"path to file", None))
        self.pushButton_26.setText(QCoreApplication.translate("MainWindow", u"Browse files", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_19), QCoreApplication.translate("MainWindow", u"Tc .h file", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"File path:", None))
        self.lineEdit_20.setText("")
        self.lineEdit_20.setPlaceholderText(QCoreApplication.translate("MainWindow", u"path to file", None))
        self.pushButton_27.setText(QCoreApplication.translate("MainWindow", u"Browse files", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_20), QCoreApplication.translate("MainWindow", u"TcTm .h file", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Output", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Directory path:", None))
        self.lineEdit_11.setText("")
        self.lineEdit_11.setPlaceholderText(QCoreApplication.translate("MainWindow", u"path to directory", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"Browse files", None))
        self.toolBox_3.setItemText(self.toolBox_3.indexOf(self.page_11), QCoreApplication.translate("MainWindow", u"MIB", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"File path:", None))
        self.lineEdit_12.setPlaceholderText(QCoreApplication.translate("MainWindow", u"path to file", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"Browse files", None))
        self.toolBox_3.setItemText(self.toolBox_3.indexOf(self.page_12), QCoreApplication.translate("MainWindow", u".docx", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Input", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Config and paths file", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Config directory path", None))
        self.lineEdit_21.setPlaceholderText(QCoreApplication.translate("MainWindow", u"path to config directory", None))
        self.pushButton_28.setText(QCoreApplication.translate("MainWindow", u"Browse files", None))
        self.pushButton_31.setText(QCoreApplication.translate("MainWindow", u"Default", None))
        self.pushButton_29.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.pushButton_30.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Config settings", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"One entry per line", None))
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setPlaceholderText("")
        self.pushButton_34.setText(QCoreApplication.translate("MainWindow", u"Use", None))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_21), QCoreApplication.translate("MainWindow", u"Parsing preprocessor config", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"One entry per line", None))
        self.pushButton_35.setText(QCoreApplication.translate("MainWindow", u"Use", None))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_22), QCoreApplication.translate("MainWindow", u"MIB generation config", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"Config", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Parsed results", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Tm .h file", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"O", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"View", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Tm .c file", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"O", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"View", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Tc .h file", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Error", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"TcTm .h file", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Error", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"->", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Parse!", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"->", None))
        self.pushButton_33.setText(QCoreApplication.translate("MainWindow", u"Compute\n"
"all", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"v", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Interpret\n"
"TC", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"v", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"v", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Interpret\n"
"TM", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"v", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"<-", None))
        self.pushButton_36.setText(QCoreApplication.translate("MainWindow", u"Generate MIB", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"<-", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"<-", None))
        self.pushButton_37.setText(QCoreApplication.translate("MainWindow", u"Generate .docx.", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"<-", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"<-", None))
        self.pushButton_38.setText(QCoreApplication.translate("MainWindow", u"Save MIB", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"<-", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"<-", None))
        self.pushButton_39.setText(QCoreApplication.translate("MainWindow", u"Save .docx", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"<-", None))
        self.textBrowser.setMarkdown("")
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textBrowser.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Warnings, errors, etc. will be displayed here...", None))
    # retranslateUi

