
# 完全背包问题
from math import inf, isqrt

N = 10000
f = [0] + [inf] * N
for i in range(1, isqrt(N)+1): # 遍历平方数的底数
    for j in range(i*i, N+1): # 遍历剩下的容量，直接从i*i开始，因为小于i*i的容量无法放下第i件物品
        f[j] = min(f[j], f[j - i * i] + 1)  # 不选 vs 选。1表示选了第i件物品


class Solution:
    def numSquares(self, n: int) -> int:
        return f[n] # 这里的f使用了上面预处理好的完全背包的结果，直接返回f[n]即可
        