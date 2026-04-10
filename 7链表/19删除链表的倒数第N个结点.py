# https://leetcode.cn/problems/remove-nth-node-from-end-of-list/description/?envType=study-plan-v2&envId=top-100-liked
# 题目：给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

from typing import ListNode, Optional

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # dummy = ListNode(next=head)等价于下面两句
        dummy = ListNode() # 初始化哨兵节点:不用额外判断需要删除头节点的情况
        dummy.next = head # 哨兵节点的next指向head链表头

        left = right = dummy # 这里不能是head！！！
        # 1. 让右指针先往前走n步：循环结束后，right 与 left 相隔 n 个节点
        for _ in range(n):
            right = right.next  # 每循环一次就往前走一步

        # 2. 左右指针一起走，直到右指针走到链表末端。此时，左指针指向的节点的下一个节点就是要删除的节点。
        while right.next:
            left = left.next
            right = right.next
        left.next = left.next.next  # 删除left的下一个节点（也就是倒数第n个节点）

        return dummy.next


# 为什么左右指针一开始不是指向head而是dummy?
# 当 n 等于链表长度时，right 从 head 出发走 n 步后会变为 None。此时 right.next 会引发 AttributeError，因为 None 没有 next 属性。
# 为了处理这种情况，代码中需要额外判断 right 是否为空，并单独处理删除头节点的逻辑，增加了代码复杂度和出错可能。