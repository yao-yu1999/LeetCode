# https://leetcode.cn/problems/search-insert-position/
# 题目：给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。请必须使用时间复杂度为 O(log n) 的算法。
# 本题是二分查找的变体, 但建议以本体为模板, 因为可插入可查找。

from typing import List

# 写法1：闭区间【推荐】
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
    
# lower_bound的另外两个写法：
# 写法2：左闭右开区间
def lower_bound2(nums: List[int], target: int) -> int:
    left, right = 0, len(nums)  # 左闭右开区间 [left, right)
    while left < right:  # 区间不为空
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1  # 范围缩小到 [mid+1, right)
        else:
            right = mid  # 范围缩小到 [left, mid)
    return left  # 或者 right

# 写法3：开区间
def lower_bound3(nums: List[int], target: int) -> int:
    left, right = -1, len(nums)  # 开区间 (left, right)
    while left + 1 < right:  # 区间不为空
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid  # 范围缩小到 (mid, right)
        else:
            right = mid  # 范围缩小到 (left, mid)
    return right  # 或者 left+1

# 测试(可选)
if __name__ == "__main__":
    nums = list(map(int, input().split())) # 1.1 读取第一行, 转换为整数列表
    target = int(input()) # 1.2 读取第二行, 转换为整数
    
    sol = Solution() # 2. 创建 Solution 对象
    result = sol.search(nums, target)  # 3. 调用
    print("目标值位置(下标):", result) # 打印结果

'''
本题思路:
在升序数组 nums 中寻找目标值 target, 对于特定下标 i, 比较 nums[i] 和 target 的大小:
如果 nums[i]=target, 则下标 i 即为要寻找的下标；
如果 nums[i]>target, 则 target 只可能在下标 i 的左侧；
如果 nums[i]<target, 则 target 只可能在下标 i 的右侧。

一、步骤
(1)定义查找的范围 [left,right], 初始是整个数组, 逐渐移动
(2)每次取查找范围的中点 mid
(3)比较 nums[mid] 和 target 的大小:
- 如果相等则 mid 即为要寻找的下标；
- 如果不相等则根据 nums[mid] 和 target 的大小关系将查找范围缩小一半

二、变量解释
left:数组左边界
right:数组右边界
nums:数组名称
mid:每次查找范围的中值
target:目标值

三、注意事项
(1)确保是升序数组left <= right, 降序数组修改循环条件为right <= left
(2)确定中值的时候, 为了防止数组长度过大, 相加易导致的溢出, 一般使用:mid=(high-low)//2 + low,先获取中间长度。
(3)len(nums) 等价于 num.length

(4)确定区间, 且后续代码在写判断条件时, 必须统一使用这个区间:
- 闭区间 [0, 100], 则后续代码中所有的区间判断都必须使用闭区间 [0, 100]
- 半开区间-左闭右开 [0, 100), 则后续代码中所有的 区间判断都必须使用半开区间 [0, 100)
- 全开区间 (0, 100), 则后续代码中所有的区间判断都必须使用全开区间 (0, 100)

循环里面的不变量:
- nums[left-1] < target
- nums[right+1] >= target

以二分查找为例:
1. 通常使用闭区间 [0, n-1] 来定义下标范围, 那么在后续的代码中, 就必须统一使用闭区间的判断条件:
(1)初始赋值:
- left, right = 0, len(nums)-1 # 定义下标范围为闭区间 [0, n-1]
(2)循环条件:
- while left <= right:  # 使用闭区间的判断条件
(3)更新边界时, 也要注意保持区间的一致性:
- left = mid + 1  # 说明在右半区间, 将左边界移动到中间+1
- right = mid - 1  # 说明在左半区间, 将右边界移动到中间-1

2. 如果是半开区间-左闭右开 [0, n):
(1)初始赋值:
- left, right = 0, len(nums) # 定义下标范围为半开区间 [0, n)

(2)循环条件:
- while left < right:  # 使用半开区间的判断条件

(3)更新边界:
判断右边界
- left = mid + 1  # 说明在右半区间, 将左边界移动到中间+1
- right = mid  # 说明在左半区间, 将右边界移动到中间

'''