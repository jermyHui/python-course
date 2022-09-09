#!/usr/bin/env python3.8
# -*- coding: UTF-8 -*-
import json2
# # 定义一个列表
# l = [1,'hhh',True,False]
# # 将列表通过json序列化
# json_l = json.dumps(l)
# # 打印序列化后的内容和类型
# print(type(json_l),json_l)

# # 将序列化后的内容存入文件
# with open('json_text.txt',mode='wt',encoding='utf-8') as f:
#     # 定义一个列表
#     l = [1,'hhh',True,False]
#     # 通过json.dump()将列表l序列化后存入文件
#     json.dump(l,f)

# 将文件中的json内容反序列化打开
with open('json_text.txt',mode='rt',encoding='utf-8') as f:
    l = json.load(f)
    print(l)
'''
@version:3.8
@author:chenchen
@file:33_序列化和反序列化.py
@time:2022/9/9 17:03
'''
