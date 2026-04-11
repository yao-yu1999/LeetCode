# https://leetcode.cn/problems/binary-tree-level-order-traversal/description/?envType=study-plan-v2&envId=top-100-liked
# 【模板题】题目：给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）
# 思路：使用队列实现二叉树的层序遍历，按层访问每个节点，并将每层的节点值存储在一个列表中，最终返回包含所有层节点值的列表。
# 因为题目要求输出格式是：[[第一层], [第二层], [第三层]]，所以需要两个数组

from collections import deque
from typing import List, Optional
from polars import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []  # 如果根节点是空，直接返回空列表
        result = [] # 用来记录全局所有层的返回结果

        queue = deque([root]) # deque初始化一个队列：存放每一层待处理的节点
        while queue: # 当队列中的节点不为空
            vals = []  # 临时存放【当前这一层】的值
            for _ in range(len(queue)): # 固定当前队列的所有节点，只用查询这一层的，不用担心下一层的污染
                node = queue.popleft() # 从队列左边选取节点
                vals.append(node.val) # 开始往vals数组，加入该节点的值

                # 把下一层节点放进队列，接在后面。如果该节点有左/右孩子就放进队列
                if node.left: 
                    queue.append(node.left)
                if node.right: 
                    queue.append(node.right)
            result.append(vals) # 当前层处理完了，把这一层加入最终结果
        return result