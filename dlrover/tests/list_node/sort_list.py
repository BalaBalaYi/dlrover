"""对链表进行排序"""
from test.list_node.node import ListNode


def sort(head: ListNode) -> ListNode:
    if not head:
        return None

    if not head.next:
        return head

    # 找中点
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    mid = slow.next
    # print(f"mid value: {mid.val}")

    # 分割
    slow.next = None

    def merge(left: ListNode, right: ListNode) -> ListNode:
        dummy_node = ListNode(0)
        cur = dummy_node
        while left and right:
            if left.val <= right.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            cur = cur.next
        if left:
            cur.next = left
        else:
            cur.next = right
        return dummy_node.next

    left_node = sort(head)
    right_node = sort(mid)

    return merge(left_node, right_node)


if __name__ == '__main__':
    n0 = ListNode(6)
    n1 = ListNode(2)
    n2 = ListNode(4)
    n3 = ListNode(1)
    n4 = ListNode(3)
    n5 = ListNode(4)
    n0.next = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5

    sort(n0).print_all()
