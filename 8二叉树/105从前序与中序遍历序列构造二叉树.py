# https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/?envType=study-plan-v2&envId=top-100-liked
# 题目：给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历， inorder 是同一棵树的中序遍历，请构造二叉树并返回其根节点。
# preorder 和 inorder 均 无重复 元素
# 106题：中序和后序遍历，889题：前序遍历和后序遍历（只是不能唯一确定一棵二叉树，那个题只要求返回一个）

from typing import List, TreeNode, Optional

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index = {x: i for i, x in enumerate(inorder)} 

        # 参数：pre_l, pre_r：当前子树在前序数组中的区间范围，左闭右开; in_l：当前子树在中序数组中的起始下标
        def dfs(pre_l: int, pre_r: int, in_l: int) -> Optional[TreeNode]: 
            if pre_l == pre_r:  # 空区间 -> 空节点
                return None
            left_size = index[preorder[pre_l]] - in_l  # 左子树节点个数。index[preorder[pre_l]] 当前子树的根节点在中序遍历数组中下标
        
            left = dfs(pre_l + 1, pre_l + 1 + left_size, in_l) # 左子树。剩下的前序中，左子树占据 pre_l+1 到 pre_l+left_size（左闭右开，共 left_size 个元素
            right = dfs(pre_l + 1 + left_size, pre_r, in_l + left_size + 1) # 右子树
            
            return TreeNode(preorder[pre_l], left, right)

        return dfs(0, len(preorder), 0)  # 左闭右开区间

# 两个优化：
# 用一个哈希表（或者数组）记录每个值在中序遍历中的下标，可以在 O(1) 时间内获取根节点在中序数组中的位置。
# 把递归参数改成子数组下标区间（左闭右开区间）的左右端点，从而避免复制数组。

# 为什么不需要 in_r？因为子树大小可以由前序区间长度确定，而中序区间的结束下标可以通过 in_l + (pre_r - pre_l) 计算得到。
# 代码中没有显式传入 in_r，但通过 left_size 和递归调用中的参数可以推导。

# left_size = index[preorder[pre_l]] - in_l 表示：
# 从 in_l 到 index[根]-1 这一段都属于左子树，因此左子树的节点个数 = index[根] - in_l

# 左子树递归区间：
# 前序区间：根节点占 pre_l，剩下的前序中，左子树占据 pre_l+1 到 pre_l+left_size（左闭右开，共 left_size 个元素）。
# 中序区间：从 in_l 开始，长度为 left_size，即 [in_l, in_l + left_size)。

# 右子树递归区间：
# 前序区间：左子树之后到当前区间结束，即 [pre_l+1+left_size, pre_r)。
# 中序区间：同一子树在前序和中序中的节点数相同。根节点之后到中序区间结束，起始下标为 in_l+left_size+1，长度由前序剩余长度决定（右子树大小 = (pre_r - pre_l) - 1 - left_size）


# 时间复杂度O(n^2)
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:  # 空节点
            return None
        left_size = inorder.index(preorder[0])  # 左子树的大小
        left = self.buildTree(preorder[1: 1 + left_size], inorder[:left_size])
        right = self.buildTree(preorder[1 + left_size:], inorder[1 + left_size:])
        return TreeNode(preorder[0], left, right)
