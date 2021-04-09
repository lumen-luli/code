#-*- coding:utf-8 _*-  
""" 
@author:lupang 
@file: 松鼠生小松鼠.py 
@time: 2021/02/24 
"""


#一对松鼠生小松鼠，从第三个月开始每个月会生一对，松鼠第十个月的时候会死亡。问N个月有多少对松鼠。

def fs(n):
    f=[]
    f[:3]=[0,1,1]
    i=3
    while  n>=i:
        # 正常增加的
        count = f[i-1]+f[i-2]
        # 死亡的
        if i>9:
            die = f[i-9]
        else:
            die =0
        f.append(count-die)
        i=i+1
    return f[n]

print(fs(9))

