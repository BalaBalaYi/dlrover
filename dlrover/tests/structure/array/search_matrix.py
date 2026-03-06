"""
给定一个二维矩阵，已知每行和每列都是增序的，尝试设计一个快速搜索一个数字是否在矩
阵中存在的算法。

输入: matrix = [[1,4,7,11,15],
               [2,5,8,12,19],
               [3,6,9,16,22],
               [10,13,14,17,24],
               [18,21,23,26,30]],
     target = 5
输出: true

从右上角开始的策略：
初始化位置为 (0, n-1)（右上角）
比较当前位置的值与 target：
如果 matrix[i][j] == target，找到目标，返回 true
如果 matrix[i][j] > target，由于列是递增的，当前列的所有元素都大于 target，可以排除整列，j--
如果 matrix[i][j] < target，由于行是递增的，当前行的所有元素都小于 target，可以排除整行，i++
重复直到找到目标或越界

"""


def search(matrix, target):
    if not matrix or not matrix[0]:
        return False

    m = len(matrix)
    n = len(matrix[0])

    i, j = 0, n -1

    while i < m and j >= 0:
        if matrix[i][j] == target:
            return True
        elif matrix[i][j] > target:
            j -= 1
        elif matrix[i][j] < target:
            i += 1

    return False


if __name__ == '__main__':
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]

    print(search(matrix, 5))  # True
    print(search(matrix, 20))  # False
