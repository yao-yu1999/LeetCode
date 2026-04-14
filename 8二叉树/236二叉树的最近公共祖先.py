# https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/description/?envType=study-plan-v2&envId=top-100-liked
# 题目：给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
# 最近公共祖先：对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

from typing import TreeNode, Optional

class Solution:
    def lowestCommonAncestor(self, root:Optional[TreeNode], p:Optional[TreeNode], q:Optional[TreeNode]) -> Optional[TreeNode]:
        # 分类讨论情况1：如果当前节点是空，或者就是p/q，直接返回当前节点
        if root in (None, p, q):  
            return root
        # 找到p/q就不往下递归了：如果下面有另一个节点，当前节点就是LCA；如果没有，也不用递归

        # 递归左右子树（后序遍历：先左、再右、最后处理当前节点）
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # 分类讨论情况2：
        # 2-1:左右子树都找到了非空结果 → 说明p在左、q在右（或反之），当前节点就是LCA
        if left and right:  
            return root  # 当前节点是最近公共祖先
        
        # 情况2-2：只有左或只有右非空 → 返回非空的那个（LCA在对应子树里）
        # 情况2-3：左右都空 → 返回None（等价于left or right，因为or会返回第一个非空值，都空则返回None）
        return left or right  

# 注：lowestCommonAncestor的返回值，是以 root 为根的子树中，p、q 的最近公共祖先候选项

# 为什么用后序遍历？
# 因为我们需要先知道左右子树的结果，再判断当前节点是不是 LCA

# 为什么找到 p/q 就不往下递归了？
# 假设当前节点是 p，如果它的子树里有 q，那么 p 就是 q 的祖先，根据定义p 就是它们的 LCA，直接返回 p 即可，不用再往下找。
# 如果 p 的子树里没有 q，那也不用递归了，直接返回 p，让父节点去右子树找 q。