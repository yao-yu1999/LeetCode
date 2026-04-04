# https://leetcode.cn/problems/symmetric-tree/description/?envType=study-plan-v2&envId=top-100-liked
from typing import Optional
from polars import TreeNode

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # 参考第100题，将递归判断相同的树，改成递归判断是否为镜像（轴对称）树
    def isMirrorTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None or q is None:
            return p is q

        return p.val == q.val and self.isMirrorTree(p.left, q.right) and self.isMirrorTree(p.right, q.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isMirrorTree(root.left, root.right) # 直接将根节点的左右子树传递，判断它们是否为镜像树即可。即判断是否是二叉对称树