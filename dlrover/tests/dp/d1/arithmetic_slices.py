"""
给定一个数组，求这个数组中连续且等差的子数组一共有多少个。

输入: nums = [1,2,3,4]
输出: 3
解释: nums 中有三个子等差数组: [1,2,3], [2,3,4] 和 [1,2,3,4] 自身。

输入: nums = [1,2,3,4,5,6]
输出: 10
解释: 长度为3: [1,2,3], [2,3,4], [3,4,5], [4,5,6]
      长度为4: [1,2,3,4], [2,3,4,5], [3,4,5,6]
      长度为5: [1,2,3,4,5], [2,3,4,5,6]
      长度为6: [1,2,3,4,5,6]
      总数: 4 + 3 + 2 + 1 = 10
"""

"""
状态定义： 
dp[i]表示以 nums[i]结尾的等差数列个数

状态转移：
如果 nums[i] - nums[i-1] == nums[i-1] - nums[i-2]，则 dp[i] = dp[i-1] + 1

结果：sum(dp)
"""


def solve(nums):
    if not nums:
        return 0

    if len(nums) < 3:
        return 0

    dp = [0] * len(nums)

    for i in range(2, len(nums)):
        if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
            dp[i] = dp[i-1] + 1

    return sum(dp)


if __name__ == '__main__':
    print(solve([1, 2, 3, 4]))  # 3
    print(solve([1, 2, 3, 4, 5, 6]))  # 10
