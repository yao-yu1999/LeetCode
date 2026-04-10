# https://leetcode.cn/problems/subarray-sum-equals-k/description/?envType=study-plan-v2&envId=top-100-liked
# 题目：给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。子数组是数组中元素的连续非空序列。
# 思路：定义前缀和 s[i] 表示 nums[0] + nums[1] + ... + nums[i-1]（即前 i 个元素的和，s[0] = 0）。那么子数组 nums[j..i-1] 的和 = s[i] - s[j]
# 要求子数组和等于 k，即 当前前缀和 s[i] - 之前某个前缀和 prev  = k，等价于 prev = s[i] - k
# 因此，当我们遍历到位置 i（前缀和为 s[i]）时，只需要知道之前有多少个前缀和等于 s[i] - k，这些前缀和对应的起始位置都能与当前位置形成和为 k 的子数组。

from collections import defaultdict
from polars import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int)  # 哈希表：记录每个前缀和出现过多少次。key=前缀和，value=出现次数
        cnt[0] = 1              # 第一个数的前缀和一定是0, 因此0的出现次数是1
        
        result = 0              # 最终：统计多少个符合条件
        s = 0                   # 当前遍历到的前缀和
        for i in range(len(nums)):          # 遍历数组中每个数字
            s += nums[i]              # 计算当前前缀和，前缀和计算公式：s[i+1] = s[i] + nums[i]
            result += cnt[s-k]        # 查询字典cnt中，出现过多少次的 s−k → result = result + 本次新找到的个数 -> 有多少个和为K
            cnt[s] += 1               # 把当前前缀和存入字典：如果有重复的前缀和，就把它的出现次数加1，如果没有，就把它的出现次数设为1

        return result
    
# 注：为什么使用前缀和？不用指针？
# 因为本题数组无序，且可能有负数。而且子数组是连续一段，不是两个数三个数，无法用指针。
# 子数组是连续的，连续区间的和 = 前缀和之差，所以用前缀和把 O (n²) 暴力降到 O (n)
# 使用哈希表查询速度也更快