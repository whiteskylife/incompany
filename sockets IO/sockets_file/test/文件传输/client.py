# -*- coding: utf-8 -*-

# CS通话简单示例

import socket
import os

obj = socket.socket()
ip_port = ('127.0.0.1', 8000)
obj.connect(ip_port)

file_size = os.stat('demo.jpg').st_size
obj.sendall(bytes(str(file_size), encoding='utf-8'))

file = open('demo.jpg', 'rb')
for line in file:
    obj.sendall(line)

file.close()
obj.close()