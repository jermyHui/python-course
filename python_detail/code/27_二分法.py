#!/usr/bin/env python3.8
# -*- coding: UTF-8 -*-
nums = [1,2,4,5,6,7,8,10]
def binary_search(find_num,l):
    print(l)
    # 如果列表为空，则所找的元素不存在
    if len(l) == 0:
        print("没找到")
        return
    # 定义列表中间元素下标
    mid_index = len(l) // 2
    # 定义列表中间元素
    mid_val = l[mid_index]
    # 如果所找元素在列表右半段，继续查找
    if find_num > mid_val:
        l = l[(mid_index +1):]  # 通过切片切出列表右半段
        binary_search(find_num,l)
    # 如果所找元素在列表左半段，继续查找
    elif find_num < mid_val:
        l = l[:mid_index]  # 通过切片切出列表左半段
        binary_search(find_num, l)
    else:
        print('find it')
binary_search(10,nums)

'''
@version:3.8
@author:chenchen
@file:27_二分法.py
@time:2022/8/11 14:46
'''
