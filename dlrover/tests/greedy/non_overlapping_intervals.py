"""
给定一个区间的集合 intervals，其中 intervals[i] = [start_i, end_i]。返回需要移除区间的最小数量，使剩余区间互不重叠。

注意：
1.可以认为区间的终点总是大于它的起点。
2.区间 [1,2]和 [2,3]的边界相互"接触"，但不会重叠。

输入: intervals = [[1,2],[2,3],[3,4],[1,3]]
输出: 1
解释: 移除 [1,3] 后，剩下的区间没有重叠。

输入: intervals = [[1,2],[1,2],[1,2]]
输出: 2
解释: 你需要移除两个 [1,2] 来使剩下的区间没有重叠。
"""

"""
核心思想：
按照区间的结束时间升序排序
总是选择结束时间最早的区间，这样可以为后面的区间留出更多空间
统计需要移除的区间数量
"""


def solve(intervals):
    result = 0
    if not intervals or len(intervals) < 2:
        return result

    # 按右边界排序
    intervals.sort(key=lambda x: x[1])
    print(intervals)

    # 当前最新的右边界
    current_end = intervals[0][1]

    for i in range(1, len(intervals)):
        if intervals[i][0] < current_end:
            # 需要移除
            result += 1
        else:
            current_end = intervals[i][1]

    return result


if __name__ == '__main__':
    print(solve([[1,2],[2,3],[3,4],[1,3]]))  # 1
