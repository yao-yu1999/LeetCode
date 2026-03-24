# https://leetcode.cn/problems/word-break/description/?envType=study-plan-v2&envId=top-100-liked


from polars import List

# 完全背包问题：容量正序遍历
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n= len(s) # 计算所给字符串的长度
        max_len = max(map(len, wordDict)) # 求出字典中最长的单词长度
        words = set(wordDict) # 把字典转换成集合，将查询速度由O(n)->O(1)
        
        f = [True] + [False]*n # 创建dp数组，初始化条件f[0]=True, 因为空字符串一定可以拼成;其他默认为False

        # 遍历:i是背包容量，判断前i个字符能不能拼成
        for i in range(1, n + 1):
            # 判断前i个字符是否由字典里的单词拼成了
            for j in range(i - 1, max(i - max_len - 1, -1), -1):
                if f[j] and s[j:i] in words: # 即f[j] == True，前j个字符能拼成；s[j:i] in words, j到i这一段是字典里的单词
                    f[i] = True # 满足条件，当前设置为True
                    break
        return f[n]


        