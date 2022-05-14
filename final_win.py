from instr import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLineEdit,QApplication, QWidget,QPushButton,QLabel,QVBoxLayout, QHBoxLayout
class ThirdWin(QWidget):
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
        self.v_line = QVBoxLayout()
        self.text1 = QLabel(txt_finalwin)
        self.text2 = QLabel(txt_index)
        self.v_line.addWidget(self.text1, alignment = Qt.AlignCenter)
        self.v_line.addWidget(self.text2, alignment = Qt.AlignCenter)
        self.setLayout(self.v_line)
    def connects(self):
        pass

