#-*- coding:utf-8 _*-  
""" 
@author:lupang 
@file: 非递减数列.py 
@time: 2021/01/13 
"""
'''
输入: nums = [4,2,3]
输出: true
解释: 你可以通过把第一个4变成1来使得它成为一个非递减数列。
'''
'''
思路：

例如[5,7,1,8]
扫描到7的时候7>1递减了
此时有两种办法
1、把7变小，这时要保证 1>=7>=4
2、把1变大,这时要保证 1>=7,1<=8
'''

def checkPossibility(nums) -> bool:
    if len(nums) < 3:
        return True
    j = 0
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            j = j + 1
            if i + 2 < len(nums) and i - 1 >= 0:
                if nums[i + 1] < nums[i-1] and nums[i+2]<nums[i]:
                    return False
        if j >= 2:
            return False

    return True

print(checkPossibility([5,7,1,8]))





