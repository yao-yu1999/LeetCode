# https://leetcode.cn/problems/validate-binary-search-tree/description/?envType=study-plan-v2&envId=top-100-liked

from typing import Optional, Tuple
from numpy import inf
from polars import TreeNode 
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None): 
#         self.val = val
#         self.left = left
#         self.right = right


# 方法1：前序遍历
class Solution:
    def isValidBST(self, root: Optional[TreeNode], left=-inf, right=inf) -> bool:
        if root is None:
            return True
        x = root.val
        return left < x < right and self.isValidBST(root.left, left, x) and self.isValidBST(root.right, x, right)

# 方法2：中序遍历，递归实现
class Solution:
    pre = -inf # 记录前一个节点的值，初始值为负无穷，保证第一个节点的值一定大于 pre
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
            
        if not self.isValidBST(root.left): # 先递归判断左子树是否为二叉搜索树，如果不是，那整棵树都不是。直接返回 False
            return False
            
        if root.val <= self.pre: # 判断当前节点的值是否大于前一个节点的值，如果不是，那就不是二叉搜索树。直接返回 False
            return False
        self.pre = root.val # 把自己设为 “下一个节点的前驱”，更新前一个节点的值为当前节点的值

        if not self.isValidBST(root.right): # 最后递归判断右子树是否为二叉搜索树，如果不是，那整棵树都不是。直接返回 False
            return False
        
        return True
    
# 方法3：后序遍历，递归实现
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode]) -> Tuple: # dfs 返回 (当前子树的最小值, 当前子树的最大值)
            
            # 1. 空节点不影响判断，所以返回 (无穷大, 负无穷大)，这样 min 和 max 不会干扰父节点
            if node is None:
                return float('inf'), -float('inf')

            # 2. 后序遍历：先递归左、右子树
            l_min, l_max = dfs(node.left)   # 左子树的最小、最大值
            r_min, r_max = dfs(node.right)  # 右子树的最小、最大值

            x = node.val  # 当前节点的值

            # 3. 核心判断：如果 当前节点 <= 左子树最大值 或者 当前节点 >= 右子树最小值 → 这不是二叉搜索树！
            if x <= l_max or x >= r_min:
                return -float('inf'), float('inf') # 返回一个"表示这棵树非法"的标记

            # 4. 到这一步说明合法，返回当前子树的最小、最大值
            return min(l_min, x), max(r_max, x)

        # 最终判断：如果返回的最大值不是无穷大，就是合法BST
        return dfs(root)[1] != float('inf')