# https://leetcode.cn/problems/search-insert-position/
# 题目：给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。请必须使用时间复杂度为 O(log n) 的算法。
# 本题是二分查找的变体, 但建议以本体为模板, 因为可插入可查找。

from typing import List

# 方法:二分查找, 闭区间【推荐】
def lower_bound(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1  # 闭区间 [left, right]
    while left <= right:  # 区间不为空
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1  # 范围缩小到 [mid+1, right]
        else:
            right = mid - 1  # 范围缩小到 [left, mid-1]
    return left  # 或者 right+1。循环结束时：right 是 最后一个 < target 的位置；left 是 第一个 >= target 的位置。left 正好等于 right + 1。

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = lower_bound(nums, target)  # 直接插入
        return i

# 测试(可选)
if __name__ == "__main__":
    nums = list(map(int, input().split())) # 1.1 读取第一行, 转换为整数列表
    target = int(input()) # 1.2 读取第二行, 转换为整数
    
    sol = Solution() # 2. 创建 Solution 对象
    result = sol.search(nums, target)  # 3. 调用
    print("目标值位置(下标):", result) # 打印结果