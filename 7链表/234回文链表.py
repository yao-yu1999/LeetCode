# https://leetcode.cn/problems/palindrome-linked-list/description/?envType=study-plan-v2&envId=top-100-liked
# 题目：给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。
# 先找到中点，再翻转后半部分。

from typing import ListNode, Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = head
        while cur:
            nxt = cur.next

            cur.next =pre
            pre = cur
            cur= nxt
        return pre

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        mid = self.middleNode(head)  # 找到链表的中点
        head2 = self.reverseList(mid)  # 从mid开始反转,得到后半部分链表的头节点head2
        
        while head2: # 只要head2不为null，就继续比较
            if head.val != head2.val:  # 只要发现值不等就返回false，说明不是回文链表
                return False
            
            head = head.next  # 后移，继续比较
            head2 = head2.next
        return True  # 所有节点都比较完且都相等, 再返回

# 为什么while循环不能用while head:
# 因为head 是整条链表（只是找到了中点，并没有断开两条链表），走到最后才停。head2 是后半段，长度只有一半。以head2为准。