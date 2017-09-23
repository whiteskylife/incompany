# -*- coding: utf-8 -*-
import socket

s = socket.socket()
s.bind(('127.0.0.1', 9999,))
s.listen(5)
#接收客户端的请求

while True:
    conn, address = s.accept()  # 连接，客户端地址信息 accept 阻塞
    conn.sendall(bytes('欢饮whisky来到python世界', encoding='utf-8'))  # 在python3中不能直接传字符串（py2.7中可以），需要转换成字节
    while True:
        ret_bytes = conn.recv(1024)
        ret_str = str(ret_bytes, encoding='utf-8')
        if ret_str == 'q':
            break
        conn.sendall(bytes(ret_str + 'Good!', encoding='utf-8'))

    print(address, conn)




