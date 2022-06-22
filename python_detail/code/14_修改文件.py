#!/usr/bin/env python3.8
# -*- coding: UTF-8 -*-
with open('fix_file.txt',mode='a+t',encoding='utf-8') as f:
    print(f.tell())
    res = f.read()
    res = res.replace('chenchen','zhuzhu')
    print(res)
    f.write(res)
'''
@version:3.8
@author:chenchen
@file:14_修改文件.py
@time:2022/6/21 21:13
'''
