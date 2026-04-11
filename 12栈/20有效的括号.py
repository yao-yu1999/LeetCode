# https://leetcode.cn/problems/valid-parentheses/?envType=study-plan-v2&envId=top-100-liked
# 题目：给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。有效字符串需满足：
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 每个右括号都有一个对应的相同类型的左括号。
# 核心思想：栈。左括号入栈；右括号出栈并匹配。最后检查栈是否为空。

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0: return False  # s 长度如果不是偶数，直接返回false。奇数一定不合法
        
        # 定义一个哈希表，用来快速查：这个右括号应该匹配谁。存放右括号和对应的左括号的映射关系
        mp = {')': '(', 
              ']': '[', 
              '}': '{'} 
        stack = [] # 创建一个空栈存放左括号

        # 遍历字符串 s 中的每个字符 c
        for c in s:
            if c not in mp:  # 如果 c 是左括号（不在 mp 中），就入栈
                stack.append(c)
            elif not stack or stack.pop() != mp[c]:  # c 是右括号，开始匹配：（1）栈空[说明没有左括号可以匹配当前的右括号]；（2）栈顶元素不是 c 对应的左括号，说明不合法
                return False # 必须在栈顶配对，否则不合法。
        
        if stack: return False  # 遍历结束后，如果栈不空，说明还有未匹配的左括号，不合法。在 Python 里,栈空为False，栈非空为True。
        
        return True  # 如果上面都没有返回 False，说明字符串合法，返回 True
        