#-*-coding:gb2312-*-

# 通过条件运算符找出变量a、b、c中的最大值
# 定义变量a、b、c
a = 10
b = 30
c = 20
# 找出a、b中较大的值复制给变量d
d = a if a > b else b
# 比较d和c的大小，将结果复制给变量max
max = c if c > d else d
# 输出max
print(max)