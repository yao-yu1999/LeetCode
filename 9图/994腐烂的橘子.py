# https://leetcode.cn/problems/rotting-oranges/description/?envType=study-plan-v2&envId=top-100-liked
# 题目：在给定的 m x n 网格 grid 中，每个单元格可以有以下三个值之一：值 0 代表空单元格；值 1 代表新鲜橘子；值 2 代表腐烂的橘子。
# 每分钟，腐烂的橘子周围 4 个方向上相邻的新鲜橘子都会腐烂。返回直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1 。

from polars import List
from collections import deque

# 方法：BFS + 队列
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        fresh = 0 # 记录新鲜橘子的个数
        queue_rotting = deque([]) # 腐烂橘子队列：记录一开始就是烂橘子和被感染为腐烂橘子的下标
        
        # 第一步：统计。遍历整个网格，统计新鲜橘子个数，并将一开始就腐烂橘子加入队列
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1  # 新鲜橘子个数
                elif grid[i][j] == 2:
                    queue_rotting.append((i, j))  # 一开始就腐烂的橘子
        
        # 第二步：BFS开始同时腐烂
        def bfs():
            dirs = [(-1,0),(1,0),(0,-1),(0,1)] # 方向数组
            nonlocal fresh # 声明：使用外层的新鲜橘子数量
            result = 0 # 记录全部腐烂需要的时间
            while queue_rotting and fresh: # 如果队列里还有烂橘子且还有新鲜橘子没有腐烂
                result += 1  # 每进一层 = 过了一分钟
                for _ in range(len(queue_rotting)):  # 遍历当前所有烂橘子，让它们同时扩散
                    x, y = queue_rotting.popleft() # 弹出队列中的烂橘子
                    for dx, dy in dirs:  # 以该橘子为源头，四个方向同时开始腐烂
                        nx, ny = x + dx, y + dy # 计算上下左右新坐标 (nx, ny)
                        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:  # 不越界 且 是新鲜橘子
                            grid[nx][ny] = 2      # 当前变成烂橘子
                            fresh -= 1          # 新鲜橘子-1
                            queue_rotting.append((nx, ny))    # 加入下一层队列，下一分钟继续腐烂
            return result if fresh==0 else -1 # 第三步：全部烂完，返回时间，否则为还有新鲜橘子，返回-1
        
        return bfs()
    
# 有一种情况是-1。左下角的橘子（第 2 行， 第 0 列）永远不会腐烂，因为他的上方和下方有隔离带。而腐烂只会发生在 4 个方向上，不会是斜方向。        
# grid = [[2,1,1],
#         [0,1,1],
#         [1,0,1]]

# 为什么 不能用 DFS？
# 答：因为 DFS 是一条路走到黑，它会先往一个方向烂到底，再回头烂另一个方向，时间是乱的，根本算不出 “第几分钟烂了谁”。
# 本题要求所有烂橘子同时扩散 → 每分钟烂一圈，所以只能使用BFS。求“最少几分钟”、“最短几步”的都用BFS

# 为什么不能用54题那种方向数组的di索引来确定腐烂方向？
# 螺旋矩阵：需要一个方向索引 di 来记住当前方向，并循环切换。方向索引 di 适用于单一路径、需要根据当前状态决定下一个方向。（单一路径，按固定顺序转向）
# 本题：每个烂橘子同时向四个方向扩散，所有方向平等且同时进行。如果使用di，同一分钟就无法感染其他橘子了。（对每个节点，遍历所有四个方向）