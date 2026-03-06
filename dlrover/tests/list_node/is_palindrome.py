"""以O¹1º 的空间复杂度，判断链表是否回文。"""
from test.list_node.node import ListNode


def solve(head) -> bool:
    if not head:
        return False

    if not head.next:
        return True

    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    mid = slow
    # print(f"mid vmoalue: {mid.val}")

    def reverse(head: ListNode) -> ListNode:
        new_head = None
        current = head
        while current:
            tmp_next = current.next
            current.next = new_head
            new_head = current
            current = tmp_next

        return new_head

    reversed = reverse(mid)

    first_part = head
    second_part = reversed
    while first_part:
        if first_part.val != second_part.val:
            return False
        first_part = first_part.next
        second_part = second_part.next

    return True


if __name__ == '__main__':
    n0 = ListNode(1)
    n1 = ListNode(2)
    n2 = ListNode(3)
    n3 = ListNode(2)
    n4 = ListNode(1)
    n0.next = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4
    print(solve(n0))

    n1.next = None
    print(solve(n0))
