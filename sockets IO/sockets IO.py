# -*- coding: utf-8 -*-
import socket

s = socket.socket()
s.bind(('127.0.0.1', 9999,))
s.listen(5)
#接收客户端的请求

while True:
    conn, address = s.accept()  # accept 阻塞
    print(address, conn)
