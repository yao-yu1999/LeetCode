# https://leetcode.cn/problems/range-sum-query-immutable/description/
# 【模板题】

from polars import List

class NumArray:
    def __init__(self, nums: List[int]):  # __init__ 在创建对象时自动执行，保证了前缀和只计算一次。
        s = [0] * (len(nums)+1) # 初始化前缀和数组
        for i ,x in enumerate(nums): # 遍历原数组nums的下标和元素
            s[i+1] = s[i] + x  # 计算前缀和，x即nums[i]
        self.s = s # 将计算好的前缀和数组 s 保存为实例的属性，这样在同一个对象的其他方法如 sumRange中，就可以通过self.s 访问到它

    def sumRange(self, left: int, right: int) -> int:
        sums = self.s[right+1] - self.s[left] # 计算区间和，时间复杂度仅O（1）
        return sums