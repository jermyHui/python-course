#!/usr/bin/env python3.8
# -*- coding: UTF-8 -*-
# 用户输入账号密码，按照"egon:18"的格式存入文件
inp_username = input("请输入用户名：").strip()
inp_password = input("请输入密码：").strip()

# 在文件中保存用户信息
with open('user_infor',mode='a',encoding='utf-8') as f:
    f.write('{}:{}\n'.format(inp_username,inp_password))
'''
@version:3.8
@author:chenchen
@file:09_注册功能.py
@time:2022/6/20 17:38
'''
