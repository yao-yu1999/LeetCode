# https://leetcode.cn/problems/search-a-2d-matrix/description/?envType=study-plan-v2&envId=top-100-liked
# 题目：给你 m x n 整数矩阵：每行中的整数从左到右按非严格递增顺序排列。每行的第一个整数大于前一行的最后一个整数。
# 给你一个整数 target ，如果 target 在矩阵中，返回 true ；否则，返回 false 。

from typing import List

# 二分查找 【推荐】
# 把 m×n 的矩阵 → 想象成一个有序的长数组，然后直接用二分查找
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])        # 行列数
        left, right = 0, m * n -1         # 虚拟一维数组长度

        while left <= right:
            mid = (left + right) // 2   # 中间位置（一维下标）
            
            # 中间值的一维索引 → 二维坐标
            row = mid // n  # 看mid在第几行 =  mid 除以列数，取整数
            col = mid % n   # 看mid在第几列 =  mid 对列数取余
            if matrix[row][col] == target:  # 在矩阵中，拿到中间值 matrix[row][col]
                return True   # 找到
            elif matrix[row][col] < target:
                left = mid+1    # 答案在右边
            else:
                right = mid-1  # 答案在左边

        return False  # 没找到



