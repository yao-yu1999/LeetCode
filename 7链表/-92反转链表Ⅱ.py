# https://leetcode.cn/problems/reverse-linked-list-ii/
# 题目：给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。

from typing import Optional, ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        node0 = dummy = ListNode(next=head) # 创建哨兵节点 dummy，其 next 指向原 head。node0 初始化位指向dummy。
        # 将node0移动到left的前一个节点
        for _ in range(left - 1):
            node0 = node0.next
        cur = node0.next # cur 指向当前要反转的第一个节点（即原 left 节点）
        
        pre = None # 反转后的新头的前驱（最终会指向反转部分的末尾）
        # 开始反转：反转从 left 到 right 的节点（共 right-left+1 个节点）
        for _ in range(right - left + 1):
            nxt = cur.next  # 保存下一个节点
            cur.next = pre  # 反转指针
            pre = cur # 移动 pre 到当前节点
            cur = nxt # 移动 cur 到下一个节点（待处理的节点）

        # 将反转后的子链表接回原链表
        node0.next.next = cur # 将原 left 节点（现在是尾节点）的 next 指向 cur
        node0.next = pre # 将 node0 的 next 指向反转后的新头节点 pre

        return dummy.next
    
# node0 = dummy = ListNode(next=head) 等价于这三句
# dummy = ListNode()
# dummy.next = head
# node0 = dummy