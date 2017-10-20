# -*- coding: utf-8 -*-
# import urllib.request
#
# f = urllib.request.urlopen('http://www.baidu.com')
# html = f.read()
# print(html)
#
import urllib.request

req = urllib.request.Request('http://www.qq.com')
s = urllib.request.urlopen(req)
d = s.readlines()
for i in d:
    print(d)
