#-*-coding:gb2312-*-
# 对布尔值进行三种逻辑运算

#定义变量a
a = True

# 对a进行非运算
not_result = not a
# 与运算
and_result = False and a
# 或运算
or_result = False or a

# 输出运算结果
print(not_result,and_result,or_result)


# 对非布尔值进行三种逻辑运算

# 定义变量b
b = 1
# 定义变量c
c = "哈哈哈哈"
# 定义变量d
d = ""

# 非运算
not_result_01 = not b
# 与运算
and_result_01 = b and d
# 或运算
or_result_01 = a or d

# 输出运算结果
print(not_result_01,and_result_01,or_result_01)
print(f"非布尔值与运算{and_result_01}" )
print(d)