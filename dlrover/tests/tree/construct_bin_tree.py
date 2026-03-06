"""给定一个二叉树的前序遍历和中序遍历结果，尝试复原这个树。已知树里不存在重复值的节
点。"""
from test.tree.node import TreeNode


def build_tree_by_pre_in(preorder, inorder) -> TreeNode:
    if not preorder or not inorder:
        return None

    # 前序遍历第一个一定是root
    root_val = preorder[0]
    root = TreeNode(root_val)

    # 中序遍历中找到root，左侧为左子树，右侧为由子树
    inorder_root_idx = inorder.index(root_val)

    # 左子树的中序
    inorder_left = inorder[:inorder_root_idx]
    # 右子树的中序
    inorder_right = inorder[inorder_root_idx + 1:]

    # 左子树的前序
    preorder_left = preorder[1:1+len(inorder_left)]
    # 右子树的前序
    preorder_right = preorder[1+len(inorder_left):]

    # 递归构建左右子树
    root.left = build_tree_by_pre_in(preorder_left, inorder_left)
    root.right = build_tree_by_pre_in(preorder_right, inorder_right)

    return root


def build_tree_by_post_in(inorder, postorder):
    if not inorder or not postorder:
        return None

    # 后序的最后一个元素是根节点
    root_val = postorder[-1]
    root = TreeNode(root_val)

    # 在中序中找到根节点的位置
    root_index = inorder.index(root_val)

    # 左子树的中序和后序
    left_inorder = inorder[:root_index]
    left_postorder = postorder[:root_index]  # 左子树节点数相同

    # 右子树的中序和后序
    right_inorder = inorder[root_index + 1:]
    right_postorder = postorder[root_index:-1]  # 去掉最后一个根节点

    # 递归构造
    root.left = build_tree_by_post_in(left_inorder, left_postorder)
    root.right = build_tree_by_post_in(right_inorder, right_postorder)

    return root


def build_tree_by_pre_post(preorder, postorder):
    if not preorder:
        return None

    # 根节点是前序的第一个元素
    root = TreeNode(preorder[0])

    # 如果只有一个节点，直接返回
    if len(preorder) == 1:
        return root

    # 左子树的根在前序中是第二个元素
    left_root_val = preorder[1]

    # 在后序中找到左子树根的位置
    left_root_index = postorder.index(left_root_val)

    # 左子树的节点数
    left_size = left_root_index + 1

    # 递归构造左右子树
    root.left = build_tree_by_pre_post(
        preorder[1:1 + left_size],
        postorder[:left_size]
    )
    root.right = build_tree_by_pre_post(
        preorder[1 + left_size:],
        postorder[left_size:-1]
    )

    return root


if __name__ == '__main__':
    # 测试
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    root = build_tree_by_pre_in(preorder, inorder)
    root.print_pre_order()
