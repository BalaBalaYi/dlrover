"""
已知存在一个按非降序排列的整数数组 nums，数组中的值不必互不相同。
在传递给函数之前，nums在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，
使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。
例如， [0,1,2,4,4,4,5,6,6,7]在下标 5处经旋转后可能变为 [4,5,6,6,7,0,1,2,4,4]。
给你 旋转后的数组 nums和一个整数 target，请你编写一个函数来判断给定的目标值是否存在于数组中。
如果 nums中存在这个目标值 target，则返回 true，否则返回 false。

你必须尽可能减少整个操作步骤。

输入: nums = [2,5,6,0,0,1,2], target = 0
输出: true

输入: nums = [2,5,6,0,0,1,2], target = 3
输出: false
"""

"""
核心思想：
使用二分查找
当 nums[mid] == nums[left]且 nums[mid] == nums[right]时，无法判断哪边有序
此时只能将 left++和 right--来缩小范围

1. 初始化 left = 0, right = n-1
2. while left <= right:
   - mid = left + (right - left) // 2
   - 如果 nums[mid] == target，返回 true
   - 处理重复元素：如果 nums[left] == nums[mid] == nums[right]，则 left++，right--
   - 判断哪一半是有序的：
     * 如果 nums[left] <= nums[mid]：左半部分有序
       - 如果 target 在 [nums[left], nums[mid]) 之间：right = mid - 1
       - 否则：left = mid + 1
     * 否则：右半部分有序
       - 如果 target 在 (nums[mid], nums[right]] 之间：left = mid + 1
       - 否则：right = mid - 1
3. 返回 false
"""


def search(nums, target):
    """
    二分查找（处理重复元素）
    """
    if not nums:
        return False

    n = len(nums)
    left, right = 0, n - 1

    while left <= right:
        mid = left + (right - left) // 2

        # 找到目标值
        if nums[mid] == target:
            return True

        # 处理重复元素：无法判断哪边有序
        if nums[left] == nums[mid] == nums[right]:
            left += 1
            right -= 1
        # 左半部分有序
        elif nums[left] <= nums[mid]:
            # target 在有序的左半部分
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # 右半部分有序
        else:
            # target 在有序的右半部分
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return False