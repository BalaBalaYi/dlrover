"""给你一个链表数组，每个链表都已经按升序排列。请你将所有链表合并到一个升序链表中，返回合并后的链表。

输入: lists = [[1,4,5],[1,3,4],[2,6]]
输出: [1,1,2,3,4,4,5,6]
解释: 链表数组如下：
[
  1->4->5,
  1->3->4,
  2->6
]
将它们合并到一个有序链表中得到。
1->1->2->3->4->4->5->6
"""

import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        # 重载小于运算符，用于堆比较
        return self.val < other.val


def mergeSortedLists(lists: List[Optional[ListNode]]):
    dummy = ListNode(-1)
    current = dummy

    heap = []

    # 初始化堆，每个链表头结点入堆
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))

    # 构建链表
    while heap:
        val, i, node = heapq.heappop(heap)
        current.next = node
        current = current.next

        # 如果链表还有下一个节点，继续入堆
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))

    return dummy.next


if __name__ == '__main__':
    pass
