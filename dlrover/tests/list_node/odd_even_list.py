"""给定一个单链表的头节点 head，将所有奇数位置的节点组合在一起，然后是所有偶数位置的节点。请注意，这里指的是节点的位置（索引），而不是节点的值。

输入: head = [1,2,3,4,5]
输出: [1,3,5,2,4]
"""
from test.list_node.node import ListNode


def solve(head) -> ListNode:
    if head is None or head.next is None:
        return head

    odd = head
    even = head.next
    even_head = even

    while even:
        # 连接奇数节点
        odd.next = even.next
        odd = odd.next

        # 连接偶数节点
        even.next = odd.next
        even = even.next

    odd.next = even_head
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
    solve(n0).print_all()  # [1,3,5,2,4]
