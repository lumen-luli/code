#-*- coding:utf-8 _*-  
""" 
@author:lupang 
@file: 解析加减法运算.py 
@time: 2020/08/17 
"""

'''
题目描述
解析加减法运算
如：
输入字符串："1+2+3" 输出："6"
输入字符串："1+2-3" 输出："0"
输入字符串："-1+2+3" 输出："4"
输入字符串："1" 输出："1"
输入字符串："-1" 输出："-1"

已知条件：输入的运算都是整数运算，且只有加减运算
要求：输出为String类型，不能使用内建的eval()函数
'''



s = input().split('+')
#print(eval(s))


num=0
for i in s:
    if '-' in i and i[0]!="-":
        k = [int(x) for x in i.split('-')]
        num = num + k[0] - sum(k[1:])
    else:
        num += int(i)

print(num)



# 1+2+33-4-3-55
# -1+2+33-4-3-55+1+1
