"""给定一个已排序链表的头节点 head，删除所有重复的元素，使得每个元素只出现一次。返回已排序的链表。

输入：head = [1,1,2,3,3]
输出：[1,2,3]
"""
from test.list_node.node import ListNode


def solve(head: ListNode) -> ListNode:
    if not head:
        return None

    if head.next is None:
        return head

    current = head
    while current:
        # current指针应该指向下一个和自己不等的node
        next_node = current.next
        while next_node and next_node.val == current.val:
            next_node = next_node.next
        current.next = next_node
        current = next_node

    return head


if __name__ == '__main__':
    n0 = ListNode(1)
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(3)
    n0.next = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4
    solve(n0).print_all()
