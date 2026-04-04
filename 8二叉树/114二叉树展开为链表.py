# https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/description/?envType=study-plan-v2&envId=top-100-liked

from typing import Optional
from polars import TreeNode

# 方法一：头插法
# 按照前序遍历的逆序顺序遍历： 右 → 左 → 根。然后，从最后一个节点开始，倒着往前拼接链表。
class Solution:
    head = None # 类变量：保存当前已经拼好的链表的头节点（放在外面）
    def flatten(self, root: Optional[TreeNode]) -> None: 
        if root is None: return None # 空节点直接返回

        self.flatten(root.right) # 先递归右子树（必须先右！）
        self.flatten(root.left) # 再递归左子树
        
        root.left = None # 清空左指针 
        root.right = self.head  # 头插法：当前节点.next = 已经建好的链表头
         
        self.head = root  # 当前节点成为新的链表头

# 嵌套函数版本：把 head 放在外部变量里，避免类变量的副作用【推荐】
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        head = None  # 定义一个外部变量 head，保存当前已经拼好的链表的头节点
        
        def dfs(node: Optional[TreeNode]) -> None:
            nonlocal head  # 声明用外部的 head
            if node is None: return None

            dfs(node.right)
            dfs(node.left)

            node.left = None # 清空左指针
            node.right = head # 头插法：当前节点.next = 已经建好的链表头

            head = node # 让当前节点成为新的链表头
        
        dfs(root) # 主函数调用，启动
        return None # 注意：题目要求返回 None，修改原树结构即可

# 注:为什么不用尾插法？
# 尾插法需要：记住当前链表的最后一个节点（尾巴）；每次把新节点挂在 tail.right；再更新 tail = tail.right
# 但问题是前序遍历过程中，会破坏树结构！因为在遍历时，树的左右孩子还在，一边遍历一边要修改 right 指针，容易把原本树结构弄丢，导致递归走丢
# 比如遍历 1 之后，立刻把 1.right = 2，但原来的 1.right 是 5，你还没递归到 5 呢

# 方法二：分治
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None: return None # 空节点返回 None
        
        left_tail = self.flatten(root.left) # 递归拉平左子树，返回左子树链表的最后一个节点
        right_tail = self.flatten(root.right) # 递归拉平右子树
        
        if left_tail: # 如果左子树存在，才需要拼接
            left_tail.right = root.right  # 左链表尾 → 右链表头 
            root.right = root.left  # 根节点 → 左链表头       
            
            root.left = None  # 清空左指针          
        
        return right_tail or left_tail or root # 返回当前整棵树链表的尾节点
