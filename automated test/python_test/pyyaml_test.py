#!/usr/bin/env python3.8
# -*- coding: UTF-8 -*-
import yaml
from yaml import FullLoader

'''print(yaml.load('''
a: 1
''', Loader=FullLoader))'''
# print(yaml.safe_load(open("demo.yml", "r")))
with open("demo1.yml", "w") as f:
    yaml.dump({'a': [1, 2]}, stream=f)
'''
@version:3.8
@author:chenchen
@file:pyyaml_test.py
@time:2023/3/20 18:50
'''
