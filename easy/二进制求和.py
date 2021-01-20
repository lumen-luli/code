#-*- coding:utf-8 _*-  
""" 
@author:lupang 
@file: 二进制求和.py 
@time: 2020/08/19 
"""
'''
给你两个二进制字符串，返回它们的和（用二进制表示）。

输入为 非空 字符串且只包含数字 1 和 0。


示例 1:
输入: a = "11", b = "1"
输出: "100"
'''

def addbinary(a,b):
    return bin(int(a, 2) + int(b, 2))[2:]