# https://leetcode.cn/problems/same-tree/description/
# 【模板题】

from typing import Optional
from polars import TreeNode
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 情况1：至少有一棵树走到空节点了
        # 1. p 和 q 都为空 => 相同；2. p 和 q 中只有一个为空 => 不同
        if p is None or q is None:
            return p is q  # 1. 当 p 和 q 都为空时，p is q 为 True；2. 当 p 和 q 中只有一个为空时，p is q 为 False
        
        # 情况2：当两个节点都不为空
        # 1. 看当前值是否相等（不能用p is q, 因为p和q是不同的对象）  2. 递归看左子树是否相同  3. 递归看右子树是否相同
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    
        # 补充：判断两棵树是否对称的
        # return p.val == q.val and self.isMirrorTree(p.left, q.right) and self.isMirrorTree(p.right, q.left)