# -*- coding: utf-8 -*-

# 服务器端：
import socket
import threading
import
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 监听端口:
s.bind(('127.0.0.1', 9999))
s.listen(5)                  # 调用listen()方法开始监听端口，传入的参数指定等待连接的最大数量
print('Waiting for connection...')
while True:
    # 接受一个新连接:
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()