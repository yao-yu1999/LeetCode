# https://leetcode.cn/problems/longest-consecutive-sequence/description/?envType=study-plan-v2&envId=top-100-liked
# 要点：哈希表 + 贪心

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums)  # 把 nums 转成哈希集合，去重 + O(1)查找
        ans = 0 # 记录最长长度
        for x in st:  # 遍历哈希集合
            if x - 1 in st:  # 如果 x-1 存在 → x 不是起点，跳过
                continue

            y = x + 1 # 走到这里，说明 x 是一段连续序列的起点
            while y in st:  # 不断查找下一个数是否在哈希集合中：一直找 x+1, x+2... 直到找不到
                y += 1
            # 循环结束后，y-1 是最后一个在哈希集合中的数
            ans = max(ans, y - x)  # 更新到目前位置的最长长度：从 x 到 y-1 一共 y-x 个数
        return ans