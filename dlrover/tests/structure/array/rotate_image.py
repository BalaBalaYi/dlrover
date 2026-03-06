"""给定一个n * n 的矩阵，求它顺时针旋转90 度的结果，且必须在原矩阵上修改（in-place）。
怎样能够尽量不创建额外储存空间呢？

输入: matrix = [[1,2,3],
               [4,5,6],
               [7,8,9]]
输出: [[7,4,1],
       [8,5,2],
       [9,6,3]]
"""


def rotate(matrix, reverse=False):
    """
    转置 + 水平翻转
    时间复杂度: O(n²)
    空间复杂度: O(1)
    """
    n = len(matrix)

    # 第一步：转置（行列交换）
    for i in range(n):
        for j in range(i, n):  # 注意 j 从 i 开始，避免重复交换
            # print(f"swap {i},{j} and {j},{i}")
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # print(matrix)

    # 逆时针
    if reverse:
        # 第二步：垂直翻转（每列上下反转）
        for j in range(n):
            bot, top = 0, n - 1
            while bot < top:
                matrix[bot][j], matrix[top][j] = matrix[top][j], matrix[bot][j]
                bot += 1
                top -= 1
    # 顺时针
    else:
        # 第二步：水平翻转（每行左右反转）
        for i in range(n):
            left, right = 0, n - 1
            while left < right:
                matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][
                    left]
                left += 1
                right -= 1

    return matrix


if __name__ == '__main__':
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    print(rotate(matrix))
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    print(rotate(matrix, True))
