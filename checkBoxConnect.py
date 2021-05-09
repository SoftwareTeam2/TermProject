import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType('checkBoxEx.ui')[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.c1.stateChanged.connect(self.chkFunction)
        self.c2.stateChanged.connect(self.chkFunction)
        self.c3.stateChanged.connect(self.chkFunction)
        self.c4.stateChanged.connect(self.chkFunction)

        self.grpc1.stateChanged.connect(self.groupboxRadFunction)
        self.grpc2.stateChanged.connect(self.groupboxRadFunction)
        self.grpc3.stateChanged.connect(self.groupboxRadFunction)
        self.grpc4.stateChanged.connect(self.groupboxRadFunction)

    def chkFunction(self):
        if self.c1.isChecked() : print('chk1 is checked')
        if self.c2.isChecked() : print('chk2 is checked')
        if self.c3.isChecked() : print('chk3 is checked')
        if self.c4.isChecked() : print('chk4 is checked')

    def groupboxRadFunction(self):
        if self.grpc1.isChecked() : print('groupbox chk_1 is checked')
        if self.grpc2.isChecked() : print('groupbox chk_2 is checked')
        if self.grpc3.isChecked() : print('groupbox chk_3 is checked')
        if self.grpc4.isChecked() : print('groupbox chk_4 is checked')

if __name__=='__main__':
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()