"""二叉树基础炒作"""
from collections import deque

from test.tree.node import TrieNode, TreeNode

"""翻转"""
def invert(root):
    if not root:
        return None

    root.left, root.right = root.right, root.left

    invert(root.left)
    invert(root.right)

    return root


"""合并"""
def merge(left, right):
    if not left and not right:
        return None

    if not left:
        return right
    if not right:
        return left

    new_node = TreeNode(left.val + right.val)
    new_node.left = merge(left.left, right.left)
    new_node.right = merge(left.right, right.right)

    return new_node


"""是否是子树"""
def is_sub(root, sub):
    if not root:
        return False
    if not sub:
        return True

    def is_same(node0, node1):
        if not node0 and not node1:
            return True
        if not node0 or not node1:
            return False
        if node0.val != node1.val:
            return False
        return is_same(node0.left, node1.left) and is_same(node0.right, node1.right)

    # 检查是否相同
    if is_same(root, sub):
        return True

    # 检查左子树和右子树是否相同
    return is_sub(root.left, sub.left) or is_sub(root.right, sub.right)


"""左叶子节点的和"""
def sum_left_leaves(root):
    if not root:
        return 0

    total = 0

    if root.left and not root.left.left and not root.left.right:
        total += root.left.value

    total += sum_left_leaves(root.left)
    total += sum_left_leaves(root.right)

    return total


"""寻找树左下角的值"""
def find_bottom_left_leaf(root):
    if not root:
        return None

    deq = deque([root])
    result = root.value

    while deq:
        result = deq[0].value
        for _ in range(len(deq)):
            node = deq.popleft()
            if node.left:
                deq.append(node.left)
            if node.right:
                deq.append(node.right)

    return result


"""求二叉树的高度"""
def get_max_depth(root):
    if not root:
        return 0

    left_depth = get_max_depth(root.left)
    right_depth = get_max_depth(root.right)

    return max(left_depth, right_depth) + 1

