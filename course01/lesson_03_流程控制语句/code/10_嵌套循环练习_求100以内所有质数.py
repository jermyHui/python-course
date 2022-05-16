#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 创建一个循环，求1-100内的所有整数
i = 2
while i < 100:
    # 创建一个状态记录i的属性，默认i是质数
    flag = True
    # 判断i是否是质数
    # 获取所有可能成为i的因数的数
    j = 2
    while j < i:
        # 判断i能否被j整除
        if i % j == 0:
            # 若i能被j整除，说明i不是质数，将i的属性改为False
            flag = False
        j += 1
    # 验证结果并输出
    if flag == True:
        print(i,"是质数")
    i += 1