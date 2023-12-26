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
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(738, 373)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionHelp = QAction(MainWindow)
        self.actionHelp.setObjectName(u"actionHelp")
        self.actionHelp_2 = QAction(MainWindow)
        self.actionHelp_2.setObjectName(u"actionHelp_2")
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
        font = QFont()
        font.setPointSize(24)
        self.labelResult.setFont(font)

        self.gridLayout.addWidget(self.labelResult, 2, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 738, 24))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionQuit)
        self.menuFile.addAction(self.actionHelp)
        self.menuAbout.addAction(self.actionHelp_2)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Save Christmas Day 1", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionHelp.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.actionHelp_2.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.buttonSelectFile.setText(QCoreApplication.translate("MainWindow", u"Select File", None))
        self.buttonCalc.setText(QCoreApplication.translate("MainWindow", u"Calculate Calibration Value", None))
        self.labelResult.setText(QCoreApplication.translate("MainWindow", u"Result:", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi

