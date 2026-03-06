"""给定一个二叉搜索树（BST），把它转换为累加树（Greater Tree)，使得每个节点的值是原来的节点值加上所有大于它的节点值之和。

关键观察
BST的中序遍历是升序的
比当前节点大的所有节点都在它的右边
如果逆中序遍历（右→根→左），访问顺序就是从大到小
在逆中序遍历过程中，可以累加已经访问过的节点值

算法步骤：
逆中序遍历BST（右子树 → 根 → 左子树）
维护一个全局累加变量 sum
访问每个节点时：
将 sum加到当前节点值
更新 sum为新的节点值

"""


def solve(root):
    sum = 0

    def reverse_inorder(node):
        nonlocal sum
        if not node:
            return

        reverse_inorder(node.right)
        sum += node.val
        node.val = sum
        reverse_inorder(node.left)

    reverse_inorder(root)
    return sum
