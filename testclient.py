# -*- encoding:utf-8 -*-
from socket import *
import sys
import threading
import time

# socket - tcp - client.py （客户端）：

# 测试，连接本机
HOST = '127.0.0.1'
# 设置侦听端口
PORT = 8555
BUFSIZ = 1024


class TcpClient:
    ADDR = (HOST, PORT)

    def __init__(self):
        self.HOST = HOST
        self.PORT = PORT
        self.BUFSIZ = BUFSIZ
        # 创建socket连接
        self.client = socket(AF_INET, SOCK_STREAM)
        self.client.connect(self.ADDR)


    def sendmsg(self,msg):

            self.client.send(msg.encode())


    def recvmsg(self):
        # 接收消息，如果链接一直存在，则持续监听接收消息
        try:
            data = self.client.recv(self.BUFSIZ)
            if data:
                data = data.decode()
                print(data)
                return data
            else:
                return '0'
        except Exception as e:
            print(e)


if __name__ == '__main__':
    client = TcpClient()
    client.sendmsg('4516546516')
    client.recvmsg()
