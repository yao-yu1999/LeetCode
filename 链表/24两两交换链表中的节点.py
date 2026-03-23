# https://leetcode.cn/problems/swap-nodes-in-pairs/description/?envType=study-plan-v2&envId=top-100-liked

from typing import ListNode, Optional
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        node0 = dummy # 哨兵节点
        node1 = head  # 头节点

        while node1 and node1.next: # 至少有两个节点
            # 提前记录node2和node3，防止交换的时候，不知道原先的位置：
            node2 = node1.next # node2原本是node1的下一个
            node3 = node2.next # node3原本是在node2后面的，是下一组要交换的第一个节点（交换后node1要指向它）

            # 核心步骤
            node0.next = node2
            node2.next = node1
            node1.next = node3

            # 指针后移，每一轮只交换了两个节点。
            node0 = node1  # 下一轮的时候node0就是node1的位置（已经与node2交换了），也就是下一组交换的哨兵节点
            node1 = node3  # node3就是下一组的第一个节点node1

        return dummy.next