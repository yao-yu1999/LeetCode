# https://leetcode.cn/problems/add-two-numbers/description/?envType=study-plan-v2&envId=top-100-likedS
from typing import ListNode, Optional
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 365逆序存储就是[5,6,3]，也就是把个位放在第一个节点，高位放在最后一个节点
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  # 哨兵节点
        cur = dummy # 用一个指针指向这个节点

        carry = 0  # 初始化进位，如果对应的位相加超过10，需要进1
        while l1 or l2 or carry: # 有进位或者有一个不是空节点就继续。例如23+155，在第四个节点才有空位；23+955，此时“2+9”有进位，到千位。
            if l1:
                carry = carry + l1.val # 如果有，节点值累加上进位的值
                l1 = l1.next # 移动到l1下一个节点
            if l2:
                carry = carry + l2.val # 如果有，节点值累加上进位的值
                l2 = l2.next # 移动到l2下一个节点

            # 算当前位的结果：取carry的个位
            cur.next = ListNode(carry%10) # 初始的时候cur指向的是listNode(-1), 故cur.next是当前位
            # 算进位的结果：取carry的十位
            carry = carry // 10

            cur = cur.next # 移动到新链表的下一个节点
        return dummy.next  # 当节点均为空且carry=0（无进位）则返回新链表


# 易错点：循环条件是or