# https://leetcode.cn/problems/merge-intervals/description/?envType=study-plan-v2&envId=top-100-liked
from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda p: p[0])  # 按照区间左端点升序排序
        result = []

        for p in intervals: # 遍历排序后的区间列表
            if result and p[0] <= result[-1][1]:  # 如果当前区间 p 的左端点不大于 result 中最后一个区间的右端点，说明它们相交，可以合并
                result[-1][1] = max(result[-1][1], p[1])  
            else:  # 不相交，无法合并
                result.append(p)  # 新的合并区间
        return result