#!/usr/bin/env python3.8
# -*- coding: UTF-8 -*-
with open('a.txt',mode='r',encoding='utf-8') as a:
    res = a.read()
    with open('c.txt',mode='w',encoding='utf-8') as c:
        c.write(res)
'''
@version:3.8
@author:chenchen
@file:10_编写文本文件copy程序.py
@time:2022/6/20 17:47
'''
