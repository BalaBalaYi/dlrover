"""给定两个链表，判断它们是否相交于一点，并求这个相交节点。

方法：双指针法（拼接遍历）

更巧妙的解法是不计算长度差，而是将两个链表“拼接”起来遍历：
指针 pA从 headA开始遍历，到达末尾后转向 headB继续遍历。
指针 pB从 headB开始遍历，到达末尾后转向 headA继续遍历。
这样，两个指针最终会同时到达相交节点（或同时到达末尾的 null），因为它们的路径长度相同

"""
from test.list_node.node import ListNode


def solve(head0, head1) -> ListNode:
    if not head0 or not head1:
        return None

    n0, n1 = head0, head1
    while n0 != n1:
        # 如果n0达到末尾，则转向headB继续
        n0 = n0.next if n0 else head1

        # 如果n1达到末尾，则转向headA继续
        n1 = n1.next if n1 else head0

    return n0

if __name__ == '__main__':
    n0 = ListNode(1)
    n1 = ListNode(2)
    n2 = ListNode(4)
    n20 = ListNode(5)
    n0.next = n1
    n1.next = n2
    n2.next = n20

    n3 = ListNode(0)
    n4 = ListNode(3)
    n3.next = n4
    n4.next = n2

    solve(n0, n3).print_all()
