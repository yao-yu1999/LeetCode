# https://leetcode.cn/problems/sliding-window-maximum/?envType=study-plan-v2&envId=top-100-liked
# 题目：给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
# 返回 滑动窗口中的最大值 。
from typing import List
from collections import deque

# 方法：双端队列+单调性
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = [0] * (len(nums) - k + 1) # 答案数组，长度 = 窗口个数。如果这里用变长数组result = [], 下面记录result也要修改
        queue = deque()   # 双端队列，存储元素下标

        for i, x in enumerate(nums):
            # 右边入：维护队列单调递减。队列中存储的值都是已经遍历过的旧值，所以只要新值更大（含相等），就要把所有旧值弹出，所以这里是while，表示不止有一个
            while queue and nums[queue[-1]] <= x: # 当队列非空 且 队尾元素对应的值（旧值） <= 当前值x时：所有旧值对应下标弹出队尾
                queue.pop()   # 注意这里不是popleft,popleft是从左边（队头）弹出，pop是队尾弹出
            queue.append(i)   # 循环结束，将当前元素x的下标i,加入队尾

            # 左边出：移除已经离开窗口的队首元素
            left = i - k + 1          # 当前窗口的左边界下标
            if queue[0] < left:       # 队首下标<左边界下标，说明已不在窗口内。这里每次只滑动一次，所以用if
                queue.popleft()       # 弹出队首

            # 记录答案：当窗口完全形成后（i走到k-1及之后），队首就是最大值
            if i >= k-1:
                result[left] = nums[queue[0]]  # 以窗口左边界 left为结果数组的下标记录当前窗口最大值 = 队首元素。left 到达最后一个窗口的左边界，即 left = len(nums)-k（此时 i = len(nums)-1），最后一个窗口处理完毕。
                # result.append(nums[queue[0]])
        return result

# 每次遍历到一个更大的新值，删除队列中所有比这个新值更小的值，因为左边的小值永远都不可能是后面的值中的最大值了
# 最新遍历到的这个值，不管其大小如何，都要加入队列。因为这个值有可能是后面的答案。
# 当 nums[队尾下标] == x 时，两个元素值相等，但新元素 x 更靠右，存活时间更长，所以也要弹出。

# 为什么本题使用队列？
# 因为可以通过维护一个单调递减的双端队列，队首为当前窗口的最大值。不用遍历窗口内的元素来找最大值。