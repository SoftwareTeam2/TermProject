from socket import *
import threading
from PyQt5.QtCore import QThread
import time

def send(sock):
    while True:
        sendData = input(">>>")
        sock.send(sendData.encode('utf-8'))

def recv(sock):
    while True:
        data = connectionSocket.recv(1024)
        print("상대방 ",data.decode('utf-8'))
    
host = 'localhost'
port = 12345

serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind((host,port))
serverSocket.listen(1)

print('대기중입니다.')

connectionSocket, addr = serverSocket.accept()

print(str(addr),"에서 접속되었습니다.")

sender = QThread(threading.Thread(target=send,args=(connectionSocket,)))
receiver = QThread(threading.Thread(target=recv,args=(connectionSocket,)))

sender.start()
receiver.start()

while True:
    time.sleep(1)
    pass

serverSocket.close()