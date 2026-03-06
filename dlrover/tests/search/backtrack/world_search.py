"""
给定一个字母矩阵，所有的字母都与上下左右四个方向上的字母相连。给定一个字符串，求
字符串能不能在字母矩阵中寻找到。
"""


def exist(board, word):
    if not board or not board[0] or not word:
        return False

    m = len(board)
    n = len(board[0])

    def backtrack(i, j, word_index):
        # 如果已匹配完所有字符
        if word_index == len(word):
            return True

        # 边界检查或字符不匹配
        if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[word_index]:
            return False

        # 临时标记当前单元格为已访问
        current = board[i][j]
        board[i][j] = "0"

        # 向四个方向搜索
        found = (backtrack(i + 1, j, word_index + 1)
                 or backtrack(i, j + 1, word_index + 1)
                 or backtrack(i - 1, j, word_index + 1)
                 or backtrack(i, j - 1, word_index + 1))

        # 恢复当前单元格
        board[i][j] = current

        return found

    # 找到第一个起点
    for i in range(m):
        for j in range(n):
            if board[i][j] == word[0]:
                if backtrack(i, j ,0):
                    return True

    return False


if __name__ == "__main__":
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]

    print(exist(board, "ABCCED"))  # True
    print(exist(board, "SEE"))  # True
    print(exist(board, "ABCB"))  # False
