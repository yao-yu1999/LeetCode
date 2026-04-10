# https://leetcode.cn/problems/merge-two-sorted-lists/?envType=study-plan-v2&envId=top-100-liked
# 题目：将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

from typing import Optional, ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 方法1：尾插法
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 1. 初始化
        dummy = ListNode() # 哨兵节点：新链表的前一个节点（-1）
        cur = dummy  # cur用来指向加入新链表的哨兵节点

        # 2.遍历两个链表
        while list1 and list2:
            # 选择值更小的加入新链表
            if list1.val < list2.val:
                cur.next = list1  # 把list1当前节点接在新链表尾部
                list1 = list1.next # list1从下一个节点开始
            else: # 相等的话，加哪个节点都可以，这里默认是list2
                cur.next = list2  # 把list2当前节点接在新链表尾部
                list2 = list2.next # list2从下一个节点开始
            cur = cur.next # cur移动到新链表尾部
        
        # 当全部或有一个链表为空时，循环结束：将剩下的拼接在新链表后面。list1不为空则拼list1，否则拼list2。 只需要判断一个list即可，一个为空另一个一定还有
        cur.next = list1 or list2  # 或者 cur.next = list1 if list1 else list2
        
        return dummy.next # 返回新链表的真实头节点（跳过哨兵点）


# 方法2：递归法
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None: 
            return list2 # list1为空，直接返回list2
        if list2 is None: 
            return list1 # list2为空，直接返回list1

        # 选择值更小的加入新链表
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        list2.next = self.mergeTwoLists(list1, list2.next)
        return list2