# https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/?envType=study-plan-v2&envId=top-100-liked
# 题目：已知一个长度为 n 的数组，预先按照升序排列，经由 1 到 n 次 旋转 后，得到输入数组。例如，原数组 nums = [0,1,2,4,5,6,7] 在变化后可能得到：
# 若旋转 4 次，则可以得到 [4,5,6,7,0,1,2]；若旋转 7 次，则可以得到 [0,1,2,4,5,6,7]
# 注意，数组 [a[0], a[1], a[2], ..., a[n-1]] 旋转一次 的结果为数组 [a[n-1], a[0], a[1], a[2], ..., a[n-2]] 。
# 给你一个元素值 互不相同 的数组 nums ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 最小元素 。
# 设计一个时间复杂度为 O(log n) 的算法解决此问题。

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1  
        while left < right:  # 左右指针重合时，找到唯一最小值
            mid = (left + right) // 2
            if nums[mid] < nums[-1]: # 将mid与最后一个值进行比较
                right = mid # 右指针可能是右半段值小的递增区间区间的第一个值（也就是最小值），因此不能移动
            else:
                left = mid + 1 # 说明mid是在左半段值更大一段的递增区间，一定不是最小值，所以要移动
        return nums[left] # nums[right]

# 注：数组最小值会将数组划分成左右两个区间。左半段递增区间的所有数都比右半段递增区间的大。

# 与普通二分查找的区别是什么？
# 二分查找是左右指针交错时，返回；旋转数组最小值是左右指针重合时，返回
# 二分查找是动态mid与固定的target比较，旋转数组最小值是mid和固定的nums[-1]比较
# 当 nums[mid] >= target 时，mid 满足条件，但寻找的是第一个满足条件的位置，所以 mid 可能是答案，也可能在它左边还有更早的满足条件的位置。所以需要继续移动指针，直到左右指针交错
