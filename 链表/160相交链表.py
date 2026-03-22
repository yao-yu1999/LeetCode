# https://leetcode.cn/problems/intersection-of-two-linked-lists/description/?envType=study-plan-v2&envId=top-100-liked
from typing import ListNode, Optional

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p, q = headA, headB  # 用两个指针，分别指向两个头节点
        while p is not q: # 当他们没有相交时
            p= p.next if p else headB  # 如果p不为空，就继续往下走；如果p为空了，就让p指向headB
            q = q.next if q else headA  # 如果q不为空，就继续往下走；如果q为空了，就让q指向headA
        return p # 相交则返回任意一个指针；不相交则返回None（因为p和q的终点，都为None）