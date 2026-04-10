# https://leetcode.cn/problems/rotate-array/?envType=study-plan-v2&envId=top-100-liked
# 题目：给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。向右轮转指，逐个从数组最后一个数移到数组最前面
# 不用返回任何

from polars import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums) # 防止 k 太大，把轮转次数变成有效次数
        if k != 0: # 如果k不为0，说明需要轮转
            nums[:k], nums[k:] = nums[-k:], nums[:-k]  
            # python中可以直接翻转列表切片：nums[-k:] 是最后 k 个元素，nums[:-k] 是前面剩下的元素。把它们交换位置，就完成了轮转。
            # 比如 nums = [1,2,3,4,5,6,7], k = 3，nums[-3:] = [5,6,7]，nums[:-3] = [1,2,3,4]，交换后 nums[:3] = [5,6,7]，nums[3:] = [1,2,3,4]
            # 最终 nums = [5,6,7,1,2,3,4]
