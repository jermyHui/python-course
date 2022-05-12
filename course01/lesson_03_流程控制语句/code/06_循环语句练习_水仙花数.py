#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 初始化变量
i = 100
while i < 1000:
    # 将变量转化为字符串用于使用下标
    num = str(i)
    # 通过公式判断i是否为水仙花，若是输出i
    a = int(num[0]) ** 3
    b = int(num[1]) ** 3
    c = int(num[2]) ** 3
    if a + b + c == i:
        print(i,"是水仙花数")
    i += 1

