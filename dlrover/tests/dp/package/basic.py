"""
01背包：
有n件物品和一个容量为 capacity的背包。第 i件物品的重量是 weight[i]，价值是 value[i]。
每件物品只能用一次，求解将哪些物品装入背包可使这些物品的总价值最大。

状态定义：
dp[j]表示：容量为 j 的背包，能装下的最大价值

情况1：不选当前物品
dp[j]
情况2：选择当前物品
dp[j-weight[i]] + value[i]

dp[j] = max(dp[j], dp[j-w] + v)  当 j ≥ w
"""


def solve_01_2d(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        weight = weights[i - 1]
        value = values[i - 1]

        for j in range(capacity + 1):
            if j < weight:  # 装不下
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)

    return dp[n][capacity]


def solve_01(weights, values, capacity):
    dp = [0] * (capacity + 1)

    for i in range(len(weights)):
        weight = weights[i]
        value = values[i]

        # 逆序遍历（每件物品只能选一个）
        for j in range(capacity, weight - 1, -1):
            dp[j] = max(dp[j], dp[j - weight] + value)

    return dp[capacity]


"""
完全背包：
有n件物品和一个容量为 capacity的背包。第i件物品的重量是 weight[i]，价值是 value[i]。
每件物品可用无限次，求解将哪些物品装入背包可使这些物品的总价值最大。

外层遍历物品，内层正序遍历容量（允许物品被重复添加）
"""

def solve_complete_2d(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        weight = weights[i - 1]
        value = values[i - 1]

        # 正序遍历（每件物品可以选n次）
        for j in range(capacity + 1):
            if j < weight:
                dp[i][j] = dp[i-1][j]  # 放不下
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j - weight] + value)

    return dp[n][capacity]


def solve_complete(weights, values, capacity):
    dp = [0] * (capacity + 1)

    for i in range(len(weights)):
        weight = weights[i]
        value = values[i]

        # 正序遍历（每件物品可以选n次）
        for j in range(weight, capacity + 1):
            dp[j] = max(dp[j], dp[j - weight] + value)

    return dp[capacity]


if __name__ == '__main__':
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    capacity = 8
    print(solve_01_2d(weights, values, capacity))  # 10
    print(solve_01(weights, values, capacity))  # 10

    weights = [2, 3, 4, 7]
    values = [1, 3, 5, 9]
    capacity = 10
    print(solve_complete_2d(weights, values, capacity))  # 12
    print(solve_complete(weights, values, capacity))  # 12
