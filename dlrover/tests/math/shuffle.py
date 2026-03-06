"""实现一个shuffle和reset的操作"""

import random
from typing import List


class Solution:
    def __init__(self, nums: List[int]):
        """
        初始化
        保存原始数组和当前数组
        """
        self.original = nums[:]  # 深拷贝保存原始数组
        self.nums = nums[:]  # 当前数组

    def reset(self) -> List[int]:
        """
        重置数组到初始状态
        时间复杂度: O(1) 或 O(n) 取决于实现
        空间复杂度: O(1)
        """
        self.nums = self.original[:]  # 恢复原始数组
        return self.nums

    def shuffle(self) -> List[int]:
        """
        随机打乱数组 (Fisher-Yates 算法)
        时间复杂度: O(n)
        空间复杂度: O(1)
        """
        n = len(self.nums)

        # 从后向前遍历
        for i in range(n - 1, 0, -1):
            # 在 [0, i] 范围内随机选择一个位置
            j = random.randint(0, i)
            # 交换当前位置和随机位置
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]

        return self.nums


if __name__ == '__main__':
    # 测试
    nums = [1, 2, 3, 4, 5]
    solution = Solution(nums)

    print("原始数组:", solution.reset())
    print("第一次打乱:", solution.shuffle())
    print("重置:", solution.reset())
    print("第二次打乱:", solution.shuffle())
