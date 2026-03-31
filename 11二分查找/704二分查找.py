# https://leetcode.cn/problems/binary-search/description/
# 直接以35题为模板，因为本题不需要插入，只需要判断是否存在，所以在最后返回时，如果不存在需要返回-1

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
    def search(self, nums: List[int], target: int) -> int:
        i = lower_bound(nums, target)
        return i if i < len(nums) and nums[i] == target else -1  # 如果不存在需要返回-1
        

'''
解法二：这个仅适用于二分查找中不重复升序数组【不建议】
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1 # 定义下标范围
        while left<=right:  # 循环条件是升序数组
            mid = (right - left)//2 + left  # 先定位中间数的位置（下标）

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1 # 说明在右半区间，将左边界移动到中间+1
            else:
                right = mid - 1 # 说明在左半区间，将右边界移动到中间-1
        return -1 # 考虑target不存在的情况
'''


# 测试（可选）
if __name__ == "__main__":
    nums = list(map(int, input().split())) # 1.1 读取第一行，转换为整数列表
    target = int(input()) # 1.2 读取第二行，转换为整数
    
    sol = Solution() # 2. 创建 Solution 对象
    result = sol.search(nums, target)  # 3. 调用
    print("目标值位置(下标)：", result) # 打印结果
