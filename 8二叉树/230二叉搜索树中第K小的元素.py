# https://leetcode.cn/problems/kth-smallest-element-in-a-bst/description/?envType=study-plan-v2&envId=top-100-liked

from typing import Optional
from polars import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = 0 # 用一个外部变量记录，保存结果
        def dfs(node: Optional[TreeNode]) -> None: # 中序遍历：左 → 根 → 右
            nonlocal k, result # 内部变量修改外部变量的值，需要声明
            if not node or k <= 0:  # 递归终止条件：空节点 or 已找到（K为负数说明已经找到了），直接返回
                return None

            dfs(node.left)    # 递归左子树
            
            # 回到当前节点, 开始计数
            k -= 1 # 每访问一个节点，k 减 1
            if k == 0: # 当 k 减到 0 时，说明当前节点就是第 K 小的元素，记录结果
                result = node.val

            dfs(node.right)   # 递归右子树

        dfs(root) # 主函数调用，启动
        return result