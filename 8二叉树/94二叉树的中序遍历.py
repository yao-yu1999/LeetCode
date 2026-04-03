# https://leetcode.cn/problems/binary-tree-inorder-traversal/description/?envType=study-plan-v2&envId=top-100-liked


from polars import List
from polars import TreeNode

# 逆序压栈才能保证正确的弹出顺序，第一次入栈时，flag=0，表示需要展开该节点的子树；第二次入栈时，flag=1，表示该节点已经展开过了，可以直接出栈输出了。

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = [(0, root)]          # 根节点第一次入栈，flag=0
        
        while stack:
            flag, node = stack.pop()   # 取出栈顶元素
            if node is None:           # 空节点直接跳过
                continue
            
            if flag == 0:              # 第一次遇到：需要展开该节点的子树
                # 按"右->根->左"的"逆中序"顺序入栈
                stack.append((0, node.right))   # 右子节点（第一次入栈）
                stack.append((1, node))         # 当前节点标记为1后入栈（第二次）
                stack.append((0, node.left))    # 左子节点（第一次入栈）
            else:                      # 第二次遇到(flag == 1):直接输出
                res.append(node.val)
        
        return res
    
# 答疑：为什么为什么根节点要标记为 1
# 因为根节点在展开时被重新入栈，并且标记为 1。当它再次出现在栈顶时，说明它的左右子树都已经处理完毕（已经被展开并弹出），此时可以直接输出根节点的值。

# 为什么要用 flag（0 和 1）？
# 因为递归有两个阶段：第一次遇到节点：刚进入，要先处理子树；第二次遇到节点：子树处理完了，可以输出自己