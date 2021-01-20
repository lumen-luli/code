#-*- coding:utf-8 _*-  
""" 
@author:lupang 
@file: 测试.py 
@time: 2020/11/05 
"""

#判断回文
def isPalindrome( x):
    # write code here
    #负数没有回文数
    s = str(x)
    s = s[-1::-1]
    if s == str(x):
        return True
    else:
        return False
# return str(x)[::-1] == str(x)
#print(isPalindrome(-2147447412))



#数字翻转
def reverse( x):
    # write code here
    if x < 0:
        x = str(-x)[-1::-1]
        return -int(x)
    else:
        x = str(x)[-1::-1]
        return int(x)

#print(reverse(10000000003))


def twoSum( numbers, target):
    # write code here
            #str=[]
            # for k, v in enumerate(numbers):
            #     if target ==0 and 0== v:
            #         str.append(k+1)
            #     if (target - v)  in numbers and (target - v)!=v:
            #         str=[numbers.index(v)+1,numbers.index(target-v)+1]
            #     if(target - v) in numbers and (target - v) == v:
            #         pass
            # return str
    res = []
    n = len(numbers)
    h = {}
    for i in range(n):
        t = target - numbers[i]
        if t in h:
            return [h[t] + 1, i + 1]
        h[numbers[i]] = i
        #print(h)
    return str

#print(twoSum([3,2,4],6))

def test(numbers,target):
    b=[]
    for k,v in enumerate(numbers):
        if target==v:
            b.append(k)
    return b
print(test([0,4,3,0],0))


def isValid(s):
    # write code here
    d={'{':'}','(':')','[':']'}
    a=[]
    for i in s:
        if i in d:
            a.append(i)
        else:
            #print(i)
            if len(a)==0:return False
            ans=a.pop()
            if d[ans]==i:
                pass
            else:
                return False
    if len(a)==0:
        return True

print(isValid("(){}"))









