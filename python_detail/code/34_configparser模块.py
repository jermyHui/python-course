#!/usr/bin/env python3.8
# -*- coding: UTF-8 -*-
import configparser
config = configparser.ConfigParser()
config.read('config.ini')
print(config.sections())
print(config.options('section1'))
print(config.items(section='section1'))
print(config.get('section1','name'))
print(type(config.getint('section1','age')))
'''
@version:3.8
@author:chenchen
@file:34_configparser模块.py
@time:2022/9/9 19:00
'''
