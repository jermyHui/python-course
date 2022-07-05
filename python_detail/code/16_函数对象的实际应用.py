#!/usr/bin/env python3.8
# -*- coding: UTF-8 -*-
# 定义功能
def login():
    print('登录功能')
def transfer():
    print('转账功能')
def check_balances():
    print('查询余额')
def withdraw():
    print('提现功能')
# 定义一个字典存储功能以及对应编号
func_dict = {
    '0':('退出',None),
    '1':('登录',login),
    '2':('转账',transfer),
    '3':('查询余额',check_balances),
    '4':('提现',withdraw)
}
# 打印提示信息
while True:
    for k in func_dict:
        print(k,func_dict[k][0])
    choice = input('请输入选项：').strip()
    # 判断用户输入的是否是数字
    if not choice.isdigit():
        print('输入的指令必须是数字')
        continue
    # 用户输入0则退出
    if choice == '0':
        break
    if choice in func_dict:
        func_dict[choice][1]()
    else:
        print('输入的编号不存在')
        continue
'''
@version:3.8
@author:chenchen
@file:16_函数对象的实际应用.py
@time:2022/7/5 12:47
'''
