#!/usr/bin/env python3.8
# -*- coding: UTF-8 -*-
import requests
r = requests.get("http://www.baidu.com")
print(r.status_code)
r.encoding = "UTF-8"
print(r.text)
'''
@version:3.8
@author:chenchen
@file:test.py
@time:2023/3/14 18:39
'''
