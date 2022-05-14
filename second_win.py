from instr import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLineEdit,QApplication, QWidget,QPushButton,QLabel,QVBoxLayout, QHBoxLayout
from final_win import *
class TestWin(QWidget):
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
        self.h_line = QHBoxLayout()
        self.l_line = QVBoxLayout()
        self.r_line = QVBoxLayout()

        self.text1 = QLabel(txt_FIO)
        self.text2 = QLineEdit(txt_hintname)
        self.text3 = QLabel(txt_age)
        self.text4 = QLineEdit(txt_hintage)
        self.text5 = QLabel(txt_test1)
        self.text6 = QPushButton(txt_knopka1)
        self.text7 = QLineEdit(txt_hinttest1)
        self.text8 = QLabel(txt_test2)
        self.text9 = QPushButton(txt_knopka2)
        self.text10 = QLabel(txt_test3)
        self.text11 = QPushButton(txt_knopka3)
        self.text12 = QLineEdit(txt_hinttest2)
        self.text13 = QLineEdit(txt_hinttest3)
        self.text14 = QPushButton(txt_knopka4)
        self.text15 = QLabel(txt_timer)

        self.l_line.addWidget(self.text1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.text2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.text3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.text4, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.text5, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.text6, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.text7, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.text8, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.text9, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.text10, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.text11, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.text12, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.text13, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.text14, alignment = Qt.AlignCenter)
        self.r_line.addWidget(self.text15, alignment = Qt.AlignRight)
        

        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)


    def connects(self):
        self.text14.clicked.connect(self.next_click)
    def next_click(self):
        self.hide()
        self.TH = ThirdWin()
      


