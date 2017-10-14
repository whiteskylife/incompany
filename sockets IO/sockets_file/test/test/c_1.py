# -*- coding: utf-8 -*-
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)

ip_port = ('127.0.0.1', 9999)

#client.connect(ip_port)

while True:
    inp = input('数据：').strip()
    content = bytes(inp, encoding='utf-8')
    client.sendto(content, ip_port)
client.close()