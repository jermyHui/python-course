#!/usr/bin/env python3.8
# -*- coding: UTF-8 -*-
import hashlib
import ujson

m1 = hashlib.md5('hahhahahahahh'.encode('utf-8'))
m1.update('1456'.encode('utf-8'))
res = m1.hexdigest()
print(res)

'''
@version:3.8
@author:chenchen
@file:35_hash.py
@time:2022/9/9 19:16
'''
