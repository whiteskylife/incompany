# -*- coding: utf-8 -*-

import os
import socket

obj = socket.socket()
ip_port = ('127.0.0.1', 9999)
obj.connect(ip_port)

# 阻塞
ret_bytes = obj.recv(1024)
ret_str = str(ret_bytes, encoding='utf-8')
print(ret_str)

# 发送当前文件大小
size = os.stat('demo.jpg').st_size          # 计算文件大小的方法：os.stat(filename).st_size
obj.sendall(bytes(str(size), encoding='utf-8'))

# 发送文件
with open('demo.jpg', 'rb') as f:
    for line in f:
        obj.sendall(line)

obj.close()

