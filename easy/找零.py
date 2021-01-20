#-*- coding:utf-8 _*-  
""" 
@author:lupang 
@file: 找零.py 
@time: 2020/10/26 
"""
# Z国的货币系统包含面值1元、4元、16元、64元共计4种硬币，以及面值1024元的纸币。
# 现在小Y使用1024元的纸币购买了一件价值为N (0 < N \le 1024)N(0<N≤1024)的商品，
# 请问最少他会收到多少硬币？

# 因为存在一元硬币，一定可以找清，所以直接贪心

N = int(input())
remain, cnt = 1024-N, 0
coins = [64, 16, 4] # coins which values greater than 1
for i in range(len(coins)):
    c = remain//coins[i]
    cnt += c
    remain -= c*coins[i]
print(remain + cnt)

# 若可能不能找清，或不存在1元硬币这种简单情况，用动态规划会更合适
N = int(input())
remain = 1024-N
coins = [2, 4, 16, 64]
# dp[i] 还剩i元未找清时的最优解
dp = [float('inf') for i in range(remain+1)]
dp[0] = 0

for i in range(remain+1):
    for c in coins:
        dp[i] = min(dp[i-c]+1, dp[i]) if i >= c else dp[i]

print(dp[-1]) # 若无法找清，则会等于float('inf')