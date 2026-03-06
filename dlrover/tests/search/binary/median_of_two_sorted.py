"""
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。
请你找出并返回这两个正序数组的 中位数。
算法的时间复杂度应该为 O(log (m+n))。

示例 1：
nums1 = [1, 3], nums2 = [2]
中位数是 2.0

示例 2：
nums1 = [1, 2], nums2 = [3, 4]
中位数是 (2 + 3) / 2 = 2.5
"""
from typing import List

"""
核心思路
1.分割思想：将两个数组分别从某个位置分割，使得左半部分的所有元素 ≤ 右半部分的所有元素。
2.长度平衡：左半部分元素总数 = 右半部分元素总数（或左半部分多1个，用于处理奇数总长度）。
3.二分查找：在较短的数组上使用二分查找确定分割点，根据边界值调整搜索范围。

算法步骤
1.预处理：确保 nums1是较短的数组，以最小化二分查找次数。
2.初始化：定义二分查找范围 low=0, high=len(nums1)。
3.循环二分：
    - 计算 nums1的分割点 i。
    - 根据总长度计算 nums2的分割点 j。
    - 检查分割是否有效（左半部分最大值 ≤ 右半部分最小值）。
    - 若 nums1左半部分最大值 > nums2右半部分最小值，说明 i偏大，需左移。
    - 若 nums2左半部分最大值 > nums1右半部分最小值，说明 i偏小，需右移。
4.计算中位数：找到正确分割后，根据总长度奇偶性返回结果。
"""


def solve(nums1: List[int], nums2: List[int]) -> float:
    # 确保 nums1 是较短的数组，以优化时间复杂度
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)
    total_left = (m + n + 1) // 2  # 左半部分应有的元素个数

    low, high = 0, m

    while low <= high:
        # i 是 nums1 的分割点，表示左半部分包含 nums1[0...i-1]
        i = (low + high) // 2
        # j 是 nums2 的分割点，表示左半部分包含 nums2[0...j-1]
        j = total_left - i

        # 处理边界情况：如果分割点导致数组越界，使用正负无穷大作为哨兵值
        nums1_left_max = float('-inf') if i == 0 else nums1[i - 1]
        nums1_right_min = float('inf') if i == m else nums1[i]
        nums2_left_max = float('-inf') if j == 0 else nums2[j - 1]
        nums2_right_min = float('inf') if j == n else nums2[j]

        # 检查分割是否满足条件：左半部分最大值 <= 右半部分最小值
        if nums1_left_max <= nums2_right_min and nums2_left_max <= nums1_right_min:
            # 找到正确分割点
            if (m + n) % 2 == 1:
                # 总长度为奇数，中位数是左半部分的最大值
                return max(nums1_left_max, nums2_left_max)
            else:
                # 总长度为偶数，中位数是 (左半部分最大值 + 右半部分最小值) / 2
                return (max(nums1_left_max, nums2_left_max) + min(
                    nums1_right_min, nums2_right_min)) / 2.0
        elif nums1_left_max > nums2_right_min:
            # nums1 的左半部分太大，需要减少 i（向左移动分割点）
            high = i - 1
        else:
            # nums2 的左半部分太大，需要增加 i（向右移动分割点）
            low = i + 1

    # 理论上循环内必会返回，此处仅为语法完整
    return 0.0


if __name__ == '__main__':
    # print(solve(nums1=[1, 3], nums2=[2]))
    # print(solve(nums1=[1, 3, 4, 7, 9, 13, 14], nums2=[2, 3, 4, 5, 6, 7, 10]))
    print(solve(nums1=[1, 2, 3, 4, 5, 6, 7], nums2=[8, 9, 10, 11, 12, 13, 14]))
