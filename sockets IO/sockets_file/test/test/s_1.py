# -*- coding: utf-8 -*-
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
ip_port = ('127.0.0.1', 9999)
s.bind(ip_port)

while True:
    data = s.recv(1024)
    print(str(data, encoding='utf-8'))
