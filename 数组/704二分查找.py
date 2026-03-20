# https://leetcode.cn/problems/binary-search/description/

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1 # 定义下标范围
        while left<=right:  # 循环条件是升序数组
            mid = (right - left)//2 + left  # 先定位中间数的位置（下标）
            mid_value = nums[mid]  # 取出中间的值，用于后续的比较

            if mid_value == target:
                return mid
            elif mid_value < target:
                left = mid + 1 # 说明在右半区间，将左边界移动到中间+1
            else:
                right = mid - 1 # 说明在左半区间，将右边界移动到中间-1
        return -1 # 考虑target不存在的情况

# 测试（可选）
if __name__ == "__main__":
    nums = list(map(int, input().split())) # 1.1 读取第一行，转换为整数列表
    target = int(input()) # 1.2 读取第二行，转换为整数
    
    sol = Solution() # 2. 创建 Solution 对象
    result = sol.search(nums, target)  # 3. 调用
    print("目标值位置(下标)：", result) # 打印结果