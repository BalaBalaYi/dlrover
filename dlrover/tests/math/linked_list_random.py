"""给定一个单向链表，要求设计一个算法，可以随机取得其中的一个数字。

核心：水库抽样算法（Reservoir Sampling）

这是一个经典的流式数据随机抽样问题。由于不知道链表的总长度，且只能遍历一次，不能使用额外空间存储所有节点，需要使用水库抽样算法。

水库抽样算法（Reservoir Sampling）：
从包含 n 个项目的集合中随机选取 k 个样本
当 k=1 时，就是本题的情况
算法步骤：
初始化结果 result = head.val，计数器 count = 1
遍历链表，对于第 i 个节点（i 从 1 开始）：
以 1/i的概率用当前节点替换结果
否则保持原结果不变
遍历完成后，result就是随机选择的节点值
为什么是等概率的？
第 i 个节点被选中的概率是：1/i × (1 - 1/(i+1)) × ... × (1 - 1/n) = 1/n
每个节点最终被选中的概率都是 1/n
"""

import random
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self, head: Optional[ListNode]):
        """
        初始化
        时间复杂度: O(1)
        空间复杂度: O(1)
        """
        self.head = head

    def getRandom(self) -> int:
        """
        随机返回一个节点值
        时间复杂度: O(n)
        空间复杂度: O(1)
        """
        node = self.head
        result = 0
        count = 0

        while node:
            count += 1
            # 以 1/count 的概率选择当前节点
            if random.randint(1, count) == 1:
                result = node.val
            node = node.next

        return result


# 测试辅助函数：创建链表
def create_linked_list(arr):
    """从数组创建链表"""
    dummy = ListNode(0)
    current = dummy
    for val in arr:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


if __name__ == '__main__':
    # 测试
    arr = [1, 2, 3, 4, 5]
    head = create_linked_list(arr)
    solution = Solution(head)

    # 测试多次
    counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    trials = 10000

    for _ in range(trials):
        val = solution.getRandom()
        counts[val] += 1

    print("测试结果:")
    for val, count in counts.items():
        print(f"  值 {val}: 出现 {count} 次, 概率 {count / trials:.4f}, 期望 0.2")
