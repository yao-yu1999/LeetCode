# https://leetcode.cn/problems/subsets/?envType=study-plan-v2&envId=top-100-liked
# 题目：一个整数数组 nums ，数组中的元素互不相同 。返回该数组所有可能的子集（幂集）。解集不能包含重复的子集。可以按 任意顺序 返回解集。
# 选或不选，枚举选哪个？两个分支都要走。是动态列表

from polars import List

# 方法1：一进来就保存，然后从剩下的数字中选择一个加入path（更适合子集/序列/组合问题）【推荐】
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = [] # 记录最终结果
        path = [] # 当前子序列

        # dfs(i)：枚举，从 i ~ n-1 中选一个数字加入 path
        def dfs(i: int):
            result.append(path.copy()) # 一进来就保存当前子集（包括空集）
            for j in range(i, n):  # 从剩下的数字中，枚举选哪个数字j. 从i开始到结尾
                path.append(nums[j]) # 选择当前下标为j的数字加入当前子序列

                dfs(j + 1)   # 递归：下一次只能选 j 后面的 (注意不是i，也不是j哦。因为不能选已经选过的数字)

                path.pop()   # 恢复现场，供其他分支使用。

        dfs(0) # 从下标0开始
        return result

# path.pop()：列表也有类似栈的弹出操作，即最后一个（也就是刚刚添加的元素）


# 方法2：选或不选。全部走完，才复制path到result（更适合排列）
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []    # 保存所有子集
        path = []      # 保存当前子集

        # dfs(i)：讨论第 i 个数 选 或 不选
        def dfs(i: int) -> None:
            if i == n:  # 所有数字讨论完毕
                result.append(path.copy()) # 复制当前的子集加入到结果集中
                return None  # 这里必须 return，否则会继续执行下面的代码

            # 不选 nums[i], 则直接递归
            dfs(i + 1) 

            # 选 nums[i]：先加入当前元素，再递归，最后回溯（恢复现场）
            path.append(nums[i])
            dfs(i + 1)
            path.pop() # 回溯：撤销“选”分支的修改，让 path 恢复原状，供后续分支（包括同层的另一个分支和上一层的其他分支）使用

        dfs(0)
        return result
