# https://leetcode.cn/problems/jump-game-ii/?envType=study-plan-v2&envId=top-100-liked
# 题目：给定一个长度为 n 的 0 索引整数数组 nums。初始位置在下标 0。
# 每个元素 nums[i] 表示从索引 i 向后跳转的最大长度。即在索引 i 处，你可以跳转到任意 (不超过i + nums[i]即可) 处：

# 核心思路：模拟人在边走边建桥。在走当前桥的每一处端点时，看看假如以当前端点建下一座桥时，能走多远。
# 当走到当前桥的最右端时（也就是桥的终点）看看之前记录的哪一个端点可以走最远，从那里开始建下一座桥。
# 建桥要保证桥和桥之间有交集，否则桥会掉下去。 返回到达 n - 1 的最小跳跃次数

from polars import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        result = 0 # 最小跳跃次数
        cur_right = 0  # 已建造的桥的右端点:当前这一步能到达的最远边界,走到这必须跳
        next_right = 0  # 下一座要建桥的右端点：选取并记录的是最远的那个
        
        for i in range(len(nums) - 1): # 只遍历到n-2，因为到最后一个位置n-1就不用再建桥了
            next_right = max(next_right, i + nums[i]) # 边走边看：从 i 出发，最远能跳到哪？更新下一座桥的最远点。i + nums[i]表示从当前位置i能跳多远？
            if i == cur_right:  # 到达当前桥的右端点了，必须建新桥
                cur_right = next_right  # # 新的桥 = 刚才记录的最远点
                result += 1  # 建桥次数 +1
        return result
    
# 答疑1：
# 贪心 真正的定义 是：不回溯、不推翻之前的跳跃决定, 不是立刻决定跳哪里且不能改。
# next_right = max(next_right, i + nums[i])这一步只是收集信息