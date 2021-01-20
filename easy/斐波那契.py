#-*- coding:utf-8 _*-  
""" 
@author:lupang 
@file: 斐波那契.py 
@time: 2020/10/28 
"""

# 0、1、1、2、3、5、8、13、21、34、

#递归
# def fib_1(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return  fib_1(n-1)+fib_1(n-2)
#
# print(fib_1(5))

#生成器
# def fib_2(n):
#     a, b = 0, 1
#     for _ in range(n):
#         a, b = b, a + b
#         yield a
#
# for val in fib_2(20):
#     print(val)



#动态规划

def fib_3(n):
    i=2
    memo = []
    memo[1:1]=[0,1]
    while i<=n and n>1:
        memo.append(memo[i-1]+memo[i-2])
        #print(memo[i])
        i+=1
    return memo[n]

print(fib_3(4))


def fib(n) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a % 1000000007

print(fib(4))

'''
大数阶乘，大数的排列组合等，一般都要求将输出结果对1000000007取模
为什么总是1000000007呢= =

大概≖‿≖✧是因为：
1.1000000007是一个质数
2.int32位的最大值为2147483647，所以对于int32位来说1000000007足够大
3.int64位的最大值为2^63-1，对于1000000007来说它的平方不会在int64中溢出
所以在大数相乘的时候，因为(a∗b)%c=((a%c)∗(b%c))%c，所以相乘时两边都对1000000007取模，再保存在int64里面不会溢出
'''
def fib2(n):
    fibs = []
    fibs[1:1] = [0, 1]
    i = 2
    while i <= n:
        fibs.append(fibs[i - 1] + fibs[i - 2])
        i = i + 1
    return int(int(fibs[n])%(1000000007))

print(fib2(4))




