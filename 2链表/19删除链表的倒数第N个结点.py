# https://leetcode.cn/problems/remove-nth-node-from-end-of-list/description/?envType=study-plan-v2&envId=top-100-liked
from typing import ListNode, Optional

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 1. 初始化哨兵节点和左右指针，并让他们都指向哨兵
        dummy = ListNode() # 初始化哨兵节点:不用额外判断需要删除头节点的情况
        dummy.next = head # 哨兵节点的next指向head链表头
        left = dummy
        right = dummy

        # 2. 让右指针先往前走n步
        for i in range(n):
            right = right.next  # 每循环一次就往前走一步

        # 3. 左右指针一起走，直到右指针走到链表末端
        while right.next:
            left = left.next
            right = right.next
        
        # 4. 删除left的下一个节点（也就是倒数第n个节点）
        left.next = left.next.next

        # 5. 返回新链表的头
        return dummy.next