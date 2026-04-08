# https://leetcode.cn/problems/word-search/submissions/715853699/?envType=study-plan-v2&envId=top-100-liked

from collections import Counter
from polars import List

# （1）递归层判断
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        cnt = Counter(c for row in board for c in row) # 统计二维网格中所有字母c出现次数：外层 for row in board，内层 for c in row 
        
        # 优化1：如果 "网格里的格子数量 >= 单词里的字母数量" 不成立 → 直接False
        if not cnt >= Counter(word): # 两个计数器，逐键(即字母)比较计数(对应的数量的大小)
            return False
        
        # 优化2：如果单词末尾字母更少 → 反转单词 → 减少搜索量（既可以正着搜也可以反着搜，选择递归次数更少的哪个即可）
        if cnt[word[-1]] < cnt[word[0]]: # 单词最后一个字母在网格里出现的次数 2 < 单词第一个字母在网格里出现的次数 20。正着搜要递归20次。
            word = word[::-1]

        m = len(board)    # 网格行数
        n = len(board[0]) # 网格列数
        # 当前位置(i,j)正在匹配第K个字母（字符）
        def dfs(i: int, j: int, k: int) -> bool: 
            if board[i][j] != word[k]: # 终止条件：当前字母不匹配 → 失败
                return False
             
            if k == len(word) - 1: # 已经匹配到最后一位 → 成功
                return True
            board[i][j] = ''  # 标记：用清空网格的格子内的字符，标记当前格子已走过（防止重复走）
            
            # 开始枚举下一步。枚举四个可以走的方向：左、右、上、下
            for x, y in [(i, j-1), (i, j+1), (i-1, j), (i+1, j)]: # 等价于for (x, y) in [(i, j-1), (i, j+1), (i-1, j), (i+1, j)]， pyhton的自动解包
                if 0 <= x < m and 0 <= y < n and dfs(x, y, k + 1): # (1)不越界:下一步移动的位置不超过网格边界范围，(2) 递归的下一个字母匹配成功 。注意：k的增加必须在下一层，否则会混乱
                    return True

            board[i][j] = word[k] # 回溯：恢复当前格子
            return False # 在这个格子的四个方向全都走完了也没找到正确路径 → 这条路径是失败的 → 告诉上一层：这里不行，换别的路 return False

        # 遍历每个格子作为起点，只要有一个起点成功就返回True
        # return any(dfs(i, j, 0) for i in range(m) for j in range(n)) 等价于：
        # for i in range(m):
        #     for j in range(n):
        #         if dfs(i, j, 0) is True:
        #             return True
        # return False
        return any(dfs(i, j, 0) for i in range(m) for j in range(n)) # 里面只要有一个是 True，整体就返回 True；全部都是 False，才返回 False
    
# （2）当前层判断
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        cnt = Counter(c for row in board for c in row) # 统计二维网格中所有字母c出现次数：外层 for row in board，内层 for c in row 
        
        # 优化1：如果 "网格里的格子数量 >= 单词里的字母数量" 不成立 → 直接False
        if not cnt >= Counter(word): # 两个计数器，逐键(即字母)比较计数(对应的数量的大小)
            return False
        
        # 优化2：如果单词末尾字母更少 → 反转单词 → 减少搜索量（既可以正着搜也可以反着搜，选择递归次数更少的哪个即可）
        if cnt[word[-1]] < cnt[word[0]]: # 单词最后一个字母在网格里出现的次数 2 < 单词第一个字母在网格里出现的次数 20。正着搜要递归20次。
            word = word[::-1]

        m = len(board)    # 网格行数
        n = len(board[0]) # 网格列数

        def dfs(i: int, j: int, k: int) -> bool:
            if i < 0 or i >= m or j < 0 or j >= n: # 终止条件1：先判断：越界 / 不满足条件 → 直接 return False
                return False
    
            if board[i][j] != word[k]:  # 终止条件2：字符不匹配 → 退出
                return False

            if k == len(word) - 1: # 已经匹配到最后一位 → 成功
                return True
            board[i][j] = '' # 标记已访问

            # 递归四个方向
            isExisted = dfs(i+1, j, k+1) or dfs(i-1, j, k+1) or dfs(i, j+1, k+1) or dfs(i, j-1, k+1) # 四个方向，必须先用变量保存，然后回溯。不能直接return
            board[i][j] = word[k] # 回溯

            return isExisted

        # 遍历所有起点
        return any(dfs(i, j, 0) for i in range(m) for j in range(n)) # 里面只要有一个是 True，整体就返回 True；全部都是 False，才返回 False
