# https://leetcode.cn/problems/container-with-most-water/description/?envType=study-plan-v2&envId=top-100-liked
# 题目：给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。找出其中的两条线，使它们与 x 轴共同构成的容器可以容纳最多的水。返回容器可以储存的最大水量。不能倾斜容器。
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        result =0 
        left, right = 0, len(height) - 1

        while left < right: # 当 left == right，容器的宽度为0，无法盛水
            area = (right - left) * min(height[left], height[right]) # 计算当前容器的面积：宽度 * 高度。宽度是 right - left，高度是左右指针中较小的那个，因为水只能盛到较矮的那根柱子高度。
            result = max(result, area) # 更新最大面积：如果当前面积大于之前记录的最大面积，就更新 result。
            
            # 移动较矮的指针：如果左边的柱子较矮，就移动左指针向右；如果右边的柱子较矮，就移动右指针向左。因为移动较矮的指针可能会找到更高的柱子，从而增加容器的高度，可能会得到更大的面积。
            if height[left] < height[right]: 
                left += 1
            else:
                right -= 1
        
        return result