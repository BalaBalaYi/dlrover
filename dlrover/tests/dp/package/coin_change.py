"""给你一个整数数组 coins，表示不同面额的硬币；以及一个整数 amount，表示总金额。
计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1。
你可以认为每种硬币的数量是无限的。

输入：coins = [1, 2, 5], amount = 11
输出：3
解释：11 = 5 + 5 + 1

输入：coins = [2], amount = 3
输出：-1
"""

"""
状态定义：
dp[i][j]表示：使用前 i种硬币（硬币种类从 1 到 i），凑成金额 j所需的最少硬币数量。

状态转移：
1. 不使用第i种硬币：
dp[i][j] = dp[i-1][j]

2. 使用第i种硬币
dp[i][j] = min(dp[i-1][j], dp[i][j - coins[i-1]] + 1))

"""

def solve(coins, amount):
    n = len(coins)
    dp = [[float('inf')] * (amount + 1) for _ in range(n + 1)]

    # 凑成金额0需要0个硬币
    for i in range(n + 1):
        dp[i][0] = 0

    for i in range(1, n + 1):
        coin_val = coins[i - 1]
        for j in range(1, amount + 1):
            if coin_val > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - coin_val] + 1)

    return dp[n][amount] if dp[n][amount] != float('inf') else -1


if __name__ == '__main__':
    print(solve([1, 2, 5], 11))  # 3(5+5+1)
