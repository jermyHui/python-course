#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 身份选择
# 初始化游戏名称，游戏角色变量
GameName = '唐僧大战白骨精' # 游戏名称
player = '唐僧'
boss = '白骨精'
# 欢迎玩家进入游戏，身份介绍
print("=" * 16,f"欢迎来到游戏《{GameName}》","=" * 16,"\n【身份选择】\n",f"1.{player}（请输入1）\n",f"2.{boss}（请输入2）")
# 提醒玩家选择身份
ChooseRole = input("请输入数字选项:")
# 根据用户选择显示不同提示
if ChooseRole == str(1):
    print(f"你已经选择{player}，恭喜你将以{player}的身份进行游戏！")
elif ChooseRole == str(2):
    print(f"什么你竟然选择了{boss}？系统将自动分配你以{player}的身份进行游戏！")
else:
    print(f"你输入的选项有误，系统将自动分配你以{player}的身份进行游戏！")
# 打印分割线
print("-"*59)
# 进入游戏

# 定义玩家初始攻击力和生命值
AttackPlayer = 2 # 玩家攻击力
LifePlayer = 2 # 玩家生命值
# 定义Boss的攻击力和生命值
AttackBoss = 10 # Boss攻击力
LifeBoss = 10 # Boss生命值

# 显示玩家信息
print(f"你的身份是→{player}←，你的攻击力是：{AttackPlayer} 你的生命值是：{LifePlayer}")
# 使用循环使每次提示选择操作
while True:
    # 显示游戏选项，游戏正式开始
    print("【请选择你要进行的操作】\n","1.练级\n","2.打Boss\n","3.逃跑")
    Game_Choose = input("请选择要做的操作【1-3】：")
    # 打印分割线
    print("-"*59)
    # 根据用户选择执行不同操作
    # 用户选择练级，提示练级成功，等级提高，提醒用户再次选择操作
    if Game_Choose == str(1):
        AttackPlayer += 2
        LifePlayer += 2
        print(f"练级成功，你现在的攻击力是:{AttackPlayer}，生命值是:{LifePlayer}")
    # 用户选择打BOSS，判断用户能否打败Boss进行不同提示
    elif Game_Choose == str(2):
        LifeBoss -= AttackPlayer
        print("BOSS当前生命值为：",LifeBoss)
        # 检查Boss是否死亡
        if LifeBoss <= 0:
            # Boss死亡，玩家胜利，游戏结束
            print(f"恭喜你已经成功打败{boss}！\nGame Over!请再次开始游戏吧~")
            break
        # Boss反击，玩家失败，游戏结束
        else:
            print(f"很遗憾，你承受了{LifePlayer}点伤害，已经被{boss}击败T~T\nGame Over!请再次发起挑战吧~")
            break
    # 玩家选择逃跑，游戏结束
    elif Game_Choose == str(3):
        print("您已选择逃跑，游戏退出，请重新开始")
        break
    # 用户输入非法选项，提示输入有误重新输入
    else:
        print("您输入的选项有误，请重新输入")
