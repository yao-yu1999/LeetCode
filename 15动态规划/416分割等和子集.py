# https://leetcode.cn/problems/partition-equal-subset-sum/description/?envType=study-plan-v2&envId=top-100-liked
# 题目：给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_nums = sum(nums)
        if sum_nums % 2: # 如果和是奇数，就不可能均分
            return False
        target = sum_nums // 2  # 背包容量：sum_nums 减半= target就是我们要凑成的和
        
        dp = [True] + [False] * target # 初始化一维 dp 数组。初始条件：dp[0] = True，和为0可以凑出（什么都不选）
        
        max_sum = 0 # 当前已遍历元素所能凑出的最大和（实际是前缀和与 target 中的最小值）
        for i, x in enumerate(nums): # 求组合数：先物品或容量均可
            max_sum = min(max_sum + x, target) # 优化遍历上限
            for j in range(max_sum, x - 1, -1): # 容量逆序:从 max_sum 到 x。
                dp[j] = dp[j] or dp[j - x] # 不选或选。dp[j], dp[j - x] 只要有一个为True, dp[j]就为True

            if dp[target]: # 提前终止：必须等当前数字 x 完整更新完 dp 数组之后，才能判断是否已经找到答案。如果已经可以组成目标和j=target，直接返回
                return True
        return False
    
# dp[j] 表示：能否选出一些元素，使其和恰好等于 j？

# 优化边界：
# max_sum 表示当前已考虑元素能凑出的最大和（遍历上限）。
#         min(max_sum + x, target) 表示已选数字的和(之前的和max_sum + 当前选的数字x), 不能超过 target。超过target的不需要遍历。
# x 表示数字本身的大小。当 j < x 时，无法选择当前元素 x。（遍历下限）

# range(max_sum, x - 1, -1) 不能写成 range(x, max_sum-1, -1)。因为range(较大值, 较小值, -1)，是从较大值开始递减。
