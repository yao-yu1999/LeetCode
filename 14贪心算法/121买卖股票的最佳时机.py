# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/?envType=study-plan-v2&envId=top-100-liked
from polars import List

# 方法1：一次遍历（维护两个值：最大利润，最低价格）
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0           # 最大利润，初始为0（不赚钱）
        min_price = prices[0]  # 股票的历史最低价，初始值是第一天价格
        
        for p in prices:   # 遍历每一天股票的价格
            max_profit = max(max_profit, p - min_price)  # 计算：假如今天卖出，利润是多少？并和当前最大利润比，保留大的
            min_price = min(min_price, p) # 更新：到今天为止，历史最低价 
        
        return max_profit  # 返回最大利润


# 方法2：动态规划
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0: return 0   # 空数组直接返回0
        
        dp = [0] * n   # dp[i] = 前i天最大利润
        min_price = prices[0]  # 历史最低价
        
        for i in range(1, n): # 从第2天开始遍历（第1天无法卖）
            min_price = min(min_price, prices[i]) # 更新到今天为止的最低价:和前一天的价格比较选出更小的即可
            dp[i] = max(dp[i - 1], prices[i] - min_price) # 状态转移：(1) 要么不操作 = dp[i-1]; (2) 要么今天卖 = prices[i] - min_price
        
        return dp[-1]  # 返回最后一天的最大利润