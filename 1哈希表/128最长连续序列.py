# https://leetcode.cn/problems/longest-consecutive-sequence/description/?envType=study-plan-v2&envId=top-100-liked
# 题目：给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。设计并实现时间复杂度为 O(n) 的算法解决此问题。
# 输入：nums = [100,4,200,1,3,2]，输出：4。解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
# 要点：哈希表 + 贪心
# 思路：对于 nums 中的元素 x，以 x 为起点，不断查找下一个数 x+1,x+2,⋯ 是否在 nums 中，并统计序列的长度。

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums)  # 把 nums 中的数都放入哈希集合，去重 + O(1)查找数字
        result = 0 # 记录数字连续的最长序列的长度
        for x in st:  # 遍历哈希集合，不是遍历数组！！
            if x - 1 in st:  # 如果 x-1 存在 → x 不是序列起点，跳过
                continue

            y = x + 1 # 走到这里，说明 x 是一段连续序列的起点。
            while y in st:  # 不断查找下一个数是否在哈希集合中：一直找 x+1, x+2... 直到找不到
                y += 1
            
            # 循环结束后，y-1 是最后一个在哈希集合中的数
            result = max(result, y - x)  # 更新到目前位置的最长长度：从 x 到 y-1 一共 y-x 个数
        return result
    
# 注：本题是不能排序的，因为排序的时间复杂度是 O(nlogn)，不符合题目 O(n) 的要求。