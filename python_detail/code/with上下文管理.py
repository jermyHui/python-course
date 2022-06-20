#!/usr/bin/env python3.8
# -*- coding: UTF-8 -*-
# 通过with方法操作文件
with open('a.txt',mode='rt') as f1,\
    open('b.xtxt',mode='rt') as f2:
    res1 = f1.read()
    res2 = f2.read()
    print(res1)
    print(res2)

'''
@version:3.8
@author:chenchen
@file:with上下文管理.py
@time:2022/6/20 13:58
'''
