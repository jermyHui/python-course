#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 定义变量name
name = " aleX"

# 练习1：移除 name 变量对应的值两边的空格,并输出处理结果
# 通过strip移除变量旁的空格
# name = name.strip()
# 打印修改后的结果
# print(name)

# 练习2：判断 name 变量对应的值是否以 "al" 开头,并输出结果
# 判断name是否以al开头
# result = name.startswith('al')
# 输出结果
# print(result)

# 练习3：判断 name 变量对应的值是否以 "X" 结尾,并输出结果
# result = name.endswith('X')
# print(result)

# 练习4：将 name 变量对应的值中的 “l” 替换为 “p”,并输出结果
# name = name.replace('l','p')
# print(name)

# 练习5：将 name 变量对应的值根据 “l” 分割,并输出结果。
# name = name.split('l')
# print(name)

# 练习6：将 name 变量对应的值变大写,并输出结果
# name = name.upper()
# print(name)

# 练习7：将 name 变量对应的值变小写,并输出结果
# name = name.lower()
# print(name)

# 练习8：请输出 name 变量对应的值的第 2 个字符?
# print(name[1])

# 练习9：请输出 name 变量对应的值的前 3 个字符?
# print(name[2])

# 练习10：请输出 name 变量对应的值的后 2 个字符?

# 练习11：请输出 name 变量对应的值中 “e” 所在索引位置?
result = name.find('e')
print(result)
# 练习12：获取子序列,去掉最后一个字符。如: oldboy 则获取 oldbo。
for i in range(0,len(name)-1):
    print(name[i],end='')

name=' aleX'
a=name[:-1]
print(a)

'''
复习：
for循环、嵌套循环
for + range

整型、浮点型、字符串
四个方面介绍：
作用、定义、转换类型、内置方法
三个角度区分：
可存多少个值、有序无序、是否可变
'''