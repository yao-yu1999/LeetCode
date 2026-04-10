# https://leetcode.cn/problems/search-a-2d-matrix-ii/description/?envType=study-plan-v2&envId=top-100-liked
# 题目：编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：
# 每行的元素从左到右升序排列。每列的元素从上到下升序排列。

from polars import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        i, j = 0, n - 1  # 从右上角开始
        while i < m and j >= 0:  # 注意这里的等号！！ 当没有越界的时候。（越界，j<0, i>=m）
            if matrix[i][j] == target:
                return True  # 找到 target

            if matrix[i][j] < target:
                i += 1  # 这一行剩余元素全部小于 target，排除。下移一行
            else:
                j -= 1  # 这一列剩余元素全部大于 target，排除。左移一列
        return False