# https://leetcode.cn/problems/implement-trie-prefix-tree/?envType=study-plan-v2&envId=top-100-liked

class TreeNode:
    __slots__ = 'son', 'end' # 限制 TreeNode 实例只能拥有 son 和 end 这两个属性，不能动态添加其他属性

    def __init__(self):
        # 每个TreeNode实例都有的两个属性。如root.son(根节点的 son 字典), cur.son(cur 所指向的那个 TreeNode 实例的 son 字典)
        self.son = {} # 子节点映射，用于存储当前节点的所有子节点：键为字符，值为子节点（另一个 TreeNode 实例，代表沿着该字符路径到达的下一个节点）
        self.end = False # 布尔值，默认是False。表示是否是单词结尾。区分“仅前缀”和“完整单词”，插入时，默认为True

class Trie:
    def __init__(self):
        # 每个Trie 实例的一个属性root
        self.root = TreeNode()  # 初始化时：创建根节点

    # 插入：遍历字符，创建缺失的节点，最后标记 end=True
    def insert(self, word: str) -> None:
        cur = self.root # 从根节点开始
        for c in word: # 遍历单词的每一个字符
            if c not in cur.son:  # 如果c不在cur.son中
                cur.son[c] = TreeNode()  # 那就创建新节点
            cur = cur.son[c] # 从子节点开始遍历
        cur.end = True # 遍历结束后，将end设为True（表示插入了一个完整的单词）

    # 由于search和startwith都需要沿着路径查找, 可以抽象一个find方法，返回的是一个状态:
    # 0：路径不存在
    # 1：路径存在且不是一个完整单词（仅前缀）
    # 2：路径存在且是一个完整单词
    def find(self, word: str) -> int:
        cur = self.root # 从根节点开始
        for c in word: # 遍历单词的每一个字符
            if c not in cur.son:  # 如果c不在cur.son中
                return 0 # 此时不是创建咯，而是说明没有找到
            cur = cur.son[c] # 从下一个子节点开始遍历
        
        return 2 if cur.end else 1 # 如果end是True，则返回2（完整单词），否则返回1（这个词作为前缀存在，但不是完整的单词）

    def search(self, word: str) -> bool:
        return self.find(word) == 2 # 当时

    def startsWith(self, prefix: str) -> bool:
        return self.find(prefix) != 0 # 包含完整单词和不完整单词，都视作前缀
        
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)