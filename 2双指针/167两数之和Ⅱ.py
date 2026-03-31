# https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/description/
# 与3不同的是，这里要求的是有序数组。
# 注意：这里下标是从1开始的，而不是从0开始的。但是我们依旧按照从0开始的方式来处理，最后返回结果时再加1即可。

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while True:
            if numbers[left] + numbers[right] > target:
                right = right -1
            elif numbers[left] + numbers[right] < target:
                left = left +1
            else:
                return [left +1, right+1]  # 按照题目要求，下标从1开始，所以返回时需要加1。正常情况下，如果题目没有做要求，就直接返回[left, right]