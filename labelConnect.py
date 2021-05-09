import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import QCoreApplication

form_class = uic.loadUiType('labelEx.ui')[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.changeButton.clicked.connect(self.changeText)
        self.printButton.clicked.connect(self.printText)
    
    def changeText(self):
        exText = input()
        self.label1.setText(exText)
        QCoreApplication.quit()
    
    def printText(self):
        print(self.label1.text())

if __name__=='__main__':
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()