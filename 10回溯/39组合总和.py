# https://leetcode.cn/problems/combination-sum/?envType=study-plan-v2&envId=top-100-liked
# 题目：一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，找出 candidates 中可以使数字和为目标数 target 的 所有 不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。
# candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。 对于给定的输入，保证和为 target 的不同组合数少于 150 个

from polars import List

# 方法1：枚举选哪个？【推荐】
# 答案视角
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()  # 先将数组进行排序
        n = len(candidates)
        result = []
        path = [] # 当前组合
        
        # 递归函数：i表示从哪个下标开始选，left表示还剩下多少和需要凑
        def dfs(i: int, left: int) -> None: 
            if left == 0: # 终止条件：不需要再凑了，说明找到了 -> 保存答案
                result.append(path.copy())  # 将该组合复制加入到结果列表中
                return None 

            # 枚举选哪个：从 i 到末尾n-1，选一个数字加入 path
            for j in range(i, n): # 开始选
                if candidates[j] > left:  # 剪枝：因为是从小到大排序，后面的数已经大于了要凑的和，直接停止（循环中需要用break停止递归）
                    break
                path.append(candidates[j]) # 把 candidates[j] 加入当前组合

                dfs(j, left - candidates[j])  # 重点！！传 j 而不是 j+1 → 因为可以重复选当前数字；left - candidates[j]表示加入之后，剩下的需要凑的和
                
                path.pop()  # 回溯，提供给其他分支使用

        dfs(0, target)
        return result


# 方法2：选或不选
# 输入视角：从 i 开始往后选数字，选了 nums [j] 后，下一轮还从 j 开始（可重复）
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()  # 先将数组进行排序
        n = len(candidates)
        result = []
        path = []

        def dfs(i: int, left: int) -> None:
            if left == 0: # 终止条件 1：不需要再凑了，说明找到了 -> 保存答案
                result.append(path.copy())  # 将该组合复制加入到结果列表中
                return None

            if i == n or candidates[i] > left:  # 终止条件 2：数字用完 或 最小的数都太大 → 剪枝退出
                return None

            # 不选
            dfs(i + 1, left) # 既然不选，那就从下一个开始

            # 选
            path.append(candidates[i]) # 把 candidates[i] 加入当前组合
            dfs(i, left - candidates[i])  # 重点！！传 i 而不是 i+1 → 因为可以重复选当前数字；left - candidates[i]表示加入之后，剩下的需要凑的和
            path.pop()  # 回溯，提供给其他分支使用

        dfs(0, target)
        return result

# 方法3：01背包
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        # 完全背包
        f = [[False] * (target + 1) for _ in range(n + 1)]
        f[0][0] = True
        for i, x in enumerate(candidates):
            for j in range(target + 1):
                f[i + 1][j] = f[i][j] or j >= x and f[i + 1][j - x]

        result = []
        path = []

        def dfs(i: int, left: int) -> None:
            if left == 0:
                # 找到一个合法组合
                result.append(path.copy())
                return None

            # 无法用下标在 [0, i] 中的数字组合出 left
            if left < 0 or not f[i + 1][left]:
                return None

            # 不选
            dfs(i - 1, left)

            # 选
            path.append(candidates[i])
            dfs(i, left - candidates[i])
            path.pop()

        # 倒着递归，这样参数符合 f 数组的定义
        dfs(n - 1, target)
        return result
