rom instr import *
from second_win import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLineEdit,QApplication, QWidget,QPushButton,QLabel,QVBoxLayout, QHBoxLayout
class ThirdWin(QWidget):
    def __init__(self,exp):
        super().__init__()
        self.exp = exp
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
        
        self.text2 = QLabel(txt_workheart + self.results())
        self.text1 = QLabel(txt_index + str(self.index))
        self.v_line.addWidget(self.text1, alignment = Qt.AlignCenter)
        self.v_line.addWidget(self.text2, alignment = Qt.AlignCenter)
        self.setLayout(self.v_line)
    def connects(self):
        pass
    def results(self):
        self.index = (4*(int(self.exp.t1)+int(self.exp.t2)+int(self.exp.t3))-200)/10
        if self.exp.age >= 7 and self.exp.age < 9:
            if self.index >= 21:
                return txt_res1
            elif self.index >= 17 and self.index < 21:
                return txt_res2
            elif self.index >= 12 and self.index < 17:
                return txt_res3
            elif self.index >= 6.5 and self.index < 12:
                return txt_res4
            elif self.index <= 6.4:
                return text_res5
        if self.exp.age >= 9 and self.exp.age <= 10:
            if self.index >= 19.5:
                return txt_res1
            elif self.index >= 15.5 and self.index < 19.5:
                return txt_res2
            elif self.index >= 10.5 and self.index < 15.5:
                return txt_res3
            elif self.index >= 5 and self.index < 10.5:
                return txt_res4
            elif self.index <= 4.9:
                return text_res5     
        if self.exp.age >= 11 and self.exp.age <= 12:
            if self.index >= 18:
                return txt_res1
            elif self.index >= 14 and self.index < 18:
                return txt_res2
            elif self.index >= 9 and self.index < 14:
                return txt_res3
            elif self.index >= 3.5 and self.index < 9:
                return txt_res4
            elif self.index <= 3.4:
                return text_res5 
        if self.exp.age >= 13 and self.exp.age <= 14:
            if self.index >= 16.5:
                return txt_res1
            elif self.index >= 12.5 and self.index < 16.5:
                return txt_res2
            elif self.index >= 7.5 and self.index < 12.5:
                return txt_res3
            elif self.index >= 2 and self.index < 7.5:
                return txt_res4
            elif self.index <= 1.9:
                return text_res5
        if self.exp.age >= 15:
            if self.index >= 15:
                return txt_res1
            elif self.index >= 11 and self.index < 15:
                return txt_res2
            elif self.index >= 6 and self.index < 11:
                return txt_res3
            elif self.index >= 0.5 and self.index < 6:
                return txt_res4
            elif self.index <= 0.4:
                return text_res5


