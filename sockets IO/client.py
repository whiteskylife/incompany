# -*- coding: utf-8 -*-

import socket

'''
obj = socket.socket()

obj.connect(('127.0.0.1', 9999))
# recv阻塞，服务端没有返回结果，客户端recv永远等待
ret_bytes = obj.recv(1024)   # 1024表示最多接收1024字节，超过1024字节下次接收
ret_str = str(ret_bytes, encoding='utf-8')
print(ret_str)

while True:
    inp = input('请输入要发送的内容：')
    if inp == 'q':
        obj.sendall(bytes(inp, encoding='utf-8'))
        break
    else:
        obj.sendall(bytes(inp, encoding='utf-8'))
        ret = str(obj.recv(1024), encoding='utf-8')
        print(ret)

obj.close()

'''

