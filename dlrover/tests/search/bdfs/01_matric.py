"""给定一个由0 和1 组成的二维矩阵，求每个位置到最近的0的距离。

输入:
mat = [[0,0,0],
       [0,1,0],
       [0,0,0]]
输出:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

 输入:
mat = [[0,0,0],
       [0,1,0],
       [1,1,1]]
输出:
[[0,0,0],
 [0,1,0],
 [1,2,1]]
"""

from collections import deque
from typing import List


def solve(mat: List[List[int]]) -> List[List[int]]:
    """
    多源BFS解法

    核心思想：
    将所有 0 的位置作为起始点，距离为 0
    从这些起始点开始进行BFS
    每次从队列中取出一个位置，更新其上下左右邻居的距离
    如果邻居未被访问过且是 1，则更新距离并入队
    """
    if not mat or not mat[0]:
        return mat

    m, n = len(mat), len(mat[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # 初始化结果矩阵
    dist = [[float('inf')] * n for _ in range(m)]
    queue = deque()

    # 将所有0的位置加入队列，距离设为0
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                dist[i][j] = 0
                queue.append((i, j))

    # 多源BFS
    while queue:
        i, j = queue.popleft()

        for dx, dy in directions:
            ni, nj = i + dx, j + dy

            # 检查边界
            if 0 <= ni < m and 0 <= nj < n:
                # 如果找到更短距离
                if dist[ni][nj] > dist[i][j] + 1:
                    dist[ni][nj] = dist[i][j] + 1
                    queue.append((ni, nj))

    return dist


if __name__ == '__main__':
    mat2 = [[0, 0, 0],
            [0, 1, 0],
            [1, 1, 1]]
    print(solve(mat2))
