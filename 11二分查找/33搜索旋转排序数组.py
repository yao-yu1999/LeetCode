# https://leetcode.cn/problems/search-in-rotated-sorted-array/description/?envType=study-plan-v2&envId=top-100-liked
# 题目：整数数组nums按升序排列，数组中的值 互不相同 。
# 在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 向左旋转，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,5,6,7] 下标 3 上向左旋转后可能变为 [4,5,6,7,0,1,2] 。
# 给你旋转后的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。

from typing import List

# 方法：两次二分【推荐】时间复杂度O(logn)
class Solution:
    # 153. 寻找旋转排序数组中的最小值（返回的是下标）
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right: 
            mid = (left + right) // 2
            if nums[mid] < nums[-1]:
                right = mid
            else:
                left = mid + 1
        return left

    # 704. 二分查找：有序数组中找 target 的下标
    def lower_bound(self, nums: List[int], left: int, right: int, target: int) -> int:
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid - 1  # 范围缩小到 (left, mid)
            else:
                left = mid + 1  # 范围缩小到 (mid, right)
        return left if left < len(nums) and nums[left] == target else -1

    # （本题）33. 搜索旋转排序数组
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:  # 数组中没有元素，所以找不到target
            return -1
        
        i = self.findMin(nums)  # 切分：找到最小值下标 i
        if target > nums[-1]: # target 只可能出现在第一段 [0, i-1]
            if i == 0:          # 第一段为空，但target比整个数组最后一个值还大，说明找不到target
                return -1
            return self.lower_bound(nums, 0, i - 1, target) 
        else: # target 只可能出现在第二段 [i, n-1]
            return self.lower_bound(nums, i, len(nums) - 1, target)