"""给定一个二叉查找树和两个整数L 和R，且L < R，试修剪此二叉查找树，使得修剪后所有
节点的值都在[L, R] 的范围内。"""


def trim_bst(root, l, r):
    if not root:
        return None

    if root.val < l:
        return trim_bst(root.right, l, r)

    if root.val > r:
        return trim_bst(root.left, l, r)

    root.left = trim_bst(root.left, l, r)
    root.right = trim_bst(root.right, l, r)

    return root
