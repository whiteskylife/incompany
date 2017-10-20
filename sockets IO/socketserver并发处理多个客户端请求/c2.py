# -*- coding: utf-8 -*-

import socket

s = socket.socket()
ip_port = ('127.0.0.1', 9999)
s.connect(ip_port)

#s.sendall(bytes('i am client 2 ', encoding='utf-8'))
while True:
    s.sendall(bytes(input('input: '), encoding='utf-8'))
    rec = str(s.recv(1024), encoding='utf-8')
    print(rec)