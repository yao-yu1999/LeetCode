# https://leetcode.cn/problems/longest-palindromic-substring/description/?envType=study-plan-v2&envId=top-100-liked
# 题目：给你一个字符串 s，找到 s 中最长的 回文 子串。

# 方法1：中心扩展法【推荐】
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res_left = res_right = 0   # 初始化最长回文子串的左右边界：左右闭区间 [res_left, res_right]

        for i in range(2 * n - 1): # 枚举 2n-1 个可能的回文中心
            l, r = i // 2, (i + 1) // 2 # 当 i 是偶数 → l = r → 奇数回文中心。当 i 是奇数 → r = l+1 → 偶数回文中心
            while l >= 0 and r < n and s[l] == s[r]: # 如果i没有越界且左边和右边的字符均匹配，就继续向左或向右扩展
                l -= 1
                r += 1
            
            # 循环结束：l和r需要往回缩。因此，最后合法回文是 s[l+1] 到 s[r-1] （闭区间）
            cur_left = l + 1
            cur_right = r - 1
            
            # 更新长度：闭区间长度 = right - left + 1
            if cur_right - cur_left + 1 > res_right - res_left + 1:
                res_left, res_right= cur_left, cur_right

        return s[res_left : res_right + 1]  # 切片是 [左闭, 右开)，所以要 +1


# 注1：回文中心有多少种情况？
# 奇数回文中心：有 n 个（每个字符自己）；偶数回文中心：有 n-1 个（每两个字符之间）。共计n+n-1 = 2n-1个

# 注2：如何统一奇数回文和偶数回文？
# l = r → 同一个字符 → 奇数回文;  r = l + 1 → 是相邻两个字符 → 偶数回文
#     aba  l=r="b"                     cbba l="b", r=l+1="b"



# 方法2： 区间DP
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        # 考虑不进入循环的情况（即n==1），因此初始值设置为1和s[0]，而不是-inf和“”
        max_len = 1
        result = s[0]

        # dp[i][j]表示字符i-j(包括)，即s[i:j+1]，是否是回文
        # 隐含条件：i <= j
        dp = [[False] * n for _ in range(n) ]
        for i in range(n-1, -1, -1):
            dp[i][i] = True
            for j in range(i+1, n): 
                # j-i<=2 是为了保证一个字符或者两个字符情况下，不再访问dp[i+1][j-1]（否则会超界）
                if (s[i] == s[j]) and (j - i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if j-i+1 > max_len:
                        max_len = j-i+1
                        result = s[i:j+1]
        return result
