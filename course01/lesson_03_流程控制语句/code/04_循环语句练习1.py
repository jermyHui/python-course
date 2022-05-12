#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 初始化表达式，创建一个变量
i = 1
# 定义奇数变量，并赋值第一个奇数
OddNumber = 1
# 奇数小于99时进入循环，并把每次循环结果相加
while i < 99:
    i += 2
    OddNumber += i
# 奇数大于99时退出循环，并且打印最终结果--一百以内所有奇数的和
else:
    print("一百以内奇数和是：",OddNumber)
