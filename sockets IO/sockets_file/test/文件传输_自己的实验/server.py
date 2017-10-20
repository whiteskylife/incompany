# -*- coding: utf-8 -*-

import socket

'''
创建套接字对象
绑定服务ip，端口
开始监听
'''
obj = socket.socket()
ip_port = ('127.0.0.1', 8000)
obj.bind(ip_port)
obj.listen(5)

conn, ip = obj.accept()
ret_str = str(conn.recv(1024), encoding='utf-8')
file_size = int(ret_str)
recv_size = 0

file = open('new.jpg', 'wb')
while True:
    if recv_size == file_size:
        break
    else:
        recv_data = conn.recv(1024)
        file.write(recv_data)
        recv_size += len(recv_data)

file.close()