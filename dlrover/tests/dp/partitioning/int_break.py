"""
给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。返回你可以获得的最大乘积。

输入: n = 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1。

输入: n = 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
"""

"""
状态定义：
dp[i]: 将正整数 i 拆分成至少两个正整数的和，这些整数的最大乘积

状态转移：
1. 只拆为2个部分：j * (i-j)
2. 如果拆为更多部分：j * dp[i-j]

dp[i] = max_{1≤j<i} { max(j × (i-j), j × dp[i-j]) }

初始化：
dp[0] = 0
dp[1] = 1
dp[2] = 1
"""


def solve(n):
    if not n:
        return 0
    if n <= 3:
        return n - 1

    # 初始化dp
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 1

    # 状态转移
    for i in range(3, n + 1):
        max_result = 0
        for j in range(1, i):
            # 拆分为2部分
            two_parts = j * (i - j)

            # 拆分为多个部分
            multi_parts = j * dp[i-j]

            max_result = max(multi_parts, two_parts)
        dp[i] = max_result

    return dp[-1]
