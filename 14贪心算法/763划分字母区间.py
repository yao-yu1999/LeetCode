# https://leetcode.cn/problems/partition-labels/description/?envType=study-plan-v2&envId=top-100-liked
# 题目：给你一个字符串 s 。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。
# 例如，字符串 "ababcc" 能够被分为 ["abab", "cc"]，但类似 ["aba", "bcc"] 或 ["ab", "ab", "cc"] 的划分是非法的。

from polars import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {c: i for i, c in enumerate(s)}  # 创建字典：记录每个字母及其最后出现的下标
        start = end = 0 # 当前片段的起始位置

        result = []
        for i, c in enumerate(s): # 遍历字符串的下标和元素
            end = max(end, last[c])  # 扩大区间边界：更新当前区间右端点的最大值为该字符c必须所在的区间
            if i == end:  # 当 i 走到了 end，说明同一个字符的所有字母都已经被包在里面了
                result.append(end - start + 1)  # 计算片段的区间长度，加入答案
                start = end + 1  # 更新：下一个片段的左端点 = 当前片段的终点+1
        return result
    
# i在一步一步走，end则是不断扩到字符的最后一次出现的下标