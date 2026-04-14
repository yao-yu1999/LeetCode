# https://leetcode.cn/problems/longest-valid-parentheses/description/?envType=study-plan-v2&envId=top-100-liked
# 题目：给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号 子串 的长度。左右括号匹配，即每个左括号都有对应的右括号将其闭合的字符串是格式正确的，比如 "(()())"。
# 和20题类似，求是否完全匹配。

# 方法1：栈【推荐】
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]      # 哨兵：虚拟红线/最后一个未匹配的右括号位置。否则无法计算第一段有效括号
        result = 0
        
        for i, ch in enumerate(s):
            if ch == '(':  # 左括号下标入栈，等待匹配
                stack.append(i)           
            else:    # 右括号，尝试匹配（弹出栈顶左括号或哨兵）
                stack.pop()               
                if not stack:  # 如果栈空，说明没有左括号匹配当前的右括号
                    stack.append(i)      # 当前右括号成为新的"红线"
                else: # 说明弹出的是左括号。而新栈顶是上一个未匹配的位置，计算长度：有效子串为 [stack[-1]+1, i]，长度为 i - stack[-1]
                    result = max(result, i - stack[-1])
        
        return result

# 方法2：动态规划
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        dp = [0] * (n + 1)
        stk = [] # 存左括号位置
        for i, c in enumerate(s):
            if c == '(':
                stk.append(i)
            elif len(stk) > 0:
                top = stk[-1] # 当前左括号
                stk.pop()
                # 如果左括号前还有串，则继续往前找有没有有效括号
                dp[i] = i - top + 1 + (dp[top - 1] if top >= 1 else 0)
        return max(dp)