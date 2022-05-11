# 让用户输入用户名
name = input("请输入用户名：")
# 如果用户名是admin则显示欢迎管理员光临，否则什么也不显示
if name == "admin" :
    print("欢迎管理员光临！")
else :
    print(f"欢迎用户 {name} 光临！")
# 练习1
# 获取用户输入的值
num = int(input("请输入一个整数："))
# 取到的值除以2取模
num = num % 2
# 判断数值是奇数还是偶数
if num == 0:
    print("用户输入的数为偶数")
else:
    print("用户输入的数为奇数")

# 练习2
# 获取用户输入的年份
year = int(input("请输入任意年份："))
# 判断用户输入的年份是否为闰年
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("该年份是闰年")
else:
    print("该年份不是闰年")

# 练习3
# 获取狗狗年龄
Dog_Age = float(input("请输入狗狗年龄："))
# 根据输入年龄的不同返回不同的提示
if Dog_Age <= 0:
    print("您输入的狗狗年龄有误")
elif Dog_Age == 1:
    print("狗狗的年龄相当于10.5岁的人类")
elif Dog_Age == 2:
    print("狗狗的年龄相当于21岁的人类")
else:
    print(f"狗狗的年龄相当于{10.5*2+(Dog_Age-2)*4}岁的人类")

