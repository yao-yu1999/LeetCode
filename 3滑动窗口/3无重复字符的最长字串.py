# https://leetcode.cn/problems/longest-substring-without-repeating-characters/solutions/?envType=study-plan-v2&envId=top-100-liked
# 题目：给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。

from collections import defaultdict

# 方法1：哈希表 + 动态窗口（整型数组：记录字符上次出现的位置）【推荐】
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0 # 记录最长子串的长度
        cnt = defaultdict(int)  # 记录从下标 left 到下标 right 的字符及其出现次数。默认创建一个值为int类型

        left = 0  # 窗口左边界
        for right, x in enumerate(s): # 窗口右边界: 右指针遍历字符串s下标和元素
            cnt[x] += 1 # 对应字符的次数+1
            while cnt[x] > 1:  # 窗口内有重复字母
                cnt[s[left]] -= 1  # 必须先将窗口左端字母计数-1 （如先移，left指向的字符就错位了）  
                left += 1  # 再左端右移，缩小窗口
            
            # 没有发现重复字母的话，更新窗口最大长度  
            max_len = max(max_len, right - left + 1)  # 更新窗口长度最大值
        return max_len
    
    
# 方法2：哈希集合（布尔数组）
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        window = set()  # 记录从下标 left 到下标 right 的字符

        left = 0
        for right, x in enumerate(s):
            while x in window:  # 在加入右侧进来的字符x前，先检查窗口内是否有 x
                window.remove(s[left]) # 有的话从窗口左端移除，为了让窗口继续移动，直到没有发现重复的字符。而不是当前这一次新加入和左端字符就一致的意思
                left += 1  # 缩小窗口
            window.add(x)  # 加入 x

            # 持续移动窗口，直到没有重复字符
            max_len = max(max_len, right - left + 1)  # 更新窗口长度最大值
        return max_len
    

