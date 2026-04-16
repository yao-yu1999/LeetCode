# https://leetcode.cn/problems/jump-game/description/?envType=study-plan-v2&envId=top-100-liked
# 题目：给你一个非负整数数组 nums ，你最初位于数组的 第一个下标 。数组中的每个元素代表你在该位置可以跳跃的最大长度。
# 判断你是否能够到达最后一个下标，如果可以，返回 true ；否则，返回 false 。

# 思路：贪心所在，每到一个可到达的位置，就贪婪地用它来扩展能到达的最远边界，而不是犹豫是否要跳得少一点。
# 因为跳得越远，就越有可能到达终点，所以局部最优（在当前步跳得尽可能远）就是全局最优策略。

from polars import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_x = 0  # 目前能跳到的最远位置
        n = len(nums) 
        
        for i in range(n):
            if i > max_x:  # 想到达第 i 个格子，但目前最远只能跳到 max_x。也就是根本过不去
                return False
            
            max_x = max(max_x, i + nums[i])  # 更新能跳的最远位置
            if max_x >= n - 1: # 提前结束：还没遍历完整个数组，只要发现 “已经能跳到终点”，立刻返回 True！
                return True
        return True # 能走完所有位置，说明能到终点