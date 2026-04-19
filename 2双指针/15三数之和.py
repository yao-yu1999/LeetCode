# https://leetcode.cn/problems/3sum/description/?envType=study-plan-v2&envId=top-100-liked
# 题目：给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。
# 也使用双指针，注意一开始先对数组排序，然后三个数要去重

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = [] # 返回的是一个二维数组
        nums.sort() # 先对待查询数组进行排序

        for i in range(len(nums)): # （1）用一个指针i固定第一个数
            if nums[i] > 0: # 剪枝：第一个数就大于0，说明后面的数都大于0，三数之和就不可能大于0
                return result 
            
            # 去重1：如果当前元素和前一个元素相同，就跳过（因为这里是已经排序好的，相同元素一定是相邻的,有可能会重复）【针对i】
            if i > 0 and nums[i] == nums[i-1]:  
                continue

            # （2）用另外两个动态指针开始在i到末尾找数=target-nums[i]。双指针初始化：left在i的下一位，right在数组末尾。
            left, right = i + 1, len(nums) - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] < 0: # 三数之和小于0
                    left += 1
                elif nums[i] + nums[left] + nums[right] > 0: # 三数之和大于0
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]]) # 加到结果中

                    # 去重2：找到解之后再次去重(针对left和right)
                    while left < right and nums[left] == nums[left+1]:  # 跳过left指针右侧的重复元素
                        left += 1
                    while left < right and nums[right] == nums[right-1]: # 跳过right指针左侧的重复元素
                        right -= 1

                    left += 1  # 寻找下一组的指针移动
                    right -= 1

        return result


# 答疑：为什么第二次查重内部还有一次left<right?
# 外层 while left < right ：保证进入双指针查找时，区间是有效的
# 内层while left < right ：而内层循环会自己移动指针，也需要保证区间有效