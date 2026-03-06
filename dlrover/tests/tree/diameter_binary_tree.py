"""求一个二叉树的最长直径。直径的定义是二叉树上任意两节点之间的无向距离。"""
from test.tree.node import TreeNode


def solve(root: TreeNode) -> int:
    result = 0

    def height(node: TreeNode) -> int:
        nonlocal result

        if not node:
            return 0

        left_height = height(root.left)
        right_height = height(root.right)

        # 更新全局最大直径：当前节点的路径长度 和 历史结果值 的最大值
        result = max(left_height + right_height, result)

        # 返回当前节点的高度
        return max(left_height, right_height) + 1

    height(root)
    return result
