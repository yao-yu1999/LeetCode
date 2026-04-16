# https://leetcode.cn/problems/majority-element/solutions/3744717/on-mo-er-tou-piao-fa-yan-jin-zheng-ming-ww1zv/?envType=study-plan-v2&envId=top-100-liked
# 题目:给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。
# 假设数组是非空的，并且给定的数组总是存在多数元素。

from typing import List

# 方法: 相同的数：抱团加血,不同的数：互相抵消.因为绝对众数比所有人加起来都多，所以绝对不可能被抵消完
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        result = 0  # 擂主：一开始为空
        count = 0      # 血量：一开始为0
        for x in nums: # 遍历每一个数字，一个个上台
            if count == 0:  # 台上没人 → 直接当擂主
                result, count = x, 1 # # 新擂主登场, 血量+1
            else: # 有人上台挑战
                if x == result:
                    count += 1   # 同门：加血！势力变大
                else:
                    count -= 1   # 敌人：互相抵消，血量-1
        return result