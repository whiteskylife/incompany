# -*- coding: utf-8 -*-

import  json
# json反序列化
f = open('test.txt', 'r')

# data = eval(f.read())
data = json.loads(f.read())


f.close()
print(data['age'])