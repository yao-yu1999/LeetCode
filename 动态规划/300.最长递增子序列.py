# https://leetcode.cn/problems/longest-increasing-subsequence/?envType=study-plan-v2&envId=top-100-liked

# 法1：时间按复杂度O(n^2)，空间复杂度O(n)
from polars import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        f = [0] * len(nums)
        for i, nums[i] in enumerate(nums): # 遍历下标及对应数字
            for j, nums[j] in enumerate(nums[:i]): # 遍历i前面的数字，j从0到i-1
                if nums[i] > nums[j]: # 如果当前数字大于前面的数字就接上去
                    f[i] = max(f[i], f[j]) # 把最长的给f[i]
            f[i] += 1 # 找到了最长队伍之后，站到最长队伍后面，长度+1
        return max(f)
    
# 法2：贪心+二分，时间复杂度O(nlogn)，空间复杂度O(n)
'''
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ng = 0  # g 的长度
        for x in nums:
            j = bisect_left(nums, x, 0, ng)
            nums[j] = x
            if j == ng:  # >=x 的 g[j] 不存在
                ng += 1 
        return ng

'''