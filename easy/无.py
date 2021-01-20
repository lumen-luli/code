#-*- coding:utf-8 _*-  
""" 
@author:lupang 
@file: 无.py 
@time: 2020/11/06 
"""

#统计一个字符串中出现次数最多的字母和次数
def tong_ji(s):
    d={}

    for i in s:
        if i not in d:
            d[i]=s.count(i)

    m=max(d,key=d.get)
    # m=max(d,key=lambda x:x[1])
    #print(m,d[m])
    ma=max(d)
    #print(ma)

tong_ji("aabbbbbcc")

#给定两个字符串str1和str2,输出两个字符串的最长公共子串，如果最长公共子串为空，输出-1。
def lcs(str1,str2):
    if len(str1)>len(str2):
        str1,str2 = str2,str1
    res,max_len='',0
    for i in range(len(str1)):
        if str1[i-max_len:i+1] in str2:
            res = str1[i-max_len:i+1]
            max_len=max_len+1
    print(res)
    if res=='':
        return -1
    else:
        return res

#print(lcs("1AB2345CD","789"))


#算法题：输入字符串1：I have a student.；输入字符串2: aeiou；
# 处理：在字符串1中，将字符串2中的字母删掉；输出：I hv stdnt
def shanchu(str1,str2):
    new_str=''
    for i in str1:
        if i not in str2:
           new_str=new_str+i
    return new_str

#print(shanchu("I have a student ","aeiou"))

import random
#生成发红包的金额
def redpacket(num,count):
    #num 人数3 ，count 总金额10
    # 先产生最大的数字
    if num<=0 or count<=0:
        return False
    if count==1:
        return num
    pac1=random.uniform(0.01,count-0.01)


# 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
# 例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，
# 超过数组长度的一半，因此输出2。如果不存在则输出0。

def more_than_half_num(arr):
    arr_len=len(arr)/2
    print(arr_len)
    for i in arr:
        if arr.count(i)>arr_len:
            return i

print(more_than_half_num([1,2,3,2,2,2,5,4,2]))



#不用循环，求数组的合
#join括号里只支持字符串由字符串组成的列表（字典，字符串，元组）
def arr_sum(arr):
    return eval("+".join(arr))
print(arr_sum(["1","2" ,"3" ]))


#输入一个数字x和字符串，将字符串前x位放到后面去3 abcdefg-defgabc
def str_move(x,str):
    n_str=str[x:]+str[0:x]
    print(n_str)
#str_move(3,'abcdefg-defgabc')


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

# 快排，冒泡，二分查找
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


def s_count():
    str="aabbccdef"
    ret={}
    for i in str:
        if i in set(str):
            ret[i]=str.count(i)
    return ret
print(s_count())










