# -*- coding: utf-8 -*-
import menu
from .import menu


'''
os.system('python C:/Users/w/PycharmProjects/python/day2/menu.py')
menu = {
    '广东': {
        '深圳': {
            '南山': ['海上世界', '世界之窗', '锦绣中华'],
            '福田': ['上沙', '下沙', '京基100'],
            '华强北': ['电子世界', '电子天堂', '元件批发']
         },
        '惠州': {
            '惠阳': ['淡水', '开发区', '新余'],
            '仲恺区': ['陈江', '惠环', '沥林'],
            '龙门县': ['南昆山',  '永汉'],
        },
        '广州': {
            '天河': ['白云']
        }
    },
    '天津': {
        '东丽': {
            '大毕庄': ['向阳']
        },
        '河东': {
            '中山门': ['常州道']
        }
    },
    '杭州': {
        '西湖': {
            '黄龙': ['古荡']
        },
        '滨江': {
            '长河': ['彩虹城']
        }
    }
}
'''
while True:
    for i in menu:
        # 打印key
        print(i)
    choice = input('your choice: ')
    if choice in menu:
        while True:
            for j in menu[choice]:
                # 打印第二层key
                print(j)
            choice2 = input('your choice2: ')
            if choice2 in menu[choice]:
                while True:
                    for k in menu[choice][choice2]:
                        # 打印第三层key
                        print(k)
                    choice3 = input('your choice3: ')
                    if choice3 in menu[choice][choice2]:
                        # 检查第二层菜单有无choice3的key值
                        for m in menu[choice][choice2][choice3]:
                            print(m)
                        choice4 = input('最后一层，按b返回： ')
                        if choice4 == 'b':
                            pass
                        elif choice4 == 'q':
                            sys.exit()
                    elif choice3 == 'b':
                        break
                    elif choice3 == 'q':
                        sys.exit()
            elif choice2 == 'b':
                break
            elif choice2 == 'q':
                sys.exit()
    elif choice == 'q':
        sys.exit()
