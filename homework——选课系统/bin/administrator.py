# -*- coding: utf-8 -*-

# 选课系统

import pickle
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from lib import modules
from config import settings


def create_teacher(admin_obj):
    '''
    创建老师，并把老师对象写入文件
    '''
    teacher_list = []
    while True:
        name = input('pls input name(q:exit): ')
        if name == 'q':
            break
        gender = input('gender: ')
        age = input('age: ')
        teacher_obj = modules.Teacher(name, gender, age, admin_obj)
        teacher_list.append(teacher_obj)
        path = os.path.join(settings.TEACHER_DB_DIR)
        if os.path.exists(path):
            exists_list = pickle.load(open(path, 'rb'))
            teacher_list.extend(exists_list)
        pickle.dump(teacher_list, open(path, 'wb'))


def create_course(admin_obj):
    """
    创建课程，并把课程对象一次放入列表，再写入文件
    """
    path = os.path.join(settings.TEACHER_DB_DIR)
    teacher_list = pickle.load(open(path, 'rb'))
    for num, teacher in enumerate(teacher_list, 1):
        print(num, teacher.name, teacher.gender, teacher.age, teacher.asset,
              teacher.create_time, teacher.create_admin.username)  # teacher.create_admin.username创建老师的管理员名字
    course_lst = []
    while True:
        name = input('pls input course name(q: exit): ')
        if name == 'q':
            break
        course_time = input('pls input course time: ')
        course_cost = input('pls input the price of the course:')
        num = input('pls input num: ')
        course_obj = modules.Course(name, course_time, course_cost, teacher_list[int(num)-1], admin_obj)  # teacher对象列表从0开始，课程序号从1开始，所以-1
        course_lst.append(course_obj)
        path = os.path.join(settings.COURSE_DB_DIR)
        if os.path.exists(path):
            exists_list = pickle.load(open(path, 'rb'))
            course_lst.extend(exists_list)
        pickle.dump(course_lst, open(path, 'wb'))


def login():
    inp_acc = input('pls input your account:')
    inp_pwd = input('pls input your password:')
    path = os.path.join(settings.BASE_ADMIN_DIR, inp_acc)
    if os.path.exists(path):
        admin_obj = pickle.load(open(path, 'rb'))
        if admin_obj.login(inp_acc, inp_pwd):
            print('login success!')
            while True:
                choose = input('1.创建老师 \n2.创建课程 ')
                if choose == '1':
                    create_teacher(admin_obj)
                elif choose == '2':
                    create_course(admin_obj)
                else:
                    break
        else:
            print('User or Password Wrong !')
    else:
        print('your account is not exists, pls register first!')


def main():
    while True:
        msg = '''
    1.管理员登录
    2.注册管理员
    3.退出
    请输入选择：
        '''
        inp = input(msg)
        if inp == '1':
            login()
        elif inp == '2':
            inp_acc = input('pls input your account:')
            admin_obj = modules.Admin()             # 调用从lib中导入的modules模块
            path = os.path.join(settings.BASE_ADMIN_DIR, inp_acc)
            if os.path.exists(path):
                print('username already exists...')
                continue
            inp_pwd = input('pls input your password:')
            admin_obj.register(inp_acc, inp_pwd)   # register会进行pickle dump
        elif inp == '3':
            exit()
        else:
            print('Wrong input--!')

if __name__ == "__main__":
        main()

