# -*- coding: utf-8 -*-

import socket

obj = socket.socket()

obj.connect(('127.0.0.1', 9999))

obj.close()



