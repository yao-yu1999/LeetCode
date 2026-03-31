# https://leetcode.cn/problems/move-zeroes/description/?envType=study-plan-v2&envId=top-100-liked
# 使用双指针，用j标记下一个非零位置，遍历数组时将非0元素与j位置元素交换，最终所有剩余位自动补0。

from polars import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i]!=0: # 当前元素!=0，就把其交换到左边，等于0的交换到右边
                nums[i], nums[j] = nums[j], nums[i] # python同时赋值，不需要临时变量。先把 nums[j] 的值保存到临时变量，再把 nums[i] 的值赋给 nums[j]，最后把临时变量的值赋给 nums[i]。这样就完成了交换。
                j += 1

# 错误示例：
# nums[i] = nums[j]   # 第一步
# nums[j] = nums[i]  # 第二步

# 第二步，这时 nums[i] 已经被修改了，所以 nums[j] = nums[i] 实际上是把修改后的 nums[i] 的值赋给 nums[j]，而不是原来的 nums[i] 的值。这就是为什么需要使用临时变量来保存原来的 nums[j] 的值，以便在第二步中正确地将其赋给 nums[i]。