# https://leetcode.cn/problems/maximum-depth-of-binary-tree/description/?envType=study-plan-v2&envId=top-100-liked
# 题目：给定一个二叉树 root ，返回其最大深度。二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。

from typing import Optional
from polars import TreeNode
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 方法一：后序遍历（DFS，自底向上），递归实现 【推荐】
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1 # 1是根节点的深度.每向上返回一层，深度就 +1
     
# 方法二：后序遍历（DFS，自顶向下），递归实现 【不建议】
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        result = 0
        def dfs(node: Optional[TreeNode], depth: int) -> None:
            if node is None:
                return None # 如果节点是空，就不用继续，直接返回。叶子节点既没有左孩子又没有右孩子，即左右孩子为空节点直接返回none
            depth += 1
            nonlocal result
            result = max(result, depth)
            dfs(node.left, depth)
            dfs(node.right, depth)
        dfs(root, 0)
        return result
    
# 方法三：层序遍历，队列实现。BFS，参考第102题的解答，本题不需要记录每层节点值，只需要记录最大深度。【推荐】
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        queue = deque([root]) # 初始化队列，开始时只有根节点，此时队列长度为1
        
        max_depth = 0
        while queue:
            max_depth += 1 # 每次进入下一层，深度加1
            for _ in range(len(queue)): # 遍历队列中：固定当前层要查询的节点数量（即当前层的节点数），每次循环处理一个节点
                node = queue.popleft()  # 从队列左边取出当前要处理的节点
                if node.left: # 如果左子节点存在，加入下一层队列
                    queue.append(node.left) # 这些节点将在下一轮循环中被处理，代表下一层
                if node.right: # 如果右子节点存在，加入下一层队列
                    queue.append(node.right)
        return max_depth
