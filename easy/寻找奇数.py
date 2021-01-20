#-*- coding:utf-8 _*-
"""
@author:lupang
@file: 寻找奇数.py
@time: 2020/08/18
"""

'''
现在有一个长度为n的正整数序列，其中只有【一种】数值出现了奇数次，其他数值均出现偶数次，请你找出那个出现奇数次的数值。
输入：
5
2 1 2 3 1
输出：
3
'''


# endstr="end"  #重新定义结束符
# str=""
# for line in iter(input,endstr):#每行接收的东西
#     str+= line+"\n"#换行
#
# slist = str.split("\n")[1].replace(' ','')
# print(slist)
#
# for i in slist:
#     if slist.count(i)%2 != 0:
#         print(i)


n = int(input())
s = list(map(int,input().split()))
num = 0
for i in s:
    num = num ^ i   ##num和i异或，0^i=i，i^i=0，0和任何数值n异或等于n，相同的数异或结果为0，所以最后只剩出现奇数次的数值
    print(num,":",i)
print(num)