# https://leetcode.cn/problems/top-k-frequent-elements/description/?envType=study-plan-v2&envId=top-100-liked
from collections import Counter, defaultdict
from polars import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. 统计每个元素的出现次数
        cnt = Counter(nums) # Counter 是 Python 自带计数器，如{1:3, 2:2, 3:1}
        
        # 2. 创建 max_cnt+1 个空列表当桶, 并在对应桶中放数字。桶下标 = 出现次数
        max_cnt = max(cnt.values()) # 找到最大出现次数，用来决定要建多少个桶
        buckets = [[] for _ in range(max_cnt + 1)]
        
        # 3. 遍历哈希表。把出现次数相同的元素，放到同一个桶中
        for num, count in cnt.items(): # 注意：遍历的是字典而不是nums数组
            buckets[count].append(num)

        result = []
        # 4. 倒序遍历 buckets，把出现次数前 k 大的元素加入答案
        # （1）因为本题题目保证，加入某个桶全部数字后就能满足K，所以可以用这个
        # for bucket in reversed(buckets):
        #     result += bucket  # 把桶里的数字全部加入答案
        #     if len(result) == k: # 满 k 个立刻返回:频率一样的数字, 全部返回
        #         return result

        # （2）但是建议这个更通用的版本，一个一个加进结果中
        for bucket in reversed(buckets): # defaultdict 是字典，不能 reversed
            for num in bucket: # 遍历桶里每一个数字，一个一个加
                result.append(num)
                if len(result) == k: # 必须写在循环里面
                    return result
            
# defaultdict()版本
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        
        # 用 defaultdict 做桶
        buckets = defaultdict(list)
        for num, count in cnt.items():
            buckets[count].append(num)  # key=频率，value=数字

        result = []
        sorted_counts = sorted(buckets.keys(), reverse=True)
        
        # 遍历排序后的频率
        for count in sorted_counts:
            for num in buckets[count]: # 取出对应频率的数字
                result.append(num)
                if len(result) == k:
                    return result