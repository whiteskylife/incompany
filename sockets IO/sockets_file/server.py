# -*- coding: utf-8 -*-

import socket

s = socket.socket()
ip_port = ('127.0.0.1', 9999)

s.bind(ip_port)

while True:
    conn, address = s.accept()   # accept阻塞
    conn.sendall(bytes('欢迎登陆whisky的python世界', encoding='utf-8'))
    # 先接收文件大小，然后开始传输文件
    file_size = str()


