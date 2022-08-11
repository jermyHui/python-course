#!/usr/bin/env python3.8
# -*- coding: UTF-8 -*-
# 统计一个文件中的字符数
with open('test.log',mode='rt',encoding='utf-8') as f:
    # 方式一
    # res = 0
    # for line in f:
    #     res += len(line)
    # print(res)
    # 方式二，生成器表达式
    res = sum(len(line) for line in f)
    print(res)
'''
@version:3.8
@author:chenchen
@file:25_生成器表达式.py
@time:2022/8/11 12:27
'''
