"""给定两个增序的链表，试将其合并成一个增序的链表。"""
from test.list_node.node import ListNode


def merge_two_sorted(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1

    dummy = ListNode(-1)
    cur = dummy

    while l1 and l2:
        if l1.val <= l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next

    if l1:
        cur.next = l1
    else:
        cur.next = l2

    return dummy.next


if __name__ == '__main__':
    n0 = ListNode(1)
    n1 = ListNode(2)
    n2 = ListNode(4)
    n0.next = n1
    n1.next = n2

    n3 = ListNode(1)
    n4 = ListNode(3)
    n5 = ListNode(4)
    n3.next = n4
    n4.next = n5

    merge_two_sorted(n0, n3).print_all()
