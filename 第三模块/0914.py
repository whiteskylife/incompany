# -*- coding: utf-8 -*-

# 导入模块
m = __import__('0912', fromlist=True)

# 去模块中找类
class_name = getattr(m, 'Foo')

# 根据类创建对象
obj = class_name('whisky')

# 去对象中找name对应的值
val = getattr(obj, 'name')
print(val)      # 输出 whisky