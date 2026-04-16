# https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/description/
# 题目：给你一个下标从 1 开始的整数数组 numbers ，该数组已按 非递减顺序排列  ，从数组中找出满足相加之和等于目标数 target 的两个数。
# 如果设这两个数分别是 numbers[index1] 和 numbers[index2] ，则 1 <= index1 < index2 <= numbers.length 。
# 以长度为 2 的整数数组 [index1, index2] 的形式返回这两个整数的下标 index1 和 index2。
# 可以假设每个输入 只对应唯一的答案 ，而且你 不可以 重复使用相同的元素。解决方案必须只使用常量级的额外空间

# 注意：这里下标是从1开始的，而不是从0开始的。但是我们依旧按照从0开始的方式来处理，最后返回结果时再加1即可。

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right: # 题目保证有 ：while True:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                return [left +1, right+1]  # 按照题目要求，下标从1开始，所以返回时需要加1。正常情况下，如果题目没有做要求，就直接返回[left, right]