#-*- coding:utf-8 _*-  
""" 
@author:lupang 
@file: 八大排序算法.py 
@time: 2020/08/27 
"""

# 冒泡
l1=[4,5,6,2,3,5,1,0,4,8]
def bubble_sort(l1):
    n=len(l1)
    # 外层循环控制从头走到尾的次数
    for i in range(n):
        # 内层循环控制走一次的过程
        for j in range(0,n-i-1):
            if l1[j]>l1[j+1]:
                l1[j],l1[j+1]=l1[j+1],l1[j]
    return l1

#print(bubble_sort(l1))

# 选择排序：首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，然后，
# 再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。

def select_sort(l1):
    select_desc=[]
    for i in range(len(l1)):
        min_id=min(l1)
        select_desc.append(min_id)
        #pop是针对下标，pop返回删掉的元素。remove是元素，不返回删掉的元素
        l1.remove(min_id)

    return select_desc
#print(select_sort(l1))

def select_sort_2(l1):
    for i in range(len(l1)):
        min_id = i
        for j in range(i+1,len(l1)):
            if l1[min_id]>l1[j]:
                min_id=j
        l1[i],l1[min_id]=l1[min_id],l1[i]
    return l1

#print(select_sort_2([4,5,6,2,3,5,1,0,4,8]))


# 快排
def quick_sort(arr):
    if len(arr)<2:
        return arr
    mid =arr[len(arr) // 2]
    left,right=[],[]
    arr.remove(mid)
    for i in arr:
        if i>=mid:
            right.append(i)
        else:
            left.append(i)
    return quick_sort(left)+[mid]+quick_sort(right)



#print(quick_sort([4,7,6,2,6,1,0,4,8]))