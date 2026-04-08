# https://leetcode.cn/problems/palindrome-partitioning/description/?envType=study-plan-v2&envId=top-100-liked

from polars import List

# 方法1：枚举j选哪个
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        result = []
        path = []

        # 考虑 s[i:] 怎么分割？从当前位置i开始
        def dfs(i: int) -> None:
            if i == n:  # s 分割完毕
                result.append(path.copy())  # 复制 path 加入到 result
                return None 

            for j in range(i, n):  # 枚举子串的结束位置
                t = s[i: j + 1]  # 分割出子串 t
                if t == t[::-1]:  # 判断 t 是不是回文串，如果是就加入;如果不是不用做任何操作，不用提前return None（否则就是忽略了其他的回文字符串，直接停止递归了）
                    path.append(t)
                    dfs(j + 1) # 考虑剩余的 s[j+1:] 怎么分割
                    path.pop()  # 回溯：恢复现场

        dfs(0)
        return result


# 方法2：选或不选
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        result = []
        path = []

        # 考虑当前位置 i 后面的逗号怎么选?start 表示当前这段回文子串的开始位置
        def dfs(i: int, start: int) -> None:
            if i == n:  # s 分割完毕
                result.append(path.copy())  # 复制 path
                return

            # 不分割：不选 i 和 i+1 之间的逗号
            if i < n - 1:  # i=n-1 时只能分割
                dfs(i + 1, start) # 考虑 i+1 后面的逗号怎么选

            # 分割：选 i 和 i+1 之间的逗号（把 s[i] 作为子串的最后一个字符）
            t = s[start: i + 1]
            if t == t[::-1]:  # 判断是否回文
                path.append(t)
                
                dfs(i + 1, i + 1) # 考虑 i+1 后面的逗号怎么选？start=i+1 表示下一个子串从 i+1 开始
                path.pop()  # 回溯：恢复现场

        dfs(0, 0)
        return result