# -*- coding: utf-8 -*-


file = open('demo.jpg', 'rb')
for line in file:
    print(len(line))