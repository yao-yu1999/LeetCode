# https://leetcode.cn/problems/binary-tree-maximum-path-sum/description/?envType=study-plan-v2&envId=top-100-liked
# 题目：二叉树中的路径被定义为一条节点序列，序列中每对相邻节点之间都存在一条边。同一个节点在一条路径序列中至多出现一次。
# 该路径至少包含一个节点，且不一定经过根节点。路径和是路径中各节点值的总和。给你一个二叉树的根节点 root ，返回其最大路径和 。

from typing import List, TreeNode, Optional
from math import inf

# 后序遍历
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = -inf # 初始化答案为负无穷（应对全是负数的情况）
        
        # 返回：以当前节点 node 为起点，往下延伸的【最大链和】
        def dfs(node: Optional[TreeNode]) -> int:
            if node is None: # 没有节点，和为 0
                return 0  

            left_chain = max(dfs(node.left), 0)   # 左子树最大链和，若为负则取0（不要）
            right_chain = max(dfs(node.right), 0) # 右子树最大链和，若为负则取0

            # 更新答案
            nonlocal result
            result = max(result, left_chain + right_chain + node.val)  # 更新路径和：左链 + 当前节点 + 右链
            
            # 返回当前节点向上的最大链和：选择左链或右链中较大的一个值 + node.val（包含当前节点）
            return max(left_chain, right_chain) + node.val
        
        dfs(root)
        return result
        
# 1. 为什么 dfs 返回的是链和，而不是路径和？
# 因为路径可能以当前节点为“拐点”，需要左右两条链拼起来。如果返回路径和，父节点无法区分哪一部分是链，会造成重复计算。
# 链是单向的，父节点只能接一条链（左或右），不能同时接左右。

# 2. 为什么对子树返回值取 max(..., 0)？
# 如果子树链和为负数，加上它会使得当前链和更小，不如不接任何子节点（即只保留当前节点自身）。与最大子数组和问题思想一致：如果前面一段和为负，就抛弃它重新开始。

# 3. 全局答案更新：l_val + r_val + node.val
# 经过当前节点的最大路径和（可能只包含一个方向）：以 node 为最高点（即拐弯处），左右链分别来自左右子树（可能为空，此时对应 0），加上当前节点值。

# 4. 如果所有节点值均为负数？
# 此时左/右子树的 dfs 返回 0（因为 max(...,0)=0），所以 l_val 和 r_val 均为 0。
# result = max(result, 0+0+node.val) = max(result, node.val)。即所有节点中的最大值

# 5. 为什么不需要考虑“只取部分子链”的情况？
# 例如左子树内部可能有一条最大路径不经过左子树的根节点，这种情况已经在左子树的递归中作为 result 被更新过了，父节点不需要重复考虑。
# 父节点只负责处理以当前节点为拐点的路径，以及向上提供链。