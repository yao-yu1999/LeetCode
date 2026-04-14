# https://leetcode.cn/problems/find-median-from-data-stream/description/?envType=study-plan-v2&envId=top-100-liked
# 题目：中位数是有序整数列表中的中间值。如果列表的大小是偶数，则没有中间值，中位数是两个中间值的平均值。
# 例如 arr = [2,3,4] 的中位数是 3 。 arr = [2,3] 的中位数是 (2 + 3) / 2 = 2.5 。
# 实现 MedianFinder 类:
# MedianFinder() 初始化 MedianFinder 对象。
# void addNum(int num) 将数据流中的整数 num 添加到数据结构中。
# double findMedian() 返回到目前为止所有元素的中位数。

# 写法一：取反。如果python版本比较老，只能用heapq(小顶堆操作)，大顶堆的操作可以取反来进行【推荐】
from heapq import heappush, heappushpop 
class MedianFinder:
    def __init__(self):
        self.left = []   # 大顶堆（用负数实现），存较小的一半。堆顶是左边最大值。
        self.right = []  # 小顶堆（正数），存较大的一半。堆顶是右边最小值。

    # 入到left时的num全部取负，出left也要取负。right的出和入均正常操作。
    # 注意：left取负，再入到right。不是入到right时要取负。
    def addNum(self, num: int) -> None:
        if len(self.left) == len(self.right): # 偶数个元素 → 添加num后要让 left 多 1 个
            heappush(self.left, -heappushpop(self.right, num)) # 把num入到right。弹出right堆顶的元素。堆顶元素取负，入到left。
        else: # 奇数个元素，left 多1 → 添加 num 后要平衡
            heappush(self.right, -heappushpop(self.left, -num)) #  把num取负，入到left。弹出left堆顶元素也要取负，入到right。

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):  # 奇数个, 中位数在left位置（因为比right多1）
            return -self.left[0]  # 取left堆顶负号即可
        else:  # 如果是偶数个，取两堆的堆顶的平均值即可
            return (-self.left[0] + self.right[0]) / 2.0
    

# 写法二：直接使用最新的库函数
from heapq import heappush, heappushpop # 小顶堆
from heapq import heappush_max, heappushpop_max # 大顶堆（版本过旧可能没有大顶堆操作，需要取反）

class MedianFinder:
    def __init__(self):
        self.left = []   # 大顶堆：堆中存放数组中更小的一批的值。堆顶是左边最大值。
        self.right = []  # 小顶堆：堆中存放数组中更大的一批的值。堆顶是右边最小值。

    def addNum(self, num: int) -> None:
        if len(self.left) == len(self.right): # 偶数个元素 → 添加num后要让 left 多 1 个
            heappush_max(self.left, heappushpop(self.right, num)) # 把 num 放进 right，弹出right最大值，将最大值插入left
        else: # 奇数个元素，left 多1 → 添加 num 后要平衡
            heappush(self.right, heappushpop_max(self.left, num)) # 把num放进left , 弹出left 的最小值，将最小值插入right

    def findMedian(self) -> float:
        if len(self.left) > len(self.right): # 奇数个, 中位数是left的最大值
            return self.left[0]
        else:  # 如果是偶数个，取两堆的堆顶的平均值即可
            return (self.left[0] + self.right[0]) / 2.0  
    
