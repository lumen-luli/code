#-*- coding:utf-8 _*-  
""" 
@author:lupang 
@file: 贪心-找钱.py
@time: 2020/10/28 
"""

# 有1元，5元，10元，20元，100元，200元的钞票无穷多张。现使用这些钞票支付x元，最少需要多少张
#俐：x=628

amount=[1,5,10,20,100,200]
amount.sort(reverse=True)
x=628
count=0

for i,val in enumerate(amount):
    use = x//amount[i]
    count += use
    x = x - use*amount[i]
    print("use",amount[i],use," count",count," remain",x)
    if x<=0:
        break



print(count)