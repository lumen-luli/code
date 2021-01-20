#-*- coding:utf-8 _*-  
""" 
@author:lupang 
@file: 贪心-分糖果.py 
@time: 2020/10/28 
"""

# 题目：已知一些孩子和一些糖果，每个孩子有需求因子g，每个糖果有大小s，当某个糖果的大小s>=某个孩子的需求因子g时，
# 代表该糖果可以满足该孩子，求使用这些糖果，最多能满足多少孩子（注意，某个孩子最多只能用1个糖果满足）
child = [5,10,2,9,15,9]
candy = [6,1,20,3,8]
child.sort()
candy.sort()
c = 0
ca=0

while c<len(child) and ca<len(candy):
    if child[c]<candy[ca]:
        c += 1
    ca += 1

print(c)








