# -*- coding: utf-8 -*-

# 客户端:创建TCP连接时，主动发起连接的叫客户端

# 导入socket库:
import socket

# 创建一个socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('www.sina.com.cn', 80))