"""给定一个二叉查找树，已知有两个节点被不小心交换了，试复原此树。"""
from test.tree.node import TreeNode


def recover(root):
    first: TreeNode = None
    second: TreeNode = None
    prev: TreeNode = None

    def inorder(node):
        nonlocal first, second, prev

        if not node:
            return

        inorder(node.left)

        if prev.val > node.val:
            if not first:
                first = prev
            else:
                second = node
        prev = node
        inorder(node.right)

    inorder(root)

    # swap
    if first and second:
        first.val, second.val = second.val, first.val
