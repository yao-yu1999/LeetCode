# https://leetcode.cn/problems/rotate-array/?envType=study-plan-v2&envId=top-100-liked
from polars import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k := (k % len(nums)):  # 海象运算符，可以在赋值的同时进行if条件判断。禁止直接在if条件里面写 k = k % len(nums)。另外，防止 k 太大，把轮转次数变成有效次数
            nums[:k], nums[k:] = nums[-k:], nums[:-k]  
            # python中可以直接翻转列表切片：nums[-k:] 是最后 k 个元素，nums[:-k] 是前面剩下的元素。把它们交换位置，就完成了轮转。
            # 比如 nums = [1,2,3,4,5,6,7], k = 3，nums[-3:] = [5,6,7]，nums[:-3] = [1,2,3,4]，交换后 nums[:3] = [5,6,7]，nums[3:] = [1,2,3,4]
            # 最终 nums = [5,6,7,1,2,3,4]
