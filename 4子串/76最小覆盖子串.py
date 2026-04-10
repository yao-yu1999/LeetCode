# https://leetcode.cn/problems/minimum-window-substring/description/?envType=study-plan-v2&envId=top-100-liked
# 题目：给定两个字符串 s 和 t，长度分别是 m 和 n，返回 s 中的 最短窗口 子串，使得该子串包含 t 中的每一个字符（包括重复字符）。如果没有这样的子串，返回空字符串 ""。
import collections
from collections import defaultdict

# 写法1：diff 数组 + geCnt（计数差值法）【推荐】
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 1.初始化差值数组和答案区间指针
        diff = defaultdict(int)  # 差值字典 = 窗口每种字母个数 - 字符串t每种字母个数。
        for c in t: # 遍历t中的所有字符：每个字符都初始化 diff 为 t 的“负计数”，每出现一个字符，就表示窗口中还需要补齐多少的字符。
            diff[c] -= 1
        k = len(diff)  # 常量：t 中有多少种不同的字母。当窗口内字符的种类数k ≥ 字符串t 中字符的种类数时，说明窗口一定涵盖了 t
        
        result_left, result_right = -1, len(s) # 记录最短答案区间：初始值设为-1和len(s)，这样第一次比较时任何合法窗口都会更短。
        win_cnt = 0  # 表示窗口有多少种字符已经达标：窗口内有 win_cnt 种字母的出现次数 >= t 中相应字母的出现次数g。即该字符的 diff[ch] >= 0，差值为正，说明已经满足了
        
        # 2. 开始扩大和收缩窗口
        left = 0 # 滑动窗口的左边界指针，初始指向 s[0]
        for right,c in enumerate(s):  # 遍历字符串s
            # （1） 右端点字母移入窗口
            diff[c] += 1  # 对应字符数差值+1
            if diff[c] == 0:  # 原来窗口内 c 的出现次数比字符串t 的少，现在一样多
                win_cnt += 1  # 从 表示该字符已经达标
            
            # 在涵盖t的基础上：用while持续收缩
            while win_cnt == k:  
                # （2-1）先更新答案区间的左右端点，防止后面移除不符合条件时，不会影响这里的记录
                if right - left < result_right - result_left:  
                    result_left, result_right = left, right  
                
                # （2-2）再移出窗口左端点的字符：开始找更短的窗口
                x = s[left]  # 字符串s的左端点字母
                if diff[x] == 0: # 先判断移出字符 x 是否会破坏该字符的达标状态
                    win_cnt -= 1  # 如果差值是0，说明会将达标数减少（这里用于退出循环）
                # 否则，说明这个左端点的字符时多余的，可以移出窗口
                diff[x] -= 1  # 字符串s左端点字母移出窗口
                left += 1 # 左指针继续向右收缩窗口

        return "" if result_left < 0 else s[result_left: result_right + 1] # 如果答案区间左端点<0，返回空串，否则返回答案区间

# 注1：diff用defaultdict， 比 Counter 快。
# 注2：diff的初始化：
# 如 t = "ABC"，则 diff 变为：{'A': -1, 'B': -1, 'C': -1}。表示目前还缺少 1 个 A、1 个 B、1 个 C（因为窗口是空的）
# 如果 diff[c] 是正数 → 窗口内该字符比字符串 t 需要的多（多余）;如果是 0 → 窗口内该字符数量刚好等于字符串 t 需要的数量; 如果是负数 → 窗口内该字符数量还不够字符串 t 需要的数量（缺少）。    


# 写法2：need 字典 + needCnt（需求计数法）
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need=collections.defaultdict(int)
        for c in t:
            need[c]+=1
        needCnt=len(t)
        i=0
        res=(0,float('inf'))
        for j,c in enumerate(s):
            if need[c]>0:
                needCnt-=1
            need[c]-=1
            if needCnt==0:       #步骤一：滑动窗口包含了所有T元素
                while True:      #步骤二：增加i，排除多余元素
                    c=s[i] 
                    if need[c]==0:
                        break
                    need[c]+=1
                    i+=1
                if j-i<res[1]-res[0]:   #记录结果
                    res=(i,j)
                need[s[i]]+=1  #步骤三：i增加一个位置，寻找新的满足条件滑动窗口
                needCnt+=1
                i+=1
        return '' if res[1]>len(s) else s[res[0]:res[1]+1]    #如果res始终没被更新过，代表无满足条件的结果
