# -*- coding: utf-8 -*-

'''
# 计算100-300之间所有能被3和7整除的所有数之和
l = []
for i in range(100, 301):
    if i % 3 == 0 and i % 7 == 0:
        l.append(i)
    else:
        pass
print(sum(l))
print(l)


# 定义函数统计一个字符串中大写字母，小写字母，数字的个数，并返回结果
# ascii码对应：  0-9 : 48-57 a-z : 97-122  A-Z : 65-90
char = '123qweqwqeASD'

num_list = []
lower_case = []
capital = []


def count(arg):
    for i in list(arg):
        if ord(i) in range(48, 58):
            num_list.append(i)
        elif ord(i) in range(97, 123):
            lower_case.append(i)
        elif ord(i) in range(65, 90):
            capital.append(i)

    print('The num is: %s , sum: %d ' % (num_list, len(num_list)))
    print('The lower is: %s , sum: %d ' % (lower_case, len(lower_case)))
    print('The capital is: %s , sum: %d ' % (capital, len(capital)))

count(char)


# 获取两个列表l1 = [11, 22, 33], l2 = [22, 33, 44] 中相同的元素集合

l1 = [11, 22, 33]
l2 = [22, 33, 44]

a = set(l1)
b = set(l2)
print(a & b)  # print(a.intersection(b))


# 将字符串“杜拉拉”转换成UTF-8编码的字节类型

import sys

print(sys.getdefaultencoding())

bytes('杜拉拉', encoding='utf-8')

# 列举布尔值为False的值
print(bool(''), bool(0), bool(False), bool([]), bool(()), bool({}), bool(None))

'''

'''
HAproxy配置文件操作：
1. 根据用户输入输出对应的backend下的server信息
2. 可添加backend 和sever信息
3. 可修改backend 和sever信息
4. 可删除backend 和sever信息
5. 操作配置文件前进行备份
6 添加server信息时，如果ip已经存在则修改;如果backend不存在则创建；若信息与已有信息重复则不操作
配置文件 参考 http://www.cnblogs.com/alex3714/articles/5717620.html

'''
import json
import re


def backup():
    with open('HAproxy.txt', 'r') as ori, open('HAproxy.txt.bak', 'w') as bak:
        for line in ori:
            bak.write(line.strip('\n'))
            bak.write('\n')


# 查询函数，根据backend查询对应节点信息
def fetch(arg):
    flag = 't'
    backend_list = []
    backend_name = arg
    with open('HAproxy.txt', 'r') as config_file:
        for line in config_file:
            if line.strip() == 'backend %s' % backend_name:
                flag = 'nt'
                continue                                       # 检测到backend，继续循环读取配置文件的行，并让flag值为nt开始记录
            if flag == 'nt':
                if line.strip().startswith('backend'):
                    flag = 't'
                    break                                      # 单个backend读取完毕，退出for循环
                else:
                    if line.strip():                           # 空行为假，排除空行
                        backend_list.append(line.strip())
        return backend_list


# 根据输入增加节点信息    #输入格式： {"backend": "test.oldboy.org","record":{"server": "100.1.7.9","weight": 20,"maxconn": 30}}
def add(arg):
    inp = arg
    dic = json.loads(inp)
    bk = dic['backend']
    record = 'server %s weight %d maxconn %d' % (dic['record']['server'], dic['record']['weight'],
                                                 dic['record']['maxconn'])
    flag = 't'
    flag_new_bk = 'f'
    var = ''
    backend_lst = fetch(dic['backend'])         # 节点信息都存在列表中
    backend_lst.append(record)                  # 添加新的节点到列表中
    new_backend_lst = []
    new_backend_lst_node = []
    with open('HAproxy.txt', 'r', encoding='utf-8') as config, open('new.txt', 'w', encoding='utf-8') as new_config:
        for l in config:
            var = re.search(bk, l.strip())
            if var != 'None':
                flag_new_bk = 't'
        if flag_new_bk == 'f':
            print(var, 'pass--------------------------------------')
            pass
        else:
            new_backend_lst.append(bk)
            new_backend_lst_node.append(record)
            new_config.write('\n\nbackend %s \n \t\t%s \n' % (new_backend_lst[0], new_backend_lst_node[0]))

    with open('HAproxy.txt', 'r', encoding='utf-8') as config, open('new.txt', 'w', encoding='utf-8') as new_config:
        for line in config:
            if line.strip() == 'backend %s' % bk:       # line默认有换行符号，不用strip无法进入这个if条件
                flag = 'f'
                new_config.write(line)
                for i in backend_lst:
                    new_config.write('\t\t%s \n' % i)
                continue
            if flag == 't':
                new_config.write(line)
            else:
                if line.strip().startswith('backend'):
                    flag = 't'
                    new_config.write(line)

    # with open('new.txt', 'a+', encoding='utf-8') as append_config:
    #     if flag_new_bk == 't':
    #         append_config.write('\n\nbackend %s \n \t\t%s \n' % (new_backend_lst[0], new_backend_lst_node[0]))

#    new_config.write('\nbackend %s \n %s \n' % (bk, record))

add('{"backend": "1test.oldboy.org","record":{"server": "11111210.1.7.19","weight": 2110,"maxconn": 30}}')


#def delete():



# msg = '''
# 1、获取ha记录
# 2、增加ha记录    # bk_name 存在，则添加记录；不存在则创建节点并添加记录
# 3、删除ha记录
# '''
# print(msg)
# num = input('请输入序号:')
#
# if num == '1':
#     bk_name = input('请输入backend名称：')
#     fetch(bk_name)