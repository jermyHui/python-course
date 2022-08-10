#!/usr/bin/env python3.8
# -*- coding: UTF-8 -*-
import time
# 定义一个index函数
def index(x,y,z):
    time.sleep(3)
    print("index函数 %s %s %s"%(x,y,z))
def outter(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        func(*args,**kwargs)
        end = time.time()
        print('运行时间为：',end - start)
    return wrapper
index = outter(index)
index(1,2,3)

'''
@version:3.8
@author:chenchen
@file:18_函数装饰器.py
@time:2022/7/5 16:14
'''
