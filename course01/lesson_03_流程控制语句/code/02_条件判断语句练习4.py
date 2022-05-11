#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 获取期末成绩
score = int(input("请输入期末成绩："))
# 判断分数不同给与不同奖励
if score == 100:
    print("奖励一辆BMW")
elif 80 <= score <= 99:
    print("奖励一台iphone")
elif 60 <= score <= 79:
    print("奖励一本参考书")
else:
    print("成绩不合格，没有奖励")
