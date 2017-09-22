# -*- coding:utf-8 -*-
count = 0
while True:
    count += 1
    if count > 50 and count < 60:
        continue
    elif count == 100:
        break
    else:
        print("你是风儿我是沙,缠缠绵绵到天涯...", count)
