from litellm import cache
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def dfs(i:int)->int:
            if i<0: # 递归边界：i<0表示没有房子可偷，收益为0，i=1直接偷即可，因此不算边界
                return 0
            return max(dfs(i-1),dfs(i-2)+nums[i]) # 拆解成“不偷第 i 间”和“偷第 i 间”
        return dfs(len(nums) - 1)  # 从最后一间房号开始偷，判断偷和不偷这个房间的收益哪个最大？
    
"""
1. 递归边界：当 i<0 时，没有房子可偷，收益为 0；当 i=0 时，只有一间房子可偷，收益 nums[0]。因此，递归边界是 i<0。
状态转移方程：对于第 i 间房子，有两种选择：
(1) 不偷第 i 间：最大收益就是 “偷到第 i-1 间的最大收益”	，即dfs(i-1)
(2) 偷第 i 间：  最大收益是 “偷到 i-2 间的最大收益 + 第 i 间的金额”，即	dfs(i-2) + nums[i]

前面怎么偷的不管，只关心当前这个，剩下的交给递归~

"""