"""给定一个整数数组和一个滑动窗口大小，求在这个窗口的滑动过程中，每个时刻其包含的最
大值。

输入: nums = [1,3,-1,-3,5,3,6,7], k = 3
输出: [3,3,5,5,6,7]
解释:
滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
"""
from collections import deque


def maxSlidingWindow(nums, k):
    if not nums or k == 0:
        return []

    if k == 1:
        return nums

    # 使用队列存储索引（队列左侧始终是最大的）
    deq = deque()
    result = []

    for i, value in enumerate(nums):
        # 移除队列中所有小于当前元素的索引
        while deq and nums[deq[-1]] <= value:
            deq.pop()

        deq.append(i)

        # 移除窗口左侧过期的索引
        # 如果队头索引不在当前窗口内，移除
        if deq[0] == i - k:
            deq.popleft()

        if i >= k - 1:
            result.append(nums[deq[0]])

    return result


if __name__ == '__main__':
    print(maxSlidingWindow([1, 6, -1, -3, 5, 3, 6, 7], 3))
    print(maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))  # [3,3,5,5,6,7]
    print(maxSlidingWindow([1], 1))
