# https://leetcode.cn/problems/copy-list-with-random-pointer/description/?envType=study-plan-v2&envId=top-100-liked
# 题目：给你一个长度为 n 的链表，每个节点包含一个额外增加的随机指针 random ，该指针可以指向链表中的任何节点或空节点。
# 构造这个链表的 深拷贝。 深拷贝应该正好由 n 个 全新 节点组成，其中每个新节点的值都设为其对应的原节点的值。
# 新节点的 next 指针和 random 指针也都应指向复制链表中的新节点，并使原链表和复制链表中的这些指针能够表示相同的链表状态。复制链表中的指针都不应指向原链表中的节点

from typing import Optional
from xml.dom import Node

"""
# 常规链表的节点定义：
class Node:
    def __init__(self, x: int, next: 'Node' = None):
        self.val = int(x)
        self.next = next

# 本题链表的节点定义：
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# 方法1：哈希表【推荐】
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return None # 剪枝
        dic = {} # 初始化一个哈希表：存放原节点和新节点的键值对

        # 1. 复制链表
        cur = head # cur第一次指向原链表头节点
        while cur:
            dic[cur] = Node(cur.val)  # dic[原节点] = 新节点，以原节点为键创建与原节点值相同的新节点的映射字典（值与原节点相同，next和random暂时为None）,并向dic中键为"cur"中添加入该新节点，构建键值对 (原cur节点：新cur节点）
            cur = cur.next # 遍历至原链表的下一个节点
        
        # 2. 构建新链表
        cur = head # cur第二次指向原链表头节点
        while cur:
            dic[cur].next = dic.get(cur.next) # 构建新链表节点的next指针：从dic表中找到原节点下一个 对应的 新节点。并让新节点指向下一个新节点
            dic[cur].random = dic.get(cur.random) # 构建新链表节点的random指针：从dic表中找到原节点随机 对应的 新节点。并让新节点指向随机新节点
            cur = cur.next

        return dic[head] # 返回新链表的头节点：从dic表中找到“原链表头节点head”所对应的新节点，即新链表的头节点
    
# 注意：该方法中，新链表，新节点都是以哈希表中的值的形式出现的 
   
# 答疑1：为什么使用 dic.get(key) 而不是 dic[key]？
# 因为当 cur.next 或 cur.random 为 None 时，None 不是字典的键。如果使用 dic[None] 会抛出 KeyError.

# 答疑2：为什么使用Node(cur.val) 创建新节点，而不是Node(cur)？
# 因为Node(cur.val) 正确地创建了一个值相同的新节点，其 next 和 random 指针后续会单独设置，与原节点无关。
# 而Node(cur) 不仅没有复制 next 和 random（因为构造器只接收 val），还让新节点的 val 指向了原节点，这破坏了深拷贝的独立性，不符合题意


# 方法2：拼接+拆分
# 把新链表和旧链表「混在一起」，依次复制原链表的每个节点，把新节点直接插到原节点的后面，形成一个交错链表：1→1′→2→2′→3→3′
# 然后再遍历交错链表，构建新链表的 random 指针：如果原节点的 random 指向某个节点，那么新节点的 random 就指向这个节点的下一个节点（即新节点）
# 最后再把交错链表拆分成两个链表：把原链表的节点删除，剩下的就是新链表
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        # 第一次遍历
        cur = head
        while cur:
            cur.next = Node(cur.val, cur.next) # 创建一个和原节点的值相同，next指向原节点的next。让原节点的next指针指向这个新节点（插在 cur 和 cur.next 中间）
            cur = cur.next.next  # 跳过新节点，继续遍历下一个原节点

        # 第二次遍历
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next # 新节点的random = 原节点random指向的节点的下一个（即对应复制节点）
            cur = cur.next.next  # 跳过新节点，继续遍历下一个原节点

        # 拆分交错链表，分离出新链表
        dummy = Node(0)  # 创建虚拟头节点，记录新链表
        cur = dummy       # 用cur指针遍历拼接新链表
        while head:       # head 遍历原链表
            cur.next = head.next # 取出新节点，接到dummy后面
            cur = cur.next
            head.next = head.next.next # 恢复原链表的next（拆分）
            head = head.next

        return dummy.next  # 返回新链表的头节点