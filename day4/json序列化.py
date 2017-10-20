# -*- coding: utf-8 -*-

#json序列化,只能处理简单的数据类型，如：字典、列表、字符串，类和函数等数据类型过于复杂，不支持序列化
import json

def sayhi(name):
    print('hello,', name)

info = {
    'name': 'whitesky',
    'age': 25,
    'func': sayhi
}

f = open('test.txt', 'w')
# f.write(str(info))
f.write(json.dumps(info))
f.close()

#json反序列化

f = open('test.txt', 'r')
data = json.loads(f.read())
print(data['func'])


#处理复杂数据类型（函数等）的方法：pickle(只支持python，不支持Java（支持json）)
import pickle

def sayhi(name):
    print('hello,', name)
info = {
    'name': 'whitesky',
    'age': 25,
    'func': sayhi
}

f = open('test.txt', 'wb')   #pickle序列化要带b
f.write(pickle.dumps(info))  #相当于 pickle._dump(info,f)



#pickle反序列化

f = open('test.txt', 'rb')
data = pickle.loads(f.read()) # 相当于 pickle.load(f)

print(data['func'])



f.close()


#注意：写程序序列化时要记住只dump一次，只load一次（py3中dump多次，再load时会出错，py2中正常），如果需要存储多个状态，就dump成多个文件