"""给定一个数组，数组每个位置的值表示该位置的权重，要求按照权重的概率去随机采样。

核心：前缀和 + 二分查找

将权重转换为前缀和数组，然后生成一个随机数，通过二分查找找到对应的下标。

算法步骤：
构建前缀和数组：
prefix[i] = w[0] + w[1] + ... + w[i]
例如：w = [1, 3, 2]→ prefix = [1, 4, 6]
随机选择：
生成一个在 [1, total_sum]范围内的随机数
通过二分查找在前缀和数组中找到第一个 ≥ 随机数的位置
返回下标：
找到的位置就是按照权重概率选择的下标
"""
import bisect
import random
from typing import List


class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sum = []

        # 构建前缀和数组
        total = 0
        for weight in w:
            total += weight
            self.prefix_sum.append(total)

        self.total = total

    def pick_index(self) -> int:
        # 生成 [1, total] 范围内的随机数
        target = random.randint(1, self.total)

        # 二分查找第一个 >= target 的位置
        # bisect_left 返回插入位置，即第一个 >= target 的位置
        return bisect.bisect_left(self.prefix_sum, target)
