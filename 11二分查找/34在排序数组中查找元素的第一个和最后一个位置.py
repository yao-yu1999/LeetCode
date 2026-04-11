# https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/
# 题目：给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。
# 如果数组中不存在目标值 target，返回 [-1, -1]。必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。

# 思路：本题结合了35题和704题，且数组中的元素是可重复的，所以需要调用两次二分查找：
# 第一次查找第一个 小于等于 target 的元素下标，第二次查找第一个 大于 target 的元素下标减一。

from typing import List

class Solution:
    # 与35和704题相比。数组中的元素是可重复的，且需要调用两次，所以建议放在类内部
    def lower_bound(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1  # 闭区间 [left, right]
        while left <= right:  # 区间不为空
            mid = (left + right) // 2
            if target <= nums[mid]:
                right = mid - 1  # 范围缩小到 [left, mid-1]
            else:
                left = mid + 1  # 范围缩小到 [mid+1, right]
        return left # 或者 right+1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = self.lower_bound(nums, target)  # 根据通用模板，可以直接获取起始位置：第一个 >= target 的元素下标
        
        # 判断start是否搜索的到
        if start == len(nums) or nums[start] != target:  # start == len(nums) 说明所有元素都 < target； nums[start] != target 说明数组中没有 target，因为start都不存在了，也就不可能存在 end
            return [-1, -1]
        
        # 如果 start 存在，那么 end 必定存在
        end = self.lower_bound(nums, target + 1) - 1 
        return [start, end]  # start到end。注意！！！这里不是数组切片nums[start:end]，而是一个闭区间
    
# nums = [5,7,7,8,8,9,10,19] target=9

# end = self.lower_bound(nums, target + 1) - 1 中：
# target + 1：end 是第一个 > target 的元素，用target + 1表示大于target的一个数（因为所有 > target 的数，一定都 >= target + 1。不一定需要找到target+1这个数）。
# -1: 需要把下标减一，变成最后一个 == target 的元素下标
