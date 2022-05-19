#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 显示员工欢迎信息
print("-"*20,"欢迎使用员工管理系统","-"*20)
# 创建列表变量，保存员工信息
emps = ['chenchen\t18\t男\t北京']
# 创建死循环，每次用户选择后打印选择提示
while  True:
    # 提示用户输入选项，选择操作
    print("请选择要做的操作：")
    print("\t1.查询员工")
    print("\t2.添加员工")
    print("\t3.删除员工")
    print("\t4.退出系统")
    user_choose = input("请选择【1-4】：")
    # 打印分隔符
    print("-" * 60)
    # 用户选择1，显示查询结果
    if int(user_choose) == 1:
        n = 0
        print("\t编号\t姓名\t年龄\t性别\t地址")
        for emp in emps:
            n += 1
            print(f"\t{n}\t{emp}")
    # 用户选择2，添加员工信息
    elif int(user_choose) == 2:
        # 提示用户输入员工信息
        emp_name = input("请输入员工姓名：")
        emp_age= input("请输入员工年龄：")
        emp_sex = input("请输入员工性别：")
        emp_address = input("请输入员工地址：")
        print("以下员工将被添加到系统中")
        # 打印分隔符
        print("-" * 60)
        # 将信息存储到变量中
        emp = f"{emp_name}\t{emp_age}\t{emp_sex}\t{emp_address}"
        # 打印用户输入的信息
        print("编号\t姓名\t年龄\t性别\t地址")
        print(emp)
        # 打印分隔符
        print("-" * 60)
        # 提醒用户确认是否新增员工
        user_add_confirm = input("是否确认该操作[Y/N]:")
        # 确认新增，将信息添加到列表中
        if user_add_confirm == "Y" or user_add_confirm == "y" or user_add_confirm == "yes":
            emps.append(emp)
            print("添加成功")
        # 用户取消新增
        else:
            print("取消新增员工")
    # 用户选择3，删除员工信息
    elif int(user_choose) == 3:
        # 提示用户输入要删除的员工编号
        del_num = input("请输入要删除的员工的序号：")
        # 用户输入的序号-1为列表对应的索引
        del_index = int(del_num) - 1
        # 如果用户输入的序号合法
        if 0 < int(del_num) <= len(emps):
            # 提示用户对应序号的员工信息将被删除，并且打印员工信息
            print("以下员工将被删除")
            # 打印分隔符
            print("-" * 60)
            print("编号\t姓名\t年龄\t性别\t地址")
            print(f'{del_num}\t{emps[del_index]}')
            # 打印分隔符
            print("-" * 60)
            # 提示员工确认是否删除
            user_del_confirm = input("该操作不可恢复，是否确认[Y/N]:")
            if user_del_confirm == "Y" or user_del_confirm == "y" or user_del_confirm == "yes":
                emps.pop(del_index)
                print("员工已被删除")
            else:
                print("操作已取消")
    elif int(user_choose) == 4:
        print("欢迎使用，再见！")
        input("请按回车键退出")
        break
    else:
        print("输入有误，请重新选择！")
    # 打印分隔符
    print("-"*60)