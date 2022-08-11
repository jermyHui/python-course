#!/usr/bin/env python3.8
# -*- coding: UTF-8 -*-
# 打印0到9
# 方法一，while循环
# n = 0
# while n < 10:
#     print(n)
#     n += 1
# 方法二，递归函数
# def f1(n):
#     if n == 10:
#         return
#     print(n)
#     n += 1
#     f1(n)
# f1(0)
# 取出列表中的每一个元素
l = [1,2,3,[4,[5,6,[7,[8,[9,[10]]]]]]]
def f1(n):
    for x in n:
        if type(x) is list:
            f1(x)
        else:
            print(x)
f1(l)
'''
@version:3.8
@author:chenchen
@file:26_函数递归.py
@time:2022/8/11 13:16
'''
