# https://leetcode.cn/problems/search-insert-position/
# 这题也是不重复的升序数组。思路：返回 nums 中的第一个（最左边的）大于或等于 target 的数的下标。

# lower_bound 返回最小的满足 nums[i] >= target 的 i
# 如果“数组为空”或者“所有数都 < target”，则返回 len(nums)；要求 nums 是非递减的，即 nums[i] <= nums[i + 1]

# 循环里面的不变量:
# nums[left-1] < target
# nums[right+1] >= target

# 通用写法:
from typing import List

# 闭区间写法
def lower_bound(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1  # 闭区间 [left, right]
    while left <= right:  # 区间不为空
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1  # 范围缩小到 [mid+1, right]
        else:
            right = mid - 1  # 范围缩小到 [left, mid-1]
    return left  # 或者 right+1

# 左闭右开区间写法
def lower_bound2(nums: List[int], target: int) -> int:
    left, right = 0, len(nums)  # 左闭右开区间 [left, right)
    while left < right:  # 区间不为空
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1  # 范围缩小到 [mid+1, right)
        else:
            right = mid  # 范围缩小到 [left, mid)
    return left  # 或者 right

# 开区间写法
def lower_bound3(nums: List[int], target: int) -> int:
    left, right = -1, len(nums)  # 开区间 (left, right)
    while left + 1 < right:  # 区间不为空
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid  # 范围缩小到 (mid, right)
        else:
            right = mid  # 范围缩小到 (left, mid)
    return right  # 或者 left+1


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = lower_bound(nums, target)  # 直接插入
        return i

# 测试（可选）
if __name__ == "__main__":
    nums = list(map(int, input().split())) # 1.1 读取第一行，转换为整数列表
    target = int(input()) # 1.2 读取第二行，转换为整数
    
    sol = Solution() # 2. 创建 Solution 对象
    result = sol.search(nums, target)  # 3. 调用
    print("目标值位置(下标)：", result) # 打印结果