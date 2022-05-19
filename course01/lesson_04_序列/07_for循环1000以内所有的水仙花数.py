#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 定义一个i大于100小于1000的循环
for i in range(100,1000):
    #print(i)
    # 通过索引取出i的每一位数复制给变量
    a = int(str(i)[0])
    b = int(str(i)[1])
    c = int(str(i)[2])
    # 判断i是否是水仙花数,如果是打印水仙花数
    if a**3 + b**3 +c**3 == i:
        print(i)
