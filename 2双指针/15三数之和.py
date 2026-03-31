# https://leetcode.cn/problems/3sum/description/
# 也使用双指针，注意一开始先对数组排序，然后三个数要去重
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = [] # 返回的是一个二维数组
        nums.sort() # 先对待查询数组进行排序

        for i in range(len(nums)): # 遍历排序后的数组
            if nums[i] > 0: # 剪枝
                return result 
            if i > 0 and nums[i] == nums[i-1]:  # 去重：如果当前元素和前一个元素相同，就跳过（因为这里是已经排序好的，所以相同元素一定是相邻的）
                continue

            # 双指针初始化：left在i的下一位，right在数组末尾。
            # 这一部分和两数之和逻辑一致,只不过最后不用返回下标，而是加入到数组中
            left = i + 1
            right = len(nums) - 1 
            while right > left:
                if nums[i] + nums[left] + nums[right] < 0:
                    left = left + 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right = right - 1
                else:
                    result.append([nums[i], nums[left], nums[right]])

                    while right > left and nums[left] == nums[left+1]:  # 跳过left指针右侧的重复元素
                        left = left + 1
                    while right > left and nums[right] == nums[right-1]: # 跳过right指针左侧的重复元素
                        right = right -1

                    left = left + 1
                    right = right -1

        return result