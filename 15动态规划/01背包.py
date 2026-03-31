# capacity表示背包的容量
# w[i]表示第i件物品的重量，v[i]表示第i件物品的价值
# 0-1背包问题：每件物品只能选一次，return:在不超过背包容量的前提下，能获得的最大价值maxValue。

from typing import List
from litellm import cache

# 动态规划：
# 初始条件：f[0][j]=0, f[i][0]=0
# 状态转移方程：f[i][j] = max(f[i-1][j], f[i-1][j-w[i-1]] + v[i-1])。f[i][j]表示前i件物品在背包容量为j时的最大价值。
def zero_one_knapsack(capacity:int, w: List[int], v: List[int]) -> int:
    n = len(w)  # 物品数量
    f = [[0]*(capacity+1) for _ in range(n+1)] # 初始化DP二维数组，f[i][j]表示前i件物品在背包容量为j时的最大价值；初始条件f[0][j]=0, f[i][0]=0。
    
    # 遍历每件物品：i从第1件物品开始，直到第n件物品
    # 遍历每个容量：j从0到capacity
    for i in range(1, n+1): 
        for j in range(capacity+1): 
            if j < w[i-1]: # 先判断当前容量能不能放下第i件物品（i-1是因为w和v是从0开始的）
                f[i][j] = f[i-1][j] # 不能的话，只能不选第i件物品
            else:
                f[i][j] = max(f[i-1][j], f[i-1][j-w[i-1]] + v[i-1]) # 放得下，就求选或者不选第i件物品的max:最大价值等于前i-1件物品在容量j-w[i-1]时的最大价值加上第i件物品的价值v[i-1]
    return f[n][capacity] # 返回：前n件物品在背包容量为capacity时的最大价值

'''
# 递归边界：dfs(i,c)=0 当 i<0 或者 c<=0 时，说明没有物品可选或者背包容量不足以放下任何物品，最大价值为0。
# 状态转移方程：对于第 i 件物品，有两种选择：
# (1) 不选第 i 件物品：最大价值等于前 i-1 件物品在当前容量 c 时的最大价值，即 dfs(i-1, c)。
# (2) 选第 i 件物品：最大价值等于前 i-1 件物品在容量 c-w[i] 时的最大价值加上第 i 件物品的价值 v[i]，即 dfs(i-1, c-w[i]) + v[i]。
# 递归入口：从最后一件物品开始考虑，背包容量为 capacity，判断选和不选这个物品哪个价值更大？

def zero_one_knapsack(capacity:int, w: List[int], v: List[int]) -> int:
    n= len(w)     # 物品数量,或者者len(v)

    @cache
    def dfs(i:int,capacity:int)->int:
        if i<0 or capacity<=0: # 递归边界：当没有物品可选（i<0）或者背包容量不足以放下任何物品（capacity<=0）时，最大价值为0
            return 0
        if w[i]>capacity: # 如果当前物品的重量超过了背包的剩余容量，那么只能选择不放这个物品，最大价值就是前i-1件物品在当前容量下的最大价值
            return dfs(i-1,capacity)
        else: # 否则，可以选择放这个物品或者不放这个物品，取两者的最大值
            return max(dfs(i-1,capacity), dfs(i-1,capacity-w[i]) + v[i])
    return dfs(n-1,capacity) # 从最后一件物品开始考虑，背包容量为capacity，判断放和不放这个物品哪个价值更大？

'''