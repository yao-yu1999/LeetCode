# https://leetcode.cn/problems/invert-binary-tree/description/?envType=study-plan-v2&envId=top-100-liked

from typing import Optional
from polars import TreeNode

# 方法一：递归法
# 根据二叉树镜像的定义，考虑递归遍历（dfs）二叉树，交换每个节点的左 / 右子节点，即可生成二叉树的镜像。
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None: return None # 大根节点为null，直接返回null。

        left = self.invertTree(root.left)  # 递归中，每一层都把自己看作 “小根root”
        right = self.invertTree(root.right)

        root.left = right
        root.right = left

        return root # 返回root，即这棵树


# 方法2：迭代法，辅助栈（或队列）
# 利用栈（或队列）遍历树的所有节点 node ，并交换每个 node 的左 / 右子节点。区别仅在于，初始化栈和队列、取出节点的方式不同。

# （1）辅助栈
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None: return None # 空树判断：没有节点，直接返回

        stack = [root] # 初始化栈，把根节点放进去
        while stack: # 栈不为空，说明还有节点没处理
            node = stack.pop()  # 弹出栈顶节点（拿到当前要处理的节点） 
            if node.left: # 左孩子不为空 → 入栈（后面要处理它的孩子）
                stack.append(node.left)
            if node.right: # 右孩子不为空 → 入栈
                stack.append(node.right)
                
            node.left, node.right = node.right, node.left  # 交换当前节点的 左、右孩子
        return root
    
from collections import deque  # 队列必须用 deque

# （2）辅助队列
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None: return None

        queue = deque([root])  # 初始化队列，把根节点放进去
        while queue:
            node = queue.popleft()  # 从队列左边取出当前要处理的节点
            
            if node.left: 
                queue.append(node.left)
            if node.right: 
                queue.append(node.right)
                
            node.left, node.right = node.right, node.left  # 交换不变
            
        return root