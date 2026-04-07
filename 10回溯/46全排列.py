# https://leetcode.cn/problems/permutations/description/?envType=study-plan-v2&envId=top-100-liked
# 排列不是子序列，每个数都要选，没有「不选」。
# 固定长度列表

from polars import List

# 方法一：标准回溯
# 写法1：使用布尔数组 【推荐 √】
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        path = [0] * n  # 存放当前排列：所有排列的长度都是一样的 n
        isUsed = [False] * n # 标记：在当前排列的情况下，该数字是否使用过？
        result = []

        # 当前排列的第i个位置填什么？给第 i 位填数字
        def dfs(i: int) -> None:
            if i == n:  # 终止条件：所有位置都填完了
                result.append(path.copy())  # 保存当前排列（必须copy）。也可以写 path[:]
                return None  # 一旦递归到达终止条件，必须立即返回，不再执行同一函数的剩余代码
            
            # 走到这一步说明没有排满，要去看数组中j对应的数字是否使用过
            for j in range(n):  #  j是用来遍历所有数字
                if not isUsed[j]: # 如果 nums[j] 没被用过
                    path[i] = nums[j]  # 选它，放到第 i 位
                    isUsed[j] = True  # 标记：已使用
                    dfs(i + 1) # # 填下一位
                    isUsed[j] = False  # isUsed要回溯：撤销标记（恢复现场）,让这个数字可以在其他分支中被使用
                    # 因为排列长度固定，直接覆盖就行，所以 path 无需恢复现场

        dfs(0) # 传入第一位
        return result
    
# 写法2：集合操作,不用手动恢复现场，因为每次传新集合
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        path = [0] * n  # 存放当前排列：所有排列的长度都是一样的 n
        result = [] # 存储所有答案

        # # dfs：给第 i 个位置填数字，s 是剩下可选的数字集合
        def dfs(i: int, s: List[int]) -> None:
            if i == n: # 终止条件：所有位置都填完了
                result.append(path.copy())  # 保存当前排列（必须copy）。也可以写 path[:]
                return None 
            
            for x in s: # 遍历所有剩下能选的数字 x
                path[i] = x   # path[i]表示正在填第 i 位
                dfs(i + 1, s - {x}) # 去填下一位，剩余可选数字集合s删除 x（自动去重）
                
        dfs(0, set(nums))
        return result


# 方法二：切片回溯。需要新数组
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(nums, tmp):
            if not nums:
                res.append(tmp)
                return 
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i+1:], tmp + [nums[i]])
        backtrack(nums, [])
        return res

'''
排列和组合问题: 
(1) 组合 = 无顺序 + 部分元素: 
i 是遍历元素, 针对每个元素nums[i]:选or不选
path存答案 + dfs + path移除答案=恢复现场
(2) 排列 =  有顺序+ 全部元素: i是答案位置, for枚举每个位置path[i]-可能的元素=所有排列+on_path标记是否用过
path存答案+on_path标记用过+dfs+on_path移除标记/标记没用过=恢复现场
(存的答案不用恢复现场, for每次覆盖path[i]) 

'''