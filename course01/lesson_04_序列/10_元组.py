#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 创建一个元组
my_tuple = ()
# 打印元组和类型
print("my_tuple:",my_tuple,"类型是：",type(my_tuple))

# 给元组赋值
my_tuple = 1,2,3
# 打印元组和类型
print("my_tuple:",my_tuple,"类型是：",type(my_tuple))
"""
# 修改元组
my_tuple[0] = 4 # 元组是不可变序列，不支持修改
print("my_tuple:",my_tuple,"类型是：",type(my_tuple))
"""
# 打印元组id
print(id(my_tuple))

# 给元组重新赋值
my_tuple = 4,5,6
# 打印元组id
print(id(my_tuple))

a,b,c = my_tuple
print(a,b,c)

a,*b = my_tuple
print(a,b)