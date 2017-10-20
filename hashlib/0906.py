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
    record_lst = []
    backend_data = 'backend %s' % arg
    with open('HAproxy.txt', 'r') as config_file:
        flag = False
        for line in config_file:
            if line.strip() == backend_data:
                flag = True
                continue
            if flag and line.startswith('backend '):
                break
            if flag and line.strip():     # line为空行为假，不记录
                record_lst.append(line.strip())

        return record_lst


# 根据输入增加节点信息    #输入格式： {"backend": "test.oldboy.org","record":{"server": "100.1.7.9","weight": 20,"maxconn": 30}}
def add(arg):
    inp = arg
    dic = json.loads(inp)
    backend_name = dic['backend']
    record_lst = fetch(backend_name)   # 获取原配置文件中的节点信息
    backend_title = 'backend %s' % backend_name
    current_record = 'server %s weight %d maxconn %d' % (dic['record']['server'], dic['record']['weight'],
                                                         dic['record']['maxconn'])
    if not record_lst:          # 添加的节点不存在,record_lst为空则添加新的backend节点信息
        record_lst.append(backend_title)
        record_lst.append(current_record)
        with open('HAproxy.txt', 'r', encoding='utf-8') as config, open('new.txt', 'w', encoding='utf-8') as new_config:
            for line in config:
                new_config.write(line)

            for new_line in record_lst:
                if new_line.startswith('backend'):
                    new_config.write('\n' + new_line + '\n')
                else:
                    new_config.write('\t\t' + new_line + '\n')

    else:                        # record 不为空，输入的backend_name在原配置文件中存在
        with open('HAproxy.txt', 'r', encoding='utf-8') as config, open('new.txt', 'w', encoding='utf-8') as new_config:
            flag = False
            for line in config:
                if line.strip() == 'backend %s' % backend_name:   # 原config中匹配到backend信息
                    new_config.write(line)                        # 记录当前行
                    for i in record_lst:
                        new_config.write('\t\t' + i + '\n')       # 写入fetch获取的节点信息
                    for j in [current_record]:
                        new_config.write('\t\t' + j + '\n\n')     # 写入当前输入的信息到配置文件中
                    flag = True
                    continue
                if flag and line.strip().startswith('backend'):
                    flag = False
                if not flag:
                    new_config.write(line)
# add('{"backend": "www.docker.com","record":{"server": "1.1.7.19 2.2.2.2","weight": 2110,"maxconn": 30}}')


def delete(arg):
    inp = arg
    dic = json.loads(inp)
    backend_name = dic['backend']
    backend_title = 'backend %s' % backend_name
    record_lst = fetch(backend_name)
    current_record = 'server %s weight %d maxconn %d' % (dic['record']['server'], dic['record']['weight'],
                                                         dic['record']['maxconn'])
    with open('HAproxy.txt', 'r', encoding='utf-8') as config, open('new.txt', 'w', encoding='utf-8') as new_config:
        if record_lst:
            if current_record not in record_lst:
                print('000000000000000000000000')
                #print(current_record)
                #print(record_lst)
            else:
                print(record_lst)
                record_lst.remove(current_record)
                print('------', current_record)
                print(record_lst)
                flag = False
                for line in config:
                    if line.strip() == backend_title:
                        print('------------------')
                        new_config.write('\n' + line + '\n')
                        for i in record_lst:
                            new_config.write('\t\t' + i + '\n')
                        flag = True
                        continue
                    if flag and line.startswith('backend'):
                        print('@@@@@@@@@@@@@@@@@@@@@@')
                        new_config.write(line)
                        flag = False
                    if flag:
                        print('++++++++++++++++++++')
                        new_config.write(line)
        else:
            print('backend is not exists')
'''
backend www.163.com
		 server 129.168.7.21 weight 12 maxconn 21

backend test.oldboy.org
 		server 1210.1.7.19 weight 2110 maxconn 30
'''

delete('{"backend": "test.oldboy.org","record":{"server": "1210.1.7.19","weight": 2110,"maxconn": 30}}')






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
#     r = fetch(bk_name)
#     print(r)

