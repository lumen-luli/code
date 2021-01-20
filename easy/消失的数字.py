#-*- coding:utf-8 _*-  
""" 
@author:lupang 
@file: 消失的数字.py 
@time: 2020/08/19 
"""

'''
数组nums包含从0到n的所有整数，但其中缺了一个。请编写代码找出那个缺失的整数。你有办法在O(n)时间内完成吗？
输入：[3,0,1]
输出：2
'''



list = [9,6,4,2,3,5,7,0,1]
list.sort()
j=list[0]
for i in range(len(list)):

    if list[i] != j:
       print(j)
    j = j + 1


# 思路2 等差数列求和，然后减去集合总和
num = [9,6,4,2,3,5,7,0,1]
n = len(num)
print((n+1)*n//2 - sum(num))
