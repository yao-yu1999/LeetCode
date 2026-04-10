# https://leetcode.cn/problems/spiral-matrix/description/?envType=study-plan-v2&envId=top-100-liked
# 题目：给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。

from polars import List

# 方法一：用方向数组DIRS模拟右下左上移动,遍历m*n次,将matrix[i][j]加入结果并标记已访问,遇到边界或已访问则转向,最终返回螺旋序列。【推荐】
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        di = 0  # 方向数组的索引:0,1,2,3

        m, n = len(matrix), len(matrix[0])
        result = []
        
        i=j=0 # 正在访问的格子
        for _ in range(m*n): # 共计要走的步数   
            result.append(matrix[i][j]) # 先把当前字符添加进去并标记已经访问过
            matrix[i][j] = None

            # 预测下一步的位置并判断是否越界：如果下一步的位置 (x, y) 出界了或者已经访问过，就更新方向
            x = i + DIRS[di][0]
            y = j + DIRS[di][1]
            if x<0 or x>=m or y<0 or y>=n or matrix[x][y] is None:
                di = (di+1)%4  # 取模。不是 di += 1，因为如果di=4，就超过方向数组索引了。

            # 更新i,j：按照新的方向走下一步
            i = i + DIRS[di][0]
            j = j + DIRS[di][1]

        return result
    

# 方法二：维护l、r、t、b四个边界,按左→右、上→下、右→左、下→上遍历,每轮收缩边界,边界交叉时结束,返回螺旋结果。
'''
从左到右,顶部一层遍历完往下移一位,top++;
从上到下,遍历完右侧往左移一位,right--;
从右到左,判断top <= bottom,即是否上下都走完了。遍历完底部上移,bottom--;
从下到上,判断left <= right,遍历完左侧右移,left++;
'''
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        l = 0 # 左边界
        r = len(matrix[0])-1 # 右边界
        t = 0 # 上边界
        b = len(matrix)-1 # 下边界
        res = []
        
        while True: # 循环条件：边界没有交叉（在下面每次更新边界后都要判断是否交叉了）
            for i in range(l, r+1): # 左 → 右：从l到r遍历当前上边界的每一列，把matrix[t][i]加入结果
                res.append(matrix[t][i])
            t +=1 # 上边界往下缩
            if t>b: break # 判断边界是否交叉：如果上边界超过下边界，说明上下都走完了，结束循环
            
            for i in range(t, b+1): # 上 → 下：从t到b遍历当前右边界的每一行，把matrix[i][r]加入结果
                res.append(matrix[i][r])
            r -=1 # 右边界往左缩
            if l>r: break # 判断边界是否交叉：如果左边界超过右边界，说明左右都走完了，结束循环
            
            for i in range(r, l-1, -1): # 右 → 左：从r到l倒着遍历当前下边界的每一列，把matrix[b][i]加入结果
                res.append(matrix[b][i])
            b -=1 # 下边界往上缩
            if t>b: break # 判断边界是否交叉：如果上边界超过下边界，说明上下都走完了，结束循环
            
            for i in range(b, t-1, -1): # 下 → 上：从b到t倒着遍历当前左边界的每一行，把matrix[i][l]加入结果
                res.append(matrix[i][l])
            l +=1 # 左边界往右缩
            if l>r: break # 判断边界是否交叉：如果左边界超过右边界，说明左右都走完了，结束循环
        
        return res 