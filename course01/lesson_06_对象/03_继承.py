#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 定义一个animal父类
class Animal:
    # 定义一个跑方法
    def run(self):
        print(f"{self}会跑")


# 定义一个dog子类继承Animal类
class Dog(Animal):
    def bark(self):
        print('汪汪汪~~~')

    def run(self):
        print(f"{self}子类会跑")

if __name__ == '__main__':
    d = Dog()
    d.run()
