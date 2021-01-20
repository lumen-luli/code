#-*- coding:utf-8 _*-  
""" 
@author:lupang 
@file: 深拷贝和浅拷贝.py 
@time: 2020/11/02 
"""

import copy

#浅拷贝
list1 = [[1,2],'test','66']
list2 = copy.copy(list1)
#对象地址不同
print(id(list1))
print(id(list2))
a = 111
b = copy.copy(a)
#对象地址同
print(id(a))
print(id(b))

#不可变类型修改
list3 = [1,2]
list4=["hhh","333"]
c = 111
all=[list3,list4,c]
all2 = copy.copy(all)
list3[0]=3
c=333

print(all)
print(all2)


#深拷贝
n=17
n1=copy.deepcopy(n)
#对象地址同
print(id(n))
print(id(n1))
l1=[1,2]
l2=copy.deepcopy(l1)
#对象地址不同
print(id(l1))
print(id(l2))

#深拷贝修改
list3 = [1,2]
list4=["hhh","333"]
d = 111
all=[list3,list4,d]
all2 = copy.deepcopy(all)
list3[0]=3
d=333

print(all)
print(all2)






