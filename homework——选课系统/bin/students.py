# -*- coding: utf-8 -*-

import os
import sys
import pickle
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from config import settings
from lib import modules


def course_info(student_obj):
    for item in student_obj.course_list:
        print(item.course_name, item.teacher.name)


def select_course(student_obj):
    course_list = pickle.load(open(settings.COURSE_DB_DIR, 'rb'))                 # 得到课程对象列表
    for num, item in enumerate(course_list, 1):                                   # 取课程对象，且课程对象中封装了老师对象
        print(num, item.course_name, item.course_cost, item.teacher.name)         # 输出课程列表
    while True:
        num = input('请选择课程(q,exit)：')
        if num == 'q':
            break
        selected_course_obj = course_list[int(num)-1]
        if selected_course_obj.course_name in student_obj.course_name_list:         # 判断课程是否被选过
            print('Course already selected...')
        else:
            student_obj.course_name_list.append(selected_course_obj.course_name)
            student_obj.course_list.append(selected_course_obj)
    pickle.dump(student_obj, open(os.path.join(settings.BASE_STUDENTS_DIR, student_obj.username), 'wb'))


def go_to_class():
    pass


def login(user, pwd):
    # path = os.path.join(os.path.dirname(os.path.dirname(__file__)) + '\db\students', user)
    # print(path)
    if os.path.exists(os.path.join(settings.BASE_STUDENTS_DIR, user)):
        student_obj = pickle.load(open(os.path.join(settings.BASE_STUDENTS_DIR, user), 'rb'))  # 拿到注册的对象
        if student_obj.login(user, pwd):
            print('login success!!')
            while True:
                inp = input('1.选课 2.上课 3.查看课程信息(q:exit)\n')
                if inp == '1':
                    select_course(student_obj)
                elif inp == '2':
                    go_to_class()
                elif inp == '3':
                    course_info(student_obj)
                elif inp == 'q':
                    break
        else:
            print('login failure... check your account/password')
    else:
        print('用户不存在！！')


def register(user, pwd):
    obj = modules.Student()
    obj.register(user, pwd)


def main():
    inp = input('1、登录；2、注册\n')
    user = input("用户名：")
    pwd = input('密码：')
    if inp == '1':
        login(user, pwd)
    elif inp == '2':
        register(user, pwd)

if __name__ == "__main__":
    main()




