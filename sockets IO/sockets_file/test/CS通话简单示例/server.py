# -*- coding: utf-8 -*-

import socket

obj = socket.socket()
ip_port = ('127.0.0.1', 8000)
obj.bind(ip_port)
obj.listen(5)

conn, ip = obj.accept()
conn.sendall(bytes('quenn',  encoding='utf-8'))
ret_str = str(conn.recv(1024), encoding='utf-8')
print(ret_str)
print(ip)   # ('127.0.0.1', 14400)


