# https://leetcode.cn/problems/edit-distance/?envType=study-plan-v2&envId=top-100-liked
# 题目：给你两个单词 word1 和 word2， 请返回将 word1 转换成 word2 所使用的最少操作数  。
# 你可以对一个单词进行三种操作：插入一个字符；删除一个字符；替换一个字符。

# 和1143题类似
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for j in range(n+1): # 初始化第一行（一次）：表示空串变成 j 个字符，只能一个个插进去，需要 j 步。
            dp[0][j] = j

        for i, x in enumerate(word1):
            dp[i+1][0] = i + 1  # 第一列：遍历每行的时候设置一次。
            for j, y in enumerate(word2):
                if x == y: # 字符相等，不做操作，直接继承（回退）。即最少步数 = word1 前 i 个 → word2 前 j 个
                    dp[i+1][j+1] = dp[i][j]
                else: # 字符不等，可以操作：3种操作取最小 +1
                    dp[i+1][j+1] = min(
                        dp[i][j+1],      # 从上面来的，word2长度不变，但此时word1多了一个字符，需要删除 word1[i]
                        dp[i+1][j],      # 从左边来的，此时word2多了一个字符，因此word1也要插入一个字符补上。
                        dp[i][j]) + 1    # 替换
                    
        return dp[m][n]

#           j=0   j=1(h)   j=2(o)   j=3(s)  ←  word2
#         ------------------------------------
# i=0     |  0      1        2        3
# i=1(r)  |  1      ?        ?        ?
# i=2(o)  |  2      ?        ?        ?
# i=3(s)  |  3      ?        ?        ?
#  ↑
# word1（竖着）

# dp[1][1] = min(
#     dp[i][j+1]   = dp[0][1] = 1   # 上：删除 r
#     dp[i+1][j]   = dp[1][0] = 1   # 左：插入 h
#     dp[i][j]     = dp[0][0] = 0   # 左上：替换 r→h
# ) + 1 (本次操作计数)


# dp[i][j]= 把 word1 前 i 个字符 → word2 前 j 个字符的最少操作次数
# 初始条件：dp[0][j] = j：空串，插 j 次 → 长度 j
#          dp[i][0] = i：长度 i，删 i 次 → 空串

# 多一行多一列：空串变成 j 个字符,空串变成 i 个字符

# 易错点:
# dp [i+1][j+1] 时，依赖三个方向:
# 左：dp[i+1][j],不是说往左就是撤回一个word2的字符!
# 上：dp[i][j+1],
# 左上：dp[i][j] (字符相等时直接继承,不等时,直接替换)