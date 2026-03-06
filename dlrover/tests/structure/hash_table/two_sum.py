"""给定一个整数数组，已知有且只有两个数的和等于给定值，求这两个数的位置。

输入: nums = [2,7,11,15], target = 9
输出: [0,1]
解释: 因为 nums[0] + nums[1] = 2 + 7 = 9
"""

def solve(nums, target):
    hash_table = {}
    result = []

    for i, num in enumerate(nums):
        if target - num in hash_table:
            result.append(hash_table[target - num])
            result.append(i)
            break
        hash_table[num] = i

    return result

if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print(solve(nums, target))  # [0, 1]
