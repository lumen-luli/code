#-*- coding:utf-8 _*-  
""" 
@author:lupang 
@file: 字符串长度最大乘积.py
@time: 2020/08/07 
"""
'''
已知一个字符串数组words，要求寻找其中两个没有重复字符的字符串，使得这两个字符串的长度乘积最大，输出这个最大的乘积。如： 
words=["abcd","wxyh","defgh"], 其中不包含重复字符的两个字符串是"abcd"和"wxyh"，则输出16
words=["a","aa","aaa","aaaa"], 找不到满足要求的两个字符串，则输出0
输入：
["a","ab","abc","cd","bcd","abcd"] 
输出
4
备注：
Input中，不包含相同字符的有三对：
"ab"和"cd"
"a"和"cd"
"a"和"bcd"
所以字符串长度乘积的最大值是4 
'''



# str=input()
# str2 = str.replace('"','').replace('[','').replace(']','')
# words = str2.split(',')


words = list(map(lambda x: x[1:-1], input().strip()[1: -1].split(',')))
res = 0

for i in range(len(words)):
    for j in range(1,len(words)):
        len1=len(words[i])+len(words[j])
        len2=len(set(words[i]+words[j]))
        if len1==len2:
            res=max(res,len(words[i])*len(words[j]))
print(res)












