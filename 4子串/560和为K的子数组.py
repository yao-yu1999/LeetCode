
from collections import defaultdict
from polars import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int)  # 哈希表：记录每个前缀和出现过多少次
        cnt[0] = 1              # 初始：前缀和 0 出现 1 次（最关键）
        result = 0              # 最终：统计多少个符合条件
        s = 0                   # 当前前缀和

        for x in nums:          # 遍历数组中每个数字
            s += x              # 计算当前前缀和，前缀和计算公式：s[i+1] = s[i] + nums[i]
            result += cnt[s-k]  # 查询字典cnt中，出现过多少次 s−k → ans = ans + 本次新找到的个数
            cnt[s] += 1         # 把当前前缀和存入字典：如果有重复的前缀和，就把它的出现次数加1，如果没有，就把它的出现次数设为1

        return result