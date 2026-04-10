# https://leetcode.cn/problems/first-missing-positive/description/?envType=study-plan-v2&envId=top-100-liked
# 题目：给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。
# 原地哈希法：将原数组作哈希表

class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        
        # 第一遍：将每个在 [1, n] 内的数字放到它应该在的位置
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:  # 只要当前数字在有效范围内，并且它没有在正确的位置上（防止重复元素造成的死循环）
                j = nums[i] - 1 # 计算它应该去的位置（下标）
                nums[i], nums[j] = nums[j], nums[i] # 交换两个位置的元素。注意：不能写成 nums[i], nums[nums[i]-1] = nums[nums[i]-1], nums[i], 因为 nums[i] 在赋值过程中会被改变，导致下标计算错误
        
        # 第二遍：寻找第一个位置不对的数字
        for i in range(n):
            if nums[i] != i + 1:   # 位置i的期望值是 i+1，实际值不是它
                return i + 1   # 缺失的就是 i+1
        
        return n + 1 # 如果所有位置都对，说明 1..n 都存在，返回n+1