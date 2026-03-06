"""给定一个链表，交换每个相邻的一对节点。

输入：head = [1,2,3,4]
输出：[2,1,4,3]
"""
from test.list_node.node import ListNode


def swap(head) -> ListNode:
    if not head:
        return None

    dummy = ListNode(0)
    dummy.next = head

    cur = dummy
    while cur.next and cur.next.next:
        n0 = cur.next
        n1 = cur.next.next

        # swap
        cur.next = n1
        n0.next = n1.next
        n1.next = n0

        cur = n0

    return dummy.next


if __name__ == '__main__':
    n0 = ListNode(0)
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n0.next = n1
    n1.next = n2
    n2.next = n3

    swap(n0).print_all()
