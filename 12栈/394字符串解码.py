# https://leetcode.cn/problems/decode-string/description/?envType=study-plan-v2&envId=top-100-liked

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []      # 栈：保存成对的元素 (重复倍数，之前的字符串)
        result = ""        # 当前正在拼接的字符串
        k = 0           # 当前累积的倍数
        
        for c in s:
            if c == '[':       # 1. 遇到 [ → 保存现场（入栈）
                stack.append((k, result)) # 入栈
                result = ""        # 重置，准备记录括号内内容
                k = 0           # 重置，倍数清零
                
            elif c == ']':     # 2. 遇到 ] → 恢复现场，拼接结果
                cur_k, last_res = stack.pop() # 弹出，准备拼接
                result = last_res + cur_k * result  # 拼接公式
                
            elif c.isdigit():  # 3. 数字：遇到多位数，把连续的数字字符，拼成一个真正的整数
                k = k * 10 + int(c)
            
            else:  # 4. c.isalpha()。所有普通字母，直接拼接到当前结果里，不参与括号运算
                result += c
        
        return result
