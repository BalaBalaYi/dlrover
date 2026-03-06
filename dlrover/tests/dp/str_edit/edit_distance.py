"""给定两个单词 word1 和 word2，返回将 word1 转换成 word2 所使用的最少操作数。

你可以对一个单词进行以下三种操作：
插入一个字符
删除一个字符
替换一个字符

输入: word1 = "horse", word2 = "ros"
输出: 3
解释:
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')

输入: word1 = "intention", word2 = "execution"
输出: 5
解释:
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')
"""


"""
状态定义：
dp[i][j]表示将 word1 的前 i 个字符转换为 word2 的前 j 个字符所需的最小操作数

状态转移：
- 如果 word1[i-1] == word2[j-1]，则 dp[i][j] = dp[i-1][j-1]（不需要操作）
- 否则，取以下三种操作的最小值加1：
    插入：dp[i][j-1]+ 1（在 word1 前 i 个字符后插入一个字符，使得与 word2 前 j 个字符相同）
    删除：dp[i-1][j]+ 1（删除 word1 的第 i 个字符）
    替换：dp[i-1][j-1]+ 1（将 word1 的第 i 个字符替换为 word2 的第 j 个字符）

初始化：
dp[0][j] = j：将空字符串转换为 word2 的前 j 个字符需要 j 次插入操作
dp[i][0] = i：将 word1 的前 i 个字符转换为空字符串需要 i 次删除操作
"""


def solve(word1, word2):
    m = len(word1)
    n = len(word2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # 初始化第一行和第一列
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j - 1] + 1, dp[i][j - 1] + 1, dp[i - 1][j]+ 1)

    return dp[m][n]


if __name__ == '__main__':
    print(solve("horse", "roses"))
