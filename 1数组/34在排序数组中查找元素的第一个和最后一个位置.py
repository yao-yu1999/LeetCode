# https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/
# lower_bound 返回最小的满足 nums[i] >= target 的下标 i
    # 如果数组为空，或者所有数都 < target，则返回 len(nums)
    # 要求 nums 是非递减的，即 nums[i] <= nums[i + 1]
# 循环不变量：
            # nums[left-1] < target
            # nums[right+1] >= target

from typing import List

class Solution:
    # 与35和704相比。该题由于需要调用两次，所以建议放在类内部
    def lower_bound(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1  # 闭区间 [left, right]
        while left <= right:  # 区间不为空
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid - 1  # 范围缩小到 [left, mid-1]
            else:
                left = mid + 1  # 范围缩小到 [mid+1, right]
        # 循环结束后 left = right+1
        # 此时 nums[left-1] < target 而 nums[left] = nums[right+1] >= target
        # 所以 left 就是第一个 >= target 的元素下标
        return left

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = self.lower_bound(nums, target)  # 根据通用模板，可以直接获取起始位置：第一个 >= target 的元素下标
        
        if start == len(nums) or nums[start] != target:  # start == len(nums) 说明所有元素都 < target； nums[start] != target 说明数组中没有 target，因为start都不存在了，也就不可能存在 end
            return [-1, -1]  # nums 中没有 target
        
        # 如果 start 存在，那么 end 必定存在
        end = self.lower_bound(nums, target + 1) - 1 # end 是第一个 >= target+1 （等价于 > target）的元素下标减一，即最后一个 == target 的元素下标
        return [start, end]
