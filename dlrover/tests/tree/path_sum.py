"""给定一个整数二叉树，求有多少条路径节点值的和等于给定值。"""
from test.tree.node import TreeNode


def solve(root: TreeNode, target: int) -> int:
    prefix_count = {0: 1}

    def dfs (node, current_sum):
        if not node:
            return 0

        # current sum累积
        current_sum += node.val

        # 将当前前缀和加入哈希表
        prefix_count[current_sum] = prefix_count.get(current_sum, 0) + 1

        # 关键：查找是否存在前缀和 = current_sum - targetSum
        # 如果存在，说明从该前缀和对应的节点到当前节点的路径和为targetSum
        count = prefix_count.get(current_sum - target, 0)

        # 递归左右子树
        count += dfs(node.left, current_sum)
        count += dfs(node.right, current_sum)

        # 回溯
        prefix_count[current_sum] -= 1
        if prefix_count[current_sum] == 0:
            del prefix_count[current_sum]

        return count

    return dfs(root, 0)
