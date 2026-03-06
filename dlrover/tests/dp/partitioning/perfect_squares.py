"""给定一个正整数，求其最少可以由几个完全平方数相加构成。"""

"""
状态定义：
dp[i]: 表示和为 i 的完全平方数的最少数量

状态转移：
对于每个数 i，我们可以枚举所有小于等于 i 的完全平方数 j²：
dp[i] = min(dp[i], dp[i - j * j] + 1)
"""


def solve(n):
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        j = 1
        while j * j <= i:
            dp[i] = min(dp[i], dp[i - j * j] + 1)
            j += 1

    return dp[n]


if __name__ == '__main__':
    print(solve(12))
