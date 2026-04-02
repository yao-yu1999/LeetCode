# https://leetcode.cn/problems/set-matrix-zeroes/description/?envType=study-plan-v2&envId=top-100-liked

from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0]) # 获取矩阵的行数和列数

        # 保存状态：记录第一行、第一列有没有0
        first_row_has_zero = 0 in matrix[0] 
        first_col_has_zero = any(row[0] == 0 for row in matrix)

        # 第一次遍历：用第一行、第一列做标记
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0   # 标记第j列有0

        # 第二次遍历：根据第一行第一列的标记置0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # 最后处理第一列、第一行
        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0 # 假如第一行有0，（遍历每一列）把第一行全置0

        if first_col_has_zero:
            for i in range(m):
                matrix[i][0] = 0  # 假如第一列有0，（遍历每一行）把第一列全置0
        
        