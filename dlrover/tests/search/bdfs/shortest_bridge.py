"""
在给定的二维二进制数组 grid中，存在两座岛。岛是由四面相连的 1组成的最大连通块。
你可以将任意数量的 0变为 1，以使两座岛连接起来，变成一个岛。
返回必须翻转的 0的最小数目。

输入：grid = [[0,1,0,0],
             [1,1,1,0],
             [0,1,0,0],
             [0,0,0,1]]
输出：1
解释：只需将中间的0变为1

输入：grid = [[1,1,1,1,1],
             [1,0,0,0,1],
             [1,0,1,0,1],
             [1,0,0,0,1],
             [1,1,1,1,1]]
输出：2
"""


from collections import deque


def shortestBridge(grid):
    """
    找到连接两个岛屿的最短桥梁长度
    """
    n = len(grid)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # 步骤1：找到并标记第一个岛屿
    def dfs(i, j):
        """深度优先搜索标记第一个岛屿"""
        if i < 0 or i >= n or j < 0 or j >= n or grid[i][j] != 1:
            return
        grid[i][j] = 2  # 标记第一个岛屿为2
        queue.append((i, j))  # 将第一个岛屿的边界加入BFS队列
        for di, dj in directions:
            dfs(i + di, j + dj)

    # 步骤2：初始化BFS队列
    queue = deque()

    # 找到第一个岛屿的起点
    found = False
    for i in range(n):
        if found:
            break
        for j in range(n):
            if grid[i][j] == 1:
                dfs(i, j)
                found = True
                break

    # 步骤3：从第一个岛屿开始BFS
    distance = 0
    while queue:
        size = len(queue)
        for _ in range(size):
            i, j = queue.popleft()

            for di, dj in directions:
                ni, nj = i + di, j + dj

                # 检查边界
                if ni < 0 or ni >= n or nj < 0 or nj >= n:
                    continue

                # 如果遇到第二个岛屿，返回距离
                if grid[ni][nj] == 1:
                    return distance

                # 如果遇到水域，标记并加入队列
                if grid[ni][nj] == 0:
                    grid[ni][nj] = 2  # 标记为已访问
                    queue.append((ni, nj))

        distance += 1

    return distance


if __name__ == '__main__':
    # 测试示例
    grid1 = [
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1]
    ]
    print(shortestBridge(grid1))  # 输出: 1

    grid2 = [
        [0, 1, 0],
        [0, 0, 0],
        [0, 0, 1]
    ]
    print(shortestBridge(grid2))  # 输出: 2
