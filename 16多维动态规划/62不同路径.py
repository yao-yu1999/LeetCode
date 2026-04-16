# https://leetcode.cn/problems/unique-paths/submissions/718121802/?envType=study-plan-v2&envId=top-100-liked
# 题目：机器人位于一个 m x n 网格的左上角 （起始点）。机器人每次只能向下或者向右移动一步。问达到网格的右下角（终点）总共有多少条不同的路径？

# 方法1：一维DP【推荐】
#  单数组滚动: 只需要上一行和当前行的左边部分，所以可以由二维转到一维
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for i in range(1, m): # 从第二行开始（索引 1 到 m-1）
            for j in range(1, n): # 从第二列开始（索引 1 到 n-1），第一列永远为 1
                dp[j] = dp[j] + dp[j-1] # 原来的 dp[j]（从上面来）+  dp[j-1]（从左边来）
        return dp[-1]

    
# 为什么第一行的路径数均为1？
# dp[j] 表示当前正在计算的这一行中，到达第 j 列位置的不同路径数。因此：
# 位置 (0,0)：起点，路径数 = 1（不移动也算一条路径）
# 位置 (0,1)：只能从 (0,0) 向右走。路径：(0,0) → (0,1)，路径数 = 1
# 位置 (0,2)：只能从 (0,1) 向右走。路径：(0,0) → (0,1) → (0,2)，路径数 = 1
# 位置 (0,3)：只能从 (0,2) 向右走。路径：(0,0) → (0,1) → (0,2) → (0,3)，路径数 = 1

# 方法2：二维DP
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]
        for i in range(1, m): # 从第二行开始（索引 1 到 m-1）
            for j in range(1, n): # 从第二列开始（索引 1 到 n-1），第一列永远为 1
                dp[i][j] = dp[i-1][j] + dp[j][j-1] # 原来的 dp[j]（从上面来）+  dp[j-1]（从左边来）
        return dp[-1][-1]