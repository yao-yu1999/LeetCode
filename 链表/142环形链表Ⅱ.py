# https://leetcode.cn/problems/linked-list-cycle-ii/?envType=study-plan-v2&envId=top-100-liked
from typing import Optional, ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow =head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast is slow:  # 如果相遇，才有下面的等式
                while slow is not head: # 当a!=0时，head和slow相遇说明到达了入环口，没有则继续移动
                    slow = slow.next
                    head = head.next
                return slow # 循环结束，最终返回走了a步的slow（head）。当a=0，head就是入环口，直接返回head=slow
        return None # 根据题意，无环则返回null