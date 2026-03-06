"""给定一个m * n 大小的非负整数矩阵，求从左上角开始到右下角结束的、经过的数字的和最
小的路径。每次只能向右或者向下移动。

输入: grid = [[1,3,1],
              [1,5,1],
              [4,2,1]]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。

状态定义：
dp[i][j]表示从 (0,0)走到 (i,j)的最小路径和

状态转移方程：
第一行：只能从左向右 → dp[0][j] = dp[0][j-1] + grid[0][j]
第一列：只能从上向下 → dp[i][0] = dp[i-1][0] + grid[i][0]
其他位置：可以从上方或左方来，取最小值
dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
"""


def solve(grid):
    if not grid:
        return 0

    m = len(grid)
    n = len(grid[0])

    dp = [[0] * n for _ in range(m)]
    dp[0][0] = grid[0][0]

    # 初始化第一行，第一列
    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] + grid[0][j]
    for i in range(1, m):
        dp[i][0] = dp[i - 1][0] + grid[i][0]

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + grid[i][j]

    return dp[-1][-1]

if __name__ == '__main__':
    grid1 = [[1, 3, 1],
             [1, 5, 1],
             [4, 2, 1]]
    print(solve(grid1))  # 7
