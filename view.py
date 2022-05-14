from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QProgressBar, QApplication
from PyQt5.QtCore import QThread, pyqtSignal
from model import *
import time


class Tread(QThread):

    countChanged = pyqtSignal(int)

    def run(self):
        for i in range(100):
            time.sleep(0.01)
            self.countChanged.emit(i+1)
            append_number()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumWidth(400)
        self.setWindowTitle('Fibo Progress')

        self.setLayout(QVBoxLayout())

        self.prog = QProgressBar()
        self.prog.setMinimum(0)
        self.prog.setMaximum(100)
        self.layout().addWidget(self.prog)

        button = QPushButton('Start')
        button.clicked.connect(self.buttonClick)
        self.layout().addWidget(button)

        self.show()

    def buttonClick(self):
        self.tre = Tread()
        self.tre.countChanged.connect(self.countChanged)
        self.tre.start()

    def countChanged(self, value):
        self.prog.setValue(value)







