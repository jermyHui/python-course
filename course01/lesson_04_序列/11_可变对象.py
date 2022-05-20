#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 创建一个列表
a = [1,2,3]
print("修改前：","a:",a,"id_a:",id(a))

# 修改对象
a[0] = 10
print("修改后：","a:",a,"id_a:",id(a))

# 修改变量
a = [10,11,12]
print("修改后：","a:",a,"id_a:",id(a))

# 新建一个和a相等的变量b
b = a
print("修改前：","b:",b,"id_b:",id(b))
# 修改b的值
b[0] = 19
print("修改后：","b:",b,"id_b:",id(b))
print("修改后：","a:",a,"id_a:",id(a))

# 修改变量b
b = [20,1,5]
print("修改后：","b:",b,"id_b:",id(b))
print("修改后：","a:",a,"id_a:",id(a))


