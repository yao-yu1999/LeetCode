# https://leetcode.cn/problems/sort-list/solutions/2993518/liang-chong-fang-fa-fen-zhi-die-dai-mo-k-caei/?envType=study-plan-v2&envId=top-100-liked
# 结合876和21题
from typing import Optional

# 方法1：归并排序（分治）
#  Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # ====================== 1. 找中点 + 切链（876题核心）======================
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head  # 快慢指针都从头开始
        pre = None          # 初始化，用来标记 slow 的前一个节点（断链），它只需要指向某个已存在的节点，不需要存值，一开始还没有前节点，当然是 None！
        
        while fast and fast.next:  # 快指针走到尾
            pre = slow             # 先让 pre 走一步，指向 当前的 slow 指向的节点
            slow = slow.next       # 慢指针再走一步，pre没有动。实际上pre就是slow的前一个。
            fast = fast.next.next  # 快指针这时走两步
        # 循环结束：slow = 中点（后半段开头），pre  = 中点前一个节点

        pre.next = None   # 关键：pre 现在指向空。不再指向slow。此时中间就断开了
        return slow       # 返回slow，作为后半段的头 head2

    # ====================== 2. 合并两个有序链表（21题核心）======================
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  # 哨兵节点（不用处理头节点为空）
        cur = dummy         # 用来拼接新链表
        
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        
        cur.next = list1 or list2 # 把剩下的直接拼上 cur.next = list1 if list1 else list2
        return dummy.next # 返回哨兵节点指向的，新链表头部

    # ====================== 3. 主函数：归并排序 ======================
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None: # 递归终止条件：空 或 只有一个节点，已经有序，直接返回
            return head

        # 切
        head2 = self.middleNode(head) # 切分成：head，head2
        # 递归排序左右 
        left = self.sortList(head)   # 左半排序
        right = self.sortList(head2) # 右半排序
        # 并
        return self.mergeTwoLists(left, right) 