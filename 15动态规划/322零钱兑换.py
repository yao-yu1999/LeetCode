# https://leetcode.cn/problems/coin-change/submissions/711477010/?envType=study-plan-v2&envId=top-100-liked
# 题目：给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。
# 计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。
# 你可以认为每种硬币的数量是无限的。【完全背包】

from typing import List
from numpy import inf

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [inf] * amount # 假设一开始除f[0]=0外，所有金额都凑不出来
        for i in coins: # 因为是求组合数，所以先遍历物品
            for j in range(i, amount + 1): # 再遍历容量
                dp[j] = min(dp[j], dp[j - i] + 1) # 完全背包，所以正序遍历

        return dp[amount] if dp[amount] < inf else -1 # 如果凑的出来返回金额，凑不出来返回-1
    
# i是背包容量，j是物品，f[j]是前j件物品在背包容量为i时的最大价值。