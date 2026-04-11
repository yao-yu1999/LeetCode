# https://leetcode.cn/problems/course-schedule/description/?envType=study-plan-v2&envId=top-100-liked
# 题目：这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。在选修某些课程之前需要一些先修课程。 
# 先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi] ，表示如果要学习课程 ai 则 必须 先学习课程  bi 。
# 如，课程对 [0, 1] ：想要学习课程 0 ，需要先完成课程 1 。判断能否完成所有课程学习？如果可以，返回 true ；否则，返回 false 。

from polars import List
from collections import deque

# 方法一：BFS和拓扑排序【推荐】
# 因为本题，课程编号是连续的0,1,2...，所以建立邻接表可以用列表；如果不连续，可以用字典存储
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 1. 建入度表和邻接表
        in_degree = [0] * numCourses # 一维数组：统计课程表每个课程(节点)的入度，入度数量表示当前课程(节点)需要先修课的数量
        adj = [[] for _ in range(numCourses)] # 二维邻接表：记录每门课学完后可以解锁哪些课。索引i：课程编号，adj[i]表示学完 i 课后能学的课，如[[1, 2], [2], []]
        for cur, pre in prerequisites: # [[cur, pre]]，[[当前课， 先修课]]
            adj[pre].append(cur)  # 建边：pre中加入解锁课程
            in_degree[cur] += 1  # 当前课程的入度+1
        
        # 2. 将所有没有先修课的节点加入队列，这类课可以先学
        queue = deque() # 存放所有入度为0的节点：入度本身就为0的课程+解锁后的课程
        for i in range(len(in_degree)):
            if in_degree[i]==0:  # 如果当前节点的入度为0，说明可以开始学习了
                queue.append(i)  # 加入可以学习的节点：课程编号i
        
        # 3. BFS：开始一门门学课，学完课的同时解锁对应的课程
        while queue:
            pre = queue.popleft() # 弹出队首节点（表示学习了的课程）
            numCourses -= 1   # 学完一门就-1
            for cur in adj[pre]: # 同时更新邻接表中的数据
                in_degree[cur] -= 1 # 当前课程的先修课-1
                if in_degree[cur] == 0: # 如果这门课的所有先修课全部学完了
                    queue.append(cur) # 表示当前课程可以解锁了
        return numCourses==0

# 注意：列表是可变的，所以不能像in_degree = [0] * numCourses一样建立adj。即adj = [] * numCourses 是错误的
# in_degree = [0] * numCourses 或者 in_degree =[0 for _ in range(numCourses)] 

# 方法二：DFS
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 1. 构建邻接表（正向边：pre -> cur）
        adj = [[] for _ in range(numCourses)] # adj[pre] 存储所有依赖于 pre 的课程，即 pre 的后继节点。
        for cur, pre in prerequisites:
            adj[pre].append(cur)

        # 状态数组：0=未访问（初始状态），1=访问中，2=已完成
        state = [0] * numCourses

        # 2. DFS：环检测函数。pre表示需要先学习的课程
        def dfs(pre: int) -> bool:
            # （1）剪枝：在当前层判断是否有环
            if state[pre] == 1:          # 遇到访问中的节点 → 有环
                return False
            elif state[pre] == 2:          # 已确定无环，直接返回 True
                return True
            
            # （2）继续访问
            state[pre] = 1               # 标记为访问中：表示当前递归路径正在处理 pre
            for cur in adj[pre]:         # 递归遍历所有后继节点（依赖于 pre 的课程）
                if not dfs(cur):         # 如果后继递归返回 False（有环），则当前也返回 False
                    return False
            state[pre] = 2               # 所有后继cur都没有返回 False（即所有后继子图均无环），则从 pre 出发不可能有环
            
            return True

        # 3. 对每个未访问节点启动 DFS
        for i in range(numCourses):
            if state[i] == 0 and not dfs(i): # 先检查 state[i] 是否未访问；如果是，调用 dfs(i) 并检查其返回值是否为 False。state[i] == 0的时候不会直接返回False
                return False           # 发现有环，无法完成
        return True                    # 无环，可以完成
