# -*- coding: utf-8 -*-

import socketserver
'''
socket只能同时处理一个请求
import socket

obj = socket.socket()
ip_port = ('127.0.0.1', 9999)
obj.bind(ip_port)
obj.listen(5)

while True:
    conn, ip = obj.accept()
    while True:
        ret = str(conn.recv(1024), encoding='utf-8')
        if ret == 'q':
            break
        conn.sendall(bytes(ret + 'server reply...', encoding='utf-8'))

'''


class MyServer(socketserver.BaseRequestHandler):

    def handle(self):
        conn = self.request
        conn.sendall(bytes('welcome login whiskys python world', encoding='utf-8'))
        while True:
            ret_bytes = conn.recv(1024)
            ret_str = str(ret_bytes, encoding='utf-8')
            if ret_str == 'q':
                break
            conn.sendall(bytes(ret_str + 'OK', encoding='utf-8'))

if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 9999), MyServer)
    server.serve_forever()

