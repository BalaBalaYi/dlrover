"""给定N 个课程和这些课程的前置必修课，求可以一次性上完所有课的顺序。
"""

"""
算法步骤
1.构建图：将课程作为节点，前置关系作为有向边。
2.计算入度：统计每个课程有多少个前置必修课。
3.初始化队列：将所有入度为 0 的课程（即没有前置必修课的课程）加入队列。
4.BFS 遍历：
    从队列中取出一个课程，将其加入结果列表。
    遍历该课程的所有后续课程（即依赖它的课程），将它们的入度减 1。
    如果某个后续课程的入度减为 0，说明它的前置课已上完，将其加入队列。
5.检查结果：如果结果列表的长度等于课程总数 N，说明可以上完所有课；否则说明存在循环依赖（死锁），无法上完。

"""

from collections import deque

def order(numCourses, prerequisites):
    """
    :type numCourses: int (N)
    :type prerequisites: List[List[int]] (每个元素 [a, b] 表示 b 是 a 的前置课)
    :rtype: List[int] (上课顺序)
    """

    result = []

    # 1. 初始化邻接表和入度数组
    graph = [[] * numCourses]  # 每个课程：对应了哪些课程
    indegree = [0] * numCourses  # 每个课程的前置依赖数量

    # 2. 构建图
    for course, pre in prerequisites:
        graph[pre].append(course)
        indegree[course] += 1

    # 3. 将入度为0的课程加入队列
    deq = deque()
    for course in range(numCourses):
        if indegree[course] == 0:
            deq.append(course)

    # 4. bfs遍历
    while deq:
        current = deq.popleft()
        result.append(current)

        # 遍历当前课程的所有后续课程
        for nxt_course in graph[current]:
            indegree[nxt_course] -= 1
            if indegree[nxt_course] == 0:
                deq.append(nxt_course)

    # 5. 检查是否所有课程都被处理
    if len(result) == numCourses:
        return result
    else:
        return []
