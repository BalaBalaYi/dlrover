"""给定一个单链表的头节点 head，其中元素已经按升序排列，将其转换为高度平衡的二叉搜索树。
"""
from test.list_node.node import ListNode
from test.tree.node import TreeNode


def list_to_bst(head: ListNode) -> TreeNode:
    if not head:
        return None

    def find_mid(start: ListNode) -> ListNode:
        slow, fast = start, start
        prev = None
        while fast.next and fast.next.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        if prev:
            prev.next = None
        return slow

    # 构建bst
    def build_tree(head):
        if not head:
            return None

        # 找到中间节点
        mid = find_mid(head)

        # 创建root
        root = TreeNode(mid.val)

        # 递归构建
        root.left = build_tree(head)
        root.right = build_tree(mid.next)

        return root

    return build_tree(head)
