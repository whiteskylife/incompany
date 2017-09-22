# -*- coding: utf-8 -*-
# url = 'www.whisky.com'
# while url:
#     print(url)
#     url = url[1:]

# x = 0
# while x < 100 and x % 2 == 0:
#     print(x)
#     x += 1


# a = ['first', 'second', 'third', 'forth', 'fifth']
# for i in a:
#     print(i)




##练习1：逐一显示指定列表中的所有元素：
# a = ['first', 'second', 'third', 'forth', 'fifth']
# count = 0
# while count < len(a):
#     print(a[count])
#     count += 1
#
# print('这是逆序显示'.center(30, '#'))
# while a:
#     print(a[-1])
#     a.pop()
#
# 对于任何可迭代对象，使用for是最简单的,效率高于while

##练习2：求100内奇数和，偶数和：
# a = 0
# sum = 0
# sum1 = 0
# while a <= 100:
#     if a % 2 != 0:
#         sum += a
#     else:
#         sum1 += a
#     a += 1
#
# print('偶数和：%d ， 奇数和：%d' % (sum,sum1))
##偶数和：2500 ， 奇数和：2550



## 练习3：逐一显示指定列表的所有键，并于显示结束后说明总键数
# a = []
# dic = {'x': 1, 'b': 2, 'c': 3, 'd': 4}
# keylist = dic.keys()
# for i in keylist:
#     a.append(i)
#
# while a:
#     print(a[0])
#     a.pop(0)
# else:
#     print('总键数：%d'.center(50, '-') % (len(dic)))



##练习4：创建一个包含了100以内所有奇数的列表,并逆序显示列表中的所有元素：
# a = 0
# l = []
# while a < 100:
#     if a % 2 != 0:
#         l.append(a)
#     a += 1
# else:
#     print('正序:', l)
#     l.reverse()
#     m = l
#     print('逆序：', l)
##逆序用到列表的reverse方法


##练习5：列表l = [0,1,2,3,4,5,6] m = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]，
##以第一个列表中的元素为键，以第二个列表中的元素为值生成字典L

# l = [0, 1, 2, 3, 4, 5, 6]
# m = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
# L = {}
# count = 0
# if len(l) == len(m):
#     while count < len(l):
#         L[l[count]] = m[count]
#         count += 1
#     else:
#         print(L)

##涉及到字典中新增键值的方法==》给键直接赋值即可



##字典的构造：zip，取一个或多个序列为参数，将给定序列中的并排的元素配成元组，返回这些元组的列表（当参数长度不通时，zip以最短序列的长度为准）
#可在for循环中用于实现并行迭代
# L = [0, 1, 2, 3, 4, 5, 6]
# m = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
# n = {}
# for (k,v) in zip(L,m):
#     n[k] = v
# print(n)
#输出：{0: 'Sun', 1: 'Mon', 2: 'Tue', 3: 'Wed', 4: 'Thu', 5: 'Fri', 6: 'Sat'}







# for循环练习
# 练习1：逐一分开显示指定字典d1中的所有元素，类似如下：
#        k1 v1
#        k2 v2
#        ...
# d1 = {0: 'Sun', 1: 'Mon', 2: 'Tue', 3: 'Wed', 4: 'Thu', 5: 'Fri', 6: 'Sat'}
# # d1 = {'0': 'Sun', '1': 'Mon', '2': 'Tue', '3': 'Wed', '4': 'Thu', '5': 'Fri', '6': 'Sat'}
# for (k, v) in d1.items():
#     print(k, v)
#
#
#
# 练习2：逐一显示列表中l1=["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]中的索引为奇数的元素
# l1 = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
# 法1：
# for i in l1:
#     if l1.index(i) % 2 != 0:
#         print(l1[l1.index(i)])
# 法2：
# for i in range(1,len(l1),2):  #非完全遍历用range
#     print(l1[i])
#
#
# 练习3：将属于列表l1=["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]，
# 但不属于列表l2=["Sun", "Tue", "Wed", "Fri"]的所有元素定义为一个新列表l3
# l1 = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
# l2 = ["Sun", "Tue", "Wed", "Fri"]
# l3 = []
# for i in l1:
#     if i not in l2:
#         l3.append(i)
# print(l3)
#
# 练习4：已知列表namelist=['stu1', 'stu2', 'stu3', 'stu4', 'stu5', 'stu6', 'stu7'],
# 删除列表removelist=['stu3', 'stu7', 'stu9']：从namelist中移除removelist，不在removelist中的忽略
# namelist = ['stu1', 'stu2', 'stu3', 'stu4', 'stu5', 'stu6', 'stu7']
# removelist = ['stu3', 'stu7', 'stu9']
# for i in removelist:
#     if i in namelist:
#         namelist.remove(i)
# print(namelist)

# l = ['stu1', 'stu2', 'stu3', 'stu4', 'stu5', 'stu6', 'stu7']
# n = iter(l)
# print(next(n))
# # print(n.__next__)

#write中换行，把1到10之间每个数的平方写到一个文件中，每个元素一行
# file = open('mage1.txt', 'w+')
# for i in range(1, 11):
#     file.write('this is %i line\n' %i)
# # file.truncate(3)
# # file.seek(0)
# print(file.tell())
# print(file.readlines())
#
#
#
#
#
# file.truncate(file.tell())

# l1 = [1, 2, 3, 4]
# l2 = [5, 6, 7, 8]
# l3 = [9, 10, 11, 12]
#
#
# def change(x, y):
#     return x*2, y*2
#
# a = map(change, l1, l2)
# print(list(a))

# 输出：[(2, 10), (4, 12), (6, 14), (8, 16)]

# class FirstClass():
#     data = 'hello class'
#
#     def printclass(self):
#         print(self.data)
#
# ins1 = FirstClass()
# # print(ins1.data)
# a = ins1.printclass()
# print(a)


# def fun2(fun1):
#     def fun3():
#         print('i am pythoner!!! ')
#         return fun1()
#     return fun3
#
#
# @fun2
# def fun1():
#     print('this is fun1')
#     return 666
# fun1()

# def gen():
#     for l in range[4]:
#         print(l)
#         yield l
# gen()
# for i in b:
#     print(i)
# a = (x for x in range(4))
# for i in a:
#     print(i)
















