# https://leetcode.cn/problems/longest-substring-without-repeating-characters/solutions/?envType=study-plan-v2&envId=top-100-liked
from collections import defaultdict

# 方法1：哈希表 + 动态窗口（整型数组：记录字符上次出现的位置）
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0 # 记录最长子串的长度
        left = 0  # 窗口左边界
        cnt = defaultdict(int)  # 记录从下标 left 到下标 right 的字符及其出现次数
        for right, x in enumerate(s): # 窗口右边界，右指针遍历字符串s
            cnt[x] += 1
            while cnt[x] > 1:  # 窗口内有重复字母
                cnt[s[left]] -= 1  # 移除窗口左端点字母
                left += 1  # 缩小窗口
            max_len = max(max_len, right - left + 1)  # 更新窗口长度最大值
        return max_len
    
# 方法2：哈希集合（布尔数组）
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        left = 0
        window = set()  # 记录从下标 left 到下标 right 的字符
        
        for right, x in enumerate(s):
            # 如果窗口内已经包含 x，那么再加入一个 x 会导致窗口内有重复元素
            # 所以要在加入 x 之前，先移出窗口内的 x
            while x in window:  # 窗口内有 x
                window.remove(s[left])
                left += 1  # 缩小窗口
            window.add(x)  # 加入 x
            max_len = max(max_len, right - left + 1)  # 更新窗口长度最大值
        return max_len
    

