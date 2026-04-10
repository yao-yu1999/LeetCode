# https://leetcode.cn/problems/swap-nodes-in-pairs/description/?envType=study-plan-v2&envId=top-100-liked
# 题目：给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。
# 可以直接将25题里面的K换成2 

from typing import ListNode, Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 方法1：直接法【推荐】
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head) # 等价于dummy = ListNode() + dummy.next = head
        
        node0 = dummy # 哨兵节点（0号节点），每一组两两交换节点的前一个节点
        node1 = head  # 头节点：每一组两两交换节点的第一个节点
        while node1 and node1.next: # 至少有两个节点
            # 1. 提前记录node2和node3，防止交换的时候，不知道原先的位置：
            node2 = node1.next # node2原本是node1的下一个
            node3 = node2.next # node3原本是在node2后面的，是下一组要两两交换的第一个节点（交换后node1要指向它）

            # 2. 交换
            node0.next = node2  # 0 -> 2
            node2.next = node1  # 2 -> 1
            node1.next = node3  # 1 -> 3

            # 指针后移，每一轮只交换了两个节点。
            node0 = node1  # 下一轮的时候node0就是node1的位置（已经与node2交换了），也就是下一组交换的哨兵节点
            node1 = node3  # node3就是下一组的第一个节点node1

        return dummy.next
    
# 为什么有node0和node1？
# 不能直接移动dummy和head。因为最后要返回交换后的链表的头指针，防止链表头丢失
# node0和node1是用来标记：本组待交换的第一个节点的前一个节点和本组待交换的第一个节点。
# 每交换两个节点（实际要交换的是node1和node2,在中间位置）都要保证这样一个关系：node0 → node1 → node2 → node3

# 方法2：参考25题
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0 # 统计节点个数
        cur = head
        while cur:
            n += 1
            cur = cur.next

        p0 = dummy = ListNode(next=head)
        pre = None
        cur = head

        # k 个一组处理
        while n >= 2:
            n -= 2
            for _ in range(2):  # 同 92 题
                nxt = cur.next
                cur.next = pre  # 每次循环只修改一个 next，方便大家理解
                pre = cur
                cur = nxt

            # 见视频
            nxt = p0.next
            nxt.next = cur
            p0.next = pre
            p0 = nxt
        return dummy.next