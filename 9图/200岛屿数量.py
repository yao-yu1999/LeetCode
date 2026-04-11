# https://leetcode.cn/problems/number-of-islands/description/?envType=study-plan-v2&envId=top-100-liked
# 题目：给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
# 此外，你可以假设该网格的四条边均被水包围。

from polars import List

# 方法1：DFS 
# （1）当前层判断版本【推荐】
# 本题：当前层可能不安全，必须立刻检查。进入 dfs (i,j) → 可能越界、可能是水、可能无效。
# 79题单词搜索：当前层一定安全，只检查下一步。进入 dfs (i,j,k) → 一定安全、不越界、是有效格子所以不需要在当前层判断越界。
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        # 表示从坐标 (i, j) 这块陆地开始，把所有相连的整块岛屿全部淹成 0，直到把这座岛所有陆地全部淹完
        def dfs(i: int, j: int) -> None:
            # 当前层一进来就判断是否合法，防止无效递归
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0': # 出界，或者格子是水，退出递归
                return None
            grid[i][j] = '0'  # 先将当前格子给淹掉，防止重复访问之前访问过的格子

            # 以当前格子的四个方向分别去递归淹岛
            dfs(i, j - 1)  # 往左走
            dfs(i, j + 1)  # 往右走
            dfs(i - 1, j)  # 往上走
            dfs(i + 1, j)  # 往下走
        
        # 主函数体
        result = 0 # 岛屿数量
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1': # 发现新岛屿，没有新岛屿的时候遍历下一个位置
                    dfs(i, j)         # 标记：递归淹掉整座岛
                    result += 1       # 岛屿数 +1
        
        return result
    
# （2）下一层判断版本
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def dfs(i: int, j: int) -> None:
            # 当前层 (i,j) 一定是合法、不越界、等于 '1' 的。所以进来不用判断越界
            grid[i][j] = '0'  # 淹掉

            # 上下左右，都先判断越界 + 是否是 '1'，再递归
            # 左
            if j-1 >= 0 and grid[i][j-1] == '1':
                dfs(i, j-1)
            # 右
            if j+1 < n and grid[i][j+1] == '1':
                dfs(i, j+1)
            # 上
            if i-1 >= 0 and grid[i-1][j] == '1':
                dfs(i-1, j)
            # 下
            if i+1 < m and grid[i+1][j] == '1':
                dfs(i+1, j)

        # 主函数体
        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    result += 1
        return result
    
# 方法2：BFS
class Solution:
    def numIslands(self, grid: [[str]]) -> int:
        def bfs(i, j) -> None:
            queue = [[i, j]]
            while queue:
                [i, j] = queue.pop(0)
                if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1':
                    grid[i][j] = '0'
                    queue += [[i + 1, j], [i - 1, j], [i, j - 1], [i, j + 1]]
        
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '0': 
                    continue
                bfs(i, j)
                result += 1

        return result