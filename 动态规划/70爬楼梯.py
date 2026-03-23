# https://leetcode.cn/problems/climbing-stairs/?envType=study-plan-v2&envId=top-100-liked
from litellm import cache

# 递推法：数组迭代版。从第一步开始往后推，递推式：f(n) = f(n-1) + f(n-2)，递推边界：f(0)=1, f(1)=1
class Solution:
    def climbStairs(self, n: int) -> int:
        f = [0]*(n+1) # 初始化一个数组，有n+1个0。楼梯阶数是从 0 到 n（比如 n=3，要算 0、1、2、3 阶）
        f[0] = f[1] = 1 # 递推边界
        for i in range(2, n+1):
            f[i] = f[i-1]+ f[i-2]
        return f[n]


'''
递归法：从最后一步往前推，递归式：f(n) = f(n-1) + f(n-2)，递归边界：f(0)=1, f(1)=1
class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def dfs(i:int) ->int:
            if i<=1: # 1. 递归边界
                return 1
            return dfs(i-1) + dfs(i-2)  # 2. 递归式：状态转移方程
        return dfs(n)

'''