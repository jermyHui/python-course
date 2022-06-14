#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 定义列表1
list1 = ['1','abc',['aa','bb']]
# copy列表1为列表3
list3 = list1.copy()

# 打印列表1
print('修改前list1:',list1)
# 打印列表3
print('修改前list3:',list3)

# 打印列表1 id
print('修改前list1:',id(list1))
# 打印列表3 id
print('修改前list3:',id(list3))

print('列表1[0]id',id(list1[0]))
print('列表3[0]id',id(list3[0]))

print('列表1[2][0]id',id(list1[2][0]))
print('列表1[2][1]id',id(list1[2][1]))
print('列表3[2][0]id',id(list3[2][0]))
print('列表3[2][1]id',id(list3[2][1]))
# 修改列表1
list1[0] = 'ccc'
list1[2][0] = 'aaa'
list1[2][1] = 'ccc'
# 打印列表1
print('修改后list1:',list1)
# 打印列表3
print('修改后list3:',list3)
# 打印列表1 id
print('修改后list1:',id(list1))
# 打印列表3 id
print('修改后list3:',id(list3))

print('列表1[2][0]id',id(list1[2][0]))
print('列表1[2][1]id',id(list1[2][1]))
print('列表3[2][0]id',id(list3[2][0]))
print('列表3[2][1]id',id(list3[2][1]))

print('列表1[0]id',id(list1[0]))
print('列表3[0]id',id(list3[0]))

print("修改后")
print('列表1[2][0]id',id(list1[2][0]))
print('列表1[2][1]id',id(list1[2][1]))
print('列表3[2][0]id',id(list3[2][0]))
print('列表3[2][1]id',id(list3[2][1]))