#!/usr/bin/python
# -*- coding: UTF-8 -*-
for i in range(1,10):
    # print("i=",i)
    for j in range(1,i+1):
        # print("j=",j)
        print(f"{j}*{i}={j*i} ",end="")
    print()