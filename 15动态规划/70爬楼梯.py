# https://leetcode.cn/problems/climbing-stairs/?envType=study-plan-v2&envId=top-100-liked
# 题目：假设你正在爬楼梯。需要 n 阶你才能到达楼顶。每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

from litellm import cache

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n+1) # 初始化一维DP数组，有n+1个0。楼梯阶数是从 0 到 n（比如 n=3，要算 0、1、2、3 阶）
        dp[0] = dp[1] = 1 # 初始条件:原地不动是一种方案;踏上阶梯也只有一种方案
        
        for i in range(2, n+1):  # 遍历每个阶数，从2到n（因为0和1的情况已经初始化了）
            dp[i] = dp[i-1] + dp[i-2] # 状态转移方程：到达第n阶的方法数 = 到达第n-1阶的方法数 + 到达第n-2阶的方法数（因为每次可以爬1阶或2阶）
        return dp[-1] # 5. 返回第n阶的方法数