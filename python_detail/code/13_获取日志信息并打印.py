#!/usr/bin/env python3.8
# -*- coding: UTF-8 -*-
import time

with open('test.log',mode='rb') as f:
    # 将指针放到文件最后
    f.seek(0,2)
    # 通过while循环获取新增的日志
    while True:
        res = f.readline().decode('utf-8')
        if len(res) == 0:
            time.sleep(0.3)
        else:
            print(res)
'''
@version:3.8
@author:chenchen
@file:13_获取日志信息并打印.py
@time:2022/6/21 20:50
'''
