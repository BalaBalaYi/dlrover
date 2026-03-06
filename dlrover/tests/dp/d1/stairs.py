"""给定n 节台阶，每次可以走一步或走两步，求一共有多少种方式可以走完这些台阶。
"""

"""
状态定义：
dp[i] 走i节台阶有多少种方式可以走完这些台阶

状态转移：
走一节或走两节
dp[i] = dp[i - 1] + dp[i - 2]

初始化：
0节和1节：1
"""

def solve(n):
    if n <= 2:
        return n

    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


def solve_optimized(n):
    if n <= 2:
        return n

    # 只保存前两个状态
    prev1, prev2 = 1, 1

    for _ in range(2, n + 1):
        current = prev1 + prev2
        prev2, prev1 = prev1, current

    return prev1


if __name__ == '__main__':
    print(solve(3))  # 3
    print(solve_optimized(4))  # 5
