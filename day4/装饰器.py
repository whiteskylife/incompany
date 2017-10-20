# -*- coding: utf-8 -*-

# import time
#
#
# def runtime(func):
#     def warpper():
#         start_time = time.time()
#         func()
#         end_time = time.time()
#         print 'run time is %s' % (end_time-start_time)
#     return warpper
#
# @runtime
# def test1():
#     time.sleep(3)
#     print 'in the test1'
#
# test1()

#
# def fun2(wtf):
#     def fun3(*args, **kwargs):
#         print('i am pythoner!!! ')
#         wtf(*args, **kwargs)
#     return fun3                 #这里不是fun3（）是因为：
#
#
#      # @fun2  当于fun1 = fun2(fun1) ，把下面的函数传递到装饰器函数里面，相当于 fun1 = fun2(fun1) = fun3,            后面再执行fun1() , 相当于执行fun3()
# @fun2
# def fun1(arg, arg2):
#     print('this is fun1: %s %d' % (arg, arg2))
# fun1('tom', 55)                      #注意此处fun1（）调用的实际是fun3（），而不是原来的fun1（）了
#
#
#
# print(__name__)
# s = set


def outer(func):
    def inner(*args, **kwargs):
        print('first decorate-------------')
        print('the arg is :', *args, **kwargs)
        r = func(*args, **kwargs)
        print('first decorate-------------')
        #return r
    return inner


def outer2(func):
    def inner2(*args, **kwargs):
        print('second decorate-----------')
        r = func(*args, **kwargs)
        print('second decorate------------')
        return r
    return inner2


@outer                 # index = outer(index) = inner
@outer2
def index(a1, a2):
    print('ori func----------')
    return a1 + a2

index(1, 2)
print(index(1, 2))

# 输出：
# first decorate-------------
# the arg is : 1 2
# second decorate-----------
# ori func----------
# second decorate------------
#first decorate-------------
3






