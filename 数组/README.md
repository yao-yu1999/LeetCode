# 数组笔记

## 一、题目

给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果 target 存在返回下标，否则返回 -1。
你必须编写一个具有 O(log n) 时间复杂度的算法。


示例 1:
输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4

示例 2:
输入: nums = [-1,0,3,5,9,12], target = 2
输出: -1
解释: 2 不存在 nums 中因此返回 -1
 

提示：
1. 你可以假设 nums 中的所有元素是不重复的。
2. n 将在 [1, 10000]之间。
3. nums 的每个元素都将在 [-9999, 9999]之间。

## 二、简单版本
'''

'''

## 三、笔记

1. 思路

在升序数组 nums 中寻找目标值 target，对于特定下标 i，比较 nums[i] 和 target 的大小：

如果 nums[i]=target，则下标 i 即为要寻找的下标；
如果 nums[i]>target，则 target 只可能在下标 i 的左侧；
如果 nums[i]<target，则 target 只可能在下标 i 的右侧。


2. 步骤

（1）定义查找的范围 [left,right]，初始是整个数组，逐渐移动

（2）每次取查找范围的中点 mid

（3）比较 nums[mid] 和 target 的大小：

如果相等则 mid 即为要寻找的下标；
如果不相等则根据 nums[mid] 和 target 的大小关系将查找范围缩小一半


3. 变量
left：数组左边界
right：数组右边界
nums:数组名称
mid：每次查找范围的中值
target：目标值


4. 注意

（1）确保是升序数组left <= right，降序数组修改循环条件为right <= left

（2）确定中值的时候，为了防止数组长度过大，相加易导致的溢出，一般使用：mid=(high-low)//2 + low,先获取中间长度。

（3）len(nums) 等价于 num.length

