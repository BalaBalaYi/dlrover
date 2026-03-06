import copy

"""给定一个整数n 和一个整数k，求在1 到n 中选取k 个数字的所有组合方法。
"""

def combine(n, k):
    def backtrack(path, start):
        if len(path) == k:
            result.append(copy.deepcopy(path))
            return

        for i in range(start, n + 1):
            path.append(i)
            backtrack(path, i + 1)
            path.pop()

    result = []
    backtrack([], 1)

    return result


"""给定一个候选人编号的集合 candidates和一个目标数 target，找出 candidates中所有可以使数字和为 target的组合。

关键约束条件：
candidates中的每个数字在每个组合中只能使用 一次。
解集不能包含重复的组合（即使数组中有重复元素）。

"""

def combine_without_repeat(candidates, target):
    n = len(candidates)

    def backtrack(path, start, total):
        if total == target:
            result.append(copy.deepcopy(path))
            return

        for i in range(start, n):
            # 因为已经排序，所以后面的数字只会更大，直接brak
            if total + candidates[i] > target:
                break

            # 跳过重复的一次，以实现去重
            if candidates[i] == candidates[i - 1]:
                continue

            path.append(candidates[i])
            backtrack(path, i + 1, total + candidates[i])
            path.pop()

    # 先排序，方便去重
    candidates.sort()

    result = []
    backtrack([], 0, 0)

    return result


if __name__ == '__main__':
    print(combine(4, 2))
