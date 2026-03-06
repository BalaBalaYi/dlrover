"""给定一个二叉树，求每一层的节点值的平均数。"""
from collections import deque

from test.tree.node import TreeNode


def solve(root: TreeNode) -> list:
    result = []
    if not root:
        return result

    deq = deque([root])
    while deq:
        n = len(deq)
        level_sum = 0
        for _ in range(n):
            node = deq.popleft()
            level_sum += node.val
            if node.left:
                deq.append(node.left)
            if node.right:
                deq.append(node.right)
        result.append(level_sum / n)

    return result


if __name__ == '__main__':
    t0 = TreeNode(0)
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t5 = TreeNode(5)

    t0.left = t1
    t0.right = t2
    t1.left = t3
    t1.right = t4
    t2.left = t5
    print(solve(t0))
