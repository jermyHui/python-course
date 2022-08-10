#!/usr/bin/env python3.8
# -*- coding: UTF-8 -*-
import time

# 定义一个统计函数运行时间的装饰器
def timmer(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        res = func(*args,**kwargs)
        end = time.time()
        print('运行时间为：',end - start)
        return res
    return wrapper

# 定义一个index函数
# 加装饰器
@timmer
def index(x,y,z):
    time.sleep(3)
    print("index函数 %s %s %s"%(x,y,z))
    return 1234

res = index(1,2,3)
print(res)
'''
@version:3.8
@author:chenchen
@file:19_统计运行时间的装饰器.py
@time:2022/7/5 17:33
'''
