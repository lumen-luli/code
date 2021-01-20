#-*- coding:utf-8 _*-  
""" 
@author:lupang 
@file: 可被5整除的2进制前缀.py 
@time: 2021/01/15 
"""

'''
给定由若干 0 和 1 组成的数组 A。我们定义 N_i：从 A[0] 到 A[i] 的第 i 个子数组被解释为一个二进制数（从最高有效位到最低有效位）。

返回布尔值列表 answer，只有当 N_i 可以被 5 整除时，答案 answer[i] 为 true，否则为 false。

输入：[0,1,1]
输出：[true,false,false]
解释：
输入数字为 0, 01, 011；也就是十进制中的 0, 1, 3 。只有第一个数可以被 5 整除，因此 answer[0] 为真。
'''
def prefixesDivBy5(A):
    ans = []
    i=1
    while i <= len(A):
        s = "".join(list(map(str,A[0:i])))
        ans.append(not int(s,2)%5)
        i=i+1
    return ans

def prefixesDivBy52(A):
    ans = []
    a=""
    for i in A:
        a+=str(i)
        ans.append(not int(a,2)%5)
    return ans



print(prefixesDivBy52([0,1,1]))