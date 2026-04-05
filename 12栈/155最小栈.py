# https://leetcode.cn/problems/min-stack/description/?envType=study-plan-v2&envId=top-100-liked
from numpy import inf

class MinStack:
    def __init__(self):
        self.stack = [(0, inf)]  # 栈底哨兵：（1）值的位置，可以写成任意数，反正用不到；（2）第二个数写成无穷大，保证第一次 min 一定是新数

    # 入栈
    def push(self, val: int) -> None:
        min_val = min(self.stack[-1][1], val) # 新最小值 = min(栈顶最小值, 新值)
        self.stack.append((val, min_val))  # 将要入栈的元素和最小值元素，按照成对的形式入栈

    # 出栈
    def pop(self) -> None:
        self.stack.pop() # 按照正常的出栈来写：直接弹出栈顶（值+最小值一起删）。由于每一步都保存了当前的最小值，所以出栈后，栈顶的最小值就是新的最小值。
    
    # 取栈顶元素
    def top(self) -> int:
        return self.stack[-1][0] # 取栈顶的第一个值

    # 获取栈内最小元素
    def getMin(self) -> int:
        return self.stack[-1][1] # 入栈的时候就直接保存了，仅用O(1)就能取出
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()