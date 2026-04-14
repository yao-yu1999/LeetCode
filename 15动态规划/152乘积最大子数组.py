# https://leetcode.cn/problems/maximum-product-subarray/?envType=study-plan-v2&envId=top-100-liked
# 题目：给你一个整数数组 nums ，请你找出数组中乘积最大的非空连续 子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
# 测试用例的答案是一个 32-位 整数。“只包含一个元素的数组”的乘积，是这个元素的值。
# 53题是求和版本

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = float('-inf')  # 最终答案，初始化为负无穷（因为可能全负）
        f_max = f_min = 1       # 滚动变量：当前最大/最小乘积
        
        for x in nums: # 遍历每个数字
            # 提前记录新的最大、最小（必须同时算）
            new_max = max(f_max * x, f_min * x, x)
            new_min = min(f_max * x, f_min * x, x)
            # 更新最大、最小值
            f_max, f_min = new_max, new_min
            
            result = max(result, f_max) # 每次更新全局最大答案
        
        return result
    
# 注1:必须同时更新 f_max 和 f_min
# (1) 错误写法：
# f_max = max(...)  # 更新 
# f_min = min(...)  # 用了新 f_max，错！

# (2) 正确写法：
# f_max, f_min = new_max, new_min

# 注2：乘法和加法最大子数组完全不同
# 加法：只维护 max；乘法：必须维护 max + min

# 0 会自动处理
# 遇到 0，f_max、f_min 都会变成 0，然后下一个数重新开始，完全正确。