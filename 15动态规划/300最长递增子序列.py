# https://leetcode.cn/problems/longest-increasing-subsequence/?envType=study-plan-v2&envId=top-100-liked
# 题目：给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
# 子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。
# 例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。
 
# 思路：每个数字，都去看它前面所有比它小的数。然后接在最长的那一条后面！

from polars import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        for i, x in enumerate(nums): # 遍历下标及对应数字
            for j, y in enumerate(nums[:i]): # 遍历i前面的数字，j从0到i-1
                if x > y: # 如果当前数字x大于前面的数字y, 就接上去
                    dp[i] = max(dp[i], dp[j]) # 把最长的给dp[i]
            dp[i] += 1 # 找到了最长队伍之后，站到最长队伍后面，长度+1
        return max(dp)
    
# dp[i] = 以第 i 个数字结尾的最长递增子序列的长度