"""
给你一个二进制字符串数组 strs和两个整数 m和 n。
请你找出并返回 strs的最大子集的长度，该子集中 最多 有 m个 0和 n个 1。

如果 x的所有元素也是 y的元素，集合 x是集合 y的 子集。

输入：strs = ["10", "0001", "111001", "1", "0"], m = 5, n = 3
输出：4
解释：最多有 5 个 0 和 3 个 1 的最大子集是 {"10", "0001", "1", "0"} ，因此答案是 4 。
其他满足题意但较小的子集包括 {"0001", "1"} 和 {"10", "1", "0"} 。{"111001"} 不满足题意，因为它含 4 个 1 ，大于 n 的值 3 。

输入：strs = ["10", "0", "1"], m = 1, n = 1
输出：2
解释：最大的子集是 {"0", "1"} ，所以答案是 2 。
"""

"""
问题分析:
这是一个 二维费用的 01背包问题：
物品：每个字符串
重量1：字符串中 0的个数
重量2：字符串中 1的个数
价值：每个字符串的价值都是 1（我们想要最大子集长度）
背包容量：m个 0和 n个 1
目标：在不超过容量限制的情况下，选择尽可能多的字符串

状态定义:
dp[i][j][k]表示：考虑前 i个字符串，最多使用 j个 0和 k个 1的情况下，能选择的最大字符串数量。

状态转移:
对于第 i个字符串（假设有 zeros个 0，ones个 1）：
1.不选第 i 个字符串：dp[i][j][k] = dp[i-1][j][k]
2.选第 i 个字符串（如果 j ≥ zeros且 k ≥ ones）：
dp[i][j][k] = max(dp[i-1][j][k], dp[i-1][j-zeros][k-ones] + 1)
"""


def solve(strs, m, n) -> int:
    length = len(strs)

    # 预处理每个字符串的0和1的个数
    counts = []
    for s in strs:
        zeros = s.count("0")
        ones = s.count("1")
        counts.append([zeros, ones])

    # 初始化dp数组
    dp = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(length + 1)]

    for i in range(1, length + 1):
        zeros, ones = counts[i]
        for j in range(m + 1):
            for k in range(n + 1):
                if zeros > j or ones > k:
                    # 没法选
                    dp = dp[i-1][j][k]
                else:
                    dp[i][j] = max(dp[i-1][j][k], dp[i][j - zeros][k - ones] + 1)

    return dp[length][m][n]
