#-*- coding:utf-8 _*-  
""" 
@author:lupang 
@file: 去除列表中重复元素.py 
@time: 2020/08/26 
"""

lis = [4, 2, 1, 3, 4, 2, 3, 1, 3, 2, 2, 2]

#解法1
print(set(lis))

#解法2
lis2=[]
for i in lis:
    if i not in lis2:
        lis2.append(i)
