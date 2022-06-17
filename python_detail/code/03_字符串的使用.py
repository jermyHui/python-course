#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 定义一个字符串
msg = 'hello world'
# 通过索引取出字符
print(msg[0])
# 通过切片取出一段字符
print(msg[0:5])  # 可以取出第一位到第四位
# 切片加步长取出一部分字符
print(msg[2:7:2])  #从第三位开始每隔两位取一个，一直取到第七位low
# 将字符串倒序排列
print(msg[::-1])
# strip()用法
msg = '******哈哈哈***哈哈******'
res = msg.strip('*')
print(res)
msg = '        哈哈哈    哈哈哈         '
res = msg.strip()
print(res)


print("-------------------------------------")  #分割线
a = 1
print("%04d" % a)
print("-------------------------------------")  #分割线
# 字符串首字母大写
print('hello world chenchen'.capitalize())
# 单词首字母大写
print('hello world chenchen'.title())