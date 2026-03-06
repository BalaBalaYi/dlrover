"""给定一个大小为n 的正方形国际象棋棋盘，求有多少种方式可以放置n 个皇后并使得她们互
不攻击，即每一行、列、左斜、右斜最多只有一个皇后。"""


def totalNQueens(n):

    def backtrack(row, cols, left_diag, right_diag):
        """
        row: 当前要放置的行
        cols: 记录哪些列已被占用
        left_diag: 记录主对角线(row-col)是否被占用
        right_diag: 记录副对角线(row+col)是否被占用
        """
        nonlocal result

        # 如果已经放置了n个皇后，找到一个解法
        if row == n:
            result += 1
            return

        for col in range(n):
            # 计算对角线索引
            ld = row - col
            rd = row + col

            # 检查冲突
            if cols[col] or left_diag[ld] or right_diag[rd]:
                continue

            # 放置皇后
            cols[col] = True
            left_diag[ld] = True
            right_diag[rd] = True

            # 递归放置下一行
            backtrack(row + 1, cols, left_diag, right_diag)

            # 回溯，撤销选择
            cols[col] = False
            left_diag[ld] = False
            right_diag[rd] = False

    result = 0

    # 使用列表或集合记录冲突
    cols = [False] * n
    left_diag = [False] * (2 * n - 1)
    right_diag = [False] * (2 * n - 1)

    backtrack(0, cols, left_diag, right_diag)

    return result


if __name__ == '__main__':
    print(totalNQueens(4))  # 2
    print(totalNQueens(1))  # 1
    print(totalNQueens(8))  # 92
