# https://leetcode.cn/problems/find-all-anagrams-in-a-string/description/?envType=study-plan-v2&envId=top-100-liked
from typing import List
from typing import Counter

# 方法1：定长滑动 + 固定窗口
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cnt_p = Counter(p)  # 窗口模板：统计 p 的每种字母的出现次数
        cnt_s = Counter()  # 创建一个空的统计字典：统计 s 当前窗口/子串 t [长为 len(p)] 的每种字母的出现次数
        result = [] # 记录所有符合条件的 t 的左端点下标的列表

        # 遍历 s 的每个字符，右指针 right 从左到右移动
        for right, x in enumerate(s):
            cnt_s[x] += 1  # 1. 右指针开始移动，右端点字母为进入窗口

            left = right - len(p) + 1 # 2. 计算当前窗口左端点下标

            # 3. 两个条件
            if left < 0:  # 判断1：窗口长度不足 len(p)
                continue   # 不满足就跳过
            if cnt_s == cnt_p:  # 判断2：t 和 p 的每种字母的出现次数都相同，证明 t 是 p 的一个异位词
                result.append(left)  # 将该子串 t 左端点下标加入列表

            cnt_s[s[left]] -= 1  # 4. 左指针开始移动，左端点字母为离开窗口

        return result # 返回所有符合条件的 t 的左端点下标的列表

# 方法2：不定长滑动 + 动态窗口（类似题3的方法）
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cnt = Counter(p)  # 统计 p 的每种字母的出现次数
        ans = []

        left = 0
        for right, c in enumerate(s):
            cnt[c] -= 1  # 右端点字母进入窗口
            while cnt[c] < 0:  # 字母 c 太多了
                cnt[s[left]] += 1  # 左端点字母离开窗口
                left += 1
            if right - left + 1 == len(p):  # t 和 p 的每种字母的出现次数都相同（证明见上）
                ans.append(left)  # t 左端点下标加入答案

        return ans