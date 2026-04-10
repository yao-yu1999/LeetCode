# https://leetcode.cn/problems/find-all-anagrams-in-a-string/description/?envType=study-plan-v2&envId=top-100-liked
# 题目：给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
from typing import List
from typing import Counter

# 方法1：定长滑动 + 固定窗口 【推荐】
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cnt_p = Counter(p)  # 窗口模板：统计 p 的每种字母的出现次数。p是已知的
        cnt_s = Counter()  # 创建一个空的统计字典：统计 s 当前窗口 t [长为 len(p)] 的每种字母的出现次数
        result = [] # 记录所有符合条件的窗口 t 的左端点下标的列表

        # 遍历 s 的每个字符，右指针 right 从左到右移动
        for right, c in enumerate(s):
            cnt_s[c] += 1  # 1. 右指针开始移动，右端点字母为进入窗口

            left = right - len(p) + 1 # 2. 计算当前窗口左端点下标
            if left < 0:  # 剪枝：窗口长度不足 len(p)
                continue   # 不满足就跳过
            
            # 3. 寻找异位词
            if cnt_s == cnt_p:  # 判断：t 和 p 的每种字母的出现次数都相同，证明 t 是 p 的一个异位词
                result.append(left)  # 将该窗口 t 左端点下标加入列表
            
            cnt_s[s[left]] -= 1  # 4. 左指针开始移动，左端点字母为离开窗口。该字符出现次数需要-1

        return result # 返回所有符合条件的 t 的左端点下标的列表

# 方法2：不定长滑动 + 动态窗口
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cnt = Counter(p)  # 统计 p 的每种字母的出现次数。即当前窗口还 “需要” 多少个字符才能凑成异位词
        result = []

        left = 0
        for right, c in enumerate(s):
            cnt[c] -= 1  # 右端点字母进入窗口
            while cnt[c] < 0:  # # 字母 c 多了，不需要这个字符了。因此窗口不合法
                cnt[s[left]] += 1  # 左端点字母离开窗口
                left += 1
            if right - left + 1 == len(p):  # t 和 p 的每种字母的出现次数都相同（证明见上）
                result.append(left)  # t 左端点下标加入答案

        return result