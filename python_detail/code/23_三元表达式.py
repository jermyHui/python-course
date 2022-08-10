#!/usr/bin/env python3.8
# -*- coding: UTF-8 -*-
# 将if、else判断改为三元表达式
# 定义一个函数返回两个数中的最大值
def maximum(x,y):
    if x > y:
        return x
    else:
        return y
res = maximum(2,3)
print(res)

# 将函数中的内容通过三元表达式实现
def maximum_1(x,y):
    return x if x >y else y
res = maximum_1(4,5)
print(res)
'''
@version:3.8
@author:chenchen
@file:23_三元表达式.py
@time:2022/8/10 18:46
'''
