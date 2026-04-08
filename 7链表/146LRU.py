# https://leetcode.cn/problems/lru-cache/description/?envType=study-plan-v2&envId=top-100-liked

# 双向链表+哈希表
class DLinkedNode: # 双向链表的节点：包含键、值、前驱指针和后继指针
    __slots__ = 'key', 'value', 'prev', 'next'
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity # 缓存的最大容量
        self.cache = {} # 存储字典：将每个缓存的key映射到它在双向链表中对应的节点（DLinkedNode 对象）
        self.size = 0 # 当前已存储的键值对数量

        # 哨兵头节点：不存任何数据，实际节点始终插入在 head 之后（成为新的第一个节点）
        self.head = DLinkedNode() # head.next 指向最近使用的节点
        # 哨兵尾节点：不存任何数据
        self.tail = DLinkedNode() # tail.prev 指向最久未使用的节点
        # 相互连接：head -> tail，head <- tail
        self.head.next = self.tail
        self.tail.prev = self.head
        

    # ---------- 双向链表操作 ----------
    def _add_to_head(self, node: DLinkedNode) -> None:
        """将节点插入到头部(head之后)""" # 顺序不能反：先操作新节点的前驱和后继，再操作原来头节点的前驱，最后让哨兵节点指向新节点
        node.prev = self.head # 新节点的前驱指向哨兵头节点
        node.next = self.head.next # 新节点的后继指向原来的第一个节点(即head指向的第一个节点head.next)
        self.head.next.prev = node # 原来的第一个节点的前驱指向新节点
        self.head.next = node # 原来的第一个节点指向新节点

    def _remove_node(self, node: DLinkedNode) -> None:
        """从链表中删除节点""" # 让 node 的前驱和后继直接相连，跳过 node。node 不再被链表中的任何节点引用，隐式删除
        node.prev.next = node.next 
        node.next.prev = node.prev

    def _move_to_head(self, node: DLinkedNode) -> None:
        """将节点移动到头部""" # 移动可以分解为两步：先删除节点（从原位置取出），再插入到头部
        self._remove_node(node) 
        self._add_to_head(node)

    def _remove_tail(self) -> DLinkedNode:
        """删除尾部节点并返回它""" # 获取最久未使用的节点（即 tail 的前一个节点），从链表中删除它，并返回该节点
        node = self.tail.prev
        self._remove_node(node)
        return node # 要从哈希表中删除，需要知道这个节点的键

    # ---------- 对外接口 ----------
    def get(self, key: int) -> int:
        if key not in self.cache: # 如果key不在哈希表里面，返回-1
            return -1
        node = self.cache[key]  # 否则，取出节点
        self._move_to_head(node) # 先将该节点移动到链表头部【重点，只要访问了key就要移到头部】
        return node.value # 再返回节点的值

    def put(self, key: int, value: int) -> None:
        if key in self.cache: # 如果key存在在哈希表中
            node = self.cache[key] # 取出节点
            node.value = value # 先更新值
            self._move_to_head(node) # 再将其移到链表头部
        else: # 如果不存在
            new_node = DLinkedNode(key, value) # 创建一个双向链表的节点
            self.cache[key] = new_node # 先将节点加入哈希表
            self._add_to_head(new_node) # 再添加到链表头部
            self.size += 1 # 存储长度+1
            if self.size > self.capacity:  # 如果当前长度超过了最大容量，需要把最久未使用的节点删除
                removed = self._remove_tail() # 取出需要删除的尾部节点（删除需要keykey）
                del self.cache[removed.key] # del执行删除，del是删除哈希表（字典）中指定 key 的键值对操作
                self.size -= 1 # 长度需要-1


# 为什么用双向链表？
# 单向链表删除任意节点需要前驱节点，而双向链表可以直接通过 node.prev 获得，实现 O(1) 删除。
# 配合哨兵节点（dummy head/tail）简化边界判断