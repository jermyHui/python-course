#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 获取男生身高、财产和帅气值
height = int(input("请输入身高(厘米)："))
property = int(input("请输入财富值(万)："))
looks = int(input("请输入帅气度(平方厘米)："))
# 根据条件不同判断是否嫁
if height > 180 and property > 1000 and looks > 500:
    print("我一定要嫁给他")
elif height > 180 or property > 1000 or looks > 500:
    print("嫁吧，比上不足，比下有余。")
elif height <= 180 and property <= 1000 and looks <= 500:
    print("不嫁！")