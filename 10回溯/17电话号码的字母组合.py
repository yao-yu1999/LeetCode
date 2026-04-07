# https://leetcode.cn/problems/letter-combinations-of-a-phone-number/?envType=study-plan-v2&envId=top-100-liked
from polars import List

# 这题输入视角也是答案视角：按输入顺序逐位构造答案，构造完才保存
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
  
        result = []
        path = [''] * n  # 注意 path 长度一开始就是 n，不是空列表。生成一个长度为 n 的列表，每个位置都是空字符

        def dfs(i: int) -> None:
            if i == n:
                result.append(''.join(path)) # 注意，不是 result.append(path.copy()) 而是将用''拼接后的结果加入到result里面
                return None 

            for c in MAPPING[digits[i]]: # 直接用数字字符串（如"2","3"）当key，找到mapping中对应的值。用c遍历第 i 个数字对应的所有字母字符串
                path[i] = c  # 直接覆盖
                dfs(i + 1)  # 递归下一个字符
                # 这里不用回溯。因为 path [i] 按位置覆盖赋值，同一层循环会自动覆盖旧值，不会污染下一轮，所以不需要回溯恢复现场
        dfs(0)
        return result