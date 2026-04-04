# https://leetcode.cn/problems/diameter-of-binary-tree/?envType=study-plan-v2&envId=top-100-liked

from typing import Optional
from polars import TreeNode
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_len = 0  # 记录全局最大直径
        
        # 嵌套递归
        def dfs(node: Optional[TreeNode]) -> int:
            if node is None: return -1 # 如当前节点为空，说明这条链不存在，定义链长为 -1，方便后面 +1 后正确算出叶子节点的链长：-1 +1 = 0
                
            l_len = dfs(node.left) + 1  # 左链长 = 左子树的最大链长 + 1（当前节点连左子节点的一条边）
            r_len = dfs(node.right) + 1 # 右链长 = 右子树的最大链长 + 1（当前节点连右子节点的一条边）

            nonlocal max_len # 在内部函数中修改外部变量，必须声明 nonlocal
            max_len = max(max_len, l_len + r_len) # 当前节点的直径 = 左链长 + 右链长，更新全局最大直径

            return max(l_len, r_len) # 递归最终返回给父节点只能选一条链

        dfs(root) # 开始递归，因为最终返回给父节点只能选一条链，所以递归函数的返回值是当前节点的最大链长，而不是当前节点的直径。所以要嵌套一个递归函数来计算链长，并在递归过程中更新全局最大直径。最后返回全局最大直径即可。
        
        return max_len # 返回全局最大直径