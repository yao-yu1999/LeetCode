# https://leetcode.cn/problems/pascals-triangle/?envType=study-plan-v2&envId=top-100-liked

from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        c = [[1]*(i+1) for i in range(numRows)] #  生成一个全是1的杨辉三角框架，第一行有1个1（i=0）,第二行有2个1（i=1），第三行有3个1（i=2），以此类推，第i行有i+1个1
        
        for i in range(2, numRows): # 从第3行开始（i=2），填充中间非1的数
            for j in range(1, i): # # 第 i 行有 i+1 个元素，列号 j 的范围是 0 → i。跳过首尾的1（i=0和i，range不包含结束），遍历当前行的中间位置（j从1到i-1，跳过首尾的1）
                c[i][j] = c[i-1][j-1] + c[i-1][j]
        return c