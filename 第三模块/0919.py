# -*- coding: utf-8 -*-
# from wsgiref.simple_server import make_server
#
# class Handler(object):
#
#     def index(self):
#         return 'index'
#
#     def news(self):
#         return 'news'
#
#
# def RunServer(environ, start_response):
#     start_response('200 OK', [('Content-Type', 'text/html')])
#     url = environ['PATH_INFO']
#     temp = url.split('/')[1]
#     obj = Handler()
#     is_exist = hasattr(obj, temp)
#     if is_exist:
#         func = getattr(obj, temp)
#         ret = func()
#         return ret
#     else:
#         return '404 not found'
#
# if __name__ == '__main__':
#     httpd = make_server('', 8001, RunServer)
#     print "Serving HTTP on port 8000..."
#     httpd.serve_forever()

'''
# 单例模式（所有的实例中封装的内容都相同时，用单例模式）
# 实现：可以通过静态方法+静态字段来实现
# 举例：数据库连接池，只需创建连接对象一次
class ConnectionPool:
    __instance = None

    def __init__(self):
        self.ip = '1.1.1.1'
        self.port = '3306'
        self.pwd = '123456'
        self.username = 'whisky'
        self.conn_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    @staticmethod
    def get_instance():
        if ConnectionPool.__instance:
            return ConnectionPool.__instance
        else:
            ConnectionPool.__instance = ConnectionPool()      # 创建一个对象，并将对象赋值给静态字段__instance
            return ConnectionPool.__instance

    def get_connection(self):
        import random
        r = random.randrange(1, 11)
        return r


obj1 = ConnectionPool.get_instance()
print(obj1)                             # 单例模式，都是同一对象
obj2 = ConnectionPool.get_instance()
print(obj2)                             # 单例模式，都是同一对象
# for i in range(1, 11):
#     pool = ConnectionPool.get_instance()
#     conn = pool.get_connection()
#     print(pool)
#     print('get a connection---- %s' % conn)




from wsgiref.simple_server import make_server


class ConnectionPool:
    __instance = None

    def __init__(self):
        self.ip = '1.1.1.1'
        self.port = '3306'
        self.pwd = '123456'
        self.username = 'whisky'
        self.conn_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    @staticmethod
    def get_instance():
        if ConnectionPool.__instance:
            return ConnectionPool.__instance
        else:
            ConnectionPool.__instance = ConnectionPool()      # 创建一个对象，并将对象赋值给静态字段__instance
            return ConnectionPool.__instance

    def get_connection(self):
        import random
        ret = random.randrange(1, 11)
        return ret


def index():
    obj = ConnectionPool.get_instance()
    conn = obj.get_connection()
    print obj                       # 从结果可知，不论从哪里访问，都是同一个对象，即单例模式成功
    return 'index...' + str(conn)


def news():
    return 'news----'


def runserver(env, start_response):
    start_response(status = '200 OK', headers = [('Content-Type', 'text/html')])
    url = env['PATH_INFO']      # 用户访问填写的URL
    if url.endswith('index'):
        r = index()
        return r
    elif url.endswith('news'):
        r = news()
        return r
    else:
        return '404'.center(10, '-')

if __name__ == '__main__':
    httpd = make_server('', 8000, runserver)
    print('Serving http on port 8000...')
    httpd.serve_forever()

'''













