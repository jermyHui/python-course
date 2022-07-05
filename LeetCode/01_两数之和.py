#!/usr/bin/env python3.8
# -*- coding: UTF-8 -*-
'''
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
'''
nums = [2,7,11,15]
target = 9
n = len(nums)
for i in range(n):
    for j in range(i+1,n):
        if nums[i] + nums[j] == target:
            print([i,j])

class Solution:
    def two_sum(self,nums,target):
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                   return[i, j]

'''
@version:3.8
@author:chenchen
@file:01_两数之和.py
@time:2022/6/22 23:51
'''
