#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 定义函数
def fun(n):
    '''
        该函数用来判断一个任意字符串是否是回文字符串

        参数：
            n需要判断的字符串
    '''
    # 退出条件
    if len(n) < 2:
        return True
    # 递归条件
    else:
        if n[0] == n[-1]:
            return fun(n[1:-1])
        else:
            return False
# 调用函数
print(fun('aa'))