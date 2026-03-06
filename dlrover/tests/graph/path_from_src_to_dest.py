"""给定一个有 n个节点的有向无环图 (DAG)，节点编号从 0到 n-1。同时还给定一个 edges数组，其中 edges[i] = [u, v]表示有向边 u → v。
给定源点 source和目标点 destination，判断从 source出发的所有可能路径是否都最终到达 destination。
换句话说，需要判断是否存在从 source出发，但不以 destination为终点的路径。

输入: n = 3, edges = [[0,1],[0,2]], source = 0, destination = 2
输出: false
解释: 存在一条路径 0→1，终点不是2
"""

"""
一、问题理解

关键点分析
所有路径都必须到达 destination
如果存在任何一条路径不以 destination为终点，返回 false
终点必须是 destination，不能是其他节点或死胡同
图是有向无环图（题目保证）
失败条件：
存在从 source出发的路径，终点是其他节点（不是 destination）
存在从 source出发的路径，终点是死胡同（没有出边的节点，但不是 destination）
特殊情况：
如果 source == destination：
如果 source没有出边：返回 true（路径就是原地）
如果 source有出边：必须保证所有出边路径都能回到​ destination
"""


def leadsToDestination(n, edges, source, destination):
    """
    DFS + 状态标记
    """
    # 构建邻接表
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)

    # 状态数组：0=未访问，1=访问中，2=已访问完成（安全）
    states = [0] * n

    def dfs(node):
        # 如果当前节点已访问完成，直接返回结果
        if states[node] == 2:
            return True
        # 如果节点在递归栈中，说明有环（但题目说无环）
        if states[node] == 1:
            return False

        # 标记为访问中
        states[node] = 1

        # 获取邻居
        neighbors = graph[node]

        # 情况1：当前节点是叶子节点
        if not neighbors:
            # 叶子节点必须是destination
            if node != destination:
                states[node] = 2  # 标记为已访问但失败
                return False
            else:
                states[node] = 2  # 标记为已访问且安全
                return True

        # 情况2：递归检查所有邻居
        for neighbor in neighbors:
            if not dfs(neighbor):
                states[node] = 2  # 标记为已访问但失败
                return False

        # 所有邻居都能到destination，当前节点安全
        states[node] = 2
        return True

    return dfs(source)