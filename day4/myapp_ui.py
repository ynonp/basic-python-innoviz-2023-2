# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'myapp.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(738, 373)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.buttonSelectFile = QPushButton(self.centralwidget)
        self.buttonSelectFile.setObjectName(u"buttonSelectFile")

        self.gridLayout.addWidget(self.buttonSelectFile, 0, 0, 1, 1)

        self.buttonCalc = QPushButton(self.centralwidget)
        self.buttonCalc.setObjectName(u"buttonCalc")

        self.gridLayout.addWidget(self.buttonCalc, 0, 1, 1, 1)

        self.labelFile = QTextEdit(self.centralwidget)
        self.labelFile.setObjectName(u"labelFile")

        self.gridLayout.addWidget(self.labelFile, 1, 0, 1, 2)

        self.labelResult = QLabel(self.centralwidget)
        self.labelResult.setObjectName(u"labelResult")

        self.gridLayout.addWidget(self.labelResult, 2, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 738, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.buttonSelectFile.setText(QCoreApplication.translate("MainWindow", u"Select File", None))
        self.buttonCalc.setText(QCoreApplication.translate("MainWindow", u"Calculate Calibration Value", None))
        self.labelResult.setText(QCoreApplication.translate("MainWindow", u"Result:", None))
    # retranslateUi

