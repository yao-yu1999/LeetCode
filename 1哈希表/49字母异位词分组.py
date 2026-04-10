# https://leetcode.cn/problems/group-anagrams/description/?envType=study-plan-v2&envId=top-100-liked
# 题目：给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
# 输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]，输出: [["bat"],["nat","tan"],["ate","eat","tea"]]
# 要点：字母异位词经过排序后一定相同，将用排序后的字符串当 key，原字符串当 value 存入哈希表中，最后返回哈希表的value

from collections import defaultdict
from polars import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list)  # d是一个如果需要就创建一个空列表的字典。 即key不在字典中，则自动插入一个空列表。
        for s in strs: # 遍历字符串数组的每一个字符串
            sorted_s = ''.join(sorted(s))  # 先把字符串s拆成一个个字母进行排序，再用join拼接，该字符串sorted_s作为哈希表的 key
            dict[sorted_s].append(s)  # 将当前字符串s加入到该key对应的列表；如果这个key哈希表中没有，则自动创建一个空列表
        
        return list(dict.values())  # 取哈希表的value，并用list转换为标准的列表， 保存分组后的结果