#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 初始化变量存储结果
sum_odd_num = 0
# for循环找出100以内所有奇数相加
for i in range(1,100,2):
    sum_odd_num += i

# 打印结果
print("100以内所有奇数和是：",sum_odd_num)