#-*- coding:utf-8 _*-  
""" 
@author:lupang 
@file: 移动0.py 
@time: 2021/01/22 
"""

# 先找出几个0，删掉，再最后补
def moveZeroes(nums):
    zero_num = 0
    for i in range(len(nums)):
        idx = i - zero_num
        if nums[idx] == 0:
            nums.pop(idx)
            nums.append(0)
            zero_num += 1
    return nums


def moveZeroes2(nums):
    # 循环遍历数组，当遇到非零元素则开始交换慢指针所指的0元素
    # i 为慢指针 指向最新一个0元素的位置
    i = 0
    for j in range(len(nums)):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    return nums



print(moveZeroes([0,1,0,3,12]))