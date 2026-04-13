# https://leetcode.cn/problems/n-queens/description/?envType=study-plan-v2&envId=top-100-liked
# 题目：按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
# 给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

from typing import List

# 由于皇后不能放在同一行，因此问题简化为当前行的皇后放在第几列？
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        queens = [0] * n  # queens[row] = 第 row 行皇后放在第几列。 (row,queens[row])

        # 三个布尔数组，快速判断是否冲突（O(1)）
        col_bool = [False] * n  # 记录哪些列被占用。初始化每每列都不能放
        diag1 = [False] * (n * 2 - 1)  # 记录左上→右下： row-col 斜线被占用
        diag2 = [False] * (n * 2 - 1)  # 记录右上→左下： row+col 斜线被占用

        # row：当前处理到第几行
        def dfs(row: int) -> None:
            if row == n: # 递归出口：所有行都放完了 → 生成答案
                result.append(['.' * col + 'Q' + '.' * (n - 1 - col) for col in queens])
                return None

            # 否则, 在 (row,col) 放皇后
            for col, ok in enumerate(col_bool):
                if not ok and not diag1[row + col] and not diag2[row - col]:  # 判断能否放皇后:对应列和斜线下标非false
                    queens[row] = col  # 直接在对应位置覆盖，无需恢复现场
                    col_bool[col] = diag1[row + col] = diag2[row - col] = True  # 皇后占用了 col 列和两条斜线
                    dfs(row + 1)
                    col_bool[col] = diag1[row + col] = diag2[row - col] = False  # 但是布尔数组需要恢复现场
        dfs(0)
        return result
    
# 为什么diag1和diag2长度是2n-1?
# 因为棋盘上同一方向最多只有 2n-1 条不同的斜线（也包含自己，如值1，3，7，9）。条数 = 1 + 2 + … + n + … + 2 + 1 = 2n -1
# 行\列  0   1   2
# 0     [1,  2,  3]
# 1     [4,  5,  6]
# 2     [7,  8,  9]

# "右上 ←→ 左下"方向，同一斜线上的格子，row + col 相等；"左上 ←→ 右下"方向，同一斜线上的格子，row - col 相等