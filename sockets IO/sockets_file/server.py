# -*- coding: utf-8 -*-

import socket

s = socket.socket()
ip_port = ('127.0.0.1', 9999)

s.bind(ip_port)
s.listen(5)

while True:
    conn, address = s.accept()   # accept阻塞
    conn.sendall(bytes('欢迎登陆whisky的python世界', encoding='utf-8'))
    # 先接收文件大小，然后开始传输文件
    file_size = str(conn.recv(1024), encoding='utf-8')
    print(file_size)

