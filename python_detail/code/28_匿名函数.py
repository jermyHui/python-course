#!/usr/bin/env python3.8
# -*- coding: UTF-8 -*-
salaries = {
    'siry':3000,
    'tom':7000,
    'lili':10000,
    'jack':2000
}
# def fun(s):
#     def funs(k):
#         for k in s:
#             return s[k]
#     res = max(s,key=funs)
#     print(res)
# fun(salaries)
res = max(salaries,key=lambda k:salaries[k])
print(res)
'''
@version:3.8
@author:chenchen
@file:28_匿名函数.py
@time:2022/8/11 19:45
'''
