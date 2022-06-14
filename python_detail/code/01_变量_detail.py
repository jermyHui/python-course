#!/usr/bin/python
# -*- coding: UTF-8 -*-

# python解释器的小整数池 -5 --- 256，pycharm处理的范围更大，但是编程时要遵循python解释器的原则

# 用变量的定义说明int、float、str、list、dict、bool类型用于记录何种状态，每种类型至少写出三个示例
# int
age = 18
height = 45
year = 2022
# float
salary = 17.3
high = 167.3
cat_height = 3.7
# str
name = 'panghu'
gender = 'female'
address = 'beijing'
# list
grade = [98,79,80]
name = ['zhubo','panghu','shiliu']
gender = ['male','male','female']
# dict
info = {'name':'panghu','gender':'male','age':1}
# bool
a = True
b = False


print("test")
def foo(n):
    print('foo say hello')
    return n
print(f"{foo(10)}")


l = ['aaa','bbb','cccc']
print('l',id(l))

l = ['bbbbb','vvvvvvv']
print('l',id(l))
print(id(l[1]))
l[0] = '1'
print('l',id(l))
print(id(l[1]))

print(10 < 3 and True)
print(10 < 3 and 5)