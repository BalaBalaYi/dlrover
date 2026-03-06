"""判断一个二叉树是否平衡。树平衡的定义是，对于树上的任意节点，其两侧节点的最大深度
的差值不得大于1。"""
from test.tree.node import TreeNode


def is_balanced(root: TreeNode) -> bool:

    def height(node: TreeNode) -> int:
        if not node:
            return 0
        left_height = height(node.left)
        if left_height == -1:
            return -1
        right_height = height(node.right)
        if right_height == -1:
            return -1

        if abs(left_height - right_height) > 1:
            return -1

        return max(left_height, right_height) + 1

    return height(root) != -1
