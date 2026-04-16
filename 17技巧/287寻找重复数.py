# https://leetcode.cn/problems/find-the-duplicate-number/?envType=study-plan-v2&envId=top-100-liked
# 题目:给定一个包含 n + 1 个整数的数组 nums ，其数字都在 [1, n] 范围内（包括 1 和 n），可知至少存在一个重复的整数。
# 假设 nums 只有 一个重复的整数 ，返回 这个重复的数 。必须 不修改 数组 nums 且只用常量级 O(1) 的额外空间。

from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0

        while True:  # do while结构
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:  # 先跑，再判断。否则一开始就判断，会死循环（一开始fast和slow就是相等的）
                break
        
        head = 0
        while slow != head: # 因为一开始就不相等，所以可以先判断
            head = nums[head]
            slow = nums[slow]
        return slow