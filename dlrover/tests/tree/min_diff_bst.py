"""给定一个二叉搜索树的根节点 root，返回树中任意两不同节点值之间的最小绝对差。
"""


def get_min_diff(root):
    if not root:
        return 0

    min_diff = -1
    last = None

    def inorder(node):
        nonlocal min_diff, last
        if not node:
            return

        inorder(node.left)

        if last:
            min_diff = min(min_diff, node.val - last.value)

        last = node

        inorder(node.right)

    inorder(root)
    return min_diff
