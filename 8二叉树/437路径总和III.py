# https://leetcode.cn/problems/path-sum-iii/description/?envType=study-plan-v2&envId=top-100-liked
# 题目：给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。
# 路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

from typing import List, TreeNode, Optional
from collections import defaultdict

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        cnt = defaultdict(int)  # key：前缀和(从根到 node 的节点值之和); value：前缀和的出现次数
        cnt[0] = 1 # 前缀和0的出现次数是1！
        result = 0 # 路径数

        # s 表示从根到当前节点的【父节点】的前缀和（还没加当前节点的值）
        def dfs(node: Optional[TreeNode], s: int) -> None:
            if node is None:
                return None # 推出递归

            s += node.val # 更新当前前缀和
            nonlocal result # 声明
            result += cnt[s - targetSum] # 找到了满足和为 targetSum 的路径：把 当前节点 node 当作路径的终点，统计有多少个起点。
            
            cnt[s] += 1 # 把当前前缀和加入哈希表，继续查找别的路径

            dfs(node.left, s) # 递归左右子树查找
            dfs(node.right, s)

            cnt[s] -= 1  # 恢复现场：递归返回后，要把当前节点的前缀和删掉，因为其他分支的路径不包含这个节点

        dfs(root, 0) # 传入根节点、前缀和 s = 0
        return result

# 注意:在递归过程中，哈希表只保存根到 node 的路径的前缀的节点值之和

# 为什么是s - targetSum？
# 当前路径和 = 最新前缀和 s − 旧前缀和 old
# 我们要找的是：当前路径和 = targetSum
# 移项之后 旧前缀和 old = 最新前缀和 s - targetSum

# 如果当前 s 正好等于 targetSum（让「从根节点开始的路径」也能被统计到），那么 s-targetSum = 0
# old = s - targetSum = 6 - 6 = 0，这时候，old = 0。哈希表中需要有一个cnt[0]=1

# 根到当前节点：1 → 2 → 3 → 5 → 6，前缀和为s = 17
# 我们要找路径和targetSum = 14，也就是：3 → 5 → 6
# 这条路径的旧前缀和是3，也就是：1 → 2