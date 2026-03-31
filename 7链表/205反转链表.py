# https://leetcode.cn/problems/reverse-linked-list/description/?envType=study-plan-v2&envId=top-100-liked
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
        cur = head # cur指针指向单链表的头节点

        while cur: # 当cur不为null时，继续循环
            nxt = cur.next # nxt记录cur的下一个节点
            cur.next = pre # 反转：把 cur 插在 pre 链表的前面。
            pre = cur # 更新
            cur= nxt
        return pre # 最后返回pre指向的链表
