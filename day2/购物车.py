# -*- coding: utf-8 -*-
#列表循环,字典循环,加入列表append用法（应用：货物加入购物车）
salary = int(input('please input salary: '))
account = 0
shopping_list = [
    ['Iphone 7', 6400, 0],
    ['Iphone 7 plus', 7400, 0],
    ['Mac book air', 6800, 0],
    ['Mac book Pro', 9288, 0],
    ['T-shirt', 588, 0],
    ['Nike', 698, 0],
    ['PC', 4680, 0]
]
shop_car = []
final_list = []

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
                for i in shop_car:
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
        print('you have bought '.center(40, '*'))
        print(final_list)
        print('your balance is \033[1;41;36m%s\033[0m,' % salary)
        flag = False
    else:
        print('pls input num'.center(50, '-'))














