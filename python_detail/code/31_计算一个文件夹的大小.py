#!/usr/bin/env python3.8
# -*- coding: UTF-8 -*-
import os
# print(os.path.isfile('D:\github\python_detail\code\19_统计运行时间的装饰器.py'))

def get_filesize(dir):
    # 初始化文件大小的变量
    size = 0
    # 列出目录下的子目录并且遍历
    f_list = os.listdir(dir)
    for i in f_list:
        # 判断目录是文件则获取大小累加
        if os.path.isfile(i):
            i_size = os.path.getsize(i)
            size += i_size
        # 判断是文件夹，则递归
        elif os.path.isdir(i):
            os.chdir(i)
            i_path = os.getcwd()
            get_filesize(i_path)
    return size
file_size = get_filesize('D:\github\python_detail\code')
print(file_size)
'''
@version:3.8
@author:chenchen
@file:31_计算一个文件夹的大小.py
@time:2022/8/25 12:18
'''
