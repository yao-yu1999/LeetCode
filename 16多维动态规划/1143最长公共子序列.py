# https://leetcode.cn/problems/longest-common-subsequence/description/?envType=study-plan-v2&envId=top-100-liked
# 题目：给定两个字符串 text1 和 text2，返回这两个字符串的最长公共子序列的长度(LCS)。如果不存在 公共子序列 ，返回 0 。
# 一个字符串的 子序列 是指：可以删字符，但不能改变顺序（也可以不删除任何字符）后组成的新字符串。
# 例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。

# 参考300题

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)] # 多一行一列，表示dp[0][*] = dp[*][0] = 0（空串的LCS为0）。
        
        for i, x in enumerate(text1):      # 遍历text1的每个字符
            for j, y in enumerate(text2):  # 遍历text2的每个字符
                if x == y: # 字符相等
                    dp[i + 1][j + 1] = dp[i][j] + 1  # 可以加入LCS
                else: # 字符不等
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])  # 取较大值（往上看：舍去text1[i]。往左看，舍去text2[j]）
        
        return dp[m][n] # dp[-1][-1]
    
# DP状态定义：text1 的前 i 个字符 和 text2 的前 j 个字符 的最长公共子序列长度.
# dp[i][j] = text1[0:i] 和 text2[0:j] 的最长公共子序列长度

# dp[0][j]：text1 为空串, text2 的前 j 个字符 → LCS = 0
# dp[i][0]：text2 为空串, text1 的前 i 个字符 → LCS = 0
# 所以第 0 行、第 0 列全部初始化为 0

# dp数组行数为m+1，列数为n+1。每行表示text1, 每列表示t