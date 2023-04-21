#!/usr/bin/env python3.8
# -*- coding: UTF-8 -*-
# 定义一个公共的game类
class Game:
    def __init__(self,hp,power):
        self.hp = hp
        self.power = power
    # 定义战斗规则属性
    def fight(self,enemy_hp,enemy_power):
        finally_hp = self.hp - enemy_power
        finally_enemy_hp = enemy_hp - self.power
        if finally_hp > finally_enemy_hp:
            print("我赢了")
        elif finally_enemy_hp > finally_hp:
            print("敌人赢了")
        elif finally_enemy_hp == finally_hp:
            print("平局")
class Houyi(Game):
    def __init__(self,defense):
        super().__init__(hp,power)
        self.defense = defense
    def houyi_fight(self,enemy_hp,enemy_power):
        finally_hp = self.hp + self.defense - enemy_power
        finally_enemy_hp = enemy_hp - self.power
        if finally_hp > finally_enemy_hp:
            print("我赢了")
        elif finally_enemy_hp > finally_hp:
            print("敌人赢了")
        elif finally_enemy_hp == finally_hp:
            print("平局")

# 实例化类
hp = 1000
power = 400
defense = 100

houyi = Houyi(defense)
houyi.houyi_fight(1000,300)
'''
@version:3.8
@author:chenchen
@file:game.py
@time:2023/3/16 14:11
'''
