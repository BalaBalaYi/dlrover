"""给定一个链表的头节点 head和一个整数 n，删除链表的倒数第 n个节点，并返回修改后链表的头节点。

输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]
解释：删除了倒数第 2 个节点（值为 4）

思路：使用快慢指针
"""
from test.list_node.node import ListNode


def solve(head, n):
    if not head:
        return head

    slow, fast = head, head
    for i in range(n):
        fast = fast.next
    print(f"slow: {slow.val}, fast: {fast.val}")

    while fast:
        slow = slow.next
        fast = fast.next

    print(f"n node: {slow.next.val}")
    slow.next = slow.next.next

    return head


if __name__ == '__main__':
    n0 = ListNode(1)
    n1 = ListNode(2)
    n2 = ListNode(3)
    n3 = ListNode(4)
    n4 = ListNode(5)
    n0.next = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4
    solve(n0, 3).print_all()  # [1, 2, 3, 5]
