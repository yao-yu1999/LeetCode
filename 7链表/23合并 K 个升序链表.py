# https://leetcode.cn/problems/merge-k-sorted-lists/?envType=study-plan-v2&envId=top-100-liked
# 题目：给你一个链表数组，每个链表都已经按升序排列。请你将所有链表合并到一个升序链表中，返回合并后的链表。

from typing import List,Optional,ListNode
from heapq import heapify,heappop,heappush

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        cur = dummy = ListNode()  # 初始化哨兵节点，作为合并后新链表头节点的前一个节点
        h = [head for head in lists if head]  # 把所有非空链表的头节点入堆
        heapify(h)  # 列表转换成小顶堆
        
        while h:  # 循环直到堆为空
            node = heappop(h)  # 弹出堆中的最小节点
            if node.next:  # 当子链表不为空（下一个节点不为空）
                heappush(h, node.next)  # 下一个节点入堆，作为新链表接在后面的，下一个候选的最小节点
            cur.next = node  # 把 node 添加到新链表的末尾
            cur = cur.next  # 后移
        return dummy.next
    
#  h = [head for head in lists if head]  等价于
#  h = []
#  for head in lists:
#      if head:
#          h.append(head)