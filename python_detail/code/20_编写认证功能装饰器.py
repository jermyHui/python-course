#!/usr/bin/env python3.8
# -*- coding: UTF-8 -*-
# 编写一个登录认证的装饰器
def verify(func):
    def wrapper(*args,**kwargs):
        inp_username = input('请输入用户名：').strip()
        inp_password = input('请输入密码：').strip()
        if inp_username == 'chenchen' and inp_password == '123':
            res = func(*args,**kwargs)
            return res
        else:
            print('用户名或密码错误')
    return wrapper

# 编写一个登录函数
@verify
def login():
    print('登录成功')

login()

'''
@version:3.8
@author:chenchen
@file:20_编写认证功能装饰器.py
@time:2022/7/5 17:41
'''
