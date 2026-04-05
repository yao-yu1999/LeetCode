# https://leetcode.cn/problems/daily-temperatures/?envType=study-plan-v2&envId=top-100-liked

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n # 初始化结果数组，全为0,存储每一天等待的天数，默认0表示没有更高温度了
        stack = []  # 单调栈，严格递减，存储“还未找到更高温度”的索引，一旦找到更高温度，就弹出索引，计算结果并更新 result 数组

        for i, t in enumerate(temperatures): # # i: 当前天的索引, t: 当前温度
            while stack and t > temperatures[stack[-1]]:  # 当栈非空 且 当前温度 > 栈顶索引对应的温度时（说明找到了更高的温度）
                j = stack.pop()  # 弹出栈顶索引 j，找到等待被填答案的result的索引
                result[j] = i - j # 在 result 数组中，j 位置的答案 = 当前索引 i - j 索引
            stack.append(i) # 循环结束（说明没有找到比今天更高的温度），就将今天入栈，等待未来答案
        return result
        