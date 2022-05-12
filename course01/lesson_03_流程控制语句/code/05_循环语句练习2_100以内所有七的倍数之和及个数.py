#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 找出一百以内所有7的倍数计算和，并输出个数

# 定义变量i用于增加7的倍数
i = 0
# 定义7的倍数变量用于判断循环次数
num = 1
# 初始化7的倍数的第一个数
sum_num = 0
# 进行循环，并存储每次循环结果的和
while num < 100:
    i += 1
    num = i * 7
    print(num)
    sum_num += num
    # print(sum_num)
# 循环结束，输出结果
else:
    print("一百以内7的倍数之和为:",sum_num - num)
    print("一百以内7的倍数的个数为：",i-1)
    print(num)


