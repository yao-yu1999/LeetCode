# https://leetcode.cn/problems/merge-intervals/description/?envType=study-plan-v2&envId=top-100-liked
# 题目：以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda inter: inter[0])  # 遍历每个区间 inter，把所有区间 按照每个区间的第一个数 inter[0] 从小到大排序。
        result = [] # 合并结果

        for inter in intervals: # 遍历排序后的区间列表
            if result and inter[0] <= result[-1][1]:  # # 可以合并：相交或相连。如果当前区间 inter 的左端点不大于 result 中最后一个区间的右端点，说明它们相交，可以合并
                result[-1][1] = max(result[-1][1], inter[1])   # 更新 result 中最后一个区间的右端点为它们的右端点的较大值
            else:  # 不相交，无法合并
                result.append(inter)  # 将当前区间 inter 添加到 result 中
        return result