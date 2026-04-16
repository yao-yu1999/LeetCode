# https://leetcode.cn/problems/sort-colors/submissions/718404493/?envType=study-plan-v2&envId=top-100-liked
# 题目:给定一个包含红色、白色和蓝色、共 n 个元素的数组 nums ，原地 对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
# 使用整数 0、 1 和 2 分别表示红色、白色和蓝色。必须在不使用库内置的 sort 函数的情况下解决这个问题。

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        p0 = 0   # 下一个 0 应该放的位置
        p1 = 0   # 下一个 1 应该放的位置
        for i, x in enumerate(nums):
            # 从2开始,依次往后覆盖,顺序不能变: 2->1->0
            nums[i] = 2 # 先把当前位置默认设为 2（最大的）

            if x <= 1: # 如果当前数是 0 或 1
                nums[p1] = 1 # 把 p1 位置设为 1
                p1 += 1 # p1 向后挪一位

            if x == 0: # 如果当前数是 0
                nums[p0] = 0 # 把 p0 位置设为 0
                p0 += 1 # p0 向后挪一位

# 维护三个区间 0:[0, p0-1]
#             1:[p0, p1-1]
#             2:[p1, p2-1]
# 因为p0和p1指向的是下一个0和1的位置,所以后面是会被覆盖的:
# (1) 来的数字是 0 → 两个 if 都执行
# 先把 1 往右挪一位（nums[p1] = 1）
# 再把 0 放进左边正确位置（nums[p0] = 0）
# (2) 来的数字是 1 → 只执行第一个 if
# 把 1 放进中间位置
# (3) 来的数字是 2 → 都不执行，保持 2
