"""
给出 n 个数对。在每一个数对中，第一个数字总是比第二个数字小。
现在，我们定义一种跟随关系，当且仅当 b < c时，数对 (c, d)才可以跟在 (a, b)后面。我们用这种形式来构造一个数对链。
给定一个数对集合 pairs，找出能够形成的最长数对链的长度。你不需要用到所有的数对，你可以以任何顺序选择其中的一些数对来构造。

输入: [[1,2], [2,3], [3,4]]
输出: 2
解释: 最长的数对链是 [1,2] -> [3,4]

输入: [[1,2], [7,8], [4,5]]
输出: 3
解释: 最长的数对链是 [1,2] -> [4,5] -> [7,8]
"""

"""
状态定义：
dp[i]：以第 i 个数对结尾的最长数对链长度

状态转移：
dp[i] = max(dp[i], dp[j] + 1) 对于所有 j < i 且 pairs[j][1] < pairs[i][0]
"""


def solve(pairs):
    if not pairs:
        return 0

    # 按第一个元素排序
    pairs.sort(key=lambda x: x[0])
    n = len(pairs)

    # 初始化DP数组
    dp = [1] * n  # 每个数对自身就是一个长度为1的链

    for i in range(n):
        for j in range(i):
            # 如果 pairs[j] 可以放在 pairs[i] 前面
            if pairs[j][1] < pairs[i][0]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)
