"""判断一个二叉树是否对称"""
from test.tree.node import TreeNode


def solve (root: TreeNode):
    if not root:
        return True

    def dfs(left, right):
        if not left and not right:
            return True
        if not left or not right or left.val != right.val:
            return False
        return dfs(left.left, right.right) and dfs(left.right, right.left)

    return dfs(root.left, root.right)
