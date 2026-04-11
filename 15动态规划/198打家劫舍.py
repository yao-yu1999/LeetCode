# https://leetcode.cn/problems/house-robber/description/?envType=study-plan-v2&envId=top-100-liked
# 题目：每间房内都藏有一定的现金，影响你偷窃的唯一因素是：如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
# 给定一个代表每个房屋存放金额的非负整数数组nums，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

from litellm import cache
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # 创建DP数组，长度 = 房屋数量 + 2
        f = [0] * (len(nums) + 2)  # 初始条件：f[0]=f[1]=0

        for i, money in enumerate(nums): # 用enumerate(nums)同时获取索引i和对应的金额nums[i]
            f[i+2] = max(f[i+1], f[i] + money)
        return f[-1]
    
# 注1：为什么长度 +2？
# 为了避免边界判断，让 i 从 0 开始时不会越界。f[0] = 0（0 间房），f[1] = 0（1 间房还没开始遍历）。
# 第一间房的结果存在 f[2]，第二间房的结果存在 f[3]

# 注2：写成 for i, nums[i] in enumerate(nums): 不规范。但是python不会报错

"""
1. 递归边界：当 i<0 时，没有房子可偷，收益为 0；当 i=0 时，只有一间房子可偷，收益 nums[0]。因此，递归边界是 i<0。
状态转移方程：对于第 i 间房子，有两种选择：
(1) 不偷第 i 间：最大收益就是 “偷到第 i-1 间的最大收益”	，即dfs(i-1)
(2) 偷第 i 间：  最大收益是 “偷到 i-2 间的最大收益 + 第 i 间的金额”，即	dfs(i-2) + nums[i]

前面怎么偷的不管，只关心当前这个，剩下的交给递归~

class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def dfs(i:int)->int:
            if i<0: # 递归边界：i<0表示没有房子可偷，收益为0，i=1直接偷即可，因此不算边界
                return 0
            return max(dfs(i-1),dfs(i-2)+nums[i]) # 拆解成“不偷第 i 间”和“偷第 i 间”
        return dfs(len(nums) - 1)  # 从最后一间房号开始偷，判断偷和不偷这个房间的收益哪个最大？
"""