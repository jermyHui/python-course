#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 初始化变量sum_num，用于存储和
sum_num = 0
# 初始化count变量，用于统计个数
count = 0
# 循环找出所有数相加
for i in range(7,100,7):
    sum_num += i
    count += 1
print("100以内所有7的倍数和是：",sum_num,"共有",count,"个")