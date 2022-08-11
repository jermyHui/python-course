#!/usr/bin/env python3.8
# -*- coding: UTF-8 -*-
# 定义一个列表
l = ['alex_dsb','lxx_dsb','wxx_dsb','xxq_dsb','egon']
# 通过列表生成式将列表内小写字母都改为大写
l = [name.upper() for name in l]
# 通过列表生成式去掉列表元素的_dsb后缀
l = [name.split('_')[0] for name in l]
print(l)
'''
@version:3.8
@author:chenchen
@file:24_列表生成式.py
@time:2022/8/10 19:06
'''
