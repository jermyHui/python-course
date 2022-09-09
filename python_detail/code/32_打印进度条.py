#!/usr/bin/env python3.8
# -*- coding: UTF-8 -*-
# 文件大小
import time
# 定义一个打印进度条的功能
def print_progress(percent):
    if percent > 1:
        percent = 1
    # 将进度转化为#个数
    res = int(50 * percent) * '#'

    print('\r【%-50s】%s%%' % (res, int(percent * 100)), end='')

# 文件总大小
file_size = 356000
# 下载速度
recv_size = 0
# 条件判断是否下载完成
while recv_size < file_size:
    time.sleep(0.1)
    recv_size += 1024
    # 下载进度
    percent = recv_size / file_size
    print_progress(percent)

'''
@version:3.8
@author:chenchen
@file:32_打印进度条.py
@time:2022/8/25 17:23
'''
