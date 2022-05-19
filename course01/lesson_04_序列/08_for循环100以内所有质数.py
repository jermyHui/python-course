#!/usr/bin/python
# -*- coding: UTF-8 -*-

for i in range(2,101):
    flag = True
    for j in range(2,i):
        if i % j == 0:
            flag = False
    if flag:
        print(i,"是质数")