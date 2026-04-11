# https://leetcode.cn/problems/letter-combinations-of-a-phone-number/?envType=study-plan-v2&envId=top-100-liked
# 题目：给定一个仅包含数字 2-9 的字符串digits，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。数字和字母映射见代码

from polars import List

# 这题输入视角也是答案视角：按输入顺序逐位构造答案，构造完才保存。固定长度
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        MAPPING = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        n = len(digits)
        if n == 0: return [] # 返回一个空列表
  
        result = [] # 记录返回结果
        path = [''] * n  # 注意 path 长度一开始就是 n，不是空列表。生成一个长度为 n 的列表，每个位置都是空字符

        # 从位置i开始
        def dfs(i: int) -> None:
            if i == n: # 如果到了当前path长度的最后一个
                result.append(''.join(path)) # 注意，不是 result.append(path.copy()) 而是将用''拼接后的结果加入到result里面
                return None 

            for c in MAPPING[digits[i]]: # digits[i]表示第i个位置上的字符，当作key，找到mapping中对应的值。用c遍历第 i 个数字对应的所有字母字符串的每一个字符
                path[i] = c  # 直接覆盖
                dfs(i + 1)  # 递归下一个字符
                # 这里不用回溯。因为 path [i] 按位置覆盖赋值，同一层循环会自动覆盖旧值，不会污染下一轮，所以不需要回溯恢复现场
        
        dfs(0)
        return result