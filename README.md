# LeetCode

写在前面，创建这个仓库单纯是为了刷题和练习git命令。速通建议直接看题解、总结思路并背题。

## 一、 刷题路线
1. 代码随想录

https://programmercarl.com/qita/12.list.html （题单）		

2. 灵茶山艾府（B站有讲解）

https://leetcode.cn/discuss/post/3141566/ru-he-ke-xue-shua-ti-by-endlesscheng-q3yd/  （科学刷题题单）

3. labuladong

https://labuladong.online/zh/roadmap/  （刷题路线）

https://labuladong.online/zh/problemset/core/  （题单）

5. 力扣

https://leetcode.cn/studyplan/top-100-liked/  （热题100） 

https://leetcode.cn/studyplan/top-interview-150/ （面试150）

6. 牛客网

https://www.nowcoder.com/exam/company?questionJobId=10&subTabName=written_page （公司笔试真题）

7. NeetCode(youtube)

https://www.youtube.com/watch?v=Y0lT9Fck7qI (题目讲解)

8. 飞书总结题单

https://my.feishu.cn/wiki/PdtGwSkxpi4EOzkvTZccjW22n8J?sheet=9EEToi

## 二、 每日刷题
(1) 详细记录表：https://docs.qq.com/sheet/DRWhpY1dYWUdVenFz?tab=BB08J2

(2) 刷题题单

基于力扣hot-100的顺序刷题：https://leetcode.cn/studyplan/top-100-liked/

如果官解没有看懂，非常建议看灵茶山艾府的题解，通俗易懂，代码写的很清爽。

有时间可以继续刷面试100：https://leetcode.cn/studyplan/top-interview-150/

（3）小程序：支持按公司、部门、岗位组合查询题目

CodeTop 企业题单：https://codetop.cc/（网站，也有微信小程序）

Github仓库地址： https://github.com/afatcoder/LeetcodeTop


## 三、 其他
力扣难度分插件：https://github.com/zhang-wangz/LeetCodeRating

## 四、 ACM模式
《代码随想录》ACM输入输出模板教程：25种笔试输入输出写法，笔试必备

https://programmercarl.com/qita/acm1.html

以下是自己例举的几种输入方式。目标：整数列表和目标整数。根据输入格式的不同，有多种方式。

#### 1. 多行输入

输入：
```
-1 0 3 5 9 12
9
```
代码：
```
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pass
        return -1

if __name__ == "__main__":
    nums = list(map(int, input().strip().split())) # 1.1 读取第一行，先转换为整数列表list
    target = int(input().strip()) # 1.2 读取第二行，转换为整数
    
    sol = Solution() # 2. 创建 Solution 对象
    result = sol.search(nums, target)  # 3. 调用
    print(result) # 4. 打印结果

```

#### 2. 单行纯数据输入

输入：
```
[-1,0,3,5,9,12], 9
```

代码:
```
from typing import List
import ast

if __name__ == "__main__":
    line = input().strip() # 1.1 读取键盘输入（去掉空格）
    
    last_comma = line.rfind(',')  # 1.2 找到最后一个逗号的位置。并按最后一个逗号分割，得到左右两部分
    left_part = line[:last_comma].strip()  # 数组切片不包含最后一个索引
    right_part = line[last_comma+1:].strip()
    
    nums = ast.literal_eval(left_part) # 1.3 分别解析，左边解析列表（安全方式，不要使用eval），右边直接转换为整数
    target = int(right_part)

    # 调用函数及打印，同上

```

#### 3. 双行纯数据输入【最简单的一种】

输入：
```
[-1,0,3,5,9,12]
9
```
注：相较于第二种输入，少了对左右两边部分分割，可直接转换；相较于第一种使用Map和List转换，这里直接用ast.literal_eval()转换即可

代码：
```
from typing import List
import ast

if __name__ == "__main__":
    nums = ast.literal_eval(input().strip()) # 第一行是列表字符串，直接用 ast.literal_eval 解析成列表
    target = int(input().strip()) # 第二行是目标值，直接变整数
    
    # 调用函数及打印，同上
```

#### 4. 单行带标签输入【最麻烦1】
输入：
```
nums = [-1,0,3,5,9,12], target = 9
```
注：不用按照逗号分隔

代码：
```
from typing import List
import ast
import re

if __name__ == "__main__":
    line = input().strip() # 1.1 读取键盘输入（去掉空格）
    
    nums_match = re.search(r'nums\s*=\s*(\[.*?\])', line) # 1.2 使用正则提取 nums 列表（.*? 表示匹配任意字符，但尽可能少[非贪婪]，这样会匹配到第一个 ] 为止）和 target 数字（\d+ 匹配一个或多个数字）
    target_match = re.search(r'target\s*=\s*(\d+)', line)
    
    if nums_match and target_match: # 如果匹配成功
        nums = ast.literal_eval(nums_match.group(1)) # nums_match.group(1) 就是第一个捕获组的内容，并转换成列表
        target = int(target_match.group(1))
        
        # 调用函数及打印，同上
    else:
        print("输入格式错误! ")  # 匹配失败
```

#### 5. 双行带标签输入【最麻烦2】
输入：
```
nums = [-1,0,3,5,9,12]
target = 9
```
代码：
```
from typing import List
import ast
import re

if __name__ == "__main__":
    first = input().strip() # 读取两行
    second = input().strip()

    nums_match = re.search(r'nums\s*=\s*(\[.*?\])', first) # 重点是分别正则匹配，不是同一行
    target_match = re.search(r'target\s*=\s*(\d+)', second) # 重点是分别正则匹配，不是同一行
    if nums_match and target_match:
        nums = ast.literal_eval(nums_match.group(1))
        target = int(target_match.group(1))
        
        # 调用函数及打印，同上
    else:
        print("输入格式错误")
```


## 力扣模式（核心代码）
无需输入，只用完成核心代码