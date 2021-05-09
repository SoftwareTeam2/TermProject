import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType('radioButtonEx.ui')[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.rdn_1.clicked.connect(self.groupboxRadFunction)
        self.rdn_2.clicked.connect(self.groupboxRadFunction)
        self.rdn_3.clicked.connect(self.groupboxRadFunction)
        self.rdn_4.clicked.connect(self.groupboxRadFunction)
    
    def groupboxRadFunction(self):
        if self.rdn_1.isChecked() : print('groupbox rdn_1 is checked')
        elif self.rdn_2.isChecked() : print('groupbox rdn_2 is checked')
        elif self.rdn_3.isChecked() : print('groupbox rdn_3 is checked')
        elif self.rdn_4.isChecked() : print('groupbox rdn_4 is checked')

if __name__=='__main__':
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()