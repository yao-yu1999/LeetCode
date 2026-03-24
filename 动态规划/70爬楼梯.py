# https://leetcode.cn/problems/climbing-stairs/?envType=study-plan-v2&envId=top-100-liked
from litellm import cache

# 动态规划：
# 初始条件：f(0)=1, f(1)=1
# f(n) = f(n-1) + f(n-2)
class Solution:
    def climbStairs(self, n: int) -> int:
        f = [0]*(n+1) # 1. 初始化一个一维数组，有n+1个0。楼梯阶数是从 0 到 n（比如 n=3，要算 0、1、2、3 阶）
        f[0] = f[1] = 1 # 2. 初始条件
        
        for i in range(2, n+1):  # 3. 遍历每个阶数，从2到n（因为0和1的情况已经初始化了）
            f[i] = f[i-1]+ f[i-2] # 4. 状态转移方程：f(n) = f(n-1) + f(n-2)，即到达第n阶的方法数等于到达第n-1阶的方法数加上到达第n-2阶的方法数（因为每次可以爬1阶或2阶）
        return f[n] # 5. 返回第n阶的方法数


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