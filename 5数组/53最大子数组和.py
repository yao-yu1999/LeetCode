# https://leetcode.cn/problems/maximum-subarray/?envType=study-plan-v2&envId=top-100-liked
# 题目：给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。子数组是数组中的一个连续部分。
# 152题是乘积版本

from typing import List

# 方法：DP（动态规划）
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)  # DP数组：dp[i] 表示以 nums[i] 结尾的最大子数组和
        dp[0] = nums[0]       # 初始条件：第一个数组的和就是第一个数的值
        
        for i in range(1, len(nums)): # 从1开始
            dp[i] = max(dp[i - 1], 0) + nums[i]  # 核心递推公式。

        return max(dp)  # 答案是所有f中的最大值
    
# 为什么是和0比较？
# 选或不选：如果前面的最大和是负数，就不要前面的了，只保留自己（当前遍历到的数）。如果是正数才带上前面的

# 为什么返回的是max(dp), 不是dp[-1]?
# 因为最大值不一定在最后一个，前面的就有可能一定得到最大值了，不一定要到最后一步