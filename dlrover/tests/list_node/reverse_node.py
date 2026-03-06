"""翻转一个链表"""
from test.list_node.node import ListNode


def reverse_node(head) -> ListNode:
    if not head:
        return None

    new_head = None
    cur = head

    while cur:
        tmp_next = cur.next
        cur.next = new_head
        new_head = cur
        cur = tmp_next

    return new_head

if __name__ == '__main__':
    n0 = ListNode(0)
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n0.next = n1
    n1.next = n2
    n2.next = n3

    n0.print_all()
    reverse_node(n0).print_all()
