#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 欢迎用户进入系统
print("-"*20,"欢迎使用员工管理系统","-"*20)

# 创建员工信息列表存储员工信息
emps = ["\tzhuzhu\t18\t男\t重庆","\tzhuzhu\t18\t男\t重庆"]

# 通过死循环，在用户每次做出选择后打印可选项
while True:
    # 展示可选择的操作选项
    print("请选择要执行的操作：")
    print("\t1.查询员工")
    print("\t2.新增员工")
    print("\t3.删除员工")
    print("\t4.退出系统")

    # 提示用户输入选项
    user_choose = input("请输入选项【1-4】：")

    # 打印分割线
    print("-"*60)

    # 用户选择查询员工信息时，打印员工列表
    if user_choose == "1":

        # 员工列表为空时，提示无信息
        if len(emps) == 0:
            print("暂无员工信息，快去新增员工吧~")

        # 员工列表不为空时，查询打印员工信息
        else:

            # 提示以下为员工信息
            print("下列为员工信息")

            # 打印分割线
            print("-" * 60)

            # 创建变量n，用作员工信息的序号
            n = 0

            # 打印员工信息表头
            print("序号\t姓名\t年龄\t性别\t地址")

            # 遍历员工列表，打印员工信息
            for emp in emps:
                n += 1
                print(f"{n}{emp}")

    # 用户选择新增员工，引导用户输入新增信息
    elif user_choose == "2":

        # 提醒用户输入新增员工信息
        print("请根据提示输入新增员工信息：")

        # 变量存储员工姓名
        emp_name = input("请输入姓名：")

        # 变量存储员工年龄
        emp_age = input("请输入年龄：")

        # 变量存储员工性别
        emp_sex = input("请输入性别：")

        # 变量存储员工地址
        emp_address = input("请输入员工地址：")

        # 将员工信息整合为一个字符串
        emp = f"\t{emp_name}\t{emp_age}\t{emp_sex}\t{emp_address}"

        # 提示用户信息将被新增
        print("以下员工信息将被新增")

        # 打印分割线
        print("-" * 60)

        # 打印员工信息表头
        print("\t姓名\t年龄\t性别\t地址")

        # 打印输入的员工信息
        print(emp)

        # 提示用户确认是否新增员工
        user_add_confirm = input("请确认是否新增员工【Y/N】:")

        # 用户选择确认新增
        if user_add_confirm == "Y" or user_add_confirm == "y" or user_add_confirm == "yes":

            # 将员工信息添加到员工列表中
            emps.append(emp)

            # 提示新增成功
            print("新增成功！")

        # 用户取消新增
        else:
            print("取消新增员工！")
    # 用户选择删除员工，引导用户输入删除编号
    elif user_choose == "3":

        # 提醒用户输入要删除员工的编号,将用户输入的内容存储到变量
        user_del_choose = input("请输入要删除员工的编号：")

        # 将用户输入的编号转换为列表下标
        user_del_index = int(user_del_choose) - 1

        # 判断序号是否合法
        if 0 < int(user_del_choose) <= len(emps):
            print("下列员工信息将被删除")

            # 打印分割线
            print("-" * 60)

            # 打印员工信息表头
            print("序号\t姓名\t年龄\t性别\t地址")

            # 查询员工信息打印
            print(f"{user_del_choose}{emps[user_del_index]}")

            # 提醒用户确认是否删除
            user_del_confirm = input("请确认是否删除【Y/N】:")

            # 用户确认删除
            if user_del_confirm == "Y" or user_del_confirm == "y" or user_del_confirm == "yes":

                # 从列表中删除员工信息
                emps.pop(user_del_index)

                # 提示删除成功
                print("已成功删除员工信息")

            # 用户取消删除
            else:
                # 提示取消删除员工信息
                print("取消删除！")
        else:
            print("输入有误，请重新输入")

    # 用户选择退出系统
    elif user_choose == "4":
        print("您将要退出系统")
        input("请按【enter】键退出：")
        print("退出系统，再见！")

        # 打印分割线
        print("-" * 60)

        # 退出程序
        break
    # 用户输入其他内容
    else:
        print("输入内容有误，请重新输入")
    # 打印分割线
    print("-" * 60)