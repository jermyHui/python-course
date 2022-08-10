#!/usr/bin/env python3.8
# -*- coding: UTF-8 -*-
# 定义一个字典
# my_dict = {'a':1,'b':2,'c':3}
# 将字典转化为迭代器对象
# my_dict_iterator = my_dict.__iter__()
# 调用迭代器,循环遍历
#



# 打开一个文件
with open('test.log',mode='r',encoding='utf-8') as f:
    f_interator = f.__iter__()
    while True:
        try:
            print(f_interator.__next__())
        except StopIteration:
            break


'''
@version:3.8
@author:chenchen
@file:22_迭代器.py
@time:2022/8/10 14:50
'''
