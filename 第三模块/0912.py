# -*- coding: utf-8 -*-

'''
class Whisky:

    def fetch(self, backend):
        print('this is :', backend)

    def add_record(self, backend, record):
        print(backend, record)

obj = Whisky()
obj.fetch('www.oldboy.com')
obj.add_record('www.oldboy.com', '192.168.2.1')
#输出
# this is : www.oldboy.com
# www.oldboy.com 192.168.2.1
'''


#面向对象三大特性之一-----封装
'''
# self详解
class Whisky:

    def fetch(self, backend):
        print(self, backend)        # <__main__.Whisky object at 0x0000000000BAE400> www.baidu.com

    def add_record(self, backend, record):
        pass

obj = Whisky()
obj.fetch('www.baidu.com')
print(obj)                           # <__main__.Whisky object at 0x0000000000BAE400>
# 由上可知，self是对象自身
'''


'''

# 利用__init__内置方法（加载类的时候会自动执行）来封装

1. 通过self间接调用被封装的内容
class Foo:
    def __init__(self, bk, time, place):
        self.name = 'whisky'        # __init__初始化信息
        self.favor = bk
        self.time = time
        self.place = place

    def sister(self):
        print('i am your sister')
        print('i work in %s' % self.place)

    def brother(self):
        print('i am your little brother')
        print('i work in %s' % self.place)
obj = Foo('women', '0912', 'SZ')    # 类传参
print(obj.name)     # whisky
print(obj.favor)    # women
print(obj.place)    # SZ

obj.sister()
obj.brother()
# 输出
# i am your sister
# i work in SZ
# i am your little brother
# i work in SZ



# 2、通过对象直接调用被封装的内容

class Foo:

    def __init__(self, name, age):
        self.name = name
        self.age = age


obj1 = Foo('whisky', '25')
print(obj1.name, obj1.age)

obj2 = Foo('alex', '32')
print(obj2.name, obj2.age)

# 输出
# whisky 25
# alex 32


# 小结
# 对于面向对象的封装来说，其实就是使用构造方法将相同内容封装到 对象 中，然后通过对象直接或者self间接获取被封装的内容。
# 封装使用场景：当同一类型的方法具有相同的参数时，直接封装（用__init__构造方法）到对象里面即可
# 类+括号，自动执行类中的__init__方法，__init__又称为构造方法，在其中执行具体封装的操作
# __del__ 解释器销毁对象时候自动调用，又称为 析构方法
'''

'''
# 练习举例：

class Person:

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = int(weight)

    def chi(self):
        self.weight += 2

    def exercise(self):
        self.weight -= 1


obj = Person('whisky', '25', '166')

obj.chi()
obj.chi()
obj.chi()
obj.exercise()
print(obj.weight)
# 输出 171



练习一：在终端输出如下信息

小明，10岁，男，上山去砍柴
小明，10岁，男，开车去东北
小明，10岁，男，最爱disco
老李，90岁，男，上山去砍柴
老李，90岁，男，开车去东北
老李，90岁，男，最爱disco

class People:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def cut(self):
        print('%s, %s, %s,上山去砍柴' % (self.name, self.age, self.gender))

    def go_to_north(self):
        print('%s, %s, %s,开车去东北' % (self.name, self.age, self.gender))

    def go_big_sord(self):
        print('%s, %s, %s,最爱disco' % (self.name, self.age, self.gender))

xiaoming = People('小明', '10岁', '男')
xiaoming.cut()
xiaoming.go_to_north()
xiaoming.go_big_sord()

laoli = People('老李', '90岁', '男')
laoli.cut()
laoli.go_to_north()
laoli.go_big_sord()




练习二：游戏人生程序

1、创建三个游戏人物，分别是：

苍井井，女，18，初始战斗力1000
东尼木木，男，20，初始战斗力1800
波多多，女，19，初始战斗力2500
2、游戏场景，分别：

草丛战斗，消耗200战斗力
自我修炼，增长100战斗力
多人游戏，消耗500战斗力



class Character:
    def __init__(self, name, gender, age, value):
        self.name = name
        self.gender = gender
        self.age = int(age)
        self.value = int(value)

    def grass_fight(self):
        self.value -= 200

    def self_fight(self):
        self.value += 100

    def multi_player(self):
        self.value -= 500

    def detail(self):
        print('your character info: name:%s gender:%s age:%s value:%s' % (self.name, self.gender, self.age, self.value))


cang = Character('苍井井', '女', '18', '1000')
dong = Character('东尼木木', '男', '20', '1800')
bo = Character('波多多', '女', '19', '2500')

cang.grass_fight()
cang.detail()

'''




'''
# 继承

# 对于面向对象的继承来说，其实就是将多个类共有的方法提取到父类中，子类仅需继承父类而不必一一实现每个方法。
# 除了 子类 和 父类 的称谓，还有 派生类 和 基类 ，他们与子类和父类只是叫法不同而已

# 简单示例：

class Animals:
    def chi(self):
        print(self.name + ' 吃')

    def he(self):
        print(self.name + '喝')

class Cat(Animals):
    def __init__(self, name):
        self.name = name

    def cry(self):
        print('喵')

class Dog(Animals):
    def __init__(self, name):
        self.name = name

    def cry(self):
        print('汪')


alex = Dog('lijie')
alex.cry()  # 汪
alex.chi()  # lijie 吃



# 注意：
# 父类也叫基类，子类也叫派生类，派生类可以继承父类中所有的功能
# 父类也可向上继承父类，父类，子类都是相对的，子类也可继承父类的父类
# 子类父类命名相同的一个方法，优先寻找子类中的方法，并执行
# 在Java中一个子类只能继承一个父类，python一个子类可以继承多个父类，优先级：从左至右


# 多继承：
class Human:
    def eat(self):
        print(self.name + '吃')

    def drink(self):
        print(self.name + 'drink')

    def shit(self):
        print(self.name + 'shit')


class Family:
    def gamble(self):
        print('gamble')

    def tour(self):
        print('tourism')

    def eat(self):
        print(self.name + 'eat....')

class Dog(Human, Family):
    def __init__(self, name):
        self.name = name

badi = Dog('badi')
badi.eat()
'''


'''
# 经典类：深度优先
class D:
    def bar(self):
        print('class D')


class C(D):
    def bar(self):
        print('class C')


class B(D):
    # def bar(self):
    #     print(B.bar)
    pass


class A(B, C):
    # def bar(self):
    #     print(A.bar)
    pass

a = A()
a.bar()

#python2.7  输出 class D
#python3.5  输出 class C

'''





'''

class F:
    def bar(self):
        print('class F')


class E(F):
    pass
    # def bar(self):
    #     print(E.bar)


class D(F):
    pass
    # def bar(self):
    #     print('class D')


class C(E):
    def bar(self):
        print('class C')

class B(D):
    pass
    # def bar(self):
    #     print(B.bar)


class A(B, C):
    # def bar(self):
    #     print(A.bar)
    pass

a = A()
a.bar()

#输出：
# python3.5  输出 class C
# python2.7  输出 class F



# 没有公共基类时，python2/3 都会按照深度优先方式查找

class E:
    def bar(self):
        print(E.bar)


class D:
    def bar(self):
        print('class D')


class C(E):
    def bar(self):
        print('class C')

class B(D):
    pass
    # def bar(self):
    #     print(B.bar)


class A(B, C):
    # def bar(self):
    #     print(A.bar)
    pass

a = A()
a.bar()

#输出：
# python3.5  输出 class D
# python2.7  输出 class D





# super 方法：执行父类的构造方法

class Animal:
    def __init__(self):
        print('A 构造方法')
        self.ty = '动物'


class Cat(Animal):
    def __init__(self):
        print('B构造方法')
        self.n = '猫'
        super(Cat, self).__init__()         # 此处self为c对象，super会自动把self传给init，所以init的括号中不需再写self
        # Animal.__init__(self)             # 注释部分是第二种执行父类构造方法的方法，推荐使用super的方法

c = Cat()
print(c.__dict__)

'''




'''
hasattr方法之反射：利用反射查找面向对象成员归属

通过类可以直接找其中的某个类成员（hasattr）；
通过对象，既可以找对象中的成员，又可以找类中的成员


class Foo:

    def __init__(self, name):
        self.name = name

    def show(self):
        print('show')

obj = Foo('whisky')
r = hasattr(Foo, 'show')
print(r)
r = hasattr(Foo, 'name')
print(r)
# 输出
# True
# False





# 静态字段：
# 存在意义：将每一个对象中重复的东西，只在类中保存一份，即称为静态字段。但如果放在__init__普通字段中，每个实例化出来的对象中都要保存一份

class Province:
    country = '中国'          # 静态字段

    def __init__(self, name):
        temp = 'xxx'         # 普通字段，对象（中）
        self.name = name

    def show(self):          # 普通方法（类中）
        print('show')
        print(self.country)


# 直接访问普通字段
obj = Province('河北省')
print(obj.name)  # 输出 河北省

# 直接访问静态字段
r = Province.country
print(r)           # 输出 中国

# 静态字段在类中，就用类去访问；普通字段在对象中，就用对象去访问，尽量自己去访问属于自己的成员,但是类中的方法，不要用类去访问
# 静态字段在内存中只保存一份
# 普通字段在每个对象中都要保存一份
# 应用场景： 通过类创建对象时，如果每个对象都具有相同的字段，那么就使用静态字段


# 静态方法, 类方法（是静态方法的特殊情况，比静态方法多传递了一个类名参数）：
# 静态方法存在的意义：不需要创建对象，就可以访问这个方法，其实就是函数的功能，无需使用对象封装的内容，和对象没关系了
# 静态方法通过类调用，通过对象也可以访问，访问规则：通过类访问-》静态字段、静态方法、类方法； 通过对象访问-》普通字段、类的方法，不到万不得已，不要乱调用
class Foo:
    country = '中国'

    def __init__(self, name):
        temp = 'xxx'
        self.name = name


    def common(self):
        print('common method')

    @staticmethod
    def xo():         #静态方法可以不带任何参数，没有self，无法传递对象
        print('xo')

    @classmethod
    def feed(cls):     #类方法，至少要有一个cls参数，传递类名
        print('feed', cls)

# 调用普通方法：
f = Foo('whisky')
f.common()      # 输出 common method

# 调用静态方法
Foo.xo()       # 输出 xo  ,通过类调用静态方法

# 调用类方法
Foo.feed()     # 输出 feed <class '__main__.Province'> 类名





# 属性
# property：特性，将方法伪造成字段的形式访问，效果：调用时无需加括号:


class Foo:
    def __init__(self, name):
        self.name = name

    def start(self):
        temp = '%s sb' % self.name
        return temp
    @property                # 定义属性
    def end(self):
        temp = '%s sb' % self.name
        return temp

obj = Foo('lilei')
ret1 = obj.start()          # 调用方法
ret2 = obj.end              # 调用属性
print(ret1)                   # lilei sb
print(ret2)                   # lilei sb

#由属性的定义和调用要注意一下几点：
# 定义时，在普通方法的基础上添加 @property 装饰器；
# 定义时，属性仅有一个self参数
# 调用时，无需括号
# 注意：1.属性存在意义是：访问属性时可以制造出和访问字段完全相同的假象
#      2.属性由方法变种而来，如果Python中没有属性，方法完全可以代替其功能。


# 实例：对于主机列表页面，每次请求不可能把数据库中的所有内容都显示到页面上，而是通过分页的功能局部显示，所以在向数据库中请求数据时就要显示的指定获取从第m条到第n条的所有数据（即：limit m,n），这个分页的功能包括：
#
# 根据用户请求的当前页和总数据条数计算出 m 和 n
# 根据m 和 n 去数据库中请求数据
# ############### 定义 ###############
class Pager:

    def __init__(self, current_page):
        # 用户当前请求的页码（第一页、第二页...）
        self.current_page = current_page
        # 每页默认显示10条数据
        self.per_items = 10


    @property                                           # 完全可以去掉property，调用start方法实现相同的功能
    def start(self):
        val = (self.current_page - 1) * self.per_items
        return val

    @property
    def end(self):
        val = self.current_page * self.per_items
        return val

# ############### 调用 ###############

p = Pager(1)
a = p.start # 就是起始值，即：m
b = p.end   # 就是结束值，即：n
print(a, b) # 输出 0 10
# 从上述可见，Python的属性的功能是：属性内部进行一系列的逻辑计算，最终将计算结果返回。





#在新式类中，具有三种@property装饰器
# setter 设置property特性属性的值，deleter 删除property特性属性的值，用得不广泛，但要看懂
class Foo:
    def __init__(self, name):
        self.name = name

    def start(self):
        temp = '%s sb' % self.name
        return temp

    @property                      # 定义属性,相当于把方法变为字段，调用end方法时不用加括号访问
    def end(self):
        temp = '%s hero' % self.name
        return temp

    @end.setter
    def end(self, value):           # 注意：装饰器中方法的名称要相同，示例中都是end
        print(value)
        self.name = value

    @end.deleter
    def end(self):
        pass
# ############### 调用 ###############

obj = Foo('whisky')
print(obj.name)         # whisky
print(obj.end)          # whisky hero  , 自动执行 @property 修饰的 end 方法，并获取方法的返回值
obj.name = '123'
print(obj.name)         # 123 ,  自动执行 @end.setter 修饰的 end 方法，并将 123 赋值给方法的参数
del obj.end             # 自动执行 @end.deleter 修饰的 price 方法
print(obj.name)         # 123

# 注：经典类中的属性只有一种访问方式，其对应被 @property 修饰的方法
# 新式类中的属性有三种访问方式，并分别对应了三个被@property、@方法名.setter、@方法名.deleter修饰的方法



class Goods(object):

    def __init__(self):
        # 原价
        self.original_price = 100
        # 折扣
        self.discount = 0.8

    @property
    def price(self):
        # 实际价格 = 原价 * 折扣
        new_price = self.original_price * self.discount
        return new_price

    @price.setter
    def price(self, value):
        self.original_price = value

    @price.deleter
    def price(self):
        del self.original_price        #删除了self.original_price这个属性
obj = Goods()
r = obj.price         # 获取商品价格
print(r)
obj.price = 200       # 修改商品原价
del obj.price        # 删除商品原价
'''

'''
# 属性的两种定义方式之二--静态字段方式

class Foo:

    def get_bar(self):
        return 'whisky'

    BAR = property(get_bar)

obj = Foo()
reuslt = obj.BAR        # 自动调用get_bar方法，并获取方法的返回值
print(reuslt)

# property的构造方法中有个四个参数
# 第一个参数是方法名，调用 对象.属性 时自动触发执行方法
# 第二个参数是方法名，调用 对象.属性 ＝ XXX 时自动触发执行方法
# 第三个参数是方法名，调用 del 对象.属性 时自动触发执行方法
# 第四个参数是字符串，调用 对象.属性.__doc__ ，此参数是该属性的描述信息
'''
'''
class Goods(object):

    def __init__(self):
        # 原价
        self.original_price = 100
        # 折扣
        self.discount = 0.8

    def get_price(self):
        # 实际价格 = 原价 * 折扣
        new_price = self.original_price * self.discount
        return new_price

    def set_price(self, value):
        self.original_price = value

    def del_price(self):
        del self.original_price

    PRICE = property(get_price, set_price, del_price, '价格属性描述...')

obj = Goods()
obj.PRICE         # 获取商品价格
obj.PRICE = 200   # 修改商品原价
del obj.PRICE     # 删除商品原价


#注意：Python WEB框架 Django 的视图中 request.POST 就是使用的静态字段的方式创建的属性

#所以，定义属性共有两种方式，分别是【装饰器】和【静态字段】，而【装饰器】方式针对经典类和新式类又有所不同
'''



'''
class C:

    name = "公有静态字段"

    def func(self):
        print(C.name)

class D(C):

    def show(self):
        print(C.name)


C.name         # 类访问

obj = C()
obj.func()     # 类内部可以访问

obj_son = D()
obj_son.show()  # 派生类中可以访问
# 输出
# 公有静态字段
# 公有静态字段
'''


class C:

    def __init__(self):
        self.__foo = "私有字段"

    def func(self):
        print(self.__foo)     # 类内部访问


class D(C):

    def show(self):
        print(self.__foo)     # 派生类中访问

obj = C()

#obj.__foo       # 通过对象访问    ==> 错误
obj.func()      # 类内部访问        ==> 正确

obj_son = D()
#obj_son.show()  # 派生类中访问  ==> 错误