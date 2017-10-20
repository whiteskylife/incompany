# -*- coding: utf-8 -*-

import random

# 生成指定范围随机数
# a = random.randrange(1, 100)  #不包括边界
# b = random.randint(1, 100)  #包括边界


# 问题描述
#
# 按照下面的要求实现对列表的操作：
#
# 产生一个列表，其中有40个元素，每个元素是0到100的一个随机整数
# 如果这个列表中的数据代表着某个班级40人的分数，请计算成绩低于平均分的学生人数，并输出
# 对上面的列表元素从大到小排序
# 知识点：random sort sum
#
# def aver(arg):
#     return sum(arg)/len(arg)
#
#
# def gener_lst():
#     lst1 = []
#     for num in range(40):
#         lst1.append(random.randint(1, 100))
#     return lst1
#
#
# lst = gener_lst()
# for i in lst:
#     if i < aver(lst):
#         lst.remove(i)
#
# print('marks lower than average: ', lst, '\ntotal is: %d stus ' % len(lst))
# lst.sort(reverse=True)
# print('sort by mark :', lst)



    