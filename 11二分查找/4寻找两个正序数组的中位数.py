# 题目：给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。
# 算法的时间复杂度应该为 O(log (m+n)) 。
# 若总长度为奇数，中位数就是左边部分的最大值。若总长度为偶数，中位数 = (左边最大值 + 右边最小值) / 2


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 保证 nums1 是较短的
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        total_left = (m + n + 1) // 2   # 两个数组左边总元素个数 = 两数组长度的1/2。
        
        # 在nums1上进行二分查找：nums1 中左边元素个数 i，范围 [0, m]
        left, right = 0, m  #  左半部分包含的元素个数 i 的取值范围是 [left, right] = [0, m]。
        while left <= right:
            i = (left + right) // 2
            j = total_left - i  # 因为 total_left = i + j，j可以推出
            
            # 处理边界：用 -inf 和 inf 表示空侧的极值
            a_left = nums1[i-1] if i > 0 else float('-inf')
            a_right = nums1[i] if i < m else float('inf')
            b_left = nums2[j-1] if j > 0 else float('-inf')
            b_right = nums2[j] if j < n else float('inf')
            
            # 判断分割是否合法
            # （1）找到正确分割
            if a_left <= b_right and b_left <= a_right: 
                if (m + n) % 2 == 1: # 两个数组总长度是奇数
                    return max(a_left, b_left) # 两个数组左半区间右边界的更大值
                else: # 两个数组总长度是偶数
                    return (max(a_left, b_left) + min(a_right, b_right)) / 2.0 # [两个数组左半区间右边界（更大值）与右半区间左边界（更小值）]除以2
            # （2）没有找到正确分割的两种情况
            elif a_left > b_right: # nums1的左区间的右边界比nums2的右区间的左边界还大。说明nums1贡献i个元素过多，需要减少
                right = i - 1 # 二分排除i右边的元素。减小 i，让 nums1 少放点元素到左边
            else: # nums2的左区间的右边界比nums1的右区间的左边界还大。说明nums1贡献i个元素过少，需要增加
                left = i + 1 # 二分排除i左边的元素。增大 i，让 nums1 多放点元素到左边
        
        return 0.0  # 不会执行到这里
    
# 为什么是total_left = (m + n + 1) // 2，而不是total_left = (m + n) // 2
# 统一偶数个和奇数个的情况。奇数情况左半区间+1个元素，后面计算的时候直接返回左半区间更大的那个值即可


# 为什么是left, right = 0, m 的是m，而不是m-1？
# 因为不是 left和right不是数组下标。而是表示左半部分包含的元素个数 i 的取值范围在 [left, right] 。
# i∈[0, m], j∈[0, n] 且 i + j = total_left。实际有效范围：                                        │
# │  • i ∈ [max(0, total_left-n), min(m, total_left)]        │
# │  • j = total_left - i ∈ [max(0, total_left-m), min(n, total_left)]

# 为什么不直接用一个 i 切分 nums1 和 nums2 的左半部分都为 i 个元素？要用 i,j 分别去切分？
# 左半部分总共需要 total_left (两个数组长度的一半)个元素，这是固定的! 但 nums1 和 nums2 各自贡献多少？
# 要动态决定，由i 和 j 配合，只要满足i+j=固定值total_left！所以不能固定各切一半，因为某一个数组可能比较短，没有 total_left的一半。

# 为什么不直接是i在[left, right]上移动取值：i = i - 1，i = i + 1；而是改变i的取值区间right = i - 1, left = i + 1？
# 因为二分区间更快：线性移动 i 每次移动1步，时间复杂度 O(m)，最坏遍历所有值；二分改变区间，每次排除一半，时间复杂度 O(log m)  。

# 为什么要交换 nums1, nums2，确保 nums1 是较短的数组？
# （1）查找时间更小：二分查找是在 nums1 上进行的，搜索范围是 [0, m]（m = len(nums1)）。如果 m > n，那么二分查找的范围更大
# 关键点在于 j = total_left - i。
# （2）防止越界：当 m > n 时，如果 i 取值很小（比如 i=0），那么 j = total_left 可能大于 n，导致后续访问 nums2[j] 或 nums2[j-1] 时越界。

# 为什么不需要计算右边总元素个数？
# 答：因为左右两边的元素总数是固定的，等于 m+n。一旦确定了左边元素个数 total_left，右边元素个数自动为 (m+n) - total_left。

# 为什么 a_left <= b_right and b_left <= a_right 涵盖等于？
# 边界相等时也是合法分割

# 本题返回的是浮点数。所以计算偶数情况中值的时候，用/2.0。而不是//2.0，也不是/2，更不是//2