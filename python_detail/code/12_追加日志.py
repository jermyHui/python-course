#!/usr/bin/env python3.8
# -*- coding: UTF-8 -*-
# 引入datetime模块
import datetime
# 定义变量获取当前时间
now_time = datetime.datetime.now()

# 打开日志文件
with open('test.log',mode='at',encoding='utf-8') as T:
    # 追加一条带有当前日期的日志在日志文件
    T.write(f'{now_time} 新增一条日志\n')
'''
@version:3.8
@author:chenchen
@file:12_追加日志.py
@time:2022/6/21 20:37
'''
