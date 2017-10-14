# -*- coding: utf-8 -*-

# CS通话简单示例

import socket
import os

obj = socket.socket()
ip_port = ('127.0.0.1', 8000)
obj.connect(ip_port)

file_size = os.stat('demo.jpg').st_size