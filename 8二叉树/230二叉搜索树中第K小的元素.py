# https://leetcode.cn/problems/kth-smallest-element-in-a-bst/description/?envType=study-plan-v2&envId=top-100-liked
# 题目：给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第 k 小的元素（k 从 1 开始计数）。
# 思路：二叉搜索树保证了，按照中序遍历，一定是升序的！
from typing import Optional
from polars import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 中序遍历
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = 0 # 返回第 k 小的元素的值
        count=0 # 计数，数到k就停止
        
        def dfs(node: Optional[TreeNode]) -> None: # 中序遍历：左 → 根 → 右
            nonlocal count, result # 内部变量修改外部变量的值，需要声明
            
            if node is None or count >= k:  # 递归终止条件：空节点 or 已找到（count为K说明已经找到了），return None 退出递归
                return None

            dfs(node.left)    # 1. 递归左子树
            
            # 2. 当前节点, 开始计数
            count += 1 # 每访问一个节点，计数加1
            if count == k: # 当 计数==k 时，说明当前节点就是第 K 小的元素，记录结果
                result = node.val

            dfs(node.right)   # 3. 递归右子树

        dfs(root) # 主函数调用，启动
        return result