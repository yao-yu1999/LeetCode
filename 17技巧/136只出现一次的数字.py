# https://leetcode.cn/problems/single-number/?envType=study-plan-v2&envId=top-100-liked
# 题目:给你一个 非空 整数数组 nums ，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
# 你必须设计并实现线性时间复杂度的算法来解决此问题，且该算法只使用常量额外空间。

from typing import List

# 方法: 异或运算
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        x = 0 # 用0来和数组第一个元素异或
        for num in nums:  # 1. 遍历 nums 执行异或运算（二进制数）
            x ^= num      
        return x;         # 2. 返回出现一次的数字 x

#  0001
# ^0011
# ------
#  0010