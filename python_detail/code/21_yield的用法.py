#!/usr/bin/env python3.8
# -*- coding: UTF-8 -*-

# 定义一个函数
# def dog(name):
#     print('道哥%s准备吃东西啦。。。。'%name)
#     while True:
#         x = yield
#         print('道哥%s吃了%s'%(name,x))
# g = dog('xx')
# next(g)
# next(g)
# next(g)

# my_list = ['zhubo','zhuzhu','chenchen']
# count = 0
# while count < len(my_list):
#     print(my_list[count])
#     count += 1

# 定义一个生成器函数
def dog(name):
    print('道哥%s准备吃东西啦。。。'%name)
    while True:
        x = yield
        print('道哥%s吃了%s'%(name,x))
g = dog('疫情')
g.send(None)  # 通过send方法可以给yield传值
g.send('大炮')
g.__next__()
'''
@version:3.8
@author:chenchen
@file:21_yield的用法.py
@time:2022/8/10 13:59
'''
