#!/usr/bin/env python3.8
# -*- coding: UTF-8 -*-
import os
import random

# 通过random方法产生一个1-100间的随机整数
computer_number = random.randint(1,100)

while True:
    # 提示用户输入1-100间的任意整数
    user_number = int(input("请输入1-100间的任意整数"))
    # 通过比较两个数值的大小提示用户
    if user_number < computer_number:
        print("大一点")
    elif user_number > computer_number:
        print("小一点")
    # 如果猜对了则退出循环
    else:
        print("猜对了")
        break
'''
@version:3.8
@author:chenchen
@file:random.py
@time:2023/3/14 12:54
'''


