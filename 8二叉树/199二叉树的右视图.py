# https://leetcode.cn/problems/binary-tree-right-side-view/description/?envType=study-plan-v2&envId=top-100-liked
# 题目：给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

from collections import deque
from typing import List, Optional
from polars import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 方法1：BFS 层序遍历【推荐】
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return []
        
        result = [] # 记录最终的结果
        queue = deque([root])  # 队列初始化，放入根节点
        while queue:
            q_len = len(queue)  # 易错点！！这里必须用一个变量保存当前层长度，否则在取出节点后，队列里的节点会减少，后面判断当前层最后一个节点的时候会混乱
            for i in range(q_len):  # 易错点！！遍历当前层的所有节点。注意哦：这里不能写_，因为需要用到下标
                node = queue.popleft()  # 从队头取出节点
                
                # 如果是当前层最后一个节点 → 就是右视图
                if i == q_len - 1:
                    result.append(node.val)
                
                # 把左右孩子加入队列（下一层）
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return result

# 方法2：DFS
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def dfs(node: Optional[TreeNode], depth: int) -> None: # 嵌套函数，depth 代表当前节点的深度（根节点的深度为0）。递归顺序：右 → 左，保证每层最先访问的节点是最右边的节点
            if node is None: return None

            if depth == len(result):  # result里存了多少个值 = 已经记录了多少层，当 depth == len(result) 时，说明当前节点是这一层第一次访问的节点（也是最右边的节点），记录结果
                # 例如根节点：此时result=[]，长度为0，且depth为0，说明当前节点是第0层第一次访问的节点，记录结果；
                result.append(node.val) # 记录结果
            dfs(node.right, depth + 1)  # 先递归右子树，保证首次遇到的一定是最右边的节点
            dfs(node.left, depth + 1) # 后递归左子树，保证同一层的其他节点不会覆盖结果
        dfs(root, 0) # 主函数调用，启动
        return result 