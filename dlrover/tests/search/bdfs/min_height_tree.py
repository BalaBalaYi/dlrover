"""
树是一个无向图，其中任何两个顶点只通过一条路径连接。换句话说，任何一个没有简单环路的连通图都是一棵树。

给你一棵包含 n个节点的树，节点标记为 0到 n-1。给定数字 n和一个有 n-1条无向边 edges的列表（其中 edges[i] = [ai, bi]表示树中节点 ai和 bi之间存在一条无向边），
请你找到所有的最小高度树并按任意顺序返回它们的根节点标签列表。

最小高度树的定义：在所有的树中，具有最小高度的树。树的高度是指根节点和叶子节点之间最长向下路径上的边数。

输入: n = 4, edges = [[1,0],[1,2],[1,3]]
输出: [1]
解释: 当根是标签为 1 的节点时，树的高度是 1，这是唯一的最小高度树。

输入: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
输出: [3,4]
解释: 有两个最小高度树：
  以3为根: 高度为2
  以4为根: 高度为2
"""

from collections import defaultdict, deque


def findMinHeightTrees(n, edges):
    """
    求直径端点 + 找中点
    时间复杂度: O(n)
    空间复杂度: O(n)
    """
    if n == 1:
        return [0]

    # 构建邻接表
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    def bfs_furthest(start):
        """BFS找到离start最远的节点和路径"""
        queue = deque([start])
        visited = {start}
        parent = {start: None}
        furthest = start

        while queue:
            node = queue.popleft()
            furthest = node
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = node
                    queue.append(neighbor)

        return furthest, parent

    # 第一次BFS：从任意节点(0)找到最远节点x
    x, _ = bfs_furthest(0)

    # 第二次BFS：从x找到最远节点y，并记录路径
    y, parent = bfs_furthest(x)

    # 重建路径
    path = []
    node = y
    while node:
        path.append(node)
        node = parent[node]

    # 找到路径中点
    m = len(path)
    if m % 2 == 1:
        return [path[m // 2]]
    else:
        return [path[m // 2 - 1], path[m // 2]]


if __name__ == '__main__':
    print(findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]]))  # [1]
    print(findMinHeightTrees(6, [[3, 0], [3, 1], [3, 2], [3, 4],
                                 [5, 4]]))  # [3,4]
