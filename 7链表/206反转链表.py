# https://leetcode.cn/problems/reverse-linked-list/description/?envType=study-plan-v2&envId=top-100-liked
# 给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。

from typing import ListNode, Optional

# 头插法（迭代）

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None # 初始化一个新链表，pre指向新链表的头节点，初始时新链表为空，所以pre为null
        cur = head # cur指针指向单链表的头节点当链表断开时，cur指向剩下链表的头节点

        while cur: # 当cur不为null时（即走到尾部，指向Null），继续循环
            nxt = cur.next # 关键！！！提前nxt记录cur的下一个节点（cur后面要过来的）
            cur.next = pre # 反转指针：把 cur 反过来插在 pre 链表的前面。
            pre = cur # 先移动pre：pre指向新链表的头节点
            cur= nxt # 再移动cue
        return pre # 最后返回pre指向的链表
