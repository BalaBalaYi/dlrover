"""
给你一个整数数组 nums，找到其中 最长严格递增子序列 的长度。
子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7]是数组 [0,3,1,6,2,2,7]的子序列。

输入：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。

输入：nums = [0,1,0,3,2,3]
输出：4
"""

"""
状态定义：
dp[i]: 表示数字i对应的最长递增子序列

状态转移：
对于j<i：有：dp[i] = dp[j] + 1

"""


def solve(nums):
    n = len(nums)
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


if __name__ == "__main__":
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print(solve(nums))
