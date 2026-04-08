# https://leetcode.cn/problems/trapping-rain-water/description/?envType=study-plan-v2&envId=top-100-liked

from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        left, right = 0, len(height) - 1
        pre_max = suf_max = 0

        while left < right:
            # 先更新最大值
            pre_max = max(pre_max, height[left])
            suf_max = max(suf_max, height[right])

            # 再计算雨量。为什么可以安全的计算雨量？
            if pre_max < suf_max:
                result += pre_max - height[left] # 直接用最大值减去自身高度，并累加即可
                left += 1 # 移动小的一边的指针：右移左指针
            else:
                result += suf_max - height[right]
                right -= 1 # 移动小的一边的指针：左移右指针
        return result
    
# left 指针从左向右移动，right 指针从右向左移动。
# pre_max 记录的是 height[0] 到 height[left] 的最大值（包括当前位置）。
# suf_max 记录的是 height[right] 到 height[n-1] 的最大值（包括当前位置）。

# 当 pre_max < suf_max 时(pre_max >= suf_max同理)：
# 处理 left 位置。对于 left 位置，它右侧所有柱子（即下标从 left+1 到 n-1）的最大值，记为 right_max。
# suf_max 是 height[right] 到 height[n-1] 的最大值。由于 left < right（循环条件保证），所以区间 [right, n-1] 是 [left+1, n-1] 的子集。
# 子集的最大值一定 ≤ 全集的最大值，即 suf_max ≤ right_max，因此 right_max ≥ suf_max

# 我们需要 min(pre_max, right_max)来计算雨量。已知：pre_max < suf_max（条件），suf_max ≤ right_max（上面推导）
# 因此 pre_max < suf_max ≤ right_max，所以 pre_max < right_max。那么 min(pre_max, right_max) 一定是 pre_max。
# 所以即使不知道 right_max 的值，只要知道 suf_max 比 pre_max 大，就能确定较小值就是 pre_max。