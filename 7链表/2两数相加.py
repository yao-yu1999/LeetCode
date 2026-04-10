# https://leetcode.cn/problems/add-two-numbers/description/?envType=study-plan-v2&envId=top-100-likedS
# 题目：给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。将两个数相加，并以相同形式返回一个表示和的链表。

from typing import ListNode, Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 365逆序存储就是[5,6,3]，也就是把个位放在第一个节点，高位放在最后一个节点。链表头节点是个位
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  # 创建哨兵节点
        cur = dummy # 用一个指针指向这个节点

        carry = 0  # 初始化进位为0，如果对应的位相加超过10，需要进1
        while l1 or l2 or carry: # 有进位或者有一个链表不为空就继续。例如23+155，虽然l1空了，但时l2还有数字；23+955，此时“2+9”有进位，到千位。
            if l1:
                carry = carry + l1.val # 如果 l1 这个位置还有数字，就加到进位里
                l1 = l1.next # 移动到l1下一个节点
            if l2:
                carry = carry + l2.val # 如果 l2 这个位置还有数字，就加到进位里
                l2 = l2.next # 移动到l2下一个节点

            # carry = 经过l1或l2或两个都有的累加后，可能变成18这种数字：包含了个位8和进位1。
            # 算当前位的结果（要存进链表的节点）：取carry的个位
            cur.next = ListNode(carry%10) # 初始的时候cur指向的是listNode(-1), 故cur.next是当前位
            # 算进位的结果（要带到下一位继续算/下一轮中会使用）：取carry的十位
            carry = carry // 10

            cur = cur.next # 把指针移到最后，准备接下一个新节点
        return dummy.next  # 当节点均为空且carry=0（无进位）则返回新链表


# 易错点：循环条件是or