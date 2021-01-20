#-*- coding:utf-8 _*-  
""" 
@author:lupang 
@file: 1比特与2比特字符.py 
@time: 2020/08/19 
"""
'''
有两种特殊字符。第一种字符可以用一比特0来表示。第二种字符可以用两比特(10 或 11)来表示。
现给一个由若干比特组成的字符串。问最后一个字符是否必定为一个一比特字符。给定的字符串总是由0结束。

输入: 
bits = [1, 0, 0]
输出: True
解释: 
唯一的编码方式是一个两比特字符和一个一比特字符。所以最后一个字符是一比特字符。

输入: 
bits = [1, 1, 1, 0]
输出: False
解释: 
唯一的编码方式是两比特字符和两比特字符。所以最后一个字符不是一比特字符。


解题：
题目说了，bits最后一个元素一定是0，所以我们只要判断最后一个0是自己组队（一比特），还是和1组队（二比特）就可以了。我们遍历bits，如果当前元素是1，那么i就走两步，否则走一步，那么如果最后一个0是和1组队的，那退出循环时候的i一定不会等于n（因为走两步的关系），反之就会等于n......


'''
def solution():
    bits = [1, 1,  0]
    for i in range(len(bits)):
        if bits[i] == 1 and i<len(bits)-2:
            i = i+2
        elif bits[i]==0 and i<len(bits) -1:
            i=i+1

        return i == len(bits)-1

print(solution())


#方法一  线性扫描
'''
我们可以对 \mathrm{bits}bits 数组从左到右扫描来判断最后一位是否为一比特字符。当扫描到第 ii 位时，如果 \mathrm{bits}[i]=1bits[i]=1，
那么说明这是一个两比特字符，将 ii 的值增加 2。如果 \mathrm{bits}[i]=0bits[i]=0，那么说明这是一个一比特字符，将 ii 的值增加 1。
如果 ii 最终落在了 \mathrm{bits}.\mathrm{length}-1bits.length−1 的位置，那么说明最后一位一定是一比特字符。

'''
class Solution(object):
    def isOneBitCharacter(self, bits):
        i = 0
        while i < len(bits) - 1:
            i += bits[i] + 1
        return i == len(bits) - 1



#方法二 贪心
'''
三种字符分别为 0，10 和 11，那么 \mathrm{bits}bits 数组中出现的所有 0 都表示一个字符的结束位置（无论其为一比特还是两比特）。
因此最后一位是否为一比特字符，只和他左侧出现的连续的 1 的个数（即它与倒数第二个 0 出现的位置之间的 1 的个数，如果 \mathrm{bits}bits 数组中只有 1 个 0，
那么就是整个数组的长度减一）有关。如果 1 的个数为偶数个，那么最后一位是一比特字符，如果 1 的个数为奇数个，那么最后一位不是一比特字符。

'''
class Solution2(object):
    def isOneBitCharacter(self, bits):
        parity = bits.pop()
        while bits and bits.pop(): parity ^= 1
        return parity == 0
