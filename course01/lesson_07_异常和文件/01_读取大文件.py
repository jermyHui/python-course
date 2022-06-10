#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 定义文件名
file_name = 'demo.txt'
# 打开文件
with open(file_name) as file_obj:
    try:
        # 通过循环来读取文件
        while True:
            # 定义一个变量，指定每次读取的大小
            chunk = 100
            # 读取文件内容
            content = file_obj.read(chunk)
            # 如果读取到的内容为空则退出循环
            if not content:
                break
            print(content,end='')
    except FileNotFoundError:
        print(f'{file_name}这个文件不存在')