# -*- coding: utf-8 -*-

# 选课系统

import pickle
import os
import time


class Teacher:
    def __init__(self, name, gender, age, admin):
        self.name = name
        self.gender = gender
        self.age = age
        self.asset = 0
        self.create_time = time.strftime('%Y-%m-%d %H:%M:%S')
        self.create_admin = admin


class Course:
    def __init__(self, course_name, course_time, course_cost, teacher, admin):
        self.course_name = course_name
        self.course_time = course_time
        self.course_cost = course_cost
        self.create_time = time.strftime('%Y-%m-%d %H:%M:%S')
        self.teacher = teacher
        self.create_admin = admin


class Student:
    def __init__(self, account, password, gender, age, course_list, class_record):
        self.account = account
        self.password = password
        self.gender = gender
        self.age = age
        self.course_list = course_list
        self.class_record = class_record

    def choose_course(self):
        pass


class Admin:                # 支持多个管理员账号
    def __init__(self):
        self.username = None
        self.userpasswd = None

    def register(self, user, passwd):
        self.username = user
        self.userpasswd = passwd
        pickle.dump(self, open(self.username, 'wb'))

    def login(self, user, passwd):
        if self.username == user and self.userpasswd == passwd:
            return True


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
        teacher_obj = Teacher(name, gender, age, admin_obj)
        teacher_list.append(teacher_obj)
        if os.path.exists('teacher_list'):
            exists_list = pickle.load(open('teacher_list', 'rb'))
            teacher_list.extend(exists_list)
        pickle.dump(teacher_list, open('teacher_list', 'wb'))


def create_course(admin_obj):
    '''
    创建课程，并把课程对象写入文件
    '''
    teacher_list = pickle.load(open('teacher_list', 'rb'))
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
        course_obj = Course(name, course_time, course_cost, teacher_list[int(num)-1], admin_obj)  # teacher对象列表从0开始，课程序号从1开始，所以-1
        course_lst.append(course_obj)
        if os.path.exists('course_list'):
            exists_list = pickle.load(open('course_list', 'rb'))
            course_lst.extend(exists_list)
        pickle.dump(course_lst, open('course_list', 'wb'))


def login():
    inp_acc = input('pls input your account:')
    inp_pwd = input('pls input your password:')
    if os.path.exists(inp_acc):
        admin_obj = pickle.load(open(inp_acc, 'rb'))
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
            admin_obj = Admin()
            #if os.path.exists(inp_acc):
            if os.path.exists(admin_obj.username):
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


'''

choose_course_lst = []
course_record = {}


s1 = Student('whisky', '123456', 'male', '26', course_ls, course_record)

input_account = input('pls input your account: ')
input_pwd = input('pls input your password: ')


def create_teacher():
    teacher_name = input('pls input teacher name: ')
    teacher_gender = input('pls input teacher gender: ')
    teacher_age = input('pls input teacher ager: ')
    teacher_obj = Teacher(teacher_name, teacher_gender, teacher_age)

if input_account == 'administrator':
    choose = input

    if choose == '1':
        create_teacher()
    elif choose == '2':
        pass

print(course_ls[0], course_ls[1])
input_course = input('Enter the name of the course you have chosen: ')

'''
