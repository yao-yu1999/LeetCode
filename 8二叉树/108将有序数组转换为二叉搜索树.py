# https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/description/?envType=study-plan-v2&envId=top-100-liked

from typing import List, Optional
from polars import TreeNode
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 方法一：双指针写法
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # 把 nums[left:right] 转成平衡二叉搜索树
        def dfs(left: int, right: int) -> Optional[TreeNode]:
            if left == right:
                return None
            m = (left + right) // 2
            return TreeNode(nums[m], dfs(left, m), dfs(m + 1, right))
        return dfs(0, len(nums))

# 方法二：切片写法
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums: # 不要写if nums is None，因为题目保证了输入的数组是非空的，所以只需要判断是否为空列表即可。
            return None
        m = len(nums) // 2
        left = self.sortedArrayToBST(nums[:m])
        right = self.sortedArrayToBST(nums[m + 1:])
        return TreeNode(nums[m], left, right)