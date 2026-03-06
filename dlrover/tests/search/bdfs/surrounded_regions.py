"""给定一个 m x n的矩阵 board，由字符 'X'和 'O'组成。找到所有被 'X'围绕的区域，并将这些区域里所有的 'O'用 'X'填充。
被围绕的区域：区域的边界上的 'O'不会被填充。与边界上的 'O'相连的 'O'也不会被填充。

输入: board = [
  ["X","X","X","X"],
  ["X","O","O","X"],
  ["X","X","O","X"],
  ["X","O","X","X"]
]
输出: board = [
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","O","X","X"]
]
解释: 被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。
任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。
如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
"""

"""
解法：
遍历四条边上的 'O'，从这些 'O' 开始 DFS/BFS，标记所有相连的 'O' 为 '#'
遍历整个矩阵：
将 'O' 变为 'X'（被围绕的）
将 '#' 恢复为 'O'（与边界相连的）
"""


def solve(board):
    if not board or not board[0]:
        return

    m = len(board)
    n = len(board[0])

    # dfs遍历相连的O
    def dfs(i, j):
        if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != "O":
            return

        # 标记，避免重复遍历
        board[i][j] = "#"

        # 四个方向搜索
        dfs(i - 1, j)
        dfs(i + 1, j)
        dfs(i, j - 1)
        dfs(i, j + 1)

    # 1. 标记四条边上的 O 及其相连区域
    # 第一列和最后一列
    for i in range(m):
        if board[i][0] == 'O':
            dfs(i, 0)
        if board[i][n-1] == 'O':
            dfs(i, n-1)
    # 第一行和最后一行
    for j in range(n):
        if board[0][j] == 'O':
            dfs(0, j)
        if board[m - 1][j] == 'O':
            dfs(m - 1, j)

    # 2.遍历矩阵，把其它地方置为O
    for i in range(m):
        for j in range(n):
            if board[i][j] == 'O':
                board[i][j] = 'X'
            elif board[i][j] == '#':
                board[i][j] = 'O'


if __name__ == '__main__':
    board = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"]
    ]
    print(solve(board))
