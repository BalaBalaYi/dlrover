"""给定一个二叉树，返回所有从根节点到叶子节点的路径。
说明：叶子节点是指没有子节点的节点。
"""
from copy import deepcopy


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solve(root):

    def dfs(node, path):
        if not node:
            return

        # 当前节点加入路径
        path.append(node.val)

        # 如果是叶子节点，将路径加入结果
        if not node.left and not node.right:
            result.append(deepcopy(path))
        else:
            # 递归左右子树
            dfs(node.left, path)
            dfs(node.right, path)

        # 回溯，移除当前节点
        path.pop()

    result = []
    dfs(root, [])
    return result


if __name__ == '__main__':
    pass
