#-*- coding:utf-8 _*-  
""" 
@author:lupang 
@file: 字符串中的单词书.py 
@time: 2021/01/19 
"""
'''
统计字符串中的单词个数，这里的单词指的是连续的不是空格的字符。
请注意，你可以假定字符串里不包括任何不可打印的字符。

示例:

输入: "Hello, my name is John"
输出: 5
解释: 这里的单词是指连续的不是空格的字符，所以 "Hello," 算作 1 个单词。

'''

def countSegments(s: str) -> int:
    #方法一
    # l=s.split(" ")
    # print(l)
    # c=0
    # for i in l:
    #     if i!="":
    #         c=c+1
    # return c

    #方法二
    a = s.split()
    return len(a)

print(countSegments("       "))