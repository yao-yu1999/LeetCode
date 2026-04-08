# https://leetcode.cn/problems/generate-parentheses/description/?envType=study-plan-v2&envId=top-100-liked
from polars import List

# 方法1：枚举选哪个？
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        path = []  # 记录选了哪些位置放左括号，最后把这些位置变成 (，其他变成 )

        # i = 当前已经填了多少个括号；balance = 左括号数 - 右括号数，还能安全填多少个右括号
        def dfs(i: int, balance: int) -> None:
            if len(path) == n: # 终止条件：选够 n 个左括号
                s = [')'] * (2 * n)  # 先全部填 )
                for j in path:
                    s[j] = '('       # 把左括号位置改成 (
                result.append(''.join(s))
                return None

            # 枚举：在放下一次左括号前，可以填 0~balance 个右括号。如，填 2 个 → 放 2 个 ) 后再放 (。最多填 balance 个，再填就非法了
            for right in range(balance + 1):
                path.append(i + right) # 将已经填写了若干个right后，判断出的左括号的位置，加入path：i + right表示下一个左括号的位置，

                # 你填了 right 个右括号 → 右括号变多了→ balance 要减去 right；你又新加了 1 个左括号 → 左括号变多了→ balance 要 +1
                dfs(i + right + 1, balance - right + 1) # 递归：新 balance = 原 balance - 填的右括号 + 新加 1 个左括号
                path.pop()  # 回溯

        dfs(0, 0)
        return result