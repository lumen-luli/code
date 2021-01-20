#-*- coding:utf-8 _*-  
""" 
@author:lupang 
@file: 字符串归一化.py
@time: 2020/08/06 
"""
'''
通过键盘输入一串小写字母(a~z)组成的字符串。
请编写一个字符串归一化程序，统计字符串中相同字符出现的次数，并按字典序输出字符及其出现次数。
例如字符串"babcc"归一化后为"a1b2c2"

输入
每个测试用例每行为一个字符串，以'\n'结尾，例如cccddecca
输出
输出压缩后的字符串ac5d2e

'''
import re
def fin():

    a = input()
    if re.match('[a-z]+',a)==None:
        print("非法字符串")
    else:
        res = {}
        for i in sorted(set(a)):
            res[i] = a.count(i)
            print(i+str(res[i]),end='')

fin()



