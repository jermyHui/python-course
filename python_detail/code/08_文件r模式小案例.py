#!/usr/bin/env python3.8
# -*- coding: UTF-8 -*-
# 提示用户输入用户名和密码
inp_username = input("请输入用户名：").strip()
inp_password = input("请输入密码：").strip()
# 打开用户信息文件，核对用户名和密码
with open('user_info.txt',mode='rt',encoding='utf-8') as f:
    # print(res)
    # 通过for循环取出文件中的每个用户信息
    for line in f:
       username,password = line.strip().split(':')
       # 判断用户输入的用户名和密码是否正确
       if inp_username == username and inp_password == password:
           print("登录成功")
           break
    else:
        print("用户名或密码错误")
'''
@version:3.8
@author:chenchen
@file:08_文件r模式小案例.py
@time:2022/6/20 15:04
'''
