# -*- coding: utf-8 -*-
# list1 = set([1, 3, 5, 2, 9, 7, 6])
# list2 = set([1,3,10,13,14])
#
# print(list1.intersection(list2))


# ss ='\xe4\xb8\xad'
# strTobytes = []
# for i in ss.split('\x'):
#     if i != '':
#         num = int(i,16)
#         strTobytes.append(num)
#
# a = bytes(strTobytes).decode()
# print(a)

# 1 1 2 3 5 8 13 21 34 55 89

def inc(count, a, b):
    if count == 5:
        return a
    c = a + b
    r = inc(count+1, b, c)
    return r
ret = inc(0, 1, 1)
print(ret)








