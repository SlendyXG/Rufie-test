from instr import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLineEdit,QApplication, QWidget,QPushButton,QLabel,QVBoxLayout, QHBoxLayout
from second_win import TestWin
class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.button = QPushButton(txt_next)
        self.instr = QLabel(txt_instruction)
        self.info = QLabel(txt_hello) 
        self.layout = QVBoxLayout()
       

        self.layout.addWidget(self.info, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.instr, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.button, alignment = Qt.AlignCenter)
        self.setLayout(self.layout)
    def connects(self):
        self.button.clicked.connect(self.next_click)
    def next_click(self):
        self.hide()
        self.TW = TestWin()
      


App = QApplication([])
main_win = MainWin()
App.exec()
