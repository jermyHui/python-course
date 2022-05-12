#!/usr/bin/python
# -*- coding: UTF-8 -*-
i = 0
while i < 5:
    j = 5
    while j > i:
        print("*",end='')
        j -= 1
    print()
    i += 1