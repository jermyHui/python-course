#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 定义变量i控制外循环
i = 1
# 让外循环共循环9次
while i <= 9:
    # 定义变量j控制内循环
    j = 1
    # 外循环一次内循环i次
    while j <= i:
        print(j,"*",i,"=",j*i,' ',end='')
        j += 1
    print()
    i = i+1