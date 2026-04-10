# https://leetcode.cn/problems/linked-list-cycle-ii/?envType=study-plan-v2&envId=top-100-liked
# 题目：给定一个链表的头节点  head ，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 
# 思路：当快指针和慢指针相遇时，让slow和head同时开始移动，当slow is p时，说明再入环口相遇。

from typing import Optional, ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if fast is slow:  # 如果相遇，才有下面的等式。比较slow和head
                while slow is not head: # head和slow相遇说明到达了入环口，没有则继续移动
                    slow = slow.next
                    head = head.next
                return slow # 循环结束，最终返回走了a步的slow（head）。当a=0，head就是入环口，直接返回head=slow
        return None # 根据题意，无环则返回null


# head -------> 入环口 -------> 相遇点 -------> 回到入环口
#         a              b              c-b   
# 入环口 到 快慢指针相遇点 的长度 = b
# head 到入环口 的长度 = a
# 因此：
# slow 慢指针 走的路程：a + b
# fast 快指针 走的路程：a + b + n * c （n 表示快指针在环里多绕了 n 圈，环的总长度 = c）
# 又因为：fast 走的路程 = 2 × slow 走的路程 ==》 a + b + n*c = 2(a + b) ==》 a = n * c - b
# 即从slow相遇点走到入环口的距离（c - b） + 绕环 n 圈 = head走到入环口的距离a