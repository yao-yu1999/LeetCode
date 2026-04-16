# https://leetcode.cn/problems/perfect-squares/description/?envType=study-plan-v2&envId=top-100-liked
# 题目：给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。
# 完全平方数 是一个整数，其值等于另一个整数的平方(其值等于一个整数自乘的积)。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。
# 思路：完全背包问题

from math import inf, isqrt

# 写法一: [推荐]
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] + [inf] * n  # 初始化DP数组。初始条件f[0] = 0，其余无穷大
        
        for i in range(1, isqrt(n) + 1):# 求组合数：先遍历所有平方数（即底数i，物品）
            square = i * i  # 当前物品的重量：i²
            for j in range(square, n + 1): # 遍历剩下的容量
                dp[j] = min(dp[j], dp[j - square] + 1) # 不选当前平方数 vs 选当前平方数。1表示选了第i件物品，计数+1
        
        return dp[n]
    
# dp[j] 的含义：凑出数字 j，最少需要多少个完全平方数
# 注1：循环 for j in range(square, n + 1): 表示遍历剩下的容量，直接从i*i开始，因为小于i*i的容量无法放下第i件物品。相当于减少循环次数
# 注2：优化方法。
# 函数内计算（每次调用都重新算）。而题目 n 最大就是 10000，所以在全局中提前把 0～10000 所有答案算好。函数直接查表返回
N= 10000
f = [0] + [inf]*N

# 写在外面,直接得到
for i in range(1, isqrt(N)+1): # 遍历平方数的底数
    for j in range(i*i, N+1): # 遍历剩下的容量
        f[j] = min(f[j], f[j-i*i]+1)

class Solution:
    def numSquares(self, n: int) -> int:
        return f[n]