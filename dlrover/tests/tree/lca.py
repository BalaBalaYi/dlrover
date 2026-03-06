"""给定一个二叉搜索树 (BST)，找到该树中两个指定节点的最近公共祖先（LCA）。

最近公共祖先的定义为："对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。"
"""

"""
假设 p.val < q.val
1. 如果 root.val > q.val：LCA在左子树
2. 如果 root.val < p.val：LCA在右子树
3. 如果 p.val ≤ root.val ≤ q.val：root就是LCA
"""
def find_lowest_ancestor_bst(root, p, q):
    # 确保p < q，方便判断
    if p.val > q.val:
        p,  q = q, p

    # 情况1：两个节点都在左子树
    if root.val > q.val:
        return find_lowest_ancestor_bst(root.left, p, q)

    # 情况2：两个节点都在右子树
    if root.val < p.val:
        return find_lowest_ancestor_bst(root.right, p, q)

    # 情况3：当前节点在p和q之间（或等于其中一个）
    else:
        return root


"""给定一个二叉树，找到该树中两个指定节点的最近公共祖先（LCA）。

最近公共祖先的定义为："对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。"
"""

"""
关键观察
如果当前节点是 p 或 q，那么当前节点可能是 LCA
如果 p 和 q 分别在当前节点的左右子树中，当前节点就是 LCA
如果 p 和 q 都在左子树，LCA 在左子树中
如果 p 和 q 都在右子树，LCA 在右子树中

"""
def find_lowest_ancestor_bin(root, p, q):
    # 递归基
    if not root or root == p or root == q:
        return root

    # 在左右子树中查找
    left = find_lowest_ancestor_bin(root.left, p, q)
    right = find_lowest_ancestor_bin(root.right, p, q)

    # 情况1: p和q分别在左右子树中
    if left and right:
        return root

    # 情况2: 只在左子树中找到
    if left:
        return left

    # 情况3: 只在右子树中找到
    return right
