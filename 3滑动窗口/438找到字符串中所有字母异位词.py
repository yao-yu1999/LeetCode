# https://leetcode.cn/problems/find-all-anagrams-in-a-string/description/?envType=study-plan-v2&envId=top-100-liked
# 题目：给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
from typing import List
from typing import Counter

# 方法1：动态窗口1 【推荐】
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cnt_p = Counter(p)  # 窗口模板：统计 p 的每种字母的出现次数。p是已知的
        cnt_s = Counter()  # 创建一个空的统计字典：统计 s 当前窗口 t [长为 len(p)] 的每种字母的出现次数
        result = [] # 记录所有符合条件的窗口t的起始索引的列表

        # 遍历 s 的每个字符，右指针 right 从左到右移动
        left = 0
        for right, x in enumerate(s):
            cnt_s[x] += 1  # 右边进入窗口
            
            if right - left + 1 > len(p): # 窗口过大时，左边收缩
                cnt_s[s[left]] -= 1
                # if cnt_s[s[left]] == 0:
                #     del cnt_s[s[left]]  # 清理0值，保证比较的正确。但Counter可以自动忽略值为 0 的键。所以后面直接比较也没问题
                left += 1
            
            # 窗口长度满足或收缩后满足：窗口长度正好等于 len(p) 时，检查是否是异位词
            if right - left + 1 == len(p) and cnt_s == cnt_p:
                result.append(left)

        return result # 返回所有符合条件的 t 的左端点下标的列表
    
# 注1：窗口过大，cnt_s 可能和 cnt_p 一致。因为cnt_s中的字符会多一些；但是窗口不足len(p)，一定不会cnt_p == cnt_s
# 注2：必须用两个if语句，而不是if...else.. 否则会忽略窗口收缩后，明明长度正好等于 len (p)的情况

# 注3：本题如果用 defaultdict：要自己删 0键。如下：
# if cnt_s[s[left]] == 0:
#     del cnt_s[s[left]]
# 但Counter会自动忽略0的值。



# 方法2：动态窗口2 + 差值
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cnt = Counter(p)  # 统计 p 的每种字母的出现次数。即当前窗口还 “需要” 多少个字符才能凑成异位词
        result = []

        left = 0
        for right, x in enumerate(s):
            cnt[x] -= 1  # 右端点字母进入窗口
            while cnt[x] < 0:  # # 字母 c 多了，不需要这个字符了。因此窗口不合法
                cnt[s[left]] += 1  # 左端点字母离开窗口
                left += 1
            if right - left + 1 == len(p):  # t 和 p 的每种字母的出现次数都相同（证明见上）
                result.append(left)  # t 左端点下标加入答案

        return result