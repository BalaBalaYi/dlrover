"""
给定一个整数数组 nums，返回所有全排列。你可以按任意顺序返回答案。
"""

import copy


def permute(nums):
    # backtrack
    def backtrack(path, used):
        if len(path) == len(nums):
            result.append(copy.deepcopy(path))
            return

        for i in range(len(nums)):
            if not used[i]:
                used[i] = True
                path.append(nums[i])
                backtrack(path, used)

                path.pop()
                used[i] = False

    # search
    result = []
    used = [False] * len(nums)
    backtrack([], used)

    return result


"""
给定一个可包含重复数字的整数数组 nums，返回所有不重复的全排列。你可以按任意顺序返回答案
"""

def permute_without_repeat(nums):

    def backtrack(path, used):
        if len(path) == len(nums):
            result.append(copy.deepcopy(path))
            return

        for i in range(len(nums)):
            if not used[i]:
                # 新增关键点：去重
                # 跳过重复数字。条件：当前数字与前一个相同且前一个数字未被使用
                if i > 0 and nums[i - 1] == nums[i] and not used[i - 1]:
                    continue

                used[i] = True
                path.append(nums[i])
                backtrack(path, used)

                path.pop()
                used[i] = False

    # 先排序，有利于去重
    nums.sort()

    # search
    result = []
    used = [False] * len(nums)
    backtrack([], used)

    return result


if __name__ == '__main__':
    print(permute([1, 2, 3]))
