#-*- coding:utf-8 _*-  
""" 
@author:lupang 
@file: 今年第几天.py 
@time: 2020/08/14 
"""

'''
输入年、月、日，计算该天是本年的第几天。 
输入： 
包括三个整数年(1<=Y<=3000)、月(1<=M<=12)、日(1<=D<=31)。 
输出： 
输入可能有多组测试数据，对于每一组测试数据， 
输出一个整数，代表Input中的年、月、日对应本年的第几天。

输入：
1990 9 20
输出：
263
'''
import datetime

Y,M,D=map(int,input().split(" "))
date=datetime.datetime(Y,M,D)
# 日期格式化  %j年内的一天
print(int(date.strftime("%j")))


