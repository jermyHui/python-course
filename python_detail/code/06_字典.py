#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 作业
# 练习1、用列表模拟队列的入队与出队操作
# 先进先出
# 定义一个空列表
'''
list = []
list.append('hahaha')
list.append('aaaa')
list.append(1)
print(list)
del list[0]
print(list)
del list[0]
print(list)
del list[0]
print(list)
'''


# 练习2、用列表模拟堆栈的入队与出队操作
# 后进先出
# list = []
# list.append('hahaha')
# print(list)
# list.append('aaaa')
# print(list)
# list.append(1)
# print(list)
# list.pop()
# print(list)
# list.pop()
# print(list)
# list.pop()
# print(list)

# 练习3
# 定义列表
l = ['egon','alex_sb','lxx']
# 剪切alex_sb,赋值给新的变量
a = l.pop(1)
print(l,a)

# 练习4
# 元组是不可变的列表，当列表只读不需要修改时可以用元组
# 练习5
# 不冲突，修改的是元组内的可变量，并没有修改元组的元素id
# 使用get
# 列表不能，字典可以（d.setdefault()、d.update()）
