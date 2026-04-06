# https://leetcode.cn/problems/jump-game/description/?envType=study-plan-v2&envId=top-100-liked

# 贪心所在：每到一个可到达的位置，就贪婪地用它来扩展能到达的最远边界，而不是犹豫是否要跳得少一点。
# 因为跳得越远，就越有可能到达终点，所以局部最优（在当前步跳得尽可能远）就是全局最优策略。
from polars import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_x = 0  # 目前能跳到的最远位置
        n = len(nums) 
        
        for i in range(n):
            if i > max_x: return False  # 如果当前位置都到不了，返回 False
            max_x = max(max_x, i + nums[i])  # 更新能跳的最远位置

            # 提前结束：还没遍历完整个数组，只要发现 “已经能跳到终点”，立刻返回 True！
            if max_x >= n - 1:
                return True
        return True # 能走完所有位置，说明能到终点