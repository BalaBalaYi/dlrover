"""给你一个整数数组 nums，返回数组 answer，其中 answer[i]等于 nums中除 nums[i]之外其余各元素的乘积。

题目数据保证数组 nums之中任意元素的全部前缀元素和后缀元素的乘积都在 32 位整数范围内。

请不要使用除法，且在 O(n) 时间复杂度内完成此题。

输入: nums = [1,2,3,4]
输出: [24,12,8,6]
解释:
answer[0] = 2×3×4 = 24
answer[1] = 1×3×4 = 12
answer[2] = 1×2×4 = 8
answer[3] = 1×2×3 = 6

对于每个位置 i，结果是左边所有数的乘积乘以右边所有数的乘积。

"""

def solve(nums):
    n = len(nums)

    # 初始化数组
    left_product = [1] * n
    right_product = [1] * n
    answer = [1] * n

    # 计算左乘积
    for i in range(1, n):
        left_product[i] = left_product[i - 1] * nums[i - 1]
    print(f"左乘积 {left_product}")

    # 计算右乘积
    for i in range(n-2, -1, -1):
        right_product[i] = right_product[i + 1] * nums[i + 1]
    print(f"右乘积 {right_product}")

    # 合并结果
    for i in range(n):
        answer[i] = left_product[i] * right_product[i]

    return answer


if __name__ == '__main__':
    print(solve([1, 2, 3, 4]))  # [24,12,8,6]
    # print(solve([-1, 1, 0, -3, 3]))  # [0,0,9,0,0]
