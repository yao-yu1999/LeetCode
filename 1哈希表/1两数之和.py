# https://leetcode.cn/problems/two-sum/?envType=study-plan-v2&envId=top-100-liked
# 题目：给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。你可以按任意顺序返回答案。

from typing import List

# 优化解法:用哈希表, 时间复杂度是 O(n) :
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = {}  # 创建一个空哈希表（字典）
        for i, x in enumerate(nums):  # 遍历数组：(下标i, 元素x), x=nums[i]
            if target - x in idx:  # 在字典找另一个数 nums[i]，满足 nums[i] + x = target
                return [idx[target - x], i]  # 返回两个数的下标
            idx[x] = i  # 没有找到，就插入(key)元素x, (value)下标为i