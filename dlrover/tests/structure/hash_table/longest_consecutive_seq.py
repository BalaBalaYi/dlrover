"""给定一个整数数组，求这个数组中的数字可以组成的最长连续序列有多长。

输入: nums = [100,4,200,1,3,2]
输出: 4
解释: 最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
"""


def solve(nums):
    if not nums:
        return 0

    if len(nums) == 1:
        return 1

    num_set = set(nums)
    max_length = 0

    for num in num_set:
        if num - 1 not in num_set:
            # 只能是一个新的起点
            current_length = 1
            next_num = num + 1
            while next_num in num_set:
                current_length += 1
                next_num += 1

            max_length = max(max_length, current_length)

    return max_length


if __name__ == '__main__':
    print(solve([100, 4, 200, 1, 3, 2]))  # 4
    print(solve([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # 9
