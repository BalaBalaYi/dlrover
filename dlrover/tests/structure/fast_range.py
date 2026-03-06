"""设计一个数据结构，使得其能够快速查询给定数组中，任意两个位置间所有数字的和。

prefix[i] = sum(nums[0] + nums[1] + ... + nums[i-1])
特殊：prefix[0] = 0
sumRange(left, right) = prefix[right+1] - prefix[left]
"""


class NumArray:
    def __init__(self, nums):
        """
        初始化前缀和数组
        时间复杂度: O(n)
        空间复杂度: O(n)
        """
        n = len(nums)
        self.prefix = [0] * (n + 1)  # prefix[0] = 0

        # 计算前缀和
        for i in range(n):
            self.prefix[i + 1] = self.prefix[i] + nums[i]

    def sumRange(self, left, right):
        """
        查询区间和
        时间复杂度: O(1)
        """
        return self.prefix[right + 1] - self.prefix[left]


# 测试
numArray = NumArray([-2, 0, 3, -5, 2, -1])
print(numArray.sumRange(0, 2))  # 1
print(numArray.sumRange(2, 5))  # -1
print(numArray.sumRange(0, 5))  # -3


"""设计一个数据结构，使得其能够快速查询给定矩阵中，任意两个位置包围的长方形中所有数
字的和。

输入: 
matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) → 8
sumRegion(1, 1, 2, 2) → 11
sumRegion(1, 2, 2, 4) → 12


prefix[i+1][j+1] = prefix[i][j+1] + prefix[i+1][j] - prefix[i][j] + matrix[i][j]
sumRegion(row1, col1, row2, col2) = 
    prefix[row2+1][col2+1] - prefix[row1][col2+1] 
    - prefix[row2+1][col1] + prefix[row1][col1]
"""


class NumMatrix:
    def __init__(self, matrix):
        """
        初始化二维前缀和
        时间复杂度: O(m×n)
        空间复杂度: O(m×n)
        """
        if not matrix or not matrix[0]:
            return

        m, n = len(matrix), len(matrix[0])

        # 创建(m+1)×(n+1)的前缀和矩阵
        self.prefix = [[0] * (n + 1) for _ in range(m + 1)]

        # 构建前缀和矩阵
        for i in range(m):
            for j in range(n):
                self.prefix[i + 1][j + 1] = (self.prefix[i + 1][j] +
                                             self.prefix[i][j + 1] -
                                             self.prefix[i][j] +
                                             matrix[i][j])

    def sumRegion(self, row1, col1, row2, col2):
        """
        查询子矩阵和
        时间复杂度: O(1)
        """
        return (self.prefix[row2 + 1][col2 + 1] -
                self.prefix[row1][col2 + 1] -
                self.prefix[row2 + 1][col1] +
                self.prefix[row1][col1])


# 测试
matrix = [
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5]
]

numMatrix = NumMatrix(matrix)
print(numMatrix.sumRegion(2, 1, 4, 3))  # 8
print(numMatrix.sumRegion(1, 1, 2, 2))  # 11
print(numMatrix.sumRegion(1, 2, 2, 4))  # 12
