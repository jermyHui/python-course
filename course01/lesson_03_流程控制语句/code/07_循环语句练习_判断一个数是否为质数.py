#!/usr/bin/python
# -*- coding: UTF-8 -*-
num = int(input("请输入任意大于1的整数："))
i = 2
flag = True
while i < num:
    if num % i == 0:
        flag = False
    i += 1
if flag == True:
    print(num,"是质数")
else:
    print(num,"不是质数")


