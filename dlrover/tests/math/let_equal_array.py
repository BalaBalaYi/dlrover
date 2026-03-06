"""给你一个长度为 n的整数数组 nums，返回使所有数组元素相等需要的最小操作数。

在一步操作中，你可以使数组中的一个元素 加 加 或者 减 1。

输入：nums = [1,2,3]
输出：2
解释：只需要两步操作（每步操作使一个元素加 1 或减 1）：
[1,2,3] => [2,2,3] => [2,2,2]
"""

def minMoves2(nums):
    nums.sort()
    median = nums[len(nums) // 2]
    return sum(abs(num - median) for num in nums)
