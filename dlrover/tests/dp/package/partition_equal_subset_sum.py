"""
给你一个 只包含正整数 的 非空 数组 nums。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

输入：nums = [1,5,11,5]
输出：true
解释：数组可以分割成 [1, 5, 5] 和 [11]。

输入：nums = [1,2,3,5]
输出：false
解释：数组不能分割成两个和相等的子集。
"""

"""
思路:
背包容量：target
物品重量：nums[i]
物品价值：nums[i]（这里价值=重量，因为我们关心和是否等于target）
每个物品只能选一次 → 01背包问题

状态定义:
dp[i][j]表示：考虑前 i个元素（索引 0 到 i-1），能否选出一些数使它们的和恰好等于 j。

状态转移:
对于第 i 个元素 nums[i-1]：
不选第 i 个元素：dp[i][j] = dp[i-1][j]
选第 i 个元素（如果 j ≥ nums[i-1]）：dp[i][j] = dp[i-1][j - nums[i-1]]

转移方程：
dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]  (当 j ≥ nums[i-1])
"""

def solve(nums):
    total = sum(nums)
    n = len(nums)

    # 如果综合是奇数，不可能平分
    if total % 2 != 0:
        return False

    # 平分值
    target = total // 2

    # 如果最大数超过target，不可能平分
    if max(nums) > target:
        return False

    # 动态规划求解
    dp = [[False] * (target + 1) for _ in range(n + 1)]

    # 和为0都是可以的
    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        num = nums[i - 1]
        for j in range(1, target + 1):
            if num > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - num]

    return dp[n][target]


if __name__ == '__main__':
    print(solve([1, 5, 11, 5]))
    print(solve([1, 2, 3, 5]))
