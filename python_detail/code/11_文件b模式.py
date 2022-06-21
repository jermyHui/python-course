#!/usr/bin/env python3.8
# -*- coding: UTF-8 -*-
# 复制拷贝文件
with open(r'C:\Users\hui\Pictures\0930-1.jpg',mode='rb') as A:
    with open(r'd.jpg',mode='ab') as B:
        A.read()
        A.seek(0,0)
        print(A.tell())
        for line in A:
            B.write(line)
'''
@version:3.8
@author:chenchen
@file:11_文件b模式.py
@time:2022/6/21 14:02
'''


