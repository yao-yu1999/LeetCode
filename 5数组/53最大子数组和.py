# https://leetcode.cn/problems/maximum-subarray/?envType=study-plan-v2&envId=top-100-liked

from typing import List

# 方法1：DP（动态规划）
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        f = [0] * len(nums)  # DP数组
        f[0] = nums[0]       # 初始条件
        
        for i in range(1, len(nums)):
            f[i] = max(f[i - 1], 0) + nums[i]  # 核心递推公式
            
        return max(f)  # 答案是所有f中的最大值