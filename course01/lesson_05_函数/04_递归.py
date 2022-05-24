#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 定义power函数计算任意数的幂运算
def power(n,i):
    # 退出条件
    if i == 1:
        return n
    else:
        return n * power(n,(i - 1))

# 调用函数，请用户输入任意两个数字
n = int(input("请输入任意数字n："))
i = int(input("请输入任意数字i："))
print(f"{n}的{i}次幂为：",power(n,i))

