# https://leetcode.cn/problems/decode-string/description/?envType=study-plan-v2&envId=top-100-liked
# 题目：给定一个经过编码的字符串，返回它解码后的字符串。
# 编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
# 可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
# 此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。
# 测试用例保证输出的长度不会超过 105。

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []      # 栈：保存成对的元素 (重复倍数，之前的字符串)
        result = ""        # 当前正在拼接的字符串
        k = 0           # 当前累积的倍数
        
        for c in s:
            if c == '[':       # 1. 遇到 [ → 保存现场（入栈）
                stack.append((k, result)) # 入栈
                result = ""        # 重置，准备记录括号内内容
                k = 0           # 重置，倍数清零。
                
            elif c == ']':     # 2. 遇到 ] → 恢复现场，拼接结果
                cur_k, last_res = stack.pop() # 弹出，准备拼接
                result = last_res + cur_k * result  # 拼接公式
                
            elif c.isdigit():  # 3. 数字：遇到多位数，把连续的数字字符，拼成一个真正的整数
                k = k * 10 + int(c)
            
            else:  # 4. c.isalpha()。所有普通字母，直接拼接到当前结果里，不参与括号运算
                result += c
        
        return result
