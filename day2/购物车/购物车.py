# -*- coding: utf-8 -*-
#列表循环,字典循环,加入列表append用法（应用：货物加入购物车）
import sys
import os
import datetime

now = datetime.datetime.now()
styleTime = now.strftime("%Y-%m-%d %H:%M:%S")   #获取时间到变量

account = 0                             #消费总金额，账单
shop_car = []                           #购物车列表
final_list = []                             #去重菜单


username = 'root'                                                           #用户名密码写死，单用户固定为root，123
userpassword = '123'
name = input('pls input you username: ')
passwd = input('pls input you passwd: ')
if name == username and passwd == userpassword:
    print('welcome to sky shop'.center(50, '-'))
else:
    print('wrong username or password,exit...')
    sys.exit(1)


if os.path.exists('shopping_record.txt'):                                      #购物记录文件存在，则直接导入购物历史
    print('import you shopping record ...')
    if os.path.exists('balance.txt'):
        with open('balance.txt', 'r', encoding='utf-8') as history_balance:    #从余额文件获取上次购物余额
            salary = int(history_balance.readline())
            print('you last shopping balance : \033[1;41;36m%s\033[0m' % salary)
            history = input('input h to print shopping history:')
            if history == 'h':
                with open('shopping_record.txt','r',encoding='utf-8') as history_line:
                    for line in history_line.readlines():
                        print(line)
            else:
                pass
else:
    salary = int(input('please input salary: '))                             #购物历史不存在则输入薪水
    if salary < 600:
        print('you can not afford any goods ,exit...')
        sys.exit(1)
    else:
        pass

shopping_list = [                                               #商品列表
    ['Iphone 7', 6400, 0],
    ['Iphone 7 plus', 7400, 0],
    ['Mac book air', 6800, 0],
    ['Mac book Pro', 9288, 0],
    ['T-shirt', 588, 0],
    ['Nike', 698, 0],
    ['PC', 4680, 0]
]

#----------------程序开始----------------------------------------------------------------------
flag = True
while flag:
    print('Product list'.center(50, '-'))
    for index, content in enumerate(shopping_list):
        p_name = content[0]
        p_price = content[1]
        print(index, '.', p_name, p_price)                       #打印商品列表
    choice = input('chose which you want: ')                   #选择商品编号
    amount = input('num : ')                                      #购买数量
    if choice.isdigit() and amount.isdigit():
        choice = int(choice)                                        #str转int
        amount = int(amount)
        if choice < len(shopping_list):                              #判断输入产品序号
            account = shopping_list[choice][1]*amount                 #消费总金额=商品单价*数量
            if account <= salary:                                     #can afford
                shopping_list[choice][2] += amount                  # 统计购买的商品数量
                shop_car.append(shopping_list[choice])              #add the goods to shop car
                for i in shop_car:                                      #购物车去重
                    if i not in final_list:
                        final_list.append(i)
                salary -= account                                      #calculating balance
                print('you have already bought \033[1;41;36m%s\033[0m, your current balance \
is \033[1;41;36m%s\033[0m' % (final_list, salary))
            else:
                print('your balance is \033[1;41;36m%s\033[0m,can not afford this item..' % salary)
        else:
            print('which your choice is not exist!!!')
            continue
    elif choice == 'q' or choice == 'quit':
        with open('shopping_record.txt', 'a+', encoding='utf-8') as record:
            record.write('shopping time:')
            record.write(styleTime)
            record.write('\n')
            for i in final_list:
                record.write(i[0])
                record.write(' ')
                record.write(str(i[1]))
                record.write(' ')
                record.write(str(i[2]))
                record.write('\n')
                print(i)

            print('you have bought '.center(40, '*'))
            print(final_list)
            print('your balance is \033[1;41;36m%s\033[0m,' % salary)
            with open('balance.txt', 'w+', encoding='utf-8') as balance:
                balance.write(str(salary))
                flag = False
    else:
        print('pls input num'.center(50, '-'))