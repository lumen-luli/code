#-*- coding:utf-8 _*-  
""" 
@author:lupang 
@file: 面试.py 
@time: 2020/11/18 
"""

#给出一个无序的正整数数组 输出这个数组中没有出现的最小正整数，要求复杂度o(n)
def min_num(arr):
    if len(arr)<1:
        return  -1
    i=0
    while i<max(arr):
        if i not in arr:
            return i
        i=i+1

print(min_num([6,5,3,0,1]))

def min_num_2(arr):

    i,j=0,1
    for i in arr:
        if i<0:
            continue
        if i>0:
            pass
    return i

print(min_num_2([6,5,3,0,1]))



list1 = [1, 2, 5, 6, 7, 4, 8, 2, 7, 9, 4, 6, 3]
list2 = []
[list2.append(i) for i in list1 if  i not in list2]  # append别忘记添加参数
print(list2)

def findTop3(arr):
    if arr == None or len(arr) < 3:
        print("参数不合法！")
        return
    r1 = r2 = r3 = 0
    i = 0
    while i < len(arr):
        if arr[i] > r1:
            r3 = r2
            r2 = r1
            r1 = arr[i]
        elif arr[i] > r2 and arr[i] != r1:
            r3 = r2
            r2 = arr[i]
        elif arr[i] > r3 and arr[i] != r2:
            r3 = arr[i]
        i += 1
    return str(r1)+","+str(r2)+","+str(r3)
print(findTop3([345,2,3,678,10]))




#求200-300之间的所有质数














