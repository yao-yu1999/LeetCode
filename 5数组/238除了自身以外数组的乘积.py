# https://leetcode.cn/problems/product-of-array-except-self/description/?envType=study-plan-v2&envId=top-100-liked
# 题目：给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除了 nums[i] 之外其余各元素的乘积 。
# 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内。不要使用除法，且在 O(n) 时间复杂度内完成此题

from polars import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)   # 数组长度
        
        # 第一步：构建前缀乘积数组 pre
        pre = [1] * n   # 初始化全1：最左边没有数，乘积默认是1
        for i in range(1, n): # i从1开始：因为i=0左边没数，不用算
            pre[i] = pre[i - 1] * nums[i - 1] # pre[i] = 前一个前缀值 × 当前位置左边第一个数

        # 第二步：构建后缀乘积数组 suf 
        suf = [1] * n   # 初始化全1：最右边没有数，乘积默认是1
        for i in range(n - 2, -1, -1): # 倒着遍历：从倒数第二个走到0
            suf[i] = suf[i + 1] * nums[i + 1] # suf[i] = 后一个后缀值 × 当前位置右边第一个数

        # 第三步：对应位置相乘出答案
        return [p * s for p, s in zip(pre, suf)] # 遍历 zip(pre,suf)：把两个列表按位置一一配对