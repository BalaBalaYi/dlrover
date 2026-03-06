"""
树可以看成是一个连通且无环的无向图。
给定往一棵 n个节点（节点值 1到 n）的树中添加一条边后的无向图。添加的边的两个顶点包含在 1到 n中间，且这条附加的边不属于树中已存在的边。
图的信息记录于长度为 n的二维数组 edges中，edges[i] = [ai, bi]表示图中在 ai和 bi之间存在一条边。
请找出一条可以删去的边，删除后可使剩下的部分是有 n个节点的树。如果有多个答案，则返回数组 edges中最后出现的边。

输入: edges = [[1,2],[1,3],[2,3]]
输出: [2,3]

解释:
原始树：
  1
 / \
2   3

添加边[2,3]后形成了环，删除[2,3]可恢复为树
"""


class UnionFind:
    def __init__(self, n):
        self.parent  = list(range(n + 1))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        self.parent[root_x] = root_y
        return True


def findRedundantConnection(edges):
    """
    并查集解法
    :type edges: List[List[int]]
    :rtype: List[int]
    """
    n = len(edges)
    uf = UnionFind(n)

    for u, v in edges:
        if not uf.union(u, v):  # 合并失败，说明u和v已连通
            return [u, v]

    return []  # 理论上不会到达这里


if __name__ == '__main__':
    edges = [[1,2],[1,3],[2,3]]
    print(findRedundantConnection(edges))
