# -*- coding: utf-8 -*-

import socket

obj = socket.socket()
ip_port = ('127.0.0.1', 8000)
obj.bind(ip_port)
obj.listen(5)



