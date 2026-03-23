# https://leetcode.cn/problems/delete-node-in-a-linked-list/description/

# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node:  # 因为题目保证给定的节点 node 不是链表中的最后一个节点，所以这里永远都是True，可以去掉
            node.val = node.next.val
            node.next = node.next.next
        