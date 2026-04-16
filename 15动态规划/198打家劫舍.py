# https://leetcode.cn/problems/house-robber/description/?envType=study-plan-v2&envId=top-100-liked
# 题目：每间房内都藏有一定的现金，影响你偷窃的唯一因素是：如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
# 给定一个代表每个房屋存放金额的非负整数数组nums，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

from litellm import cache
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 2)  # 创建DP数组，长度 = 房屋数量 + 2. 初始条件：f[0]=f[1]=0

        for i, money in enumerate(nums): # 用enumerate(nums)同时获取索引i和对应的金额nums[i]
            dp[i+2] = max(dp[i+1], dp[i] + money) 
            # 由前两个房子决定:不偷这间, 就是前一间的最大值=dp[i+1]
            #                偷这间的话, 前一间绝对不能偷。最大钱=前前间的最大值 + 这间的钱
        return dp[-1]
    
# dp[i]：前 i 间房子，最多偷多少钱

# 注1：为什么长度 +2？
# 为了避免边界判断，让 i 从 0 开始时不会越界。f[0] = 0（0 间房），f[1] = 0（1 间房还没开始遍历）。
# 第一间房的结果存在 f[2]，第二间房的结果存在 f[3]

# 注2：写成 for i, nums[i] in enumerate(nums): 不规范。但是python不会报错