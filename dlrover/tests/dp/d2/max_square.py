"""
给定一个二维的0-1 矩阵，求全由1 构成的最大正方形面积。

状态转移方程推导：
对于以 (i,j)为右下角的正方形，它的边长受限于：
上方能形成的正方形边长：dp[i-1][j]
左方能形成的正方形边长：dp[i][j-1]
左上方能形成的正方形边长：dp[i-1][j-1]
只有当这三个方向都能形成正方形时，当前位置才能形成更大的正方形。

如果 matrix[i][j] == '1':
    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
否则:
    dp[i][j] = 0
"""


def solve(mat):
    if not mat or not mat[0]:
        return 0

    m = len(mat)
    n = len(mat[0])
    dp = [[0] * (n) for _ in range(m)]
    max_side = 0

    for i in range(1, m):
        for j in range(1, n):
            if mat[i][j] == "1":
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                max_side = max(max_side, dp[i][j])

    return max_side ** 2


if __name__ == '__main__':
    matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]
    print(solve(matrix))  # 4
