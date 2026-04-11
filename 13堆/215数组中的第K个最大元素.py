# https://leetcode.cn/problems/kth-largest-element-in-an-array/submissions/715293225/?envType=study-plan-v2&envId=top-100-liked
# 题目：给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
# 你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。必须设计并实现时间复杂度为 O(n) 的算法解决此问题。

from random import randint, random
from polars import List

# 方法一：快速选择算法（Quick Select）- 三路快排 【推荐】
# 每次随机选一个数 pivot, 把数组分成 3 堆：(1) 比 pivot 大的 → big；(2) 比 pivot 小的 → small；(3) 和 pivot 一样的 → equal
# 然后只去目标所在那堆继续找：(1)第k大在big里 → 去big找; (2)第k大在equal里 → 直接返回pivot; (3)第k大在small里 → 去small找
class Solution:
    def findKthLargest(self, nums, k):
        def quick_select(nums, k):
            pivot = random.choice(nums) # 随机选择基准数：随机选择一个数 pivot, 避免退化成 O(n^2) 的情况。随机选择的 pivot 可以是数组中的任意一个元素, 这样可以保证算法的平均时间复杂度为 O(n)。
            big, equal, small = [], [], [] # 将大于、小于、等于 pivot 的元素划分至 big, small, equal 中, 且最大的一堆在前面
            
            # 1. 开始划分
            for num in nums: # 遍历的是数字
                if num > pivot:
                    big.append(num)
                elif num < pivot:
                    small.append(num)
                else:
                    equal.append(num)
            
            # 或者可以遍历下标
            # for i in range(len(nums)): 
            #     if nums[i] > pivot:
            #         big.append(nums[i])
            #     elif nums[i] < pivot:
            #         small.append(nums[i])
            #     else:
            #         equal.append(nums[i])

            # 2. 去对应的堆继续找
            if k <= len(big): # 第 k 大元素在 big 中
                return quick_select(big, k) # 递归划分big
            elif k > len(big) + len(equal): # 第 k 大元素在 small 中
                return quick_select(small, k - len(big) - len(equal)) # 递归划分small(不能直接传k, 因为在small堆里面的排序是k - len(big) - len(equal))
            else: # 第 k 大元素在 equal 
                return pivot   # equal 堆里所有数都等于 pivot所以直接返回 pivot 就是答案
            
        return quick_select(nums, k)
    
# 方法二：快速选择算法（Quick Select）- 双路快排
# 
class Solution:
    def partition(self, nums: List[int], left: int, right: int) -> int:
        """
        在子数组 [left, right] 中随机选择一个基准元素 pivot
        根据 pivot 重新排列子数组 [left, right], <= pivot 的元素都在 pivot 的左侧, >= pivot 的元素都在 pivot 的右侧
        返回 pivot 在重新排列后的 nums 中的下标
        特别地, 如果子数组的所有元素都等于 pivot, 会返回子数组的中心下标, 避免退化
        """

        # 1. 在子数组 [left, right] 中随机选择一个基准元素 pivot
        i = randint(left, right)
        pivot = nums[i]
        
        nums[i], nums[left] = nums[left], nums[i] # 把 pivot 与子数组第一个元素交换, 避免 pivot 干扰后续划分, 从而简化实现逻辑

        # 2. 相向双指针遍历子数组 [left + 1, right]
        # 循环不变量：在循环过程中, 子数组的数据分布始终如下图
        # [ pivot | <=pivot | 尚未遍历 | >=pivot ]
        #   ^                 ^     ^         ^
        #   left              i     j         right

        i, j = left + 1, right
        while True:
            while i <= j and nums[i] < pivot:
                i += 1
            # 此时 nums[i] >= pivot

            while i <= j and nums[j] > pivot:
                j -= 1
            # 此时 nums[j] <= pivot

            if i >= j:
                break

            # 维持循环不变量
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

        # 循环结束后
        # [ pivot | <=pivot | >=pivot ]
        #   ^             ^   ^     ^
        #   left          j   i     right

        # 3. 把 pivot 与 nums[j] 交换, 完成划分（partition）
        # 为什么与 j 交换？
        # 如果与 i 交换, 可能会出现 i = right + 1 的情况, 已经下标越界了, 无法交换
        # 另一个原因是如果 nums[i] > pivot, 交换会导致一个大于 pivot 的数出现在子数组最左边, 不是有效划分
        # 与 j 交换, 即使 j = left, 交换也不会出错
        
        nums[left], nums[j] = nums[j], nums[left]

        # 交换后
        # [ <=pivot | pivot | >=pivot ]
        #               ^
        #               j

        # 返回 pivot 的下标
        return j

    def findKthLargest(self, nums: list[int], k: int) -> int:
        n = len(nums)
        target_index = n - k  # 第 k 大元素在升序数组中的下标是 n - k
        left, right = 0, n - 1  # 闭区间
        while True:
            i = self.partition(nums, left, right)
            if i == target_index: # 找到第 k 大元素
                return nums[i]
            if i > target_index: # 第 k 大元素在 [left, i - 1] 中
                right = i - 1
            else: # 第 k 大元素在 [i + 1, right] 中
                left = i + 1