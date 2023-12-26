"""
A GUI program that uses our designed code
that was saved to myapp.ui, and converted to python
to the file myapp_ui.py
"""

from PySide6.QtWidgets import *
from myapp_ui import Ui_MainWindow


def select_file():
    filename, _ = QFileDialog.getOpenFileName()
    content = open(filename).read()
    ui.labelFile.setText(content)


def calculate_calibration_value():
    ui.labelResult.setText("Result: 15")

app = QApplication()
w = QMainWindow()

ui = Ui_MainWindow()
ui.setupUi(w)

ui.buttonSelectFile.clicked.connect(select_file)
ui.buttonCalc.clicked.connect(calculate_calibration_value)


w.show()

app.exec()
