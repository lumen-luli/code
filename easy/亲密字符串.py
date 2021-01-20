#-*- coding:utf-8 _*-  
""" 
@author:lupang 
@file: 亲密字符串.py 
@time: 2021/01/15 
"""

'''
1 字符串不相等直接返回true
2 字符串相等有重复的，返回true
3 字符串不等，交换后是否相等
'''
def buddyStrings( A: str, B: str) :
    if len(A)!=len(B):
        return False
    if A == B and len(set(A)) !=len(A):
        return True
    tmp=[]
    for i in range(len(A)):
        if A[i]!=B[i]:
            tmp.append(i)
    print(tmp)
    if len(tmp)==2 and A[tmp[0]] ==B[tmp[1]] and A[tmp[1]]==B[tmp[0]]:
        return True
    else:
        return False





print(buddyStrings(A = "abab", B = "abab"))
