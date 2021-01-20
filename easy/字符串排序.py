
#-*- coding:utf-8 _*-
""" 
@author:lupang 
@file: 字符串排序.py
@time: 2020/08/06 
"""

"""
~字符串、排序

每个测试用例的第一行是一个正整数M（1<=M<=100)，表示数据集的样本数目
接下来输入M行，每行是数据集的一个样本，每个样本均是字符串，且后六位是数字字符。

输入：
4
abc123455
boyxx213456
cba312456
cdwxa654321

输出：
123455
213456
312456
654321

"""

a=[]
for i in range(int(input())):
    a.append(int(input()[-6:]))
for i in sorted(a):
    print(i)




# for n in sorted([int(input()[-6:]) for i in range(int(input()))]):
#     print(n)
