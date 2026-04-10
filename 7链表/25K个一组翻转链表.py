# https://leetcode.cn/problems/reverse-nodes-in-k-group/description/?envType=study-plan-v2&envId=top-100-liked
# 题目：给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
# 24的升级版。
# 92题：指定区间的节点反转链表。205题：整个链表的反转

from typing import ListNode, Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 1. 统计节点个数
        n = 0 
        cur = head 
        while cur:
            n += 1
            cur = cur.next

        # 2. 创建哨兵节点 + 初始化指针
        node0 = dummy = ListNode(next=head) # dummy防止链表头丢失。node0表示每组的前一个节点，用于看守
        pre = None # 翻转后的前一个节点
        cur = head # 表示当前正在翻转的节点

        # 3. k 个一组处理
        while n >= k: # 当初始链表或剩下的节点数满足 k 个一组时
            n -= k # 更新剩下的节点数。用于判断是否退出循环
            
            # 翻转 k 个节点：反转链表（205题和92题）
            for _ in range(k): 
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt

            nxt = node0.next # 保存当前组的尾节点（翻转前的本组第一个节点）
            nxt.next = cur # 当前组的尾节点，指向下一组的头节点
            node0.next = pre  # 当前组的前驱指向本组的头节点
            node0 = nxt # 更新node0为下一组的前驱（此时为nxt）
            
        return dummy.next
        