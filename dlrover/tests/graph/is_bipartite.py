"""
给定一个无向图，判断它是否是一个二分图（Bipartite Graph）。

二分图定义：图中的所有顶点可以被分成两个独立的集合 U 和 V，使得每条边都连接一个 U 中的顶点和一个 V 中的顶点（即同集合内的顶点之间没有边）。

等价条件：图可以被二染色（用两种颜色给所有顶点染色，相邻顶点颜色不同）。

"""

from collections import deque


def isBipartite(graph):
    """
    判断图是否为二分图
    :type graph: List[List[int]] 邻接表表示
    :rtype: bool
    """
    n = len(graph)  # 节点数
    colors = [-1] * n  # -1表示未染色，0和1表示两种颜色

    for i in range(n):
        if colors[i] == -1:  # 未染色的节点
            if not bfs(graph, i, colors):
                return False
    return True


# BFS实现
def bfs(graph, start, colors):
    """
    BFS染色
    """
    queue = deque([start])
    colors[start] = 0  # 起始节点染成颜色0

    while queue:
        node = queue.popleft()
        current_color = colors[node]

        for neighbor in graph[node]:
            if colors[neighbor] == -1:  # 邻居未染色
                colors[neighbor] = 1 - current_color  # 染成相反颜色
                queue.append(neighbor)
            elif colors[neighbor] == current_color:  # 邻居颜色相同
                return False
    return True
