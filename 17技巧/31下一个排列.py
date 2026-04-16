# https://leetcode.cn/problems/next-permutation/?envType=study-plan-v2&envId=top-100-liked
# 题目:整数数组的一个 排列  就是将其所有成员以序列或线性顺序排列。
# 例如，arr = [1,2,3] ， arr 的排列：[1,2,3]、[1,3,2]、[2,1,3]、[2,3,1]、[3,1,2]、[3,2,1] 。
# 整数数组的 下一个排列 是指其整数的下一个字典序更大的排列。
# 如果数组的所有排列根据其字典顺序从小到大排列在一个容器中，那么数组的 下一个排列 就是在这个有序容器中排在它后面的那个排列。
# 如果不存在下一个更大的排列，那么这个数组必须重排为字典序最小的排列（即，其元素按升序排列）。

from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)

        # 第一步：从右向左找到第一个小于右侧相邻数字的数 nums[i]
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1 # 继续向左找

        # 如果找到了，进入第二步:从右向左找到 nums[i] 右边最小的大于 nums[i] 的数 nums[j]
        if i >= 0: # 写在循环外面,不要写在while里.否则每次都要检查一遍,但实际i不会变
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            
            nums[i], nums[j] = nums[j], nums[i] # 交换 nums[i] 和 nums[j]

        # 第三步：反转 nums[i+1:]（如果上面跳过第二步，说明 i = -1）
        # nums[i+1:] = nums[i+1:][::-1] 这样写也可以，但空间复杂度不是 O(1) 的
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1