# https://leetcode.cn/problems/container-with-most-water/description/?envType=study-plan-v2&envId=top-100-liked

from polars import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = left = 0
        right = len(height) - 1

        while left < right: # 当 left == right，容器的宽度为0，无法盛水
            area = (right - left) * min(height[left], height[right]) # 计算当前容器的面积：宽度 * 高度。宽度是 right - left，高度是左右指针中较小的那个，因为水只能盛到较矮的那根柱子高度。
            ans = max(ans, area) # 更新最大面积：如果当前面积大于之前记录的最大面积，就更新 ans。
            
            # 移动较矮的指针：如果左边的柱子较矮，就移动左指针向右；如果右边的柱子较矮，就移动右指针向左。因为移动较矮的指针可能会找到更高的柱子，从而增加容器的高度，可能会得到更大的面积。
            if height[left] < height[right]: 
                left += 1
            else:
                right -= 1
        return ans