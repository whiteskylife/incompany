# -*- coding: utf-8 -*-

import time
import pickle
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from config import settings


class Teacher:
    '''
    创建老师
    '''
    def __init__(self, name, gender, age, admin):
        self.name = name
        self.gender = gender
        self.age = age
        self.asset = 0
        self.create_time = time.strftime('%Y-%m-%d %H:%M:%S')
        self.create_admin = admin


class Course:
    '''
    创建课程
    '''
    def __init__(self, course_name, course_time, course_cost, teacher, admin):
        self.course_name = course_name
        self.course_time = course_time
        self.course_cost = course_cost
        self.create_time = time.strftime('%Y-%m-%d %H:%M:%S')
        self.teacher = teacher
        self.create_admin = admin


class Admin:                # 支持多个管理员账号
    '''
    管理员注册、登录
    '''
    def __init__(self):
        self.username = None
        self.userpasswd = None

    def register(self, user, passwd):
        self.username = user
        self.userpasswd = passwd
        path = os.path.join(settings.BASE_ADMIN_DIR, self.username)  # 拼接管理员注册存储文件的路径
        pickle.dump(self, open(path, 'wb'))

    def login(self, user, passwd):
        if self.username == user and self.userpasswd == passwd:
            return True


class Student:
    """
    学生信息
    """
    def __init__(self):
        self.username = None
        self.password = None

        self.course_list = []
        self.course_name_list = []
        self.study_dict = {}

    def select_course(self, course_obj):
        """
        选课
        :param course_obj:
        :return:
        """
        self.course_list.append(course_obj)

    def study(self, course_obj):
        """
        上课
        :param course_obj:
        :return:
        """
        class_result = course_obj.have_lesson()

        if course_obj in self.study_dict.keys():
            self.study_dict[course_obj].append(class_result)
        else:
            self.study_dict[course_obj] = [class_result, ]

    def login(self, user, pwd):
        """
        学生登录
        :param user:
        :param pwd:
        :return:
        """

        if self.username == user and self.password == pwd:
            return True
        else:
            return False

    def register(self, user, pwd):
        """
        学生注册, 把注册对象写入文件
        :param user:
        :param pwd:
        :return:
        """
        self.username = user
        self.password = pwd
        path = os.path.join(settings.BASE_STUDENTS_DIR, self.username)
        pickle.dump(self, open(path, 'wb'))

