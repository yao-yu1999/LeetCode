# https://leetcode.cn/problems/middle-of-the-linked-list/description/
from typing import ListNode, Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast =head  # 用一个慢指针（一次走一步）和一个快指针（一次走两步）
        while fast and fast.next: # 当快指针存在且快指针走完链表  （如果fast不存在，也就不会判断fast.next）
            slow = slow.next
            fast = fast.next.next # 走两步
        return slow  # 当循环结束，slow指向的就是中间节点        