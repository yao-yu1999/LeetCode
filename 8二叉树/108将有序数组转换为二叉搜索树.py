# https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/description/?envType=study-plan-v2&envId=top-100-liked
# 题目：给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 平衡 二叉搜索树。

from typing import List, Optional
from polars import TreeNode

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 方法一：切片写法。直接调用自己【推荐】
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums: # 不要写if nums is None，因为题目保证了输入的数组是非空的，所以只需要判断是否为空列表即可。
            return None
        
        m = len(nums) // 2
        left = self.sortedArrayToBST(nums[:m])
        right = self.sortedArrayToBST(nums[m + 1:])
        return TreeNode(nums[m], left, right)
    
    
# 方法二：双指针写法，嵌套递归
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # 递归把 nums[left:right] 转成平衡二叉搜索树
        def dfs(left: int, right: int) -> Optional[TreeNode]:
            if left == right:  # 如果左右子树相等，一定是平衡二叉树。什么也不用操作
                return None
            
            m = (left + right) // 2 # 按照左右指针的区间划分，计算中点
            t = TreeNode(nums[m], dfs(left, m), dfs(m + 1, right)) # 建子树，递归建立节点：值、左孩子、右孩子
            return t  # 返回这颗树
        return dfs(0, len(nums)) # 传入数组区间