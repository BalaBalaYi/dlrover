"""树的遍历"""

from collections import deque
from typing import List

from test.tree.node import TreeNode


def pre_order(root: TreeNode) -> List[int]:
    def dfs (node, result):
        if not node:
            return
        result.append(root.val)
        dfs(root.left, result)
        dfs(root.right, result)

    result = []
    dfs(root, result)
    return result


def in_order(root: TreeNode) -> List[int]:
    def dfs(node, result):
        if not node:
            return
        dfs(root.left, result)
        result.append(root.val)
        dfs(root.right, result)

    result = []
    dfs(root, result)
    return result


def post_order(root: TreeNode) -> List[int]:
    def dfs(node, result):
        if not node:
            return
        dfs(root.left, result)
        dfs(root.right, result)
        result.append(root.val)

    result = []
    dfs(root, result)
    return result


def level_order(root: TreeNode) -> List[List[int]]:
    if not root:
        return []

    queue = deque([root])
    result = []

    while queue:
        n = len(queue)
        # 当前层的结果
        level = []

        for _ in range(n):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)

    return result


def pre_order_traversal(root: TreeNode) -> List[int]:
    result = []
    if not root:
        return result

    deq = deque([root])
    while deq:
        top_node = deq.pop()
        result.append(top_node.val)

        if top_node.right:
            deq.append(top_node.right)
        if top_node.left:
            deq.append(top_node.left)

    return result


def in_order_traversal(root: TreeNode) -> List[int]:
    result = []
    if not root:
        return result

    stack = []
    current = root

    while current or stack:
        # 向左走到底，沿途压栈
        while current:
            stack.append(current)
            current = current.left

        # 达到最左端，弹出并访问
        current = stack.pop()
        result.append(current.val)

        # 转向右子树
        current = current.right

    return result


def post_order_traversal(root: TreeNode) -> List[int]:
    result = []
    if not root:
        return result

    deq = deque([root])
    # 根右左
    while deq:
        top_node = deq.pop()
        result.append(top_node.val)

        if top_node.left:
            deq.append(top_node.left)
        if top_node.right:
            deq.append(top_node.right)
    # 反过来就是左右根
    return result[::-1]
