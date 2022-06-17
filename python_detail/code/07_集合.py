#!/usr/bin/env python3.8
# -*- coding: UTF-8 -*-
# 分别定义两个列表，且两个列表中存在相同元素
# l1 = [1,2,3,4,5]
# l2 = [3,4,5,6,7]
# 找出两个列表中相同的元素并且存到新的列表中
# 定义一个空列表用于存放共同元素
# l3 = []
# 使用for循环找出相同的元素
# for i in l1:
#     if i in l2:
#         l3.append(i)
# print(l3)

# 定义三个集合
s1 = {1,2,3,4,5}
s2 = {3,4,5,6,7}
s3 = {4,5}
# 并集
print(s1 | s2)

# 交集
print(s1 & s2)

# 差集
print(s1 - s2)
print(s2 - s1)

# 对称差集
print(s1 ^ s2)

# 父子级
print(s1 > s2)  # False
print(s2 > s1)  # False
print(s2 > s3)  # True
