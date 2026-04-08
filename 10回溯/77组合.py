# https://leetcode.cn/problems/combinations/description/
# 【模板题】返回范围 [1, n] 中所有可能的 k 个数的组合。
from polars import List

# 方法1：枚举选哪个？
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        path = []

        # 枚举选哪个：i表示从数字i开始往后选,i, i+1, i+2...
        def dfs(i: int) -> None:
            d = k - len(path)  # 还要选 d 个数, 才能填满path
            if d == 0:  # 已经选完了，剪枝退出
                result.append(path.copy())
                return None

            # j是循环变量，正着枚举后面的数。j 最大只能到 n - d + 1，否则后面不够选，避免无效递归
            for j in range(i, n - d + 2): # j 超过 n-d+1 就会凑不齐，直接剪枝（你还需要选 d 个数，必须给后面留够 d-1 个数）
                path.append(j)
                dfs(j + 1) # 逆序递归
                path.pop()  # 恢复现场

        dfs(1)  # 从1开始:这道题的数字是 1～n, 不是下标0～n-1
        return result

# 方法2：选或不选
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        path = []

        # 选或不选：讨论 i 是否加入 path。i表示正在处理的第i个数字
        def dfs(i: int) -> None:
            d = k - len(path)  # 还要选 d 个数
            if d == 0:  # 已经选完了，剪枝退出
                result.append(path.copy())
                return None

            if i > n:  # 正在处理的数字i的大小，已经超出 n（n是给定区间范围的最大值），不能再选了
                return None
            
            # 不选i
            dfs(i + 1)

            # 选 i
            path.append(i)
            dfs(i + 1) # 逆序枚举
            path.pop()  # 恢复现场

        dfs(1)  # 从1开始:这道题的数字是 1～n, 不是下标0～n-1
        return result
