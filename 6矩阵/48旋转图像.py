# https://leetcode.cn/problems/rotate-image/description/?envType=study-plan-v2&envId=top-100-liked
# 给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。必须在 原地 旋转图像

from polars import List

# 方法一：两次翻转【推荐】
# 先转置再左右翻转
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        
        # 第一步：转置
        for i in range(n):
            for j in range(i):  # 遍历对角线下方元素（0到i-1）：为了只交换上 / 下三角，对角线元素不变
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # 第二步：左右翻转（同一行内，左右对称交换）
        for i in range(n):
            for j in range(n // 2): # 只需要翻转前一半与后一半（n-j-1） 交换
                matrix[i][j], matrix[i][n-j-1] = matrix[i][n-j-1], matrix[i][j]

# 先水平翻转再转置
'''
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # 水平翻转
        for i in range(n // 2):
            for j in range(n):
                matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]
        # 主对角线翻转
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
'''

# 方法二：原地旋转
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n // 2):
            for j in range((n + 1) // 2):
                matrix[i][j], matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1] \
                    = matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1], matrix[i][j]

