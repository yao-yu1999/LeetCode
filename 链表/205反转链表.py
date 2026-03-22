# https://leetcode.cn/problems/reverse-linked-list/description/?envType=study-plan-v2&envId=top-100-liked
from typing import ListNode, Optional

# 头插法（迭代）
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = head
        while cur:
            nxt = cur.next  # 用一个变量nxt，记录当前节点指向的下一个节点
            cur.next = pre  # 把 cur 插在 pre 链表的前面
            pre = cur
            cur = nxt
        return pre
