# https://leetcode.cn/problems/minimum-path-sum/description/?envType=study-plan-v2&envId=top-100-liked
# 题目：给定一个包含非负整数的 m x n 网格，找出一条从左上角到右下角的路径，使路径上数字总和最小。每次只能向下或者向右移动一步。

from typing import List
from math import inf

# 方法1：一维DP。偏移+1和inf巧妙处理边界【推荐】
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [inf] * (len(grid[0]) + 1)  # dp[0] 哨兵：虚拟的左侧边界。多开一位，防止越界。
        dp[1] = 0                        # 起点“虚拟位”，让第一个数能正确计算
        
        for row in grid:                 # 遍历每一行
            for j, x in enumerate(row):  # 遍历当前行每一列
                dp[j + 1] = min(dp[j + 1], dp[j]) + x  # 从上和左边来的路径和。由于偏移一位，不用单独初始化第一行、第一列
        
        return dp[-1]                    # 最后一个就是答案

# dp[j] 的含义：到达 当前行、第 j 列 的最小路径和。列号从1开始，对应网格的下标0
# 为什么是dp[j+1]?
# 按照 dp[j] = min(dp[j-1], dp[j]) + x，当j=0时，dp[j-1]=dp[-1]，下标越界。

# 为什么初始化为全部是inf？
# 表示不可达，min自动处理边界

# 函数没有传n，这里用len(grid[0])

# 方法2：二维DP
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        # 1. 创建二维dp数组
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = grid[0][0]
        
        # 2. 初始化第一行
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        
        # 3. 初始化第一列
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        
        # 4. 核心DP
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        
        return dp[-1][-1]