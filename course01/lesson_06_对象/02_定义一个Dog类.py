#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 定义Dog类
class Dog:
    # 初始化方法
    def __init__(self,name,age,gender,height):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
       # print(f'{name}是一个{age}岁{height}斤的{gender}狗')
    # 声明一个狗叫方法
    def jiao(self):
        print(self.name,"在叫")
    # 声明一个狗咬人方法
    def yao(self):
        print(self.name,"在咬人")
    # 声明一个狗跑的方法
    def pao(self):
        print(self.name,"在跑")
# 定义一个小狗变量
dog1 = Dog('wangwang',6,'nv',25)
dog1.pao()