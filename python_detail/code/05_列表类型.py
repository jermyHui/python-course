#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 1、作用：用来按照位置存多个值
# 2、定义
# l = [1,'a',[1,2,3]]
# 3、类型转换:但凡能被for循环遍历的类型都可以当做参数传给list()转成列表-----字符串、字典
# 4、内置方法
# 1、按照索引取值（正向存取、反向存取）：即可存也可取
'''
l = ['chenchen','18','女']
# 正向取
print(l[0])
# 反向取
print(l[-1])
# 可以取可以改
l[0] = 'zhuzhu'
print(l)
'''
# 在列表添加元素
# append()、insert()、extend()
# 删除列表中的元素
# del无返回值（公共的都可以用，不止针对列表使用）
# pop有返回值,返回删除的值（仅列表使用）
'''
l = ['chenchen','18','女']
res = l.pop(1)
print(l)
print(res)
'''
# remove,根据元素删除，返回值为空