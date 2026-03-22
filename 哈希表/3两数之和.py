# https://leetcode.cn/problems/two-sum/description/
from typing import List

# 优化解法:用哈希表,时间复杂度是 O(n) :
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = {}  # 创建一个空哈希表（字典）
        for i, x in enumerate(nums):  # x=nums[i]
            if target - x in idx:  # 在左边找 nums[i]，满足 nums[i]+x=target
                return [idx[target - x], i]  # 返回两个数的下标
            idx[x] = i  # 保存 nums[i] 和 i



'''
暴力解法: 用两层for 循环,时间复杂度是 O(n^2) :
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)): 
            for j in range(i+1, len(nums)): # 从 i+1 开始，避免重复计算和自己与自己相加
                if nums[i] + nums[j] == target: 
                    return [i, j]

                    
暴力解法2: 对于每个元素 nums[i]，在剩下的元素中查找是否存在一个数等于 target-nums[i]。时间复杂度是 O(n^2) 。
class Solution(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            res = target-nums[i]  # 计算出需要的另一个数 res,在剩下的元素中查找 res
            if res in nums[i+1:]:       
                return [i, nums[i+1:].index(res)+i+1] # 先获得目标元素在nums[i+1:]这个切片中的索引，再需加上i+1才是该元素在原数组nums中的索引。这里的1是因为切片是从i+1开始的，所以需要加上i+1才能得到在原数组中的正确索引。
'''