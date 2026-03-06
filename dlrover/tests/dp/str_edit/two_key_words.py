"""
最初记事本上只有一个字符 'A' 。你每次可以对这个记事本进行两种操作：
Copy All：复制记事本中所有字符（不允许部分复制）
Paste：粘贴上一次复制的字符

给定一个整数 n，返回打印出 n个 'A' 所需的最少操作次数。

输入：n = 3
输出：3
解释：
最初，只有一个 'A'。
第 1 步：使用 Copy All 操作。
第 2 步：使用 Paste 操作，得到 "AA"。
第 3 步：使用 Paste 操作，得到 "AAA"。

输入：n = 1
输出：0
解释：已经有一个 'A'，不需要任何操作。
"""

"""
状态定义：
dp[i][j]表示当前记事本上有 i个字符，剪贴板上有 j个字符所需的最少操作次数
其中 i表示当前记事本上的字符数量，j表示剪贴板上的字符数量

状态转移：
1.Paste 操作：当剪贴板不为空时，可以将剪贴板的内容粘贴到记事本
dp[i+j][j] = min(dp[i+j][j], dp[i][j] + 1)
2.Copy All 操作：只能复制当前记事本上的所有字符
dp[i][i] = min(dp[i][i], dp[i][j] + 1)

初始化：
dp[1][0] = 0：初始状态有 1 个 'A'，剪贴板为空
"""


def solve(n):
    if n == 1:
        return 0

    # 初始化
    dp = [[float("inf")] * (n + 1) for _ in range(n + 1)]
    # 最初只有一个A
    dp[1][0] = 0

    for i in range(1, n + 1):
        for j in range(n + 1):
            if dp[i][j] == float("inf"):
                continue

            # paste操作
            if j > 0 and i + j <= n:
                dp[i + j][j] = min(dp[i + j][j], dp[i][j] + 1)

            # copy all操作：
            dp[i][i] = min(dp[i][i], dp[i][j] + 1)

    # 找到最小值
    result = float("inf")
    for j in range(1, n + 1):
        result = min(result, dp[n][j])

    return int(result) if result != float("inf") else 0
