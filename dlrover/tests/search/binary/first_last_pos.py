"""
给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。
如果数组中不存在目标值 target，返回 [-1, -1]。
你必须设计并实现时间复杂度为 O(log n)的算法解决此问题。

输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
"""

"""
核心思想：
1.使用二分查找找到第一个等于 target的位置
2.使用二分查找找到最后一个等于 target的位置

查找第一个位置（左边界）：
当 nums[mid] >= target时，继续向左搜索
最终检查找到的位置是否等于 target

查找最后一个位置（右边界）：
当 nums[mid] <= target时，继续向右搜索
最终检查找到的位置是否等于 target

"""


def searchRange(nums, target):
    """
    两次二分查找法
    """

    def find_left(nums, target):
        """
        查找第一个等于target的位置
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return left

    def find_right(nums, target):
        """
        查找最后一个等于target的位置
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return right

    if not nums:
        return [-1, -1]

    left_idx = find_left(nums, target)
    right_idx = find_right(nums, target)

    # 检查是否找到
    if left_idx <= right_idx < len(nums) and nums[left_idx] == target and nums[
        right_idx] == target:
        return [left_idx, right_idx]

    return [-1, -1]
