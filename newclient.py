from socket import *
import sys
import threading
import time


host = '127.0.0.1'
port = 8555
bufsiz = 1024


class Myclient:
    addr = (host, port)

    def __init__(self):
        self.host = host
        self.port = port
        self.bufsiz = bufsiz
        self.client = socket()
        self.client.connect(self.addr)


    def myconn(self,msg):

        self.client.send(msg.encode())

    def myrecv(self):
        data = self.client.recv(self.bufsiz)
        try:
            if data :
                data = data.decode()

                return data
            else:
                return None
        except Exception as e:
            print(e)


if __name__ == '__main__':
    myc = Myclient()
    myc.myconn('login')
    data = myc.myrecv()

    print(data)