#!/usr/bin/env python3.8
# -*- coding: UTF-8 -*-
# 找出两个数中的最大值
def max2(a,b):
    if a > b:
        return a
    else:
        return b
# 找出四个数的最大值
def max4(a,b,c,d):
    # 比较a、b得到res1
    res1 = max2(a,b)
    # 比较 res1、c得到res2
    res2 = max2(res1,c)
    # 比较res2、d得到res3
    res3 = max2(res2,d)
    return res3
res = max4(1,2,3,4)
print(res)
'''
@version:3.8
@author:chenchen
@file:17_函数的嵌套.py
@time:2022/7/5 13:15
'''
