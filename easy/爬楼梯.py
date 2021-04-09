#-*- coding:utf-8 _*-  
""" 
@author:lupang 
@file: 爬楼梯.py 
@time: 2021/01/21 
"""
'''
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
'''

def climbStairs(n: int):
    #1,1 2,2 3,3
    f={}
    f[0]=1
    f[1]=1
    i=2
    while i<=n:
        f[i] = f[i-1]+f[i-2]
        i=i+1
    return f[n]




print(climbStairs(4))