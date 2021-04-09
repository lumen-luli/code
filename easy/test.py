#-*- coding:utf-8 _*-  
""" 
@author:lupang 
@file: test.py 
@time: 2021/03/29 
"""

#冒泡
def bubble(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
#print(bubble([1,3,4,9,7]))


# 快排
def quick(arr):
    if len(arr)<2:
        return arr
    mid = arr[len(arr)//2]
    left,right=[],[]
    arr.remove(mid)
    for i in arr:
        if i>mid:
            left.append(i)
        else:
            right.append(i)
    return quick(left)+[mid]+quick(right)

#print(quick([1,3,4,9,7]))


#选择
def select(arr):
    res=[]
    for i in range(len(arr)):
        m=max(arr)
        arr.remove(m)
        res.append(m)
    return res
#print(select([1, 3, 4, 9, 7]))

#斐波那契
def fib(n):
    #0,1,1,2,3,5,8
    f=[]
    f[1:1]=0,1
    i=2
    while n>1 and i<=n:
        f.append(f[i-1]+f[i-2])
        i=i+1
    return f[n]

#print(fib(4))


#
def sale(arr):
    if len(arr)<2:
        return 0
    s=[]
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            s.append(arr[j]-arr[i])
    return max(s) if max(s)>0 else 0

#print(sale([7]))

def countPrimes(n):
    count=0
    num=0
    for i in range(n):
        for j in range(1,i+1):
            num=num+i
            count=count+1
    return count

print(countPrimes(10))