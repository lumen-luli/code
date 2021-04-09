#-*- coding:utf-8 _*-  
""" 
@author:lupang 
@file: 行列互换.py 
@time: 2021/02/25 
"""

#需要行列数相同
arr = [[1, 2, 3], [4, 5, 6], [7,8, 9], [10, 11, 12]]
#列表推导式
print([[r[col] for r in arr] for col in range(len(arr[0]))]
[[1, 4, 7, 10], [2, 5, 8, 11],[3, 6, 9, 12]])

# zip函数
print(map(list,zip(*arr)))