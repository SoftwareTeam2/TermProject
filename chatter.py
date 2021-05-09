import sys
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import *
from PyQt5 import uic
from socket import *
import threading
import time

form_class = uic.loadUiType('textInput.ui')[0]

class Signal(QObject):
    recv_signal = pyqtSignal(str)
    disconn_signal = pyqtSignal()

class WindowClass(QMainWindow, form_class):
    def __init__(self,sock):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.send)
        recv_thread = threading.Thread(target=self.recieve,args=(sock,))
        recv_thread.start()
        self.recv = Signal()
        self.recv.recv_signal.connect(self.appendMsg)

    def send(self,sock):
        sendData = self.textEdit.toPlainText()
        clientSocket.send(sendData.encode('utf-8'))
        self.textEdit.clear()

    def recieve(self,sock):
        while True:
            msg = sock.recv(1024)
            try:
                if msg:
                    self.recv.recv_signal.emit(msg.decode('utf-8'))
            except:
                break
            
    def appendMsg(self, msg):
        self.textBrowser.append(msg)

if __name__=='__main__':
    app = QApplication(sys.argv)

    clientSocket = socket(AF_INET,SOCK_STREAM)
    ip = 'gywnd2.iptime.org'
    port = 208
    
    clientSocket.connect((ip,port))
    print('접속 완료')

    myWindow = WindowClass(clientSocket)
    myWindow.show()
    app.exec_()

    while True:
        time.sleep(1)
        pass

    clientSocket.close()