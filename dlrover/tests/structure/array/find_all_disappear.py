"""给定一个长度为n 的数组，其中包含范围为1 到n 的整数，有些整数重复了多次，有些整数
没有出现，求1 到n 中没有出现过的整数。"""


def findDisappearedNumbers(nums):
    """
    原地标记法
    时间复杂度: O(n)
    空间复杂度: O(1) (输出数组不计入空间复杂度)
    """
    n = len(nums)

    # 第一遍：标记出现过的数字
    for i in range(n):
        # 获取数字对应的索引（取绝对值，因为可能已被标记为负数）
        index = abs(nums[i]) - 1
        # 如果该位置的数字为正数，标记为负数
        if nums[index] > 0:
            nums[index] = -nums[index]

    print(nums)

    # 第二遍：收集未标记的索引
    result = []
    for i in range(n):
        if nums[i] > 0:
            result.append(i + 1)

    return result


if __name__ == '__main__':
    # 测试
    print(findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))  # [5,6]
    # print(findDisappearedNumbers([1, 1]))  # [2]
